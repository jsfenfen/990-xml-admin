from django.core.management.base import BaseCommand
from django.conf import settings 


from filing.models import xml_submission

DOWNLOAD_IF_MISSING = True
BATCH_SIZE = 1000

class Command(BaseCommand):
    help = """Refresh the yearly csv file. 
            Takes the four-digit year as a positional argument
            $ manage.py retrieve_annual_file 2016
            """

    def add_arguments(self, parser):
            # Positional arguments
            parser.add_argument('year', nargs='+', type=int)

    def handle(self, *args, **options):

        for year in options['year']:
            print("Setting json for year=%s" % year)
            count = 0
            while True:
                empty_submissions = xml_submission.objects.filter(year=year, as_json__isnull=True, json_set=False)[:BATCH_SIZE]
                if not empty_submissions:
                    break
                for xs in empty_submissions:

                    if not xs.file_available():
                        print("File missing")
                        if DOWNLOAD_IF_MISSING:
                            print ("Retrieving missing file %s" % xs.get_s3_URL() )
                            xs.retrieve_file()
                        else:
                            continue

                    print("Setting json for %s from %s" % (xs.return_id, xs.get_local_file() ) )

                    xs.set_json(save=True)
                    count += 1

                    if count%BATCH_SIZE==0:
                        print("Set %s rows" % count)