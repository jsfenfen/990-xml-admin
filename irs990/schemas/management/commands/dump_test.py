
from irsx.runner import Runner
from filing.models import xml_submission

import unicodecsv as csv

from django.core.management.base import BaseCommand
from django.conf import settings

def get_type(schedule_list):
    if 'IRS990' in schedule_list:
        return 'IRS990'
    elif 'IRS990EZ' in schedule_list:
        return 'IRS990EZ'
    elif 'IRS990PF' in schedule_list:
        return 'IRS990PF'    
    else:
        # todo - make a specific error so it can be caught?
        raise Exception("Missing 990, 990EZ and 990PF")

def get_sked(result, schedule_list, sked_name):
    if sked_name == 'IRS990ScheduleK':
        pass
        #for i, result in enumerate(schedule_list):
        #    print i, result

    else:
        sked_index = None
        try:
            sked_index = schedule_list.index(sked_name)
        except ValueError:
            return None
        
        return result[sked_index]


class Command(BaseCommand):
    help = 'Dump some fields that are of interest'
    
    def handle(self, *args, **options):
        self.xml_runner = Runner()

        headers = ["taxpayer_name", "ein", "tax_period", "object_id", "name", "title", "org_comp", "related_comp", "other_cmp", "form", "source"]


        outfile = open("dumptest.csv", 'wb')
        dw = csv.DictWriter(outfile, fieldnames=headers, extrasaction='ignore')
        dw.writeheader()


        submissions =  xml_submission.objects.all()[:100]
        #submissions = xml_submission.objects.filter(object_id='201533089349301428')
        #submissions = xml_submission.objects.filter(return_type='990PF')
        for submission in submissions:
            print submission.object_id

            result = self.xml_runner.run_filing(
                submission.object_id,
                verbose=True,
            )
            filing_info = {
                'taxpayer_name': submission.taxpayer_name,
                'tax_period': submission.tax_period
            }
            schedule_list = [sked['schedule_name'] for sked in result]
            print schedule_list

            ## type
            form_type = get_type(schedule_list)
            print form_type

            sked990 = get_sked(result, schedule_list, 'IRS990')
            sked990EZ = get_sked(result, schedule_list, 'IRS990EZ')
            sked990PF = get_sked(result, schedule_list, 'IRS990PF')
            sked990J = get_sked(result, schedule_list, 'IRS990ScheduleJ')

            
            if sked990: 
                print("\n\t990")
                #print sked990
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
                        'form':'IRS990',
                        'source': 'Frm990PrtVIISctnA'
                    }
                    this_employee.update(filing_info)
                    #print "\n"
                    #print this_employee
                    dw.writerow(this_employee)
 

            if sked990EZ:
                print("\n\n\t990EZ %s" % sked990EZ['schedule_name'])
                assert sked990EZ['schedule_name']=='IRS990EZ'
                group_name = "EZOffcrDrctrTrstEmpl"

                try:
                    employee_list = sked990EZ['groups'][group_name]
                except KeyError:
                    employee_list = []

                for employee in employee_list:
                    print employee
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
                    print this_employee
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
                    print this_employee
                    dw.writerow(this_employee)
                    print employee


            if sked990PF:
                print("\n\t990PF %s" % sked990PF['schedule_name'])
                assert sked990PF['schedule_name']=='IRS990PF'
                

                group_name = "PFOffcrDrTrstKyEmpl"
                employee_list = []
                try:
                    employee_list = sked990PF['groups'][group_name]
                except KeyError:
                    pass

                for employee in employee_list:
                    print "\n\n"
                    print employee
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
                    print this_employee
                    dw.writerow(this_employee)


                group_name = "PFCmpnstnHghstPdEmpl" # also rare
                employee_list = []
                try:
                    employee_list = sked990PF['groups'][group_name]
                except KeyError:
                    pass

                for employee in employee_list:
                    print employee
                    this_employee = {
                        'ein': employee['ein'],
                        'object_id': employee['object_id'],
                        'name': employee.get('CmpnstnHghstPdEmpl_PrsnNm'),
                        'title': employee.get('PFCmpnstnHghstPdEmpl_TtlTxt'),
                        'org_comp': employee.get('PFCmpnstnHghstPdEmpl_CmpnstnAmt'),
                        # 'related_comp': NA 
                        #'other_cmp': CmpnstnHghstPdEmpl_EmplyBnftsAmt + CmpnstnHghstPdEmpl_ExpnsAccntAmt ? 
                        'form':'IRS990PF',
                        'source': 'PFCmpnstnHghstPdEmpl'
                    }
                    this_employee.update(filing_info)
                    #print "\n"
                    print this_employee
                    dw.writerow(this_employee)
                    
            if sked990J:
                print("\n\t990J %s" % sked990J['schedule_name'])
                assert sked990J['schedule_name']=='IRS990ScheduleJ'
                

                group_name = "SkdJRltdOrgOffcrTrstKyEmpl"
                employee_list = []
                try:
                    employee_list = sked990J['groups'][group_name]
                except KeyError:
                    pass

                for employee in employee_list:
                    print "\n\n"
                    print employee
                    this_employee = {
                        'ein': employee['ein'],
                        'object_id': employee['object_id'],
                        'name': employee.get('PrsnNm'),
                        'bus_line_1':employee.get('BsnssNmLn1Txt'),
                        'title': employee.get('TtlTxt'),
                        'org_comp': employee.get('TtlCmpnstnFlngOrgAmt'),
                        'related_comp': employee.get('CmpRprtPrr990RltdOrgsAmt'),
                        #'other_cmp': OffcrDrTrstKyEmpl_EmplyBnftPrgrmAmt + OffcrDrTrstKyEmpl_ExpnsAccntOthrAllwncAmt ? 
                        'form':'IRS990ScheduleJ',
                        'source': 'SkdJRltdOrgOffcrTrstKyEmpl'
                    }
                    this_employee.update(filing_info)
                    #print "\n"
                    print this_employee
                    dw.writerow(this_employee)




                



                