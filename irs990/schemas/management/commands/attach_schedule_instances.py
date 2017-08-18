import os

from django.core.management.base import BaseCommand

from django.conf import settings
from schemas.models import ScheduleName, XSDFile, ProductionVersion, ScheduleInstance
from filing.schema_name_utils import version

class Command(BaseCommand):
    help = """Create ScheduleInstance objects for each XSDFile
                Optionally pass a version_string as an arg
                to run only on that version, e.g. 
                $ python manage.py attach_schedule_instances 2013v4.0
                Hard undo: delete from schemas_scheduleinstance [ where version_string='2013v4.0'];
            """

    def add_arguments(self, parser):
            # Positional arguments
            parser.add_argument('schema', nargs='?', type=version)

    def handle(self, *args, **options):

        if options['schema']:
            version_list = [options['schema']]
            print("Entering versions: %s" % version_list)

        else:
            print("Entering all versions")
            version_list = [i.version_string for i in ProductionVersion.objects.all().order_by('version_string')]

        for v in version_list:
            this_version = ProductionVersion.objects.get(version_string=v)
            all_schedules = ScheduleName.objects.all()
            for sked in all_schedules:
                try:
                    this_sked_instance = ScheduleInstance.objects.get(schedule_type=sked, version_string=v)

                except ScheduleInstance.DoesNotExist:
                    try:
                        print("Getting xsdfile  version_string = '%s' name = schedule_name'%s'" % (v, this_version))

                        xsd_file = XSDFile.objects.get(version_string=v, name=sked.schedule_name)
                        print("Creating sked instance '%s' '%s'" % (sked.schedule_name, this_version))
                        ScheduleInstance.objects.create(schedule_instance=xsd_file,version_string=v,schedule_name=sked.schedule_name, schedule_type=sked)

                    except XSDFile.DoesNotExist:
                        print("xsd file missing -- couldn't create for '%s' '%s'" % (sked.schedule_name, this_version))