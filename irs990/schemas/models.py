# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings


class ProductionVersion(models.Model):
    version_string = models.CharField(max_length=15, blank=True, null=True)
    # This is different than filing.known_version_string because it only 
    # contains versions we will process, but...
    # insert into schemas_productionversion (version_string) select version_string from filing_known_version_string;

    def __unicode__(self):
        return self.version_string


class ScheduleName(models.Model):
    """ The names of schedules we 'support'. Enter from fixtures, TK """
    schedule_name = models.CharField(max_length=31, blank=True, null=True, help_text="Schedule name", editable=False)
    xml_root_path = models.CharField(max_length=255, blank=True, null=True, help_text="", editable=False)
        
    def __unicode__(self):
        return "%s" % (self.schedule_name)

    class Meta:
        managed=True

class SchedulePart(models.Model):
    db_model_name = models.CharField(max_length=64, blank=True, null=True, help_text="db compliant name")
    ordering_ordinal = models.IntegerField(null=True, blank=True, help_text="sort order of parts")
    parent_sked = models.ForeignKey(ScheduleName)
    raw_part_name = models.CharField(max_length=511, blank=True, null=True, help_text="From corrected XSD files")
    canonical_version_string = models.CharField(max_length=15, blank=True, null=True, help_text="What version were the canonical form parts derived from?") 


    def __unicode__(self):
        return "%s - %s " % (self.raw_part_name, self.parent_sked)

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

class ScheduleInstance(models.Model):

    schedule_instance = models.ForeignKey(XSDFile, null=True)
    version_string = models.CharField(max_length=15, blank=True, null=True)
    schedule_name = models.CharField(max_length=31, blank=True, null=True, help_text="Schedule name", editable=False)
    schedule_type = models.ForeignKey(ScheduleName, null=True)

    def __unicode__(self):
        return "%s - %s - %s" % (self.schedule_year, self.schedule_version, self.schedule_type.schedule_name)

###### Stuff below is contents of XSD files, helper classes


class FileInclude(models.Model):
    version = models.ForeignKey(ProductionVersion, null=True)
    version_string = models.CharField(max_length=15, blank=True, null=True) # denormalize
    source_file = models.ForeignKey(XSDFile, null=True, related_name="source")
    included_file = models.ForeignKey(XSDFile, null=True, related_name="included")


    class Meta:
        unique_together = (("source_file", "included_file", "version"),)

    def __unicode__(self):
        return "%s source_file='%s' included_file='%s'" % (self.version_string, self.source_file, self.included_file)

class NoJSONManager(models.Manager):
    # Django's default is to return all models on all queries
    # We don't want it to return the json unless we really want it
    def get_queryset(self):
        # should we pass the field names in as args, not hard code this?
        return super(NoJSONManager, self).get_queryset().defer('as_json')

class XSD_Base(models.Model):
    """
    Base class for things that we find in the XSD files that we care about
    """
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

    # Specify objects with or without json
    objects = models.Manager()
    objects_no_json = NoJSONManager()

    class Meta:
        abstract = True

    # This logic should go somewhere else, and get simplified
    # Probably there should be an object version of this
    def get_standardized_hash(self, 
                                process_runs=None, 
                                xsd_type=None, 
                                xsd_prefix=None, 
                                ignore_name=False,
                                parent_ordering=None  
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

        ordering = None
        try:
            ordering = self.ordering
        except AttributeError:
            pass


        if parent_ordering and process_runs > 1:
            if process_runs==2:
                ordering = parent_ordering + (self.ordering / 1000.0)
            elif process_runs==3:
                ordering = parent_ordering + (self.ordering / 1000000.0)
            else:
                ordering = parent_ordering

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


### Could prob refactor the common fields: 

class CanonicalGroup(models.Model):
    db_safe_name = models.CharField(max_length=64, blank=True, null=True, help_text="database compliant name")
    original_xpath = models.CharField(max_length=255, blank=True, null=True, help_text="xpath in the canonical version, may not be correct for all")
    name = models.CharField(max_length=127, blank=True, null=True, help_text="Name")
    version = models.ForeignKey(ProductionVersion, null=True)
    version_string = models.CharField(max_length=15, blank=True, null=True, help_text="denormalized version string")
    parent_sked = models.ForeignKey(ScheduleName, null=True)
    parent_sked_part= models.ForeignKey(SchedulePart, null=True)
    ordering = models.IntegerField(null=True, help_text="Integer used to order groups within a form")
    empty_head = models.NullBooleanField(default=False, help_text="If the corresponding variable doesn't take variables, this is true")



class CanonicalVariable(models.Model):
    db_safe_name = models.CharField(max_length=64, blank=True, null=True, help_text="database compliant name")
    original_xpath = models.CharField(max_length=255, blank=True, null=True, help_text="xpath in the canonical version, may not be correct for all")
    version = models.ForeignKey(ProductionVersion, null=True)
    version_string = models.CharField(max_length=15, blank=True, null=True, help_text="denormalized version string")
    description = models.TextField(null=True)
    line_number = models.TextField(null=True)
    in_a_group = models.NullBooleanField(default=False, help_text="Is this variable in a group")
    parent_group = models.ForeignKey(CanonicalGroup, null=True, help_text="Link to canonical group", on_delete=models.SET_NULL)
    parent_sked = models.ForeignKey(ScheduleName, null=True)
    parent_sked_part= models.ForeignKey(SchedulePart, null=True)
    ordering = models.FloatField(null=True, help_text="non-integer used to order groups within a form")
    irs_type = models.CharField(max_length=255, blank=True, null=True, help_text="IRS type, as recorded")
    raw_type = models.CharField(max_length=255, blank=True, null=True, help_text="native type before translation to django / sql alchemy")
    django_type = models.CharField(max_length=255, blank=True, null=True, help_text="Literal type for django")
    sql_alch_type = models.CharField(max_length=255, blank=True, null=True, help_text="Literal type for sql alchemy")  

    ## vars from NODC
    var_name = models.CharField(max_length=255, blank=True, null=True, help_text="native type before translation to django / sql alchemy")
    full_name = models.CharField(max_length=255, blank=True, null=True, help_text="full name per NODC")
    scope = models.CharField(max_length=255, blank=True, null=True, help_text="scope")

    ## NODC var but populated by PP
    required = models.NullBooleanField(default=False)

class VersionedGroup(models.Model):
    name = models.CharField(max_length=127, blank=True, null=True, help_text="Name")
    xpath = models.CharField(max_length=255, blank=True, null=True, help_text="xpath style key")
    version = models.ForeignKey(ProductionVersion, null=True)
    version_string = models.CharField(max_length=15, blank=True, null=True, help_text="denormalized version string")
    parent_sked = models.ForeignKey(ScheduleName, null=True)
    parent_sked_part= models.ForeignKey(SchedulePart, null=True)
    ordering = models.IntegerField(null=True, help_text="Integer used to order groups within a form")
    canonical_group = models.ForeignKey(CanonicalGroup, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return "VersionedGroup %s %s" % (self.name, self.version_string)

class VersionedVariable(models.Model):
    name = models.CharField(max_length=127, blank=True, null=True, help_text="Name")
    xpath = models.CharField(max_length=255, blank=True, null=True, help_text="xpath style key")
    description = models.TextField(null=True)
    line_number = models.TextField(null=True)
    version = models.ForeignKey(ProductionVersion, null=True)
    version_string = models.CharField(max_length=15, blank=True, null=True, help_text="denormalized version string")
    parent_sked = models.ForeignKey(ScheduleName, null=True)
    parent_sked_part= models.ForeignKey(SchedulePart, null=True)
    ordering = models.FloatField(null=True, help_text="non-integer used to order groups within a form")
    in_a_group = models.NullBooleanField(default=False, help_text="Is this variable in a group")
    parent_group = models.ForeignKey(VersionedGroup, null=True, help_text="If this is in_a_group, link to it. ")
    irs_type = models.CharField(max_length=255, blank=True, null=True, help_text="IRS type, as recorded")
    django_type = models.CharField(max_length=255, blank=True, null=True, help_text="Literal type for django")
    sql_alch_type = models.CharField(max_length=255, blank=True, null=True, help_text="Literal type for sql alchemy")  
    canonical_variable = models.ForeignKey(CanonicalVariable, null=True, on_delete=models.SET_NULL)

    # to add: link to lookup table for certain types: states, countries, etc. 

    def __unicode__(self):
         return "VersionedVariable %s %s" % (self.xpath, self.version_string)

    



