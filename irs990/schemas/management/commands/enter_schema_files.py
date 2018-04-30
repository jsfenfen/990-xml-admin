import os
import sys


from django.core.management.base import BaseCommand

from django.conf import settings
from schemas.models import XSDFile, ProductionVersion
from filing.schema_name_utils import version



class Command(BaseCommand):
    help = """Enter schema files by walking the SCHEMA_DIR.
                Optionally pass a version_string as an arg
                to run only on that version, e.g. 
                $ python manage.py enter_schema_files 2013v4.0
                Hard undo: delete from schemas_xsdfile [ where version_string='2013v4.0'];
            """

    def add_arguments(self, parser):
            # Positional arguments
            parser.add_argument('schema', nargs='?', type=version)

    def query_yes_no(self, question, default="yes"):

        """
        from: https://stackoverflow.com/a/3041990
        Should go somewhere else if we keep this. 
        Ask a yes/no question via raw_input() and return their answer.

        "question" is a string that is presented to the user.
        "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

        The "answer" return value is True for "yes" or False for "no".
        """
        valid = {"yes": True, "y": True, "ye": True,
                 "no": False, "n": False}
        if default is None:
            prompt = " [y/n] "
        elif default == "yes":
            prompt = " [Y/n] "
        elif default == "no":
            prompt = " [y/N] "
        else:
            raise ValueError("invalid default answer: '%s'" % default)

        while True:
            sys.stdout.write(question + prompt)
            choice = raw_input().lower()
            if default is not None and choice == '':
                return valid[default]
            elif choice in valid:
                return valid[choice]
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' "
                                 "(or 'y' or 'n').\n")

    def walk_dir(self, DIR, version_string):
        print("Walk dir %s version %s" % (DIR, version_string) ) 
        try:
            this_version = ProductionVersion.objects.get(version_string=version_string)
            this_version_name = this_version.version_string
        except ProductionVersion.DoesNotExist:
            question = ("There is no Production Version for %s. Should I create one?" % version_string)
            result = self.query_yes_no(question, default="no")
            if result:
                print("Now creating one")
                this_version = ProductionVersion.objects.create(version_string=version_string)
                this_version_name = this_version.version_string
            else:
                return None


        count = 0
        for root, dirs, files in os.walk(DIR, topdown=False):
            for name in files:
                if name.endswith(".xsd"):
                    full_path = (os.path.join(root, name))
                    assert full_path.startswith(DIR) 
                    relative_dir = full_path.lstrip(DIR)
                    name = name.replace(".xsd","")
                    (obj, created) = XSDFile.objects.get_or_create(
                        file_path=relative_dir, 
                        version_string=this_version_name,
                        defaults={
                            'version': this_version,
                            'version_string': this_version_name,
                            'name': name
                            # set schedule at a later point
                        })
                    if created:
                        count += 1

        print("Total of %s new XSDFile's created" % count)

    def handle(self, *args, **options):

        if options['schema']:
            version_list = [options['schema']]
            print("Entering versions: %s" % version_list)

        else:
            print("Entering all versions")
            version_list = [i.version_string for i in ProductionVersion.objects.all().order_by('version_string')]

        for v in version_list:
            dir = os.path.join(settings.SCHEMA_DIR, ("efile990x_%s" % v ), v)
            self.walk_dir(dir, v)