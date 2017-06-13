
import os
from collections import defaultdict, Counter
from filing.type_utils import orderedDictType, listType, unicodeType, noneType
import xmltodict
from schemas.models import SimpleType, XSDFile, FileInclude
from django.conf import settings


SCHEMA_DIR = settings.SCHEMA_DIR

# Control whether we do each step
# -- used in development
SIMPLE_TYPE = True
INCLUDE_FILE = True
# PROCESS_ELEMENT = False
# PROCESS_GROUP = False
# PROCESS_COMPLEX = False


def count_children(orderedDict):

    for key in orderedDict.keys():
        print "key %s" % (key)

def add_documentation(node, obj, force_save=False):
    """
    Adds line_number and description when available to existing model.
    Checks a variety of places, is there a versioned approach usable? 
    """
    documentation = None

    try:
        documentation=documentation = node['xsd:annotation']['xsd:documentation']
    except KeyError:
        #print "No documentation in %s" % (node)
        return None
    num_found = 0 # Did we find any documentation?
    
    if type(documentation) == unicodeType:
        obj.description = documentation

    elif type(documentation) == orderedDictType:
        try:
            obj.line_number = documentation['LineNumber']
            print("Line number: %s" % obj.line_number)
            num_found += 1
        except KeyError:
            pass

        try:
            obj.description = documentation['Description']
            print("description: %s" % obj.description)
            num_found += 1
        except KeyError:
            pass         

    if num_found>0:
        if force_save:
            obj.save()
        return obj

    return None # No need to save if we found nothing.
"""

def get_documentation(xsdNode):
    documentation = ""
    try:
        documentation = xsdNode['xsd:annotation']['xsd:documentation']
    except KeyError:
        pass
    this_element= defaultdict(lambda:'')

    if documentation:
        if type(documentation) == unicodeType:
            this_element['description'] = documentation
        
        elif type(documentation) == orderedDictType:
            try:
                this_element['line_number'] = documentation['LineNumber']
            except KeyError:
                pass

            try:
                this_element['description'] = documentation['Description']
            except KeyError:
                pass

    return this_element

"""

def get_simple(node, version_string=None, version=None, name=None):
    """ 
    Finds data for "simple" types.
    Mapped to schemas.models.SimpleType
    
    """
    st = SimpleType()

    try:
        st.base_type=node['xsd:restriction']['@base']
    except KeyError:
        pass

    try: 
        st.max_length = node['xsd:restriction']['xsd:maxLength']['@value']
    except KeyError:
        pass

    try: 
        st.max_length = node['xsd:restriction']['xsd:maxLength']['@value']
    except KeyError:
        pass

    try: 
        st.min_length = node['xsd:restriction']['xsd:minLength']['@value']
    except KeyError:
        pass

    try:
        st.fraction_digits=node['xsd:restriction']['xsd:fractionDigits']['@value']
    except KeyError:
        pass

    try:
        st.total_digits=node['xsd:restriction']['xsd:totalDigits']['@value']
    except KeyError:
        pass

    if version_string:
        st.version_string=version_string
    if version:
        st.version=version
    if name:
        st.name = name

    add_documentation(node, st)
    return st



class XSD_Parser:

    def __init__(self, XSDFileInstance):
        self.xsd_file = XSDFileInstance
        self.file_path = XSDFileInstance.get_local_path()
        self.version_string = XSDFileInstance.version_string
        self.version_string_obj = XSDFileInstance.version

    def read(self):
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
                # In general we only care about named elements with names
                pass

            if element_name:
                parent_path = parent_path + "/" + element_name
            

            if parent_type=="xsd:element":
                pass


            elif parent_type=="xsd:include":
                if INCLUDE_FILE:
                    relative_file_path = node['@schemaLocation']
                    included_filepath = os.path.abspath(os.path.join(os.path.dirname(self.file_path) , relative_file_path))
                    this_version_base = "efile990x_%s" % (self.version_string)
                    this_dir_base = os.path.join(SCHEMA_DIR, this_version_base, self.version_string)
                    included_file_relative = os.path.relpath(included_filepath, this_dir_base)
                    
                    try:
                        included_file = XSDFile.objects.get(file_path=included_file_relative, version=self.version_string_obj)

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
                        raise
                            

            elif parent_type=="xsd:group":
                #print("Got xsd:group")
                pass

            elif parent_type=="xsd:complexType":
                #print("Got xsd:complexType")
                pass

            elif parent_type=="xsd:simpleType":
                if element_name:
                    
                    simple_data = get_simple(node, name=element_name,version_string=self.version_string, version=self.version_string_obj)
                    if SIMPLE_TYPE:
                        print("Saving simple type %s" % (simple_data))
                        simple_data.save()


            keys = node.keys()
            for key in keys:
                self.parse_ordered_dict(node[key], parent_path=parent_path, parent_documentation=parent_documentation, parent_type=key)

        elif this_node_type == noneType:
            pass

        else:
            raise Exception ("Unhandled type: %s" % (type(node)))

    def parse(self):
        read = self.read()
        if read:
            self.parse_ordered_dict(self.xsd_dict)
        else:
            print("Skipping")

