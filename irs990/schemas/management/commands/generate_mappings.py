from django.core.management.base import BaseCommand
from schemas.models import XSDFile, ProductionVersion 
from filing.schema_name_utils import version
from django.conf import settings
from schemas.mapping_utils import XSDReader

# Should eventually go in settings or elsewhere




# what files are we processing?
#FILENAME_WHITELIST = [ 'IRS990EZ', ]
#FILENAME_WHITELIST = [ 'IRS990SCHEDULEJ', ]
#FILENAME_WHITELIST = [ 'IRS990ScheduleA', ]

#FILENAME_WHITELIST = [ 'ReturnHeader990x', ]

FILENAME_WHITELIST = [ 'IRS990', ]
#FILENAME_WHITELIST = ['IRS990', 'IRS990PF','IRS990EZ', 'IRS990SCHEDULEA', 'IRS990SCHEDULEB', 'IRS990SCHEDULEC', 'IRS990SCHEDULEJ' ] 

## name alternates 


# ReturnHeader990x --> name_alternate='ReturnHeader'

class Command(BaseCommand):
    help = """  Generate mappings from whitelisted forms/schedules.
                Optionally pass a version_string as an arg
                to run only on that version, e.g. 
                $ python manage.py generate_mappings 2013v4.0
                Hard undo: TK;
                
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
                this_reader.make_mappings()                    
                
                #this_reader.make_mappings(name_alternate='ReturnHeader', name_prefix="/Return/ReturnHeader")
                # Need more comprehensive testing approach, hack

                # 990
                #sample_file = '/Users/jfenton/github-whitelabel/irs/irs990_admin/sample_990s/raw_examples/201500329349300000_public.xml'
        
                # 990ez: 
                
                #sample_file = '/Users/jfenton/github-whitelabel/irs/irs990_admin/sample_990s/raw_examples/201500329349200000_public.xml'

                #this_reader.mappings_from_sample_file(sample_file, "/IRS990EZ/")

                #this_reader.mappings_from_db(xpath_prefix="/Return/ReturnData/IRS990/")
                #this_reader.mappings_from_db(xpath_prefix="/Return/ReturnData/IRS990EZ/")
                this_reader.mappings_from_db(xpath_prefix="/Return/ReturnData/%s/" % (versioned_schema.name))
                #this_reader.mappings_from_db(xpath_prefix="/Return/ReturnData/ReturnHeader" )

                # for header
                #this_reader.mappings_from_db(xpath_prefix="/Return/ReturnHeader/" )



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
            

                    # get all named elements--requires resolving complex types. 