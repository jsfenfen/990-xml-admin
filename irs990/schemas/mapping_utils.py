import xmltodict
import json
import csv

from schemas.models import XSDFile, ProductionVersion, FileInclude, Element, \
    Group, ComplexType, SimpleType


from filing.stats_utils import json_stats_tracker
from filing.models import xml_submission, observed_xpath



# fix for name tobe
from filing.models import observed_xpath as ObservedXpath



class XSDReader(object):
    
    def __init__(self, xsdfile_obj):

        if not xsdfile_obj:
            # Ideally we wouldn't see this
            # but better to flag now
            raise RuntimeError("Must include xsdfile_obj!")

        self.xsdfile_obj = xsdfile_obj

        # shorthand
        self.version_string = xsdfile_obj.version_string

        # Retrieve relevent elements from db once and hash them in the below
        self.all_named_entities = {} 


        self.simpletypes = {}

        self.unprocessed_elements = []
        self.unprocessed_complextypes = []
        self.unprocessed_groups = []


        self.group_roots = {}

        self.file_dependency_pk_list = []


        # put the 'derived' xpaths by following types / unpacking complex types. 
        self.derived_keys = {}



    def mappings_from_sample_file(self, sample_file, key_prefix):
        """ Test a set of mappings against a sample xml file """ 


        print("Reading from sample file %s" % sample_file)
        raw_file = open(sample_file).read()
        as_json = json.dumps( xmltodict.parse(raw_file)['Return']['ReturnData'] )
        #print("File as json is: %s" % as_json)
        jst = json_stats_tracker(json.loads(as_json))  
        (self.xpath_counter, self.list_root_counter) = jst.parse()
        print ("Len self.xpath_counter %s" % (len(self.xpath_counter) ))

        
        total = 0
        failures = 0

        keylist = self.xpath_counter.keys()
        for key in keylist.sorted:

            # Ignore @attributes or #ids in the xml
            # Which appear like this:
            # /IRS990/ReportLandBuildingEquipmentInd/@referenceDocumentId
            # We make no attempt to match IRS' documentids

            # There are a few important bits buried in attributes, maybe in the return header?
            # but not worth testing for here

            name = key.split("/")[-1]
            if name.find('#')==0 or name.find('@')==0:
                continue

            if key.startswith(key_prefix):
                total += 1
                try:
                    self.derived_keys[key]
                    print("Succeeded on key '%s'" % key)

                except KeyError:
                    print("Failed on key '%s'" % key)
                    failures += 1

        print ("Total failures %s totals %s" % (failures, total))
    

    def mappings_from_db(self, xpath_prefix="/Return/ReturnData/IRS990/"):
        """ Test against all element mappings from the db. Fails if that version hasn't been entered! """

        version = self.version_string
        elements = observed_xpath.objects.filter(version_string=version, raw_xpath__startswith=xpath_prefix).values('raw_xpath').distinct().order_by('raw_xpath')
        if len(elements)==0:
            print("No elements found matching version string %s" % version)
            return None
        total = 0
        failures = 0
        for element in elements:
            raw_key = element['raw_xpath']
            key = raw_key.replace("/Return/ReturnData/","/")

            name = key.split("/")[-1]
            if name.find('#')==0 or name.find('@')==0:
                continue


            try:
                self.derived_keys[key]
                self.derived_keys[key]['isfound']=True

                print("Succeeded on key '%s' " % (key))
                total += 1
            except KeyError:
                print("Failed on key '%s'" % key)
                failures += 1

        print ("Total failures %s totals %s" % (failures, total))

        # Now find unused keys.
        # Having unused legal keys is *not* an error, it just means tax preparers didn't 
        # use every last possible legal field. (e.g. 'business name line 2')
        unused = 0
        keylist = self.derived_keys.keys()
        keylist.sort()
        for key in keylist:
            thisdata = self.derived_keys[key]
            try:
                thisdata['isfound']
            except KeyError:
                print("Unused key: %s" % (key) )
                unused += 1

        print("Total unused keys %s" % unused)
        explanation = """
            Unused keys do not mean there's an error.
            Some group root keys appear here 
            Also some rare keys are legitimately not used.
        """
        print(explanation)



    def hash_by_name(self):
        """ Hash elements, simple types and complex types together so we can look up in one step """

        all_simpletypes = SimpleType.objects_no_json.filter(source_file__pk__in=self.file_dependency_pk_list)
        print ("Adding Simples with %s" % self.file_dependency_pk_list)
        for e in all_simpletypes:
            print ("Adding simpletype %s" % e)
            self.all_named_entities[e.name] =   e.get_standardized_hash(process_runs=0, xsd_type='simple') 


        all_complextypes = ComplexType.objects_no_json.filter(source_file__pk__in=self.file_dependency_pk_list)
        print ("Adding Complexs with %s" % self.file_dependency_pk_list)
        for e in all_complextypes:

            # why are these coming without names? 
            if e.name:
                print("Adding complextype %s" % e.name)
                self.all_named_entities[e.name] =   e.get_standardized_hash(process_runs=0, xsd_type='complex') 


        all_groups = Group.objects_no_json.filter(source_file__pk__in=self.file_dependency_pk_list)
        print ("Adding groups with %s" % self.file_dependency_pk_list)
        for g in all_groups:

            # why are these coming without names? 
            if g.name:
                print("Adding group %s" % g.name)
                self.all_named_entities[g.name] = g.get_standardized_hash(process_runs=0, xsd_type='group') 


    def resolve_type(self, type_name):
        try:
            this_type = self.all_named_entities[type_name]
            return this_type
        except KeyError:
            print ("***Not found %s" % type_name)
            return None

    def test_for_repeating(self, element_dict):
        max_occurs = element_dict.get('max_occurs')
        print("Max_occurs '%s'" % max_occurs)
        if not max_occurs:
            return False

        if max_occurs <> 1:
            print("Found repeating group root: '%s'" % (element_dict['derived_xpath']) )

            try:
                self.group_roots[element_dict['derived_xpath']]+= 1
            except KeyError:
                self.group_roots[element_dict['derived_xpath']] = 1

            return True



    def process_child_element(self, child, parent, search_xpath):

        xpath_name = child.xpath.split(search_xpath + "/")[-1]
        if xpath_name.find('/')>-1:
            print("*** excluding element  grandchild %s" % xpath_name)
            return False

        print("Found complex child element named %s type: %s xpath raw: %s" % (child.name, child.type, child.xpath) )

        child_data = None

        ## Is it a simple type? 
        if child.type:
            this_type = self.resolve_type(child.type)
            
            if this_type['xsd_type']=='simple': 
                
                child_data = child.get_standardized_hash(process_runs=parent['process_runs']+1, 
                                                            xsd_type='element', 
                                                            xsd_prefix=parent['derived_xpath']                                                                ) 
                self.unprocessed_elements.append(child_data)
                child_data = self.add_documentation(child_data, parent['line_number'], parent['name'], parent['documentation'] )


            elif this_type['xsd_type']=='complex':
                child_data = child.get_standardized_hash(process_runs=parent['process_runs']+1, 
                                                        xsd_type='complex', 
                                                        xsd_prefix=parent['derived_xpath']                                                            ) 
                child_data = self.add_documentation(child_data, parent['line_number'], parent['name'], parent['documentation'] )
                print("Adding complex child %s process runs %s" % (child_data, parent['process_runs'] ) )
                self.unprocessed_complextypes.append(child_data)

        else:
            # treat as simple type ? This may be wrong. 
            child_data = child.get_standardized_hash(process_runs=parent['process_runs']+1, 
                                                    xsd_type='element', 
                                                    xsd_prefix=parent['derived_xpath']
                                                    )
            child_data = self.add_documentation(child_data, parent['line_number'], parent['name'], parent['documentation'] )

            #

            self.unprocessed_elements.append(child_data)

        self.test_for_repeating(child_data)

        return True



    def process_element(self, element):
        """ Add the element, hashed by it's derived key
        """
        ## Elements can have unnamed complex types.
        ## We only generally care about named complex types
        ## In this instance, treat any children of this element
        ## as if they are part of an anonymous complex type
        ## the vast majority of elements *do not* have this
        ## So perhaps we need a more streamlined way of testing?

        ## It's also possible we should handle this differently upstream
        ## by explicitly assigning these a parent name?

        search_xpath = element['xpath']
        if element.get('type'):
            search_xpath="/" + element.get('type')

        print("process_element: %s" % element)
        child_elements = Element.objects_no_json.filter(source_file__pk__in=self.file_dependency_pk_list, xpath__startswith=search_xpath).order_by('name')
        print ("Num results %s for process_element %s" % (len(child_elements), element['xpath']))

        for child in child_elements:
            self.process_child_element(child, element, search_xpath)

        self.derived_keys[element['derived_xpath']]=element



    def add_documentation(self, child_data, line_number, name, documentation):
        # refactor this when we know what we want

        if line_number:
            if child_data['line_number']:
                child_data['line_number'] = "%s; [%s] %s" % (line_number, child_data['name'], child_data['line_number']) 
            else:
                child_data['line_number'] = "%s" % (line_number) 

        else:
            if child_data['line_number']:
                child_data['line_number'] = "[%s] %s" % (child_data['name'], child_data['line_number']) 
            else:
                child_data['line_number'] = ""  


        if documentation:
            if child_data['documentation']:
                child_data['documentation'] = "%s; [%s] %s" %  (documentation, child_data['name'], child_data['documentation'])
            else:
                child_data['documentation'] = "%s" % (documentation) 

        else:

            if child_data['documentation']:
                child_data['documentation'] = "[%s] %s" %  (child_data['name'], child_data['documentation'])
            else:
                child_data['documentation'] = ""

        return child_data

    def process_complex(self, complex):
        """ Process a complex type and add children entities
         to processing queue.
        """
        # 
        print("process complex %s : %s" % (complex, complex['derived_xpath'] ) )

        search_xpath = complex['xpath']
        if complex.get('type'):
            search_xpath="/" + complex.get('type')

        child_elements = Element.objects_no_json.filter(source_file__pk__in=self.file_dependency_pk_list, xpath__startswith=search_xpath).order_by('name')
        print ("Num results %s for %s" % (len(child_elements), search_xpath))
        for child in child_elements:
            self.process_child_element(child, complex, search_xpath)

        # child groups
        child_groups = Group.objects_no_json.filter(source_file__pk__in=self.file_dependency_pk_list, xpath__startswith=search_xpath )
        for child_group in child_groups:
            child_data = child_group.get_standardized_hash(process_runs=complex['process_runs']+1, xsd_type='group', xsd_prefix=complex['derived_xpath'], ignore_name=False) 
            child_data = self.add_documentation(child_data, complex['line_number'], complex['name'], complex['documentation'] )
            self.unprocessed_groups.append(child_data)
            self.test_for_repeating(child_data)

        # child complexes ? Thus far not needed ? Not sure they're legal?


    def process_group(self, group):
        """ Process a group and add children entities
         to processing queue.
        """
        print("Process group %s" % group)

        # Some are id'ed by ref and don't have a name
        resolved_type = None
        if group['ref']:
            ## It's a group that's just a reference to something else. 
            group_type = group['ref']


            resolved_type = self.resolve_type(group_type)
            print("Group %s resolved to %s" % (group, resolved_type) )

            if resolved_type['xsd_type']=='group':

                print "id is %s" % resolved_type['id']
                child_group = Group.objects.get(pk=resolved_type['id'])
                child_data = child_group.get_standardized_hash(process_runs=group['process_runs']+1, xsd_type='group', xsd_prefix=group['derived_xpath'], ignore_name=True) 
                child_data = self.add_documentation(child_data, group['line_number'], group['name'], group['documentation'] )
                print "Child data: %s" % (child_data)
                self.unprocessed_groups.append(child_data)
                self.test_for_repeating(child_data)

            else:
                print("Group linked to non-group?")
                assert False
        else:
            resolved_type = self.resolve_type(group['name'])



        ## Get children of this group:
        search_xpath = resolved_type.get('xpath')
        print("Search xpath is '%s'" % search_xpath)

        # this will get grandchild elements as well, but making django's iregex filter work to ignore these is super annoying
        child_elements =  Element.objects_no_json.filter(source_file__pk__in=self.file_dependency_pk_list, xpath__startswith=search_xpath).order_by('name')
        #  Could use a regex like [^\/], but using backslashes and slashes within regexes leads to escaping craziness
        #  Works from terminal: Element.objects.filter(xpath__iregex=r'\/IRS990Type\/[^\/]+\Z')

        for child in child_elements:

            child_xpath = child.xpath
            xpath_name = child_xpath.split(search_xpath + "/")[-1]

            # Rest of hack to exclude grandchildren; make them wait their turn. 
            if xpath_name.find('/')>-1:
                print("*** excluding group grandchild %s" % child_xpath)
                continue

            print("Got child '%s'  ref %s  of group '%s'type %s" % (child.name, group['ref'], group['name'], child.type) )
            ## Is it a simple type? 
            if child.type:
                this_type = self.resolve_type(child.type)
                
                if this_type['xsd_type']=='simple': 
                    
                    child_data = child.get_standardized_hash(process_runs=0, 
                                                                xsd_type='element', 
                                                                xsd_prefix=group['derived_xpath']
                                                                ) 
                    self.unprocessed_elements.append(child_data)
                    child_data = self.add_documentation(child_data, group['line_number'], group['name'], group['documentation'] )


                elif this_type['xsd_type']=='complex':

                    child_data = child.get_standardized_hash(process_runs=complex['process_runs']+1, 
                                                            xsd_type='complex', 
                                                            xsd_prefix=group['derived_xpath'], 
                                                            ignore_name=False
                                                            ) 
                    print("complex derived_xpath: %s xpath: %s " % (group['derived_xpath'], ))
                    child_data = self.add_documentation(child_data, group['line_number'], group['name'], group['documentation'] )
                    self.unprocessed_complextypes.append(child_data)

            else:
                    child_data = child.get_standardized_hash(process_runs=0, 
                                                            xsd_type='element', 
                                                            xsd_prefix=group['derived_xpath']
                                                            )
                    child_data = self.add_documentation(child_data, group['line_number'], group['name'], group['documentation'] )
                    self.unprocessed_elements.append(child_data)

        # groups that are children of groups.

        if group['process_runs'] < 10:
            ## Only run this if we haven't already added a group child
            ## Hack to prevent repeating children of children groups? 


            child_groups =  Group.objects_no_json.filter(source_file__pk__in=self.file_dependency_pk_list, xpath__startswith=search_xpath).exclude(pk=group['id']).order_by('name')
            #  Could use a regex like [^\/], but using backslashes and slashes within regexes leads to escaping craziness
            #  Works from terminal: Element.objects.filter(xpath__iregex=r'\/IRS990Type\/[^\/]+\Z')
        else:
            child_groups = []

        for child in child_groups:


            child_xpath = child.xpath
            xpath_name = child_xpath.split(search_xpath + "/")[-1]

            # Rest of hack to exclude grandchildren; make them wait their turn. 
            if xpath_name.find('/')>-0:
                print("*** excluding group grandchild %s" % child_xpath)
                continue

            print("GRoup within group!")

            child_data = child.get_standardized_hash(process_runs=10, xsd_type='group', xsd_prefix=group['derived_xpath'], ignore_name=True) 
            child_data = self.add_documentation(child_data, group['line_number'], group['name'], group['documentation'] )
            print "Child data: %s" % (child_data)
            self.unprocessed_groups.append(child_data)



    def print_lengths(self):
        print("\n\nUnprocessed elements: %s current elements: %s" % (len(self.unprocessed_elements), len(self.current_elements) ) )
        print("Unprocessed complexes: %s current complexes: %s" % (len(self.unprocessed_complextypes), len(self.current_complextypes) ) )
        print("Unprocessed groups: %s current groups: %s" % ( len(self.unprocessed_groups), len(self.current_groups)))

    def process_once(self):
        """ 
        Process one level of xml. If there are children, put them in unprocessed lists.
        Return the number of outstanding items (if 0, we are done)
        """

        # transfer the unprocessed queue to processing_queue
        self.current_elements = self.unprocessed_elements
        self.unprocessed_elements = []

        self.current_complextypes = self.unprocessed_complextypes
        self.unprocessed_complextypes = []

        self.current_groups = self.unprocessed_groups
        self.unprocessed_groups = []

        # Now run them each
        for this_group in self.current_groups:
            #print("Processing group: %s" % this_group)
            self.process_group(this_group)

        for this_element in self.current_elements:
            self.process_element(this_element)

        print("before complex")
        self.print_lengths()

        for this_complex in self.current_complextypes:
            #print("Processing complex: %s" % this_complex)
            self.process_complex(this_complex)

        print("after complex...")
        self.print_lengths()
        return (len(self.unprocessed_elements) + len(self.unprocessed_complextypes) + len(self.unprocessed_groups) )

    def run(self):
        """ Process repeatedly until there are no elements left """
        while True:
            num_results = self.process_once()
            if num_results == 0:
                break

    def start_from_root_element(self, root_name, root_prefix):
        """ 
        Create all the possible xpaths in a doc by starting at the doc root
        """

        print("start_from_root_element '%s'" % root_name)

        initial_root = ComplexType.objects_no_json.get(source_file__pk__in=self.file_dependency_pk_list, name=root_name)

        if not initial_root:
            return None
            raise RuntimeError("Initial root missing '%s' version %s" % (root_name, self.version_string) )

        initial_data = initial_root.get_standardized_hash(process_runs=0, xsd_type='element', xsd_prefix="/" + root_prefix, ignore_name=True) 
        initial_data['line_number']= ''
        initial_data['documentation']=''

        self.unprocessed_complextypes.append(initial_data)
        print("Found initial root %s" % initial_data)
        self.run()

    def test_against_groups(self, xpath):
        for key in self.group_roots.keys():
            if xpath.startswith(key):
                print(" ++++ group child: '%s' parent '%s' " % (xpath, key) )
                return key

        return ''


    def write_entities_to_file(self, filename):
        """ Hack for debugging """


        #for key in self.group_roots.keys():
        #    print(" ^^^^^ group root: '%s' " % key)


        headers = ['ordering', 'derived_xpath', 'group_root', 'name', 'line_number', 'documentation', 'min_occurs', 'max_occurs', 'type']

        with open(filename + '.csv', 'wb') as outfile:
            dw = csv.DictWriter(outfile, fieldnames=headers, extrasaction='ignore')
            dw.writeheader()

            keylist = self.derived_keys.keys()
            keylist.sort()

            for key in keylist:
                group_result = self.test_against_groups(key)
                self.derived_keys[key]['group_root']= group_result               

                dw.writerow(self.derived_keys[key])



    def make_mappings(self, name_alternate=None):
        print ("make_mappings %s name='%s'" % (self.xsdfile_obj, self.xsdfile_obj.name) )

        # What are the file dependencies ? 
        file_dependencies = FileInclude.objects.filter(source_file=self.xsdfile_obj)
        self.file_dependency_pk_list = [self.xsdfile_obj.pk]
        for file_dependency in file_dependencies:
            print ("Processing file dependency %s" % (file_dependency) )
            self.file_dependency_pk_list.append(file_dependency.included_file.pk)
            ## Many files just include Common/efileTypes.xsd
        print("file_dependency_pk_list %s" % (self.file_dependency_pk_list))

        self.hash_by_name()
        if name_alternate:
            self.start_from_root_element(name_alternate + "Type", name_alternate)
        else:
            self.start_from_root_element(self.xsdfile_obj.name + "Type", self.xsdfile_obj.name)

        self.write_entities_to_file(self.xsdfile_obj.name)
        

