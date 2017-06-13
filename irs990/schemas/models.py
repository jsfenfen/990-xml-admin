# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings

# sql for testing/etc
# insert into schemas_productionversion (version_string) select version_string from filing_known_version_string;
#
class ProductionVersion(models.Model):
    version_string = models.CharField(max_length=15, blank=True, null=True)
    # Should this be identical to filing.known_version_string ? 

    def __unicode__(self):
        return self.version_string

class ScheduleName(models.Model):
    schedule_name = models.CharField(max_length=31, blank=True, null=True, help_text="Schedule name", editable=False)
    # Should this include other random stuff ? i.e. INVESTMENTSCORPSTOCKSCHEDULE
    
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
    file_read = models.NullBooleanField(null=True, help_text="Has this file been read? Not all must be, only those we care about and their dependencies.")

    def __unicode__(self):
        return "%s %s" % (self.version_string, self.file_path)

    def get_local_path(self):
        main_dir = "efile990x_%s" % self.version_string
        version_dir = self.version_string
        return os.path.join(settings.SCHEMA_DIR, main_dir, version_dir, self.file_path)

class FileInclude(models.Model):
    version = models.ForeignKey(ProductionVersion, null=True)
    version_string = models.CharField(max_length=15, blank=True, null=True) # denormalize
    source_file = models.ForeignKey(XSDFile, null=True, related_name="source")
    included_file = models.ForeignKey(XSDFile, null=True, related_name="included")


    def __unicode__(self):
        return "%s source_file='%s' included_file='%s'" % (self.version_string, self.source_file, self.included_file)

#class Part(models.Model):
#    part_ordinal_text = models.CharField(max_length=15, blank=True, null=True, help_text="Roman numerals?")
#    ordering = models.IntegerField(null=True, help_text="Integer used to order parts as they appear")
#    schedule = TK


class XSD_Base(models.Model):
    version = models.ForeignKey(ProductionVersion, null=True)
    version_string = models.CharField(max_length=15, blank=True, null=True) # denormalize
    source_file = models.ForeignKey(XSDFile, null=True)
    name = models.CharField(max_length=127, blank=True, null=True, help_text="Name")
    ref = models.CharField(max_length=63, blank=True, null=True, help_text="Ref to another thing")
    xpath = models.CharField(max_length=511, blank=True, null=True)
    description = models.TextField(null=True)
    line_number = models.TextField(null=True)
    type = models.CharField(max_length=127, blank=True, null=True, help_text="type attribute")
    as_json = JSONField(null=True)

    class Meta:
        abstract = True

class SimpleType(XSD_Base):
    def __unicode__(self):
        return "Simple %s %s" % (self.name, self.version_string)

class ComplexType(XSD_Base):
    def __unicode__(self):
        return "Complex %s %s" % (self.name, self.version_string)

class Group(XSD_Base):
    def __unicode__(self):
        return "XSD_Base %s %s" % (self.name, self.version_string)


class Element(XSD_Base):
    min_occurs = models.IntegerField(null=True)
    max_occurs = models.IntegerField(null=True)
    base_type = models.CharField(max_length=63, blank=True, null=True, help_text="")
    max_length = models.IntegerField(null=True, help_text="")
    min_length = models.IntegerField(null=True, help_text="")
    total_digits = models.IntegerField(null=True, help_text="")
    fraction_digits = models.IntegerField(null=True, help_text="")

    data_type = models.CharField(max_length=511, blank=True, null=True, help_text="Internal representation of db column type")
    ## We don't bother with xsd lists, or unions or other rare-ish xsd constructs








