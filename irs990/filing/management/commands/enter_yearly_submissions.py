import csv
import os

from django.core.management.base import BaseCommand
from filing.models import xml_submission
from django.conf  import settings

BATCH_SIZE = 10000

class Command(BaseCommand):
    help = 'Read the yearly csv file line by line and add new lines if they don\'t exist. Lines are added in bulk at the end.'

    def add_arguments(self, parser):
            # Positional arguments
            parser.add_argument('year', nargs='+', type=int)

    def handle(self, *args, **options):

        for year in options['year']:
            filepath = settings.LOCAL_INDEX_FILE % year
            print("Entering xml submissions from %s" % filepath)
            fh = open(filepath, 'r')
            reader = csv.reader(fh)
            rows_to_enter = []

            # ignore header rows
            headers = reader.next()
            count = 0
            for line in reader:
                (return_id, filing_type, ein, tax_period, sub_date, taxpayer_name, return_type, dln, object_id) = line
                
                try:
                    obj = xml_submission.objects.get(object_id=object_id)
                except xml_submission.DoesNotExist:
                    new_sub  = xml_submission(
                        return_id=return_id,
                        year=year,
                        filing_type=filing_type,
                        ein=ein,
                        tax_period=tax_period,
                        sub_date=sub_date,
                        taxpayer_name=taxpayer_name,
                        return_type=return_type,
                        dln=dln,
                        object_id=object_id
                    )
                    

                    rows_to_enter.append(new_sub)
                    count += 1

                if count % BATCH_SIZE == 0 and count > 0:
                    print("Committing %s total entered=%s" % (BATCH_SIZE, count) )
                    xml_submission.objects.bulk_create(rows_to_enter)
                    print("commit complete")
                    rows_to_enter = []

            xml_submission.objects.bulk_create(rows_to_enter)
            print("Added %s new entries." % (count) )