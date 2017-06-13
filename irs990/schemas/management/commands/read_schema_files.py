from django.core.management.base import BaseCommand
from schemas.models import XSDFile, ProductionVersion
from filing.schema_name_utils import version
from django.conf import settings
from schemas.schema_parse_utils import XSD_Parser


class Command(BaseCommand):
    help = """Read schema file data by reading files.
                Optionally pass a version_string as an arg
                to run only on that version, e.g. 
                $ python manage.py read_schema_files 2013v4.0
                Hard undo: TK;
                delete from schemas_simpletype;
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
            versioned_schemas = XSDFile.objects.filter(version_string=vs.version_string).exclude(file_read=True)
            for versioned_schema in versioned_schemas:
                #print("\tRunning %s" % versioned_schema.file_path) 
                parser = XSD_Parser(versioned_schema)
                parser.parse()