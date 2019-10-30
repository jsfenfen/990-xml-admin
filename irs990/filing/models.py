# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import xmltodict
import os

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings 

from filing.file_utils import stream_download
from filing.schema_name_utils import get_year_version_from_schema
from filing.type_utils import unicodeType

class xml_submission(models.Model):
    ## Fields taken from index_YYYY.csv files
    year = models.IntegerField(blank=True, null=True, help_text="Index file year")
    return_id = models.CharField(max_length=31, blank=True, null=True, db_index=True, help_text="IRS' unique id, so index this")
    filing_type = models.CharField(max_length=15, blank=True, null=True, help_text="probably EFILE")
    ein = models.CharField(blank=False, max_length=15, help_text="employee id number")
    tax_period = models.IntegerField(blank=True, null=True, help_text="Filing month YYYYMM")
    sub_date = models.CharField(max_length=511, blank=True, null=True, help_text="submitted date: YYYY-MM-DD")
    taxpayer_name = models.CharField(max_length=511, blank=True, null=True)
    return_type = models.CharField(max_length=7, blank=True, null=True)
    dln = models.CharField(max_length=31, blank=True, null=True)
    object_id = models.CharField(max_length=31, blank=True, null=True)
    ## Fields added on
    schema_year = models.IntegerField(blank=True, null=True, help_text="Schema year")
    schema_version = models.TextField(null=True, help_text="Schema version") 
    json_set = models.BooleanField(default=False, help_text="Has the json been set in ProcessedFiling?")

    def get_s3_URL(self):
        return  settings.IRS_XML_HTTP_BASE + "%s_public.xml" % self.object_id

    def get_local_file(self):
        return settings.LOCAL_DATA_DIR + "/%s_public.xml" % self.object_id

    def retrieve_file(self):
        stream_download(self.get_s3_URL(), self.get_local_file())

    def file_available(self):
        return os.path.isfile(self.get_local_file())

    class Meta:
        verbose_name="XML Submission"
        managed=True

class ProcessedFiling(models.Model):
    """ Place to hold processed json. This should hold standardized json only"""
    ein = models.CharField(blank=False, max_length=15, help_text="employee id number")
    object_id = models.CharField(max_length=31, primary_key=True)
    version_string = models.CharField(max_length=15, blank=True, null=True)
    processed_json = JSONField(null=True)
    has_keyerrors = models.NullBooleanField() 
    keyerrors = JSONField(null=True)
    submission = models.ForeignKey(xml_submission, null=True, on_delete=models.PROTECT)
    is_saved = models.NullBooleanField()   # has it been saved to related db?

    # A psycopg2 / django / postgres config returns string not json
    # make sure it's actually json
    def get_json(self):
        if type(self.processed_json)==unicodeType:
            return json.loads(self.processed_json)
        else:
            return self.processed_json


class master_observed_group(models.Model):
    raw_xpath = models.CharField(max_length=511, blank=True, null=True)

class observed_group(models.Model):
    """ These are groups -- often they end in "Grp" -- that may repeat. They have child values. """
    index_file_year = models.IntegerField(blank=True, null=True, help_text="Index file year") 
    version_string = models.CharField(max_length=15, blank=True, null=True)
    raw_xpath = models.CharField(max_length=511, blank=True, null=True)
    num_observed = models.IntegerField(blank=True, null=True, help_text="Index file year") 
    last_update = models.DateTimeField(auto_now=True, null=True)
    master_xpath = models.ForeignKey(master_observed_group, null=True, on_delete=models.PROTECT)


    def __unicode__(self):
        return("%s %s" % (self.version_string, self.raw_xpath) )


class master_observed_xpath(models.Model):
    raw_xpath = models.CharField(max_length=511, blank=True, null=True)

class observed_xpath(models.Model):
    """ These are elements with values assigned to them, including attributes, which have @ prepended """
    index_file_year = models.IntegerField(blank=True, null=True, help_text="Index file year") 
    version_string = models.CharField(max_length=15, blank=True, null=True)
    raw_xpath = models.CharField(max_length=511, blank=True, null=True)
    num_observed = models.IntegerField(blank=True, null=True, help_text="Index file year") 
    last_update = models.DateTimeField(auto_now=True, null=True)
    observed_type = models.CharField(max_length=511, blank=True, null=True, help_text="character representation of data type, as observed")
    master_xpath = models.ForeignKey(master_observed_xpath, null=True, on_delete=models.PROTECT)
    containing_group = models.ForeignKey(observed_group, null=True, on_delete=models.PROTECT)

    def __unicode__(self):
        return("%s %s" % (self.version_string, self.raw_xpath) )


class known_version_string(models.Model):
    """ Stats on xml submission """
    version_string = models.CharField(max_length=15, blank=True, null=True)
    num_observed = models.IntegerField(blank=True, null=True, help_text="Index file year") 
    max_year = models.IntegerField(blank=True, null=True, help_text="max index file year") 
    min_year = models.IntegerField(blank=True, null=True, help_text="min index file year")

    def __unicode__(self):
        return self.version_string
