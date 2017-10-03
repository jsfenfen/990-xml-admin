from django.core.management.base import BaseCommand
from filing.models import ProcessedFiling

SAMPLE_SIZE = 1000

class Command(BaseCommand):
    help = """  Drop and regenerate canonical groups and variables.
            """
    def handle(self, *args, **options):

        missing_dict = {}

        haskeyerrors = ProcessedFiling.objects.filter(has_keyerrors=True)[:SAMPLE_SIZE]
        for thisfiling in haskeyerrors:
            print("Processing filing %s" % thisfiling.object_id)
            for schedule in thisfiling.keyerrors:
                print("Handling keyerrors for sked %s" % schedule['schedule_name'])
                for keyerror in schedule['keyerrors']:
                    #print ("keyerror: %s" % keyerror['element_path'])
                    try:
                        missing_dict[keyerror['element_path']]+= 1
                    except KeyError:
                        missing_dict[keyerror['element_path']] = 1

                for keyerror in schedule['group_keyerrors']:
                    print ("group_keyerrors: %s" % keyerror['element_path'])


        for row in list(missing_dict):
            print('%s: %s' % (row,  missing_dict[row]) )