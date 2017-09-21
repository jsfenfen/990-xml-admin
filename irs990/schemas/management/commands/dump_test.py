import unicodecsv as csv
import json

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import reset_queries

from irsx.xmlrunner import XMLRunner
from irsx.filing import Filing
from irsx.standardizer import Standardizer
from filing.models import xml_submission as XMLSubmission


class Command(BaseCommand):
    help = 'Dump some fields that are of interest'
    
    def handle(self, *args, **options):
        self.xml_runner = None
        self.standardizer = Standardizer()
        count = 0
        headers = ["taxpayer_name", "ein", "tax_period", "sub_date", "object_id", "name", "title", "org_comp", "related_comp", "other_cmp", "form", "source"]

        outfile = open("dumptest.csv", 'wb')
        dw = csv.DictWriter(outfile, fieldnames=headers, extrasaction='ignore')
        dw.writeheader()

        submissions =  XMLSubmission.objects.filter(schema_year__gte=2013, sub_date__contains='2017').values('taxpayer_name', 'tax_period', 'sub_date', 'object_id')
        #submissions = XMLSubmission.objects.filter(object_id='201513209349102976').values('taxpayer_name', 'tax_period', 'sub_date', 'object_id')
        #submissions = XMLSubmission.objects.filter(return_type='990PF').values('taxpayer_name', 'tax_period', 'sub_date', 'object_id')
        for submission in submissions:
            
            count += 1
            if count % 100 == 0:
                print ("Processed %s filings" % count)
                reset_queries()  # not sure this will matter, but...
                self.xml_runner = None  # Erase this to prevent memory leaks

            if not self.xml_runner:
                self.xml_runner = XMLRunner(standardizer=self.standardizer)  # will start up faster if we don't have to reread/import csvs

            whole_submission = XMLSubmission.objects.get(object_id=submission['object_id'])
            assert whole_submission.json_set
            # This is a bug--should be returned as json? https://stackoverflow.com/questions/36352721/django-1-9-jsonfield-stored-dictionary-returns-unicode-instead
            # Is this behaving correctly or not? 

            submission_json = json.loads(whole_submission.as_json) 

            filingobj = Filing(submission['object_id'], json=submission_json)
            #print("\n\nObject id %s\n" % submission['object_id'])
            #print submission_json

            processedFiling = self.xml_runner.run_from_filing_obj(
                filingobj,
                verbose=False,
            )

            #print ("\n\nProcessed filing is %s" % processedFiling.get_result())

            filing_info = {
                'taxpayer_name': submission['taxpayer_name'],
                'tax_period': submission['tax_period'],
                'sub_date': submission['sub_date']
            }
            schedule_list = processedFiling.list_schedules()
            result = processedFiling.get_result()

            sked990_list = processedFiling.get_parsed_sked('IRS990')
            sked990EZ_list = processedFiling.get_parsed_sked('IRS990EZ')
            sked990PF_list = processedFiling.get_parsed_sked('IRS990PF')
            sked990J_list = processedFiling.get_parsed_sked('IRS990ScheduleJ')

            
            if sked990_list: 
                #print("\n\t990")
                sked990 = sked990_list[0]
                assert sked990['schedule_name']=='IRS990'     
                group_name = "Frm990PrtVIISctnA"
                try:
                    employee_list = sked990['groups'][group_name]
                except KeyError:
                    employee_list = []

                for employee in employee_list:
                    #print "\n\n"
                    #print employee 
                    this_employee = {
                        'ein': employee['ein'],
                        'object_id': employee['object_id'],
                        'name': employee.get('PrsnNm'),
                        'title': employee.get('TtlTxt'),
                        'org_comp': employee.get('RprtblCmpFrmOrgAmt', 0),
                        'related_comp': employee.get('RprtblCmpFrmRltdOrgAmt', 0),
                        'other_cmp': employee.get('OthrCmpnstnAmt', 0),
                        'highest_ind':employee.get('HghstCmpnstdEmplyInd'),
                        'form':'IRS990',
                        'source': 'Frm990PrtVIISctnA'
                    }
                    this_employee.update(filing_info)
                    #print "\n"
                    #print this_employee
                    dw.writerow(this_employee)
 

            if sked990EZ_list:
                sked990EZ = sked990EZ_list[0]
                #print("\n\t990EZ %s" % sked990EZ['schedule_name'])
                assert sked990EZ['schedule_name']=='IRS990EZ'
                group_name = "EZOffcrDrctrTrstEmpl"

                try:
                    employee_list = sked990EZ['groups'][group_name]
                except KeyError:
                    employee_list = []

                for employee in employee_list:
                    #print employee
                    this_employee = {
                        'ein': employee['ein'],
                        'object_id': employee['object_id'],
                        'name': employee.get('PrsnNm', ''),
                        'title': employee.get('TtlTxt', ''),
                        'org_comp': employee.get('CompnstnAmt', 0),
                        # 'related_comp': NA 
                        #'other_cmp': EmplyBnftsAmt + ExpnsAccntAmt ? 
                        'form':'IRS990EZ',
                        'source': 'EZOffcrDrctrTrstEmpl'
                    }
                    this_employee.update(filing_info)
                    #print this_employee
                    dw.writerow(this_employee)

                ##

                group_name = "EZCmpnstnHghstPdEmpl" # This is very rare
                try:
                    employee_list = sked990EZ['groups'][group_name]
                except KeyError:
                    employee_list = []

                for employee in employee_list:

                    this_employee = {
                        'ein': employee['ein'],
                        'object_id': employee['object_id'],
                        'name': employee.get('PrsnNm'),
                        'title': employee.get('TtlTxt'),
                        'org_comp': employee.get('CompnstnAmt'),
                        # 'related_comp': NA 
                        #'other_cmp': EmplyBnftsAmt + ExpnsAccntAmt ? 
                        'form':'IRS990EZ',
                        'source': 'EZCmpnstnHghstPdEmpl'
                    }
                    this_employee.update(filing_info)
                    #print "\n"
                    #print this_employee
                    dw.writerow(this_employee)
                    #print employee


            if sked990PF_list:
                sked990PF = sked990PF_list[0]
                #print("\n\t990PF %s" % sked990PF['schedule_name'])
                assert sked990PF['schedule_name']=='IRS990PF'
                

                group_name = "PFOffcrDrTrstKyEmpl"
                employee_list = []
                try:
                    employee_list = sked990PF['groups'][group_name]
                except KeyError:
                    pass

                for employee in employee_list:
                    #print "\n\n"
                    #print employee
                    this_employee = {
                        'ein': employee['ein'],
                        'object_id': employee['object_id'],
                        'name': employee.get('OffcrDrTrstKyEmpl_PrsnNm'),
                        'title': employee.get('OffcrDrTrstKyEmpl_TtlTxt'),
                        'org_comp': employee.get('OffcrDrTrstKyEmpl_CmpnstnAmt'),
                        # 'related_comp': NA 
                        #'other_cmp': OffcrDrTrstKyEmpl_EmplyBnftPrgrmAmt + OffcrDrTrstKyEmpl_ExpnsAccntOthrAllwncAmt ? 
                        'form':'IRS990PF',
                        'source': 'PFOffcrDrTrstKyEmpl'
                    }
                    this_employee.update(filing_info)
                    #print "\n"
                    #print this_employee
                    dw.writerow(this_employee)


                group_name = "PFCmpnstnHghstPdEmpl" # also rare
                employee_list = []
                try:
                    employee_list = sked990PF['groups'][group_name]
                except KeyError:
                    pass

                for employee in employee_list:
                    #print employee
                    this_employee = {
                        'ein': employee['ein'],
                        'object_id': employee['object_id'],
                        'name': employee.get('CmpnstnHghstPdEmpl_PrsnNm'),
                        'title': employee.get('CmpnstnHghstPdEmpl_TtlTxt'),
                        'org_comp': employee.get('CmpnstnHghstPdEmpl_CmpnstnAmt'), 
                        # 'related_comp': NA 
                        #'other_cmp': CmpnstnHghstPdEmpl_EmplyBnftsAmt + CmpnstnHghstPdEmpl_ExpnsAccntAmt ? 
                        'form':'IRS990PF',
                        'source': 'PFCmpnstnHghstPdEmpl'
                    }
                    this_employee.update(filing_info)
                    #print "\n"
                    #print this_employee
                    dw.writerow(this_employee)
                    
            if sked990J_list:
                sked990J = sked990J_list[0]
                #print("\n\t990J %s" % sked990J['schedule_name'])
                assert sked990J['schedule_name']=='IRS990ScheduleJ'
                

                group_name = "SkdJRltdOrgOffcrTrstKyEmpl"
                employee_list = []
                try:
                    employee_list = sked990J['groups'][group_name]
                except KeyError:
                    pass

                for employee in employee_list:
                    print "\n\n sked J"
                    print employee
                    this_employee = {
                        'ein': employee['ein'],
                        'object_id': employee['object_id'],
                        'name': employee.get('PrsnNm'),
                        'bus_line_1':employee.get('BsnssNmLn1Txt'),
                        'title': employee.get('TtlTxt'),
                        'org_comp': employee.get('TtlCmpnstnFlngOrgAmt'),
                        'related_comp': employee.get('TtlCmpnstnRltdOrgsAmt'),
                        #'other_cmp': OffcrDrTrstKyEmpl_EmplyBnftPrgrmAmt + OffcrDrTrstKyEmpl_ExpnsAccntOthrAllwncAmt ? 
                        'form':'IRS990ScheduleJ',
                        'source': 'SkdJRltdOrgOffcrTrstKyEmpl'
                    }
                    this_employee.update(filing_info)
                    #print "\n"
                    print this_employee
                    dw.writerow(this_employee)


        print ("Total of %s processed" % count)



                



                