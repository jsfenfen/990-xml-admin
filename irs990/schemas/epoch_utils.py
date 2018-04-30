"""
Gnarly custom variable transformations to stitch variables across years. Current target: 2013 forwards.
Double check the documentation; it's possible for *meaning* of a var to change even if xpath doesn't. 
This assigns groups (schemas.models VersionedGroup to CanonicalGroup and VersionedVariable to CanonicalVariable)
Additional details that are sourced through the canonical vars (specifically, the group and form/part hierarchy)
are assigned in a later management command (propagate_from_canonical).
"""

MODERN_EPOCH = ['2013v3.0', '2013v3.1', '2013v4.0', '2014v5.0', '2014v6.0', '2015v2.0', '2015v2.1', '2015v3.0', '2016v3.0']
EARLY_AWS_EPOCH = ['2009v1.0', '2009v1.1', '2009v1.2', '2009v1.3', '2009v1.4', '2009v1.7', '2010v3.2', '2010v3.4', '2010v3.6', '2010v3.7', '2011v1.2', '2011v1.3', '2011v1.4', '2011v1.5', '2012v2.0', '2012v2.1', '2012v2.2', '2012v2.3', '2012v3.0']
ENTIRE_AWS_ERA = MODERN_EPOCH + EARLY_AWS_EPOCH
EPOCH_2012 = ['2012v2.0', '2012v2.1', '2012v2.2', '2012v2.3', '2012v3.0']
EPOCH_2013 = ['2013v3.0', '2013v3.1', '2013v4.0']
EPOCH_2014 = ['2014v5.0', '2014v6.0']
EPOCH_2014_FORWARDS = ['2014v5.0', '2014v6.0', '2015v2.0', '2015v2.1', '2015v3.0', '2016v3.0']

EPOCH_2017 = ['2017v2.0', '2017v2.1', '2017v2.2', '2017v2.3']  


GROUP_TRANSFORMATIONS =  {
    ### Needed for the "modern" era
    '/IRS990ScheduleA/Form990ScheduleAPartVIGrp': {
        'versions':['2013v4.0', '2013v3.0', '2013v3.1'],
        'corrected_value':'/IRS990ScheduleA/Form990ScheduleAPartIVGrp',
        },

    ## Experimental modern to early transformations:
    '/IRS990/OtherExpensesGrp': {
        'versions':EARLY_AWS_EPOCH,
        'corrected_value':'/IRS990/OtherExpenses',
        },
    '/IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp': {
        'versions':EARLY_AWS_EPOCH,
        'corrected_value':'/IRS990PF/CapitalGainsAndLosses/CapitalGainsAndLossesInfo',
        }
    }

## the versions listed are for where the var *is* present
## Only entered for 2013 and forwards
MISSING_VARS = {
    ## This is an incomplete listing of variables that appear in *some but not all* of the MODERN_EPOCH and onwards. 
    #### Newly created variables, sked A additions
    '/IRS990ScheduleA/OtherSupportSumAmt':{'versions':['2014v6.0', '2015v2.0', '2015v2.1', '2015v3.0']},
    '/IRS990ScheduleA/DistributionAllocationsGrp/ExcessFromYear3Amt':{'versions':['2015v2.0', '2015v2.1', '2015v3.0']}, # see diff in 
    '/IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistributionCyovYr2Amt':{'versions':['2015v2.0', '2015v2.1', '2015v3.0']},

    ## 'Discontinued' variables
    '/IRS990ScheduleA/CertificationInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleA/Contribution35ControlledInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleA/ContributionControllerInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleA/ContributionFamilyInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleA/SupportedOrgInformationGrp/SupportedOrgNotifiedInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleA/SupportedOrgInformationGrp/USOrganizedInd':{'versions':EPOCH_2013},

    # Schedule H rewrite of Part V section B CHNA, FAP, Billing & Collection 
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/AdoptBudgetInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/AdoptImplementationStrategyInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/AllNeedsAddressedInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/AttachedToInvoiceInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/AvailableOnRequestInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/BodyAttachmentsInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/DevelopCommunityWidePlanInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ExecCommunityWidePlanInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ExecImplementationStrategyInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FPGUsedDeterEligFreeCareInd':{'versions':EPOCH_2013},  # replaced by measure of free and discounted care: FPGUsedDeterEligFreeCareInd
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FPGUsedDetermEligDscntCareInd':{'versions':EPOCH_2013}, # replaced by measure of free and discounted care: FPGUsedDeterEligFreeCareInd
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/IncludeOperationalPlanInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/LawsuitInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/LiensOnResidencesInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/MedicaidMedicareInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherNeedsAddressedInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitBodyAttachmentsInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitLawsuitInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitLienOnResidenceInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PostedInAdmissionOfficeInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PostedInEmergencyRoomInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PrioritizeHealthNeedsInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PrioritizeServicesInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ProvidedOnAdmissionInd':{'versions':EPOCH_2013},    
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/StateRegulationInd':{'versions':EPOCH_2013},
    '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/UninsuredDiscountInd':{'versions':EPOCH_2013},
    # Return Header:
    '/ReturnHeader/DeviceId':{'versions':EPOCH_2014_FORWARDS}
}

def test_for_missing(var, version):
    # returns true if a var is missing in this version
    try:
        missing_var = MISSING_VARS[var]
        return not version in missing_var['versions']
    except KeyError:
        return False

def apply_var_translation(var, version):
    result = var

    ## 2013 transformations
    if version in EPOCH_2013:

        if var.endswith('Nm'):
            result = result.rstrip('Nm')
        if var.endswith('Txt'):
            result = result.rstrip('Txt')  
        if var.endswith('StateAbbreviationCd'):
            result = result.replace('StateAbbreviationCd', 
                'State')  
        if var.endswith('ZIPCd'):
            result = result.replace('ZIPCd', 'ZIPCode')
        if var.endswith('ForeignAddress/ForeignPostalCd'):
            result = result.replace('ForeignAddress/ForeignPostalCd',
                'ForeignAddress/PostalCode')  
        
        if var.endswith('OrganizationTypeCd'):
            result = result.replace('OrganizationTypeCd', 
                'OrganizationTypeDesc')  
        elif var.endswith('Cd'):
            result = result.rstrip('Cd')
        
        if "PrincipalOfcrBusinessName" in var:
            result = result.replace('PrincipalOfcrBusinessName', 
                'PrincipalOfcrBusinessAddress') 

        """
        This transition is maybe debatable, since the wording of the question
        changes, slightly; unclear if meaning does. 

        2013 part V line 8: ['/IRS990/ExcessBusinessHoldingsInd'] Sponsoring
        organizations maintaining donor advised funds and section 509(a)(3)
        supporting organizations. Did the supporting organization, or a
        donor advised fund maintained by a sponsoring organization, have 
        excess business holdings at any time during the year? 

        2016: ['/IRS990/DAFExcessBusinessHoldingsInd'] 8 Sponsoring
        organizations maintaining donor advised funds. Did a donor
        advised fund maintained by the sponsoring organization have
         excess business holdings at any time during the year?

        """
        if var == '/IRS990/DAFExcessBusinessHoldingsInd':
            result = '/IRS990/ExcessBusinessHoldingsInd'


        if var.startswith('/IRS990ScheduleA/'):
            # Sked A
            if var.endswith('OrganizationTypeCd'):
                result = var.replace('OrganizationTypeCd', 'OrganizationTypeDesc')

            if '/IRS990ScheduleA/Form990ScheduleAPartVIGrp' in var:
                result = result.replace('/IRS990ScheduleA/Form990ScheduleAPartVIGrp', 
                    '/IRS990ScheduleA/Form990ScheduleAPartIVGrp')

        if var.startswith('/IRS990ScheduleG/'):
            if var == '/IRS990ScheduleG/FundraisingEventInformationGrp/Event2Nm':
                result = '/IRS990ScheduleG/FundraisingEventInformationGrp/NameOfEvent2Amt'

            if var == '/IRS990ScheduleG/FundraisingEventInformationGrp/Event1Nm':
                result = '/IRS990ScheduleG/FundraisingEventInformationGrp/NameOfEvent1Amt'


        if var.startswith('/IRS990ScheduleH/'):
            result = result.replace("CriteriaInd", "Ind") 

            if var == '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherCriteriaInd':
                result = '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherFactorsInd'

            if var == '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPAvailableOnWebsiteInd':
                result = '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PostedOnWebsiteInd'

            if var == '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PaperCopyPublicInspectionInd':
                result = '/IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/RptAvailableUponRequestInd'


    ## 2014 transformations
    if version in EPOCH_2014:
        if var.endswith('OrganizationTypeCd'):
            result = result.replace('OrganizationTypeCd', 'OrganizationTypeDesc')
        if var == '/IRS990ScheduleA/Form990ScheduleAPartVIGrp/ExplanationTxt':
            result = '/IRS990ScheduleA/Form990ScheduleAPartIVGrp/ExplanationTxt'


    if version in EPOCH_2017:
        if var.endswith('AppliedToEsTaxAmt'):
            result = result.replace('AppliedToEsTaxAmt', 'AppliedToESTaxAmt')  # Capitalization introduced in 2017


        if var.endswith('ContinutationTotalEmployeeCnt'):
            result = result.replace('ContinutationTotalEmployeeCnt', 'ContinuationTotalEmployeeCnt')  # Capitalization introduced in 2017
        

        if var.endswith('ContinutationTotalOfficeCnt'):
            result = result.replace('ContinutationTotalOfficeCnt', 'ContinuationTotalOfficeCnt')  # Capitalization introduced in 2017


    print("apply_var_translation: '%s' => '%s'" % (var, result))
    return result


""" Notes for earlier epoch transitions

2012 => 2013

One type of change in groups....

 2012v3.0       | TransactionsRelatedOrgsTable
 2013v3.0       | TransactionsRelatedOrgGrp

Another:
 2012v3.0       | ProgramServiceRevenue
 2013v3.0       | ProgramServiceRevenueGrp

Some variables change like: 

 2012v3.0       | /IRS990ScheduleA/CertificationCheckbox
 2013v3.0       | /IRS990ScheduleA/CertificationInd

 """
