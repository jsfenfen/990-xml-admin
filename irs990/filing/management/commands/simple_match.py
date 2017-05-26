from datetime import date

from django.core.management.base import BaseCommand
from django.conf import settings 
from django.db import reset_queries
from django.db.models import Count


from filing.models import *


YEARS = range(2011,date.today().year+1)

class Command(BaseCommand):
    help = """ Generate a master list of case-independent xpaths
            for elements and groups, and populate db appropriately.
            """

    def handle_groups(self):

        all_group_xpaths = observed_group.objects.all().order_by('raw_xpath').values('raw_xpath').distinct()

        for group_xpath in all_group_xpaths:
            this_group_xpath = group_xpath['raw_xpath']
            this_master_path, created = master_observed_group.objects.get_or_create(raw_xpath=this_group_xpath.upper() )

            versioned_groups = observed_group.objects.filter(raw_xpath__iexact=this_group_xpath).order_by('version_string')
            print("Handling group %s" % (this_group_xpath))
            for versioned_group in versioned_groups:
                versioned_group.master_xpath = this_master_path
                versioned_group.save()

    def handle_xpaths(self):

        all_xpaths = observed_xpath.objects.all().order_by('raw_xpath').values('raw_xpath').distinct()

        for xpath in all_xpaths:
            this_xpath = xpath['raw_xpath']
            this_master_path, created = master_observed_xpath.objects.get_or_create(raw_xpath=this_xpath.upper() )

            versioned_xpaths = observed_xpath.objects.filter(raw_xpath__iexact=this_xpath).order_by('version_string')
            print("Handling xpath %s" % (this_xpath))
            for versioned_xpath in versioned_xpaths:
                versioned_xpath.master_xpath = this_master_path
                versioned_xpath.save()

    def link_xpaths_to_groups(self, version_string_list):
        """ 
        If an xpath is a member of a group, link it.
        If it's the member of more than one group, 
        chose the group that's longer
        """
        for vs in version_string_list:
            print("Linking groups for %s" % vs['version_string'])
            versioned_groups = observed_group.objects.filter(
                version_string=vs['version_string']
                ).extra(select={'length':'Length(raw_xpath)'}).order_by('-length')
            for group in versioned_groups:
                #print "Handling %s" % (group.raw_xpath)

                contained_groups = observed_group.objects.filter(
                    raw_xpath__icontains=group.raw_xpath + "/", 
                    version_string=group.version_string,
                    index_file_year = group.index_file_year
                    ).extra(select={'length':'Length(raw_xpath)'}).order_by('-length')
                if contained_groups:
                    print("Group %s contained in group %s" % (group, contained_groups[0]))
                    ## Can this happen? Do we need to worry about this? 
                    assert False

                # find matching xpaths
                #matching_xpaths = observed_xpath.objects.filter(
                #    raw_xpath__icontains=group.raw_xpath, 
                #    version_string=group.version_string,
                #    index_file_year = group.index_file_year)








    def handle(self, *args, **options):


        ## get version strings.
        version_strings = observed_xpath.objects.order_by('version_string').values('version_string').annotate(Count("num_observed"))
        version_strings_list = [i for i in version_strings] # Keys are now 'num_observed__count', 'version_string'

        #self.handle_groups()
        #self.handle_xpaths()

        self.link_xpaths_to_groups(version_strings_list)







