from django.core.management.base import BaseCommand
from schemas.models import XSDFile, ProductionVersion
from filing.schema_name_utils import version
from django.conf import settings
from schemas.schema_parse_utils import XSD_Parser


class Command(BaseCommand):
    help = """  Read schema file data by reading files.
                Default is to run all files;
                Optionally pass a version_string as an arg
                to run only on that version, e.g. 
                $ python manage.py read_schema_files 2013v4.0

                Checks the existence before creating (so rerunning shouldn't
                cause errors). But runs slower. 
                
                Nuke from DB manually: [ +- where version_string='2013v4.0']
                delete from schemas_simpletype;
                delete from schemas_fileinclude;
                delete from schemas_element;
                delete from schemas_group;
                delete from schemas_complextype;
            """

    def add_arguments(self, parser):
            # Positional arguments
            parser.add_argument('schema', nargs='?', type=version)

    def handle(self, *args, **options):

        if options['schema']:
            version_list = [options['schema'],]
            print("Entering versions: %s" % version_list)

        else:
            print("Entering all versions")
            version_list = ProductionVersion.objects.all().order_by('version_string')

        for vs in version_list:
            print("Running schemas from version %s" % vs)
            vsname = vs
            if not isinstance(vs, basestring):
                vsname = vs.version_string
            


            versioned_schemas = XSDFile.objects.filter(version_string=vsname).exclude(file_read=True)
            for versioned_schema in versioned_schemas:
                print("\tRunning %s" % versioned_schema.file_path) 
                parser = XSD_Parser(versioned_schema)
                parser.parse()