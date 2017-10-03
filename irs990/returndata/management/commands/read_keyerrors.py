from django.core.management.base import BaseCommand
from filing.models import ProcessedFiling

SAMPLE_MAX = 100000

class Command(BaseCommand):
    help = """  Drop and regenerate canonical groups and variables.
            """
    def handle(self, *args, **options):

        missing_dict = {}

        haskeyerrors = ProcessedFiling.objects.filter(has_keyerrors=True).only('keyerrors', 'version_string')[:SAMPLE_MAX]
        for thisfiling in haskeyerrors:
            print("Processing filing %s" % thisfiling.object_id)
            for schedule in thisfiling.keyerrors:
                print("Handling keyerrors for sked %s" % schedule['schedule_name'])
                for keyerror in schedule['keyerrors']:
                    #print ("keyerror: %s" % keyerror['element_path'])
                    thiskey = thisfiling.version_string + keyerror['element_path']
                    try:

                        missing_dict[thiskey]+= 1
                    except KeyError:
                        missing_dict[thiskey] = 1

                for keyerror in schedule['group_keyerrors']:
                    print ("group_keyerrors: %s" % keyerror['element_path'])


        for row in list(missing_dict):
            print('%s: %s' % (row,  missing_dict[row]) )