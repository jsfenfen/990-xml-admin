import json
from django.core.management.base import BaseCommand
#from django.conf import settings
from irsx.xmlrunner import XMLRunner
from irsx.filing import Filing
from irsx.standardizer import Standardizer
from filing.models import xml_submission as XMLSubmission, ProcessedFiling
from filing.type_utils import unicodeType
from schemas.model_accumulator import Accumulator


BATCHSIZE = 100
LOOP_MAX = 100
ids = ['201520859349200502', '201520859349200522', '201500799349200600', '201500799349200605', '201500799349200625', '201500799349200715', '201500799349200720', '201520799349200127', '201520799349200202', '201520799349200217', '201500819349200255', '201510799349200111', '201510799349200116', '201510909349200001', '201510909349200106', '201520829349200022', '201520869349200312', '201500859349100200', '201520869349200727', '201520929349200017', '201540869349200209', '201540869349200224', '201540869349200334', '201540869349200609', '201510829349100606', '201510869349100001', '201510869349100111', '201510869349100201', '201530799349100003', '201530799349100103', '201530799349100408', '201530799349100503', '201530799349100808', '201530859349100503', '201530859349100508', '201530859349100603', '201530859349100703', '201530859349100708', '201540149349100204', '201540849349100004', '201540849349100014', '201540829349100104', '201540829349100204', '201540829349100354', '201540829349100359', '201540829349100454', '201540829349100604', '201510839349100506', '201510879349100201', '201510879349100301', '201510879349100501', '201510879349100601', '201510929349100016', '201510929349100101', '201510929349100106', '201510929349100116', '201510929349100121', '201530809349100103', '201530809349100303', '201520869349200707', '201540859349100109', '201540859349100204']
def processed_filing_from_result_filing(completed_filing, parent_submission):
    """ Turn the returned filing object into an unsaved ProcessedFiling  """

    newpf = ProcessedFiling(
        ein = completed_filing.get_ein(),
        object_id = completed_filing.get_object_id(),
        version_string = completed_filing.get_version(),
        processed_json = json.dumps(completed_filing.get_result()),
        has_keyerrors = False,
        submission = parent_submission,
        is_saved = False
    )

    keyerrors = completed_filing.get_keyerrors()
    if keyerrors:
        newpf.has_keyerrors = True 
        newpf.keyerrors = completed_filing.get_keyerrors()

    return newpf

class Command(BaseCommand):
    help = 'Enter new files, as json an in the relational tables. '


    def process_sked(self, sked):
        """ Enter just one schedule """ 
        #print("Processing schedule %s" % sked['schedule_name'])
        for part in sked['schedule_parts'].keys():
            partname = part
            partdata = sked['schedule_parts'][part]

            self.accumulator.add_model(partname, partdata)

        for groupname in sked['groups'].keys():
            for groupdata in sked['groups'][groupname]:
                #print("group %s " % (groupname))
                #try:
                #    # hack for testing some older data
                #    groupdata['object_id']=groupdata['return_id']
                #    del groupdata['return_id']
                #except KeyError:
                #    pass
                if  groupname == 'null':    # wtf?
                    print("\n\n\n%s" % groupdata)
                else:
                    self.accumulator.add_model(groupname, groupdata)


    def enter_from_result(self, result):
        for sked in result:
            #print ("running from result %s" % sked)
            self.process_sked(sked)


    def process_batch(self, xml_submission_queryset):
        newpf_list = []
        for xml_submission in xml_submission_queryset:

            print("Handling object id %s sub_date=%s." % (xml_submission.object_id, xml_submission.sub_date))
            try:
                exists = ProcessedFiling.objects.get(object_id=xml_submission.object_id)
            except ProcessedFiling.DoesNotExist:
                completed_filing = self.xml_runner.run_filing(xml_submission.object_id)

                new_pf = processed_filing_from_result_filing(completed_filing, xml_submission)
                
                xml_submission.json_set=True
                xml_submission.save()

                raw_json = new_pf.processed_json
                if not raw_json:
                    print ("No raw json -- skipping %s" % xml_submission.object_id)
                    continue

                read_json = json.loads(raw_json)
                if not read_json:
                    print ("No json loaded -- skipping %s" % xml_submission.object_id)
                    continue
                if type(read_json)==unicodeType:
                    self.enter_from_result(json.loads(read_json))
                else:
                    self.enter_from_result(read_json)
                new_pf.is_saved = True

                newpf_list.append(new_pf)

        
                #self.accumulator.commit_all() # for testing, should go at the end when running. 
        self.accumulator.commit_all()


        print("Processing %s filings in bulk" % len(newpf_list))
        ProcessedFiling.objects.bulk_create(newpf_list)

            

    def handle(self, *args, **options):
        self.xml_runner = XMLRunner()
        self.accumulator = Accumulator()

        count = 0
        while True:
            xml_batch = XMLSubmission.objects.filter(year=2014).exclude(json_set=True)[:BATCHSIZE]
            #xml_batch = XMLSubmission.objects.filter(object_id__in=ids).exclude(json_set=True)[:BATCHSIZE]
            #xml_batch = XMLSubmission.objects.filter(object_id__in=['201540859349100204',])[:BATCHSIZE]
            #xml_batch = XMLSubmission.objects.filter(object_id__in=test2016ids).exclude(json_set=True)[:BATCHSIZE]
            #xml_batch = XMLSubmission.objects.filter(sub_date__regex=r'^8.+2017.*').exclude(json_set=True)[:BATCHSIZE]
            #xml_batch = XMLSubmission.objects.filter(object_id__in=test2016ids).exclude(json_set=True)[:BATCHSIZE]
            #xml_batch = XMLSubmission.objects.filter(object_id__in=['201601349349304030',])


            count += 1
            print count
            if len(xml_batch)==0:
                break

            self.process_batch(xml_batch)


            # for testing
            if count > LOOP_MAX:
                break

