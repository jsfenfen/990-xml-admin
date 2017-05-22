# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import xmltodict
import os

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings 

from filing.file_utils import stream_download

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
    as_json = JSONField(null=True)
    schema_year = models.IntegerField(blank=True, null=True, help_text="Schema year")
    schema_version = models.TextField(null=True, help_text="Schema version") 
    json_set = models.BooleanField(default=False, help_text="Has the json been set?")
    

    def get_s3_URL(self):
        return  settings.IRS_XML_HTTP_BASE + "%s_public.xml" % self.object_id

    def get_local_file(self):
        return settings.LOCAL_DATA_DIR + "/%s_public.xml" % self.object_id

    def retrieve_file(self):
        stream_download(self.get_s3_URL(), self.get_local_file())

    def file_available(self):
        return os.path.isfile(self.get_local_file())

    def set_json(self, save=False):
        try:
            fh = open(self.get_local_file())
            raw_file=fh.read()
            fh.close()
        except IOError:
            return False

        self.as_json = json.dumps( xmltodict.parse(raw_file) )
        self.json_set = True
        if save:
            self.save()
        return True


    class Meta:
        verbose_name="XML Submission"
        managed=True


class observed_xpath(models.Model):
    index_file_year = models.IntegerField(blank=True, null=True, help_text="Index file year") 
    version_string = models.CharField(max_length=15, blank=True, null=True)
    raw_xpath = models.CharField(max_length=511, blank=True, null=True)
    num_observed = models.IntegerField(blank=True, null=True, help_text="Index file year") 
    last_update = models.DateTimeField(auto_now=True, null=True)
    observed_type = models.CharField(max_length=511, blank=True, null=True, help_text="character representation of data type, as observed")

    def __unicode__(self):
        return("%s %s" % (self.version_string, self.raw_xpath) )

