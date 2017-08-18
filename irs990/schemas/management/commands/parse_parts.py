"""
Adapted from a distribution of 'fixed' XSD files from The Chronicle of Higher Education

This script reads the XSD files and determines which variables are in which parts of the files. 

The form parts are listed only in the comments, so we parse the comments out with regexes
and some of the xml too. This is not really a great strategy, but then again, it's maybe 
not a great strategy to list the form parts in comments?

This relies on "fixed" version of the XSD that add back missing parts. 

A hack to relate elements to their position in parts, and the part delineation
only appears in the comments. 
Basically we're assuming the elements are not self-closing and closure tags appear on their own line. 



hard delete with

delete from schemas_schedulepart;

update schemas_versionedvariable set parent_sked_part_id = Null;
update schemas_versionedgroup set parent_sked_part_id = Null;

"""



import os
import re
from django.core.management.base import BaseCommand
from django.conf import settings

from schemas.naming_utils import fix_part_name, ordinal_hash
from schemas.models import XSDFile, ScheduleInstance, SchedulePart, VersionedVariable, ScheduleName

filelist = settings.SUPPORTED_SCHEMAS

## Regexes
PART_RE = re.compile(r'<!-- Part (.+?)-->')
WHOLE_ELEMENT_RE = re.compile(r'<xsd:element(.+?)>')
END_OF_MAIN = re.compile(r'= Local types, types for repeating groups etc. =')
NAME_IN_ELEMENT = re.compile(r'name="(.+?)"')
ELEMENT_END = re.compile(r'</xsd:element>')


class Command(BaseCommand):
    help = 'Load schema file names; '

    def walk_schema_dir(self, file_base):
        print("Wsd: %s" % file_base)

        xsd_files = []
        for root, dirs, files in os.walk(file_base, topdown=False):
            for name in files:
                print("name: %s" % name)
                if name.endswith(".xsd"):
                    full_path = os.path.join(root, name)
                    relative_path = full_path.replace(file_base, '')
                    xsd_files.append({'relative_path':relative_path, 'file_name':name})
        return xsd_files

    def process_element(self, element_name, part, this_schema_file, sort_ordinal, this_form_part, db_model_name):
        mappings = None
        # find element in versioned data:
        parent_skedname = this_schema_file.name
        sn = ScheduleName.objects.get(schedule_name=parent_skedname)
        full_element_name = "/" + sn.schedule_name + "/" + element_name

        print("process element element_name %s, this_form_part %s db model name %s " % (full_element_name, this_form_part, db_model_name) )


        vvs = VersionedVariable.objects.filter(xpath__startswith=full_element_name, version_string=settings.CANONICAL_VERSION, parent_sked=sn)
        
        if not vvs:
            element_name_fixed = "/" + sn.schedule_name + "/" + element_name.split("/")[-1]
            print ("No results for xpath__startswith=%s version_string %s parent_sked %s" % (full_element_name, settings.CANONICAL_VERSION, sn) )

            vvs = VersionedVariable.objects.filter(xpath__startswith=element_name_fixed, version_string=settings.CANONICAL_VERSION, parent_sked=sn)
            print("Using results for %s" % element_name_fixed )
            print vvs

        if vvs:
            for vv in vvs:
                print("vv:\n %s" % vv)
                vv.parent_sked_part  = this_form_part

                if vv.in_a_group:
                    group = vv.parent_group
                    if not group.parent_sked_part or group.parent_sked_part != this_form_part:
                        print("Setting group parent %s to part %s" % (group, this_form_part))
                        group.parent_sked_part = this_form_part
                        group.save()

                vv.save()


    def get_ordinal_from_part_name(self, part_found):
        # get a sorting ordinal from roman numeral bits. 
        # since there are parts a and b, just use a dict.

        part_found = part_found.strip(" ")
        first_part = part_found.split(' ')[0]
        ordinal = ordinal_hash[first_part]
        return ordinal


    def parse_file(self, file_path, file_name):
        if file_name in filelist:

        #if file_name in ['ReturnHeader990x.xsd']:

            this_file = open(file_path, 'r')
            file_name_fixed = file_name.replace(".xsd","")

            print "\n\n%s handling version_string = '%s', name='%s'" % (file_name_fixed, settings.CANONICAL_VERSION, file_name_fixed)

            this_schema_file = XSDFile.objects.get(version_string = settings.CANONICAL_VERSION, name=file_name_fixed)
            print("seeking instance for id=%s" % this_schema_file.pk)
            this_sked_instance = ScheduleInstance.objects.get(schedule_instance=this_schema_file)
            this_sked = this_sked_instance.schedule_type

            current_part = None
            current_ordinal = 1
            fixed_name = None
            this_form_part = None
            element_hierarchy_array = []

            for line in this_file:


                part_found = re.search(PART_RE, line)
                if part_found:
                    found_name = part_found.group(1)
                    full_name = this_sked.schedule_name + " Part " + found_name
                    full_name = full_name.replace("IRS990", "")
                    current_part =  this_sked.schedule_name + " Part " + found_name.split(" ")[0]
                    current_part = current_part.strip(" ")
                    part_ordinal = self.get_ordinal_from_part_name(found_name)
                    fixed_name = fix_part_name(current_part)
                    print "\n\n\n\nFound name '%s' in %s with ordinal %s fixed_name='%s'" % (found_name, this_sked.schedule_name, part_ordinal, fixed_name)

                    # prob should make creating this optional based on command-line arg
                    this_form_part, created = SchedulePart.objects.get_or_create(parent_sked=this_sked, raw_part_name=full_name, defaults={'db_model_name':fixed_name, 'ordering_ordinal':part_ordinal, 'canonical_version_string':settings.CANONICAL_VERSION})
                    if created:
                        print ("Created form part %s" % full_name)

                element_found = re.search(WHOLE_ELEMENT_RE, line)
                if element_found:
                    element_text = element_found.group(1)

                    name = re.search(NAME_IN_ELEMENT, element_text).group(1)
                    print "Found name '%s' in %s form part = %s" % (name, current_part, this_form_part)
                    element_hierarchy_array.append(name)


                    # ignore the complex type that's the entire form
                    if name not in self.prohibited_names:
                        full_name = "/".join(element_hierarchy_array)
                        self.process_element(full_name, current_part, this_schema_file, current_ordinal, this_form_part, fixed_name)
                        current_ordinal += 1


                element_end_found = re.search(ELEMENT_END, line)
                if element_end_found:
                    del element_hierarchy_array[-1:]


                end_found = re.search(END_OF_MAIN, line)
                if end_found:
                    print "Found End!"
                    break
                


        

    
    def handle(self, *args, **options):

        self.prohibited_names = [i.replace(".xsd","") for i in filelist]
        self.prohibited_names.append('ReturnHeader') # why, I dunno. 

        schema_base = settings.SCHEMA_PARTS_DIR

        # /Users/jfenton/github-whitelabel/irs/irs990_admin/irs990/schemas/schema_parts_fixed"
        xsd_files = self.walk_schema_dir(schema_base)
        for xsd_file in xsd_files:
            xsd_file['full_path'] = schema_base + xsd_file['relative_path']
            self.parse_file(xsd_file['full_path'], xsd_file['file_name'])






"""
Random notes:

Part II of 990 is a signature block, with no variables. 


"""


