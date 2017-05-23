from collections import Counter

from django.core.management.base import BaseCommand
from django.db import reset_queries
from filing.models import xml_submission, observed_xpath, observed_group
import json

from filing.stats_utils import json_stats_tracker
from filing.schema_name_utils import get_year_version_from_schema

BATCH_SIZE = 1000

class Command(BaseCommand):
    help = 'Run stats on a year of filings'

    def add_arguments(self, parser):
            # Positional arguments
            parser.add_argument('year', nargs='+', type=int)

    def get_json(self, pk):
        this_json = json.loads(xml_submission.objects.get(pk=pk).as_json)

    def get_stats(self, pk):
        this_json = json.loads(xml_submission.objects.get(pk=pk).as_json)
        version_string = this_json['Return']['@returnVersion']
        jst = json_stats_tracker(this_json)
        (xpath_counter, list_root_counter) = jst.parse()
        #print(xpath_counter.most_common(5))
        return version_string, xpath_counter, list_root_counter

    def handle(self, *args, **options):
        total_count = Counter()
        num_files = 0
        self.counter_hash = {}
        self.group_hash = {}

        for year in options['year']:


            print("Deleting stats for year=%s and rerunning" % year)
            observed_xpath.objects.filter(index_file_year=year).delete()
            observed_group.objects.filter(index_file_year=year).delete()

            submission_pks = xml_submission.objects.filter(year=year, json_set=True).values('pk')
            if not submission_pks:
                break
            for xs in submission_pks:
                (version, key_counter, list_root_counter) = self.get_stats(xs['pk'])

                try:
                    self.counter_hash[version].update(key_counter)
                except KeyError:
                    self.counter_hash[version] = key_counter

                try:
                    self.group_hash[version].update(list_root_counter)
                except KeyError:
                    self.group_hash[version] = list_root_counter

                num_files += 1
                if num_files % BATCH_SIZE == 0:
                    print("Handled %s files" % num_files)

            print("Aggregate results from %s files from year=%s:\n\n" % (num_files, year) )
            for key in self.counter_hash.keys():
                print("Writing key summary for version: %s" % (key) )
                this_counter = self.counter_hash[key]
                for counter_key in this_counter:  
                    observed_xpath.objects.create(raw_xpath=counter_key, num_observed=this_counter[counter_key], version_string=key, index_file_year=year)
            
            for key in self.group_hash.keys():
                print("Writing group summary for version: %s" % (key) )
                this_counter = self.group_hash[key]
                for counter_key in this_counter:  
                    observed_group.objects.create(raw_xpath=counter_key, num_observed=this_counter[counter_key], version_string=key, index_file_year=year)





        