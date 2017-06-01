import csv

from django.core.management.base import BaseCommand
from django.conf import settings 
from django.db import reset_queries
from django.db.models import Sum


from filing.models import xml_submission, master_observed_xpath, observed_xpath, known_version_string
from filing.schema_name_utils import get_version_string

DOWNLOAD_IF_MISSING = True
BATCH_SIZE = 1000
XPATH_CSV_FILE = "xpaths.csv"

# VERSION_STRINGS = ["2013v4.0","2014v5.0","2014v6.0","2015v2.0","2015v2.1"] # for testing--complete list is much longer


class Command(BaseCommand):
    help = """Dump a csv showing xpath occurence.
            An 'X' is given where it's a path; a 'G' where 
            it is part of a repeated group.
            """

    def handle(self, *args, **options):
        csvout = open(XPATH_CSV_FILE, 'w')
        all_versions = known_version_string.objects.all().order_by('version_string')
        VERSION_STRINGS = [ i.version_string for i in all_versions]

        fieldnames = ["xpath",] + VERSION_STRINGS
        dw = csv.DictWriter(csvout, fieldnames=fieldnames, restval='', extrasaction='ignore')
        dw.writeheader()

        all_xpaths = master_observed_xpath.objects.all().order_by('raw_xpath')
        results = []
        for xpath in all_xpaths:
            child_xpaths = observed_xpath.objects.filter(master_xpath=xpath).values("version_string", "raw_xpath", "containing_group").annotate(Sum("num_observed"))
            this_result = {'xpath':xpath.raw_xpath}
            for this_observed_xpath in child_xpaths:
                this_version_string = this_observed_xpath['version_string']
                letter_entry = 'X'
                if not this_observed_xpath['containing_group'] == None:
                    letter_entry = 'G'
                letter_entry += " %s" % this_observed_xpath['num_observed__sum']
                this_result[this_version_string]=letter_entry
            results.append(this_result)
        for result in results:
            dw.writerow(result)




