from django.core.management.base import BaseCommand

from django.db.models import Count, Min, Max


from filing.models import xml_submission, known_version_string

from filing.schema_name_utils import get_version_string

class Command(BaseCommand):
    help = """Enters version strings, frequency
                max and min index_file_year they appear in.
            """



    def handle(self, *args, **options):

        print("Erasing version string data and recalculating")
        known_version_string.objects.all().delete()

        version_strings = xml_submission.objects.exclude(schema_year__isnull=True, schema_version__isnull=True).values('schema_year', 'schema_version').annotate(num_observed=Count('return_id'), min_year=Min('year'), max_year=Max('year'))
        for vs in version_strings:
            vs_formatted = get_version_string(vs['schema_year'], vs['schema_version'])
            print("Creating %s %s" % (vs_formatted, vs))
            known_version_string.objects.create(version_string=vs_formatted, num_observed=vs['num_observed'], max_year=vs['max_year'], min_year=vs['min_year'])

