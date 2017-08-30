import re
import unidecode

from django.core.management.base import BaseCommand
from django.conf import settings


from filing.schema_name_utils import version
from schemas.models import ProductionVersion, XSDFile, ScheduleName, \
    SchedulePart, VersionedVariable, VersionedGroup

fileoutput = "%s_documentation.md"

BRACKET_RE = re.compile(r'\[.*?\]')

class Command(BaseCommand):
    help = """  Generate documentation for whitelisted forms/schedules.
                Optionally pass a version_string as an arg
                to run only on that version, e.g. 
                $ python manage.py generate_mappings 2013v4.0

                Output is to DOCUMENTATION settings dir

            """

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('schema', nargs='?', type=version)

    def markupify(self, string):
        """ replace _ with \_  [ not need for all markup ] """
        return string.replace("_","\_")

    def debracket(self, string):
        """ Eliminate the bracketed var names in doc, line strings """
        result = re.sub(BRACKET_RE, ';', string)
        result = unidecode.unidecode(result)
        return result

    def most_recent(self, semicolon_delimited_string):
        result = semicolon_delimited_string.split(";")[-1]
        return result


    def format_varoutput(self, var):
        return_string = "\n\n  ***%s***  \n" % (self.markupify(var.xpath) ) 
        return_string += "Line number: %s  \n" % (self.most_recent( self.debracket(var.line_number) ) ) 
        return_string += "Description: %s  \n" % (self.most_recent( self.debracket(var.description) ) )
        if var.django_type:
            return_string += "Type: %s  \n" % ( var.django_type ) 

        return return_string


    def handle_version(self, version_string):

        outfile = fileoutput % version_string
        outputfh = open(outfile, 'w')

        print("Running schemas from version %s" % version_string)
        skedlist = ScheduleName.objects.all().order_by('schedule_name')
        for schedule in skedlist:
            print("Running schedule %s" % schedule)
            outputfh.write("\n\n# <a name=\"%s\"></a>%s" % (self.markupify(schedule.schedule_name), self.markupify(schedule.schedule_name) ) )
            form_parts = SchedulePart.objects.filter(parent_sked=schedule).order_by('ordering_ordinal')
            for form_part in form_parts:
                print("\n\n- Found part %s: %s" % (self.markupify(form_part.db_model_name), self.markupify(form_part.raw_part_name)) )
                outputfh.write("\n\n## %s: %s" % (self.markupify(form_part.db_model_name), self.markupify(form_part.raw_part_name)) )

                variables_in_this_part = VersionedVariable.objects.filter(parent_sked_part=form_part, version_string=version_string).exclude(in_a_group=True).order_by('ordering',)
                for var in variables_in_this_part:
                    print("-- %s" % (var.xpath))
                    outputfh.write( self.format_varoutput(var) )


                groups_in_this_part = VersionedGroup.objects.filter(parent_sked_part=form_part, version_string=version_string).order_by('ordering',)
                for group in groups_in_this_part:
                    print("\n %s-> %s" % (form_part,group) )
                    outputfh.write("\n\n## %s" % (group.name) )


                    variables_in_this_group = VersionedVariable.objects.filter(version_string=version_string, parent_group=group).order_by('ordering',)
                    for var in variables_in_this_group:
                        outputfh.write( self.format_varoutput(var) )







    def handle(self, *args, **options):

        if options['schema']:
            version_list = [options['schema'],]
            print("Entering versions: %s" % version_list)

        else:
            print("Entering all versions")
            version_list = ProductionVersion.objects.all().order_by('version_string')

        for vs in version_list:
            self.handle_version(vs)
            