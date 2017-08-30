from django.core.management.base import BaseCommand
from schemas.models import XSDFile, ProductionVersion 
from filing.schema_name_utils import version
from django.conf import settings
from schemas.mapping_utils import XSDReader

# Should eventually go in settings or elsewhere?
# Which files are we processing?
MAIN_SKEDS = [ 'ReturnHeader990x', 'IRS990', 'IRS990PF','IRS990EZ'] 
LETTERED_SKEDS = [ 'IRS990ScheduleA', 'IRS990ScheduleB', 'IRS990ScheduleC', 'IRS990ScheduleD', 'IRS990ScheduleE',
    'IRS990ScheduleF', 'IRS990ScheduleG', 'IRS990ScheduleH', 'IRS990ScheduleI', 'IRS990ScheduleJ', 'IRS990ScheduleK',
    'IRS990ScheduleL', 'IRS990ScheduleM', 'IRS990ScheduleN', 'IRS990ScheduleO', 'IRS990ScheduleR']
FILENAME_WHITELIST = MAIN_SKEDS + LETTERED_SKEDS
#FILENAME_WHITELIST = MAIN_SKEDS 

# FILENAME_WHITELIST = ['IRS990',]

class Command(BaseCommand):
    help = """  Generate mappings from whitelisted forms/schedules.
                Optionally pass a version_string as an arg
                to run only on that version, e.g. 
                $ python manage.py generate_mappings 2013v4.0
                Hard undo: 
                - elements: delete from schemas_versionedvariable
                - groups: delete from schemas_versionedgroup;

            """

    def add_arguments(self, parser):
            # Positional arguments
            parser.add_argument('schema', nargs='?', type=version)

    def handle_version(self, vsname):
        print("Running schemas from version %s" % vsname)
        versioned_schemas = XSDFile.objects.filter(version_string=vsname).exclude(file_read=True)
        for versioned_schema in versioned_schemas:
            # Decide if we should process it
            if versioned_schema.name in FILENAME_WHITELIST:
                this_reader = XSDReader(versioned_schema)

                if versioned_schema.name == 'ReturnHeader990x':
                    this_reader.make_mappings(name_alternate='ReturnHeader')
                    #this_reader.mappings_from_db(xpath_prefix="/Return/ReturnHeader/" )
                else:
                    this_reader.make_mappings()
                    #this_reader.mappings_from_db(xpath_prefix="/Return/ReturnData/%s/" % (versioned_schema.name))


    def handle(self, *args, **options):

        if options['schema']:
            version_list = [options['schema'],]
            print("Entering versions: %s" % version_list)

        else:
            print("Entering all versions")
            version_list = ProductionVersion.objects.all().order_by('version_string')

        for vs in version_list:
            vsname = vs
            if not isinstance(vs, basestring):
                vsname = vs.version_string
            self.handle_version(vsname)
            