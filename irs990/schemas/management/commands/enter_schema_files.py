import os

from django.core.management.base import BaseCommand

from django.conf import settings
from schemas.models import XSDFile, ProductionVersion
from filing.schema_name_utils import get_year_version_from_schema

class Command(BaseCommand):
    help = """Enter schema files by walking the SCHEMA_DIR.
                Optionally pass a version_string as an arg
                to run only on that version, e.g. 
                $ python manage.py enter_schema_files 2013v4.0
                Hard undo: delete from schemas_xsdfile [ where version_string='2013v4.0'];
            """

    def valid_version(self, string):
        get_year_version_from_schema(string)
        return string

    def add_arguments(self, parser):
            # Positional arguments
            parser.add_argument('schema', nargs='?', type=self.valid_version)

    def walk_dir(self, DIR, version_string):
        print "Walk dir %s" % DIR
        this_version = ProductionVersion.objects.get(version_string=version_string)
        this_version_name = this_version.version_string

        count = 0
        for root, dirs, files in os.walk(DIR, topdown=False):
            for name in files:
                if name.endswith(".xsd"):
                    full_path = (os.path.join(root, name))
                    assert full_path.startswith(DIR) 
                    relative_dir = full_path.lstrip(DIR)
                    name_upper = name.upper().replace(".XSD","")
                    (obj, created) = XSDFile.objects.get_or_create(
                        file_path=relative_dir, 
                        version_string=this_version_name,
                        defaults={
                            'version': this_version,
                            'version_string': this_version_name,
                            'name': name_upper
                            # set schedule at a later point
                        })
                    if created:
                        count += 1

        print("Total of %s new XSDFile's created" % count)

    def handle(self, *args, **options):

        if options['schema']:
            version_list = options['schema']
            print("Entering versions: %s" % version_list)

        else:
            print("Entering all versions")
            version_list = [i.version_string for i in ProductionVersion.objects.all().order_by('version_string')]

        for v in version_list:
            dir = os.path.join(settings.SCHEMA_DIR, ("efile990x_%s" % v ), v)
            self.walk_dir(dir, v)