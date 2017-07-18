
import os
from collections import defaultdict, Counter
from filing.type_utils import orderedDictType, listType, unicodeType, noneType
import xmltodict
from schemas.models import SimpleType, XSDFile, FileInclude, Element, Group, ComplexType
from django.conf import settings


SCHEMA_DIR = settings.SCHEMA_DIR

# XSD spec allows "unbounded" as the max occurrence
# but if we're saving in a db, it's useful to make this an int.
STORE_UNBOUNDED_AS = -1 


# Control whether we do each step
# -- used in development
SIMPLE_TYPE = True
INCLUDE_FILE = True
RUN_ELEMENT = True
RUN_GROUP = True
RUN_COMPLEX = True

"""
Undo with: 

delete from schemas_simpletype;
delete from schemas_fileinclude;
delete from schemas_element;
delete from schemas_group;
delete from schemas_complextype;
"""


class XSD_Parser:

    def __init__(self, XSDFileInstance):
        self.xsd_file = XSDFileInstance
        self.file_path = XSDFileInstance.get_local_path()
        self.version_string = XSDFileInstance.version_string
        self.version_string_obj = XSDFileInstance.version

        self.element_count = 0

    def read(self):
        """ Reads the file to dict, doesn't do anything further """
        try:
            fh = open(self.file_path)
            raw_file=fh.read()
            fh.close()
        except IOError:
            print("IO Error with %s" % (self.file_path))
            return False

        self.xsd_dict =  xmltodict.parse(raw_file)
        self.version_string_id = self.xsd_file.pk
        return True

    ### Formatting, fixing

    def max_occurs_to_int(self, max_occurs):
        # max_occurs should be an integer, but 'unbounded' is legal
        # Use error code set above in STORE_UNBOUNDED_AS
        if max_occurs == 'unbounded':
            return(STORE_UNBOUNDED_AS)

        elif max_occurs == '':
            return(1)

        if not max_occurs:
            return (1)
        
        return int(max_occurs)

    ### One-off retrieval functions

    def get_documentation(self, xsdNode):
        """
        Todo: investigate documentation prior to 2012-ish, are there variations of this we need to check for?
        """
        documentation = None

        try:
            documentation = xsdNode['xsd:annotation']['xsd:documentation']
        except KeyError:
            pass

        this_element= {
                'description':None,
                'line_number':None
                }

        if documentation:

            if type(documentation) == unicodeType:
                this_element['description'] = documentation
            
            elif type(documentation) == orderedDictType:
                try:
                    this_element['line_number'] = documentation['LineNumber']
                    print("Found documentation  %s in %s " % (this_element, xsdNode) )

                except KeyError:
                    pass

                try:
                    this_element['description'] = documentation['Description']
                except KeyError:
                    pass

        return this_element


    def get_simple(self, node, version_string=None, version=None, name=None):
        """ 
        Finds data for "simple" types.
        Mapped to schemas.models.SimpleType
        
        """
        #st = SimpleType()
        st = {}

        try:
            st['base_type'] = node['xsd:restriction']['@base']
        except KeyError:
            st['base_type'] = None

        try: 
            st['max_length'] = node['xsd:restriction']['xsd:maxLength']['@value']
        except KeyError:
            st['max_length'] = None

        try: 
            st['max_length'] = node['xsd:restriction']['xsd:maxLength']['@value']
        except KeyError:
            st['max_length'] = None

        try: 
            st['min_length'] = node['xsd:restriction']['xsd:minLength']['@value']
        except KeyError:
            st['min_length'] = None

        try:
            st['fraction_digits'] = node['xsd:restriction']['xsd:fractionDigits']['@value']
        except KeyError:
            st['fraction_digits'] = None

        try:
            st['total_digits'] = node['xsd:restriction']['xsd:totalDigits']['@value']
        except KeyError:
            st['total_digits'] = None

        if version_string:
            st['version_string'] = version_string
        if version:
            st['version'] = version
        if name:
            st['name'] = name

        return st

    def get_common_data(self, node):
        """ Looks for stuff we care about in element / complex / group """
        item_data = {}
        try:
            item_data['type'] = node['@type']
        except KeyError:
            item_data['type'] = None


        try:
            item_data['ref'] = node['@ref']
        except KeyError:
            item_data['ref'] = None
            print("No ref in %s" % node)

        try:
            item_data['min_occurs'] = node['@minOccurs']
        except KeyError:
            item_data['min_occurs'] = None

        try:
            item_data['max_occurs'] = node['@maxOccurs']
        except KeyError:
            item_data['max_occurs'] = None

        item_data['max_occurs']  = self.max_occurs_to_int(item_data['max_occurs']) # Fix 'unbounded'

        return item_data

    def get_xsd_base_data(self, node):
        return_dict = self.get_common_data(node) 
        return_dict.update( self.get_documentation(node) )
        return return_dict

    ## TODO: Instead of pruning only capture minimum... 
    def prune_non_element(self, dict):
        del dict['min_occurs']
        del dict['max_occurs']
        return dict

    ### Parsing stuff  

    def run_include(self, node):
        relative_file_path = node['@schemaLocation']
        included_filepath = os.path.abspath(os.path.join(os.path.dirname(self.file_path) , relative_file_path))
        this_version_base = "efile990x_%s" % (self.version_string)
        this_dir_base = os.path.join(SCHEMA_DIR, this_version_base, self.version_string)
        included_file_relative = os.path.relpath(included_filepath, this_dir_base)
        
        try:
            included_file = XSDFile.objects.get(file_path=included_file_relative, version=self.version_string_obj)

            # Probably not enough of these to make it worth saving in bulk
            (obj, created) = FileInclude.objects.get_or_create(
                source_file=self.xsd_file, 
                included_file=included_file, 
                version=self.version_string_obj, 
                version_string=self.version_string
                )
            if created:
                print("Created include %s" % obj)

        except XSDFile.DoesNotExist:
            print("No match for %s: %s" % (self.version_string_obj, included_file_relative) )
            
            #raise

    ### Next three need refactoring to eliminate redundancy... 

    def run_element(self, node, element_dict, xpath, element_name):
        print("Run element %s %s" % (self.version_string, xpath))
        try:
            Element.objects.get(version=self.version_string_obj,source_file=self.xsd_file, xpath=xpath)
        except Element.DoesNotExist:
            element_dict['xpath']=xpath
            element_dict['name']=element_name
            element_dict['as_json']=node
            element_dict['ordering']=self.element_count
            element_dict['version']=self.version_string_obj
            element_dict['version_string']=self.version_string
            element_dict['source_file']=self.xsd_file
            self.element_count += 1
            Element.objects.create(**element_dict)

    def run_group(self, node, group_dict, xpath, element_name):


        ref = group_dict.get('ref')
        print("Run group %s %s name=%s ref=%s" % (self.version_string, xpath, element_name, group_dict.get('ref')))
        try:
            Group.objects.get(version=self.version_string_obj,source_file=self.xsd_file, xpath=xpath, ref=ref)
        except Group.DoesNotExist:
            group_dict['xpath']=xpath
            group_dict['name']=element_name
            group_dict['as_json']=node
            group_dict['ordering']=self.element_count
            group_dict['version']=self.version_string_obj
            group_dict['version_string'] = self.version_string
            group_dict['source_file']=self.xsd_file
            self.element_count += 1
            group_dict = self.prune_non_element(group_dict)
            Group.objects.create(**group_dict)
            print("Group created")

    def run_complex(self, node, complex_dict, xpath, complex_name):

        print("Run complex %s %s" % (self.version_string, xpath))
        try:
            ComplexType.objects.get(version=self.version_string_obj,source_file=self.xsd_file, xpath=xpath)
        except ComplexType.DoesNotExist:
            complex_dict['xpath']=xpath
            complex_dict['name']=complex_name
            complex_dict['as_json']=node
            complex_dict['ordering']=self.element_count
            complex_dict['version']=self.version_string_obj
            complex_dict['version_string'] = self.version_string
            complex_dict['source_file']=self.xsd_file
            self.element_count += 1
            complex_dict = self.prune_non_element(complex_dict)
            ComplexType.objects.create(**complex_dict)
            print("Complex created: %s" % complex_dict)
 


    def parse_ordered_dict(self, node, parent_path="", parent_documentation=[], parent_type=""):

        this_node_type = type(node)

        if this_node_type == unicodeType:
            #print("Unicode type: %s %s" % (node, parent_path))
            pass
        
        elif this_node_type == listType:
            #print("listType %s" % (parent_path))
            for child_node in node:
                self.parse_ordered_dict(child_node, parent_path=parent_path, parent_documentation=parent_documentation, parent_type=parent_type)
        

        elif this_node_type == orderedDictType:

            element_name = ""
            try:
                element_name=node['@name']
            except KeyError:
                # In general we only care about elements with names
                pass

            if element_name:
                parent_path = parent_path + "/" + element_name

            # record groups if they have no name but a ref.
            if parent_type=="xsd:group":
                if RUN_GROUP:
                    print("\n\nGot xsd:group: %s\n\n" % node)
                    self.run_group(node, self.get_xsd_base_data(node), parent_path, element_name)

            if parent_type=="xsd:element":
                if RUN_ELEMENT: 
                    print( "Element %s :  %s" % (node, element_name) ) 
                    self.run_element(node, self.get_xsd_base_data(node), parent_path, element_name)            

            elif parent_type=="xsd:include":
                if INCLUDE_FILE:
                    self.run_include(node)

            elif parent_type=="xsd:complexType":
                if RUN_COMPLEX:
                    self.run_complex(node, self.get_xsd_base_data(node), parent_path, element_name)


            elif parent_type=="xsd:simpleType":
                if SIMPLE_TYPE:
                    if element_name:
                        simple_data = self.get_simple(node, name=element_name,version_string=self.version_string, version=self.version_string_obj)
                        simple_data.update(self.get_documentation(node))
                        simple_data['source_file'] = self.xsd_file
                        
                        try:
                            SimpleType.objects.get(source_file=self.xsd_file, name=element_name)


                        except SimpleType.DoesNotExist:
                            SimpleType.objects.create(**simple_data)

            keys = node.keys()
            for key in keys:
                self.parse_ordered_dict(node[key], parent_path=parent_path, parent_documentation=parent_documentation, parent_type=key)

        elif this_node_type == noneType:
            pass

        else:
            raise Exception ("Unknown type: %s" % (type(node)))

    def parse(self):
        read = self.read()

        self.element_count = 0


        if read:
            self.parse_ordered_dict(self.xsd_dict)
        else:
            print("Skipping")

