from django.core.management.base import BaseCommand

from django.db.models import Count, Min, Max, Q

from filing.models import xml_submission, known_version_string
from filing.schema_name_utils import get_version_string
from django.db import reset_queries



BATCH_SIZE = 1000
SET_UNSET = True

class Command(BaseCommand):
    help = """Enters version strings, frequency
                max and min index_file_year they appear in.
            """



    def handle(self, *args, **options):

        years_set = 0
        while True:
            empty_submissions = xml_submission.objects.filter(json_set=True).filter( Q(schema_year__isnull=True)|Q(schema_version__isnull=True) ).defer('as_json')[:BATCH_SIZE]
            if not empty_submissions:
                break
            for xs in empty_submissions:
                xs.set_year_version_from_json(save=True)
                years_set += 1
                if years_set % BATCH_SIZE == 0:
                    print("Set %s version_strings" % years_set)
            reset_queries() 

           

        print("Erasing version string data and recalculating")
        known_version_string.objects.all().delete()

        version_strings = xml_submission.objects.exclude(schema_year__isnull=True, schema_version__isnull=True).values('schema_year', 'schema_version').annotate(num_observed=Count('return_id'), min_year=Min('year'), max_year=Max('year'))
        for vs in version_strings:
            vs_formatted = get_version_string(vs['schema_year'], vs['schema_version'])
            print("Creating %s %s" % (vs_formatted, vs))
            known_version_string.objects.create(version_string=vs_formatted, num_observed=vs['num_observed'], max_year=vs['max_year'], min_year=vs['min_year'])

