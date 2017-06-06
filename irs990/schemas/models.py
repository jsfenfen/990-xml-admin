# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.db import models
from django.conf import settings

# sql for testing/etc
# insert into schemas_productionversion (version_string) select version_string from filing_known_version_string;
#
class ProductionVersion(models.Model):
    version_string = models.CharField(max_length=15, blank=True, null=True)
    # Should this be identical to filing.known_version_string ? 

    def __unicode__(self):
        return version_string

class ScheduleName(models.Model):
    schedule_name = models.CharField(max_length=31, blank=True, null=True, help_text="Schedule name", editable=False)
    # Can include other forms ? i.e. INVESTMENTSCORPSTOCKSCHEDULE
    
    def __unicode__(self):
        return "%s" % (self.schedule_name)

    class Meta:
        managed=True

class XSDFile(models.Model):
    version = models.ForeignKey(ProductionVersion, null=True)
    version_string = models.CharField(max_length=15, blank=True, null=True) # denormalize
    name=models.CharField(max_length=127, blank=True, null=True, help_text="File name")
    file_path=models.CharField(max_length=511, blank=True, null=True, help_text="relative file from SCHEMA_PATH")
    schedule = models.ForeignKey(ScheduleName, null=True)

    def __unicode__(self):
        return "%s v%s %s" % (self.version_string, self.file_path)

    def get_local_path(self):
        main_dir = "efile990x_%s" % self.version_string 
        return os.path.join(settings.SCHEMA_DIR, main_dir, self.file_path)

