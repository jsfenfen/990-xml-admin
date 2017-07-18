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


    class Meta:
        unique_together = (("source_file", "included_file", "version"),)

    def __unicode__(self):
        return "%s source_file='%s' included_file='%s'" % (self.version_string, self.source_file, self.included_file)

#class Part(models.Model):
#    part_ordinal_text = models.CharField(max_length=15, blank=True, null=True, help_text="Roman numerals?")
#    ordering = models.IntegerField(null=True, help_text="Integer used to order parts as they appear")
#    schedule = TK



class NoJSONManager(models.Manager):
    def get_queryset(self):
        # should we pass the field names in as args, not hard code this?
        return super(NoJSONManager, self).get_queryset().defer('as_json')


"""
            'name':initial_root.name, 
            'xpath':initial_root.xpath, 
            'documentation':initial_root.description, 
            'line_number':initial_root.line_number, 
            'derived_path':initial_root.xpath, 
            'type':initial_root.type,
            'process_runs':0}
"""


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
    min_occurs = models.IntegerField(null=True)
    max_occurs = models.IntegerField(null=True)
    as_json = JSONField(null=True)


    # convenience method so django doesn't return us the json
    # since the json objs can be rather large
    objects = models.Manager()
    objects_no_json = NoJSONManager()

    class Meta:
        abstract = True

    def get_standardized_hash(self, 
                                process_runs=None, 
                                xsd_type=None, 
                                xsd_prefix=None, 
                                ignore_name=False, 
                            ):

        derived_xpath = self.xpath
        ordering = None
        try:
            ordering = self.ordering
        except AttributeError:
            pass

        if xsd_prefix:
            if ignore_name:
                derived_xpath = xsd_prefix
            else:
                derived_xpath = xsd_prefix +"/"+ self.name

        if derived_xpath:          
            derived_xpath = derived_xpath.replace("//","/")
        print ("Get standardized hash '%s'   '%s'  '%s'" % (self.name, derived_xpath, self.xpath))
        return {            
            'name':self.name, 
            'xpath':self.xpath, 
            'type':self.type,
            'ref':self.ref,
            'process_runs':process_runs,
            'documentation':self.description,
            'line_number':self.line_number,
            'xsd_type':xsd_type,
            'derived_xpath':derived_xpath,
            'min_occurs':self.min_occurs,
            'max_occurs':self.max_occurs,
            'ordering':ordering,
            'id':self.pk
        }

        

class SimpleType(XSD_Base):
    base_type = models.CharField(max_length=63, blank=True, null=True, help_text="")
    max_length = models.IntegerField(null=True, help_text="")
    min_length = models.IntegerField(null=True, help_text="")
    total_digits = models.IntegerField(null=True, help_text="")
    fraction_digits = models.IntegerField(null=True, help_text="")

    def __unicode__(self):
        return "Simple %s %s" % (self.name, self.version_string)

class ComplexType(XSD_Base):
    ordering = models.IntegerField(null=True, help_text="Integer used to order parts as they appear")

    def __unicode__(self):
        return "Complex %s %s" % (self.name, self.version_string)

class Group(XSD_Base):
    ordering = models.IntegerField(null=True, help_text="Integer used to order parts as they appear")

    def __unicode__(self):
        return "XSD_Base %s %s" % (self.name, self.version_string)


class Element(XSD_Base):
    base_type = models.CharField(max_length=63, blank=True, null=True, help_text="")
    max_length = models.IntegerField(null=True, help_text="")
    min_length = models.IntegerField(null=True, help_text="")
    total_digits = models.IntegerField(null=True, help_text="")
    fraction_digits = models.IntegerField(null=True, help_text="")
    ordering = models.IntegerField(null=True, help_text="Integer used to order parts as they appear")

    data_type = models.CharField(max_length=511, blank=True, null=True, help_text="Internal representation of db column type")
    ## We don't bother with xsd lists, or unions or other rare-ish xsd constructs

    def __unicode__(self):
        return "Element %s %s %s" % (self.name, self.version_string, self.xpath)







