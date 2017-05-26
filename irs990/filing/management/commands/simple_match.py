from datetime import date

from django.core.management.base import BaseCommand
from django.conf import settings 
from django.db import reset_queries
from django.db.models import Count

from filing.models import *

from django.db import connection

YEARS = range(2011,date.today().year+1)

class Command(BaseCommand):
    help = """ Generate a master list of case-independent xpaths
            for elements and groups, and populate db appropriately.
            """

    def print_slow_query(self):
        last_queries = connection.queries[-2:]
        for last_query in last_queries:
            if float(last_query['time'])>0.01:
                print(last_query)
        
    def handle_groups(self):
        all_group_xpaths = observed_group.objects.all().order_by('raw_xpath').values('raw_xpath').distinct()        
        self.print_slow_query()

        for group_xpath in all_group_xpaths:
            this_group_xpath = group_xpath['raw_xpath']
            this_master_path, created = master_observed_group.objects.get_or_create(raw_xpath=this_group_xpath.upper() )
            self.print_slow_query()

            versioned_groups = observed_group.objects.filter(raw_xpath__iexact=this_group_xpath).order_by('version_string')
            self.print_slow_query()

            for versioned_group in versioned_groups:
                versioned_group.master_xpath = this_master_path
                versioned_group.save()

    def handle_xpaths(self):
        all_xpaths = observed_xpath.objects.all().order_by('raw_xpath').values('raw_xpath').distinct()
        self.print_slow_query()

        for xpath in all_xpaths:
            this_xpath = xpath['raw_xpath']
            this_master_path, created = master_observed_xpath.objects.get_or_create(raw_xpath=this_xpath.upper() )
            self.print_slow_query()

            versioned_xpaths = observed_xpath.objects.filter(raw_xpath__iexact=this_xpath).order_by('version_string')
            self.print_slow_query()
            for versioned_xpath in versioned_xpaths:
                versioned_xpath.master_xpath = this_master_path
                versioned_xpath.save()

    def link_xpaths_to_groups(self, version_string_list):
        """ 
        If an xpath is a member of a group, link it.
        If it's the member of more than one group, 
        chose the group that's longer
        """

        print("Erasing group - element linkages and rerunning")
        observed_xpath.objects.all().update(containing_group=None)
        self.print_slow_query()

        for vs in version_string_list:
            print("Linking groups for %s" % vs['version_string'])
            versioned_groups = observed_group.objects.filter(
                version_string=vs['version_string']
                ).extra(select={'length':'Length(raw_xpath)'}).order_by('-length')
            # Analyse these in reverse order of length, because groups can contain groups.
            for group in versioned_groups:
                #print "Handling %s" % (group.raw_xpath)

                # Note that groups can contain other groups
                # EG /Return/ReturnData/IRS990ScheduleK vs /Return/ReturnData/IRS990ScheduleK/Form990ScheduleKPartIII

                # find matching xpaths
                matching_xpaths = observed_xpath.objects.filter(
                    raw_xpath__icontains=group.raw_xpath, 
                    version_string=group.version_string,
                    index_file_year = group.index_file_year,
                    containing_group__isnull = True
                    ).update(containing_group=group)


    def handle(self, *args, **options):

        ## get version strings.
        version_strings = observed_xpath.objects.order_by('version_string').values('version_string').annotate(Count("num_observed"))
        self.print_slow_query()
        version_strings_list = [i for i in version_strings] # Keys are now 'num_observed__count', 'version_string'
        self.print_slow_query()
        self.handle_groups()
        self.handle_xpaths()

        self.link_xpaths_to_groups(version_strings_list)







