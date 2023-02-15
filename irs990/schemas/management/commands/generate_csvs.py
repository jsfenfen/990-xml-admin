import os
import unicodecsv as csv

from django.core.management.base import BaseCommand
from django.db.models import Count
from django.conf import settings


from schemas.documentation_utils import most_recent, debracket
from schemas.models import * 
from schemas.epoch_utils import  MODERN_EPOCH
#MODERN_EPOCH = EPOCH_1012 + OLD_MODERN_EPOCH   # HACK, TESTING EARLIER YEARS

GENERATED_MODELS_DIR = settings.GENERATED_MODELS_DIR
SUPPORTED_VERSIONS = settings.CSV_OUTPUT_SUPPORTED
BASE_DIR = settings.BASE_DIR

CURRENT_YEAR = 2018

class Command(BaseCommand):
    help = """  Generate csv files for groups and variables. 
                Hard overwrites the default location.

            """

    def read_blacklist(self):
        # read the list of blacklisted xpaths, return a hash

        infilepath = os.path.join(BASE_DIR, "schemas", "emptyhead_blacklist.txt")
        infile = open(infilepath, 'r')
        for row in infile:
            xpath = row.replace("\n", "")
            xpath = xpath.replace("\r", "")

            print("blacklisting xpath '%s' " % xpath)
            self.blacklist[xpath] = True


    def clean_value(self, value):
        """ This gets run on every value """
        try:
            value = value.lstrip(" ")     # Remove leading whitespace
            if value=='NA':               # Throw out NA's
                return ''
        except AttributeError:
            pass
        return value

    def fix_row(self, rowdict):
        for key in rowdict.keys():
            rowdict[key] = self.clean_value(rowdict[key])
        return rowdict


    def write_schedule_parts(self):
        sked_data = []

        print("Running write_schedule_part")
        skedlist = ScheduleName.objects.all().order_by('schedule_name')
        for schedule in skedlist:
            
            print("Running schedule %s" % schedule)
            form_parts = SchedulePart.objects.filter(parent_sked=schedule).order_by('parent_sked', 'ordering_ordinal')
            int_ordinal = 0
            for form_part in form_parts:
                this_sked_data = {}
                int_ordinal += 1
                print("\n\n- Found part %s: %s" % (form_part.db_model_name, form_part.raw_part_name)) 
                this_sked_data['part_name']=form_part.raw_part_name
                this_sked_data['parent_sked_part'] = form_part.db_model_name
                this_sked_data['parent_sked'] = form_part.parent_sked.schedule_name # NA
                this_sked_data['ordering'] = int_ordinal
                this_sked_data['is_shell'] = False

                if form_part.parent_sked.schedule_name == 'ReturnHeader990x':
                    this_sked_data['xml_root'] = '/Return'
                else:
                    this_sked_data['xml_root'] = '/Return/ReturnData'



                variables_in_this_part = CanonicalVariable.objects.filter(parent_sked_part=form_part).exclude(in_a_group=True).order_by('ordering')
                if len(variables_in_this_part)==0:
                    print("Apparently empty part %s" % form_part)
                    this_sked_data['is_shell'] = True

                sked_data.append(this_sked_data)


        headers = ['parent_sked', 'parent_sked_part', 'ordering', 'part_name', 'xml_root', 'is_shell']
        with open(self.schedule_path, 'wb') as outfile:
            dw = csv.DictWriter(outfile, fieldnames=headers, extrasaction='ignore')
            dw.writeheader()
            for row in sked_data:           
                dw.writerow(row)



    def write_group_file(self):
        group_data = []
        all_group_xpaths = VersionedGroup.objects.filter(version_string__in=MODERN_EPOCH).select_related('parent_sked_part').values('xpath').order_by('parent_sked','parent_sked_part__ordering_ordinal', 'ordering').distinct()
        this_sked = None    
        sked_ordering = None

        for gx in all_group_xpaths:
            this_xpath = gx['xpath']
            this_xpath_data = {'xpath':this_xpath}
            versioned_groups = VersionedGroup.objects.filter(version_string__in=MODERN_EPOCH,xpath=this_xpath).order_by('version_string')
            first_year = int(versioned_groups[0].version_string.split("v")[0])
            length = len(versioned_groups)
            last_year = int(versioned_groups[length-1].version_string.split("v")[0])


            #print ("%s %s" % (this_xpath, first_year))
            canonical_group = versioned_groups.last().canonical_group
            if not canonical_group:
                continue

            this_xpath_data['db_name'] = canonical_group.db_safe_name
            this_xpath_data['parent_sked'] = canonical_group.parent_sked.schedule_name
            this_xpath_data['parent_sked_part'] = canonical_group.parent_sked_part.db_model_name

            this_xpath_data['version_start'] = first_year
            if last_year == CURRENT_YEAR:
                this_xpath_data['version_end'] = ''
            else:
                this_xpath_data['version_end'] = last_year

            if this_sked != this_xpath_data['parent_sked']:
                sked_ordering = 1
                this_sked = this_xpath_data['parent_sked']
            else:
                sked_ordering += 1
            this_xpath_data['ordering'] = sked_ordering

            # look for variables with this xpath
            twin_variables = VersionedVariable.objects.filter(version_string__in=MODERN_EPOCH, xpath=this_xpath)
            tv = twin_variables.last()
            if tv:
                cv = tv.canonical_variable
                if cv:
                    #print("cv %s %s" % (cv.line_number, cv.description))
                    #this_xpath_data['line_number'] = cv.line_number
                    #this_xpath_data['description'] = cv.description
                    this_xpath_data['line_number'] = debracket(cv.line_number).strip(";")
                    this_xpath_data['description'] = debracket(cv.description).strip(";")

            #print("data: %s" % this_xpath_data )
            group_data.append(this_xpath_data)

        
        group_data_sorted = sorted(group_data, key=lambda k: k['xpath']+ '_' + str(k['version_start'])) 

        headers = ['parent_sked', 'parent_sked_part','ordering','xpath', 'db_name', 'line_number', 'description', 'headless', 'version_start', 'version_end']
        with open(self.group_path, 'wb') as outfile:
            dw = csv.DictWriter(
                outfile, 
                fieldnames=headers, 
                delimiter=',',
                quotechar='"',
                lineterminator='\n',
                quoting=csv.QUOTE_MINIMAL,
                extrasaction='ignore')
            dw.writeheader()
            for row in group_data_sorted:           
                dw.writerow(self.fix_row(row))




    def write_var_file(self):

        ordering_hash = {}

        var_data = []
        #all_var_xpaths = VersionedVariable.objects.filter(version_string__in=MODERN_EPOCH).select_related('parent_sked_part').order_by('parent_sked', 'xpath').values('parent_sked_part', 'xpath').distinct()
        
        #all_var_xpaths = CanonicalVariable.objects.all().select_related('parent_sked_part').values('original_xpath').order_by('parent_sked','parent_sked_part__ordering_ordinal', 'ordering').distinct()

        all_var_xpaths = VersionedVariable.objects.filter(version_string__in=MODERN_EPOCH).exclude(canonical_variable__isnull=True).select_related('parent_sked_part').order_by('parent_sked').values('xpath').distinct()
        
        xpath_count =0
        for var in all_var_xpaths:
            xpath_count += 1
            if (xpath_count % 100 == 0):
                print("processed %s xpaths" % xpath_count)
            this_xpath = var['xpath']
            #print ("processing %s" % this_xpath)
            this_var_data = {'xpath':this_xpath}

            versioned_vars = VersionedVariable.objects.filter(version_string__in=MODERN_EPOCH,xpath=this_xpath).order_by('version_string')
            first_year = int(versioned_vars[0].version_string.split("v")[0])
            length = len(versioned_vars)
            last_year = int(versioned_vars[length-1].version_string.split("v")[0])



            most_recent = None
            if len(versioned_vars)>0:
                most_recent=versioned_vars.last()
                version_strings = ""
                for i, vs in enumerate(versioned_vars):
                    if i>0:
                        version_strings +=";"
                    version_strings += vs.version_string


            if most_recent:
                canonical_variable = most_recent.canonical_variable
                if not canonical_variable:
                    print("Missing var? %s " % (this_xpath))
                    # some historical variables don't translate so, skip
                    continue

                # Is it blacklisted? We maintain a blacklist of "empty heads" that get generated but should be left out
                try:
                    self.blacklist[canonical_variable.original_xpath]
                    # it's blacklisted, so ignore
                    print("ignoring blacklisted xpath %s" % canonical_variable.original_xpath)
                    continue

                except KeyError:
                    pass
                    # not blacklisted, so continue

                #print("Got canonical var id %s %s %s" % (canonical_variable.id, canonical_variable.original_xpath, canonical_variable.parent_sked_part))
                this_var_data['db_name'] = canonical_variable.db_safe_name
                this_var_data['parent_sked'] = canonical_variable.parent_sked.schedule_name
                this_var_data['parent_sked_part'] = canonical_variable.parent_sked_part.db_model_name
                this_var_data['line_number'] = debracket(canonical_variable.line_number).strip(";").replace("; ; ", "; ")
                this_var_data['description'] = debracket(canonical_variable.description).strip(";").replace("; ; ", "; ")
                this_var_data['irs_type'] = canonical_variable.irs_type
                this_var_data['in_a_group'] = canonical_variable.in_a_group

                this_var_data['version_start'] = first_year
                if last_year == CURRENT_YEAR:
                    this_var_data['version_end'] = ''
                else:
                    this_var_data['version_end'] = last_year


                if canonical_variable.in_a_group:
                    this_var_data['db_table'] = canonical_variable.parent_group.db_safe_name
                else:
                    this_var_data['db_table'] = canonical_variable.parent_sked_part.db_model_name
                this_var_data['db_type'] = canonical_variable.sql_alch_type

                if not this_var_data['db_type']:
                    this_var_data['db_type'] = 'Text'


            try: 
                ordering_hash[this_var_data['parent_sked']] += 1

            except KeyError:
                ordering_hash[this_var_data['parent_sked']] = 1

            this_var_data['ordering'] = ordering_hash[this_var_data['parent_sked']]

            var_data.append(this_var_data)

        headers = ['parent_sked', 'parent_sked_part','in_a_group', 'db_table', 'ordering', 'db_name', 'xpath', 'irs_type', 'db_type', 'line_number', 'description', 'version_start', 'version_end']
        

        var_data_sorted = sorted(var_data, key=lambda k: k['xpath']+ '_' + str(k['version_start'])) 

        with open(self.var_path, 'wb') as outfile:
            dw = csv.DictWriter(
                outfile,
                fieldnames=headers,
                delimiter=',',
                quotechar='"',
                lineterminator='\n',
                quoting=csv.QUOTE_MINIMAL,
            )
            dw.writeheader()
            for row in var_data_sorted:           
                dw.writerow(self.fix_row(row))


    def handle(self, *args, **options):
        self.blacklist = {}
        self.read_blacklist()
        self.group_path =  os.path.join(GENERATED_MODELS_DIR, "groups_generated.csv")
        self.var_path =  os.path.join(GENERATED_MODELS_DIR, "variables_generated.csv")
        self.schedule_path =  os.path.join(GENERATED_MODELS_DIR, "schedule_parts_generated.csv")

        self.write_schedule_parts()
        self.write_group_file()
        self.write_var_file()