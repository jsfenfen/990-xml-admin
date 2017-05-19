from django.core.management.base import BaseCommand
from django.conf import settings 

from filing.file_utils import stream_download

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
            remote_url = settings.IRS_INDEX_FILE % year
            local_path = settings.LOCAL_INDEX_FILE % year
            print("Refreshing file for %s ; retrieving from %s and saving to %s" % (year, remote_url, local_path) )
            stream_download(remote_url, local_path,verbose=True)
