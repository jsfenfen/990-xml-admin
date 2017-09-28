import unicodecsv as csv
import json

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import reset_queries, connection

from irsx.xmlrunner import XMLRunner
from irsx.filing import Filing
from irsx.standardizer import Standardizer
from filing.models import xml_submission as XMLSubmission, ProcessedFiling

unicodeType = type(unicode()) 


class Command(BaseCommand):
    help = 'Dump some fields that are of interest'
 
    def handle(self, *args, **options):
        self.xml_runner = None
        self.standardizer = Standardizer()
        count = 0

        submissions =  XMLSubmission.objects.filter(
            schema_year__gte=2013, 
            sub_date__contains='2017'
        ).values('taxpayer_name', 'tax_period', 'sub_date', 'object_id')
        for submission in submissions:


            
            count += 1
            if count % 100 == 0:
                print ("Processed %s filings" % count)
                reset_queries()  # not sure this will matter, but...
                self.xml_runner = None  # Erase this to prevent memory leaks

            if not self.xml_runner:
                # will start up faster if we don't have to reread/import csvs
                self.xml_runner = XMLRunner(standardizer=self.standardizer)

            whole_submission = XMLSubmission.objects.get(
                object_id=submission['object_id']
            )
            

            if type(whole_submission.as_json)==unicodeType:
                submission_json = json.loads(whole_submission.as_json)
            else:
                # Assume it's a dict? 
                # We don't have any "working" installations that return json as json
                submission_json=whole_submission.as_json

            filingobj = Filing(submission['object_id'], json=submission_json)

            parsedFiling = self.xml_runner.run_from_filing_obj(
                filingobj,
                verbose=False,
            )
            result = parsedFiling.get_result()
            keyerrors = parsedFiling.get_keyerrors()
            has_keyerrors = len(keyerrors) > 0

            try:
                ProcessedFiling.objects.get(object_id=submission['object_id'])
            except ProcessedFiling.DoesNotExist:
                ProcessedFiling.objects.create(
                    ein = whole_submission.ein,
                    object_id = whole_submission.object_id,
                    processed_json = result,
                    keyerrors = keyerrors,
                    has_keyerrors = has_keyerrors,
                    submission = whole_submission
                )




            