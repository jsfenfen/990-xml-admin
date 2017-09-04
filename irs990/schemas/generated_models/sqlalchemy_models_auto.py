from sqlalchemy import Column, Integer, String, BigInteger, Text, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


#######
#
# IRS990 -  Part 0 Prefatory material 
#
#######

class part_0(Base):
    __tablename__='part_0'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    AddrssChngInd = Column(String(length=1))
    # Line number:  B  Description:  Indicates this return has an address change  xpath: /IRS990/AddressChangeInd 

    IntlRtrnInd = Column(String(length=1))
    # Line number:  B  Description:  Indicates this is an initial return  xpath: /IRS990/InitialReturnInd 

    FnlRtrnInd = Column(String(length=1))
    # Line number:  B  Description:  Indicates this return is a terminated return  xpath: /IRS990/FinalReturnInd 

    AmnddRtrnInd = Column(String(length=1))
    # Line number:  B  Description:  Indicates this return is an amended return  xpath: /IRS990/AmendedReturnInd 

    DngBsnssAsNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  C  Description:  Business name line 1  xpath: /IRS990/DoingBusinessAsName/BusinessNameLine1Txt 

    DngBsnssAsNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  C  Description:  Business name line 2  xpath: /IRS990/DoingBusinessAsName/BusinessNameLine2Txt 

    GrssRcptsAmt = Column(BigInteger)
    # Line number:  G  Description:  Gross receipts  xpath: /IRS990/GrossReceiptsAmt 

    GrpRtrnFrAffltsInd = Column(String(length=5))
    # Line number:  H(a)  Description:  Group return for affiliates?  xpath: /IRS990/GroupReturnForAffiliatesInd 

    AllAffltsInclddInd = Column(Text)
    # Line number:  H(b)  Description:  All affiliates included?  xpath: /IRS990/AllAffiliatesIncludedInd 

    GrpExmptnNm = Column(Text)
    # Line number:  H(c)  Description:  Group exemption number  xpath: /IRS990/GroupExemptionNum 

    WbstAddrssTxt = Column(String(length=100))
    # Line number:  J  Description:  Web site  xpath: /IRS990/WebsiteAddressTxt 

    OfOrgnztnCrpInd = Column(String(length=1))
    # Line number:  K  Description:  Type of organization - corporation  xpath: /IRS990/TypeOfOrganizationCorpInd 

    OfOrgnztnTrstInd = Column(String(length=1))
    # Line number:  K  Description:  Type of organization - trust  xpath: /IRS990/TypeOfOrganizationTrustInd 

    OfOrgnztnAsscInd = Column(String(length=1))
    # Line number:  K  Description:  Type of organization - association  xpath: /IRS990/TypeOfOrganizationAssocInd 

    OfOrgnztnOthrInd = Column(String(length=1))
    # Line number:  K  Description:  Type of organization - other  xpath: /IRS990/TypeOfOrganizationOtherInd 

    OthrOrgnztnDsc = Column(String(length=100))
    # Line number:  K  Description:  Type of organization - other description  xpath: /IRS990/OtherOrganizationDsc 

    FrmtnYr = Column(Integer)
    # Line number:  L  Description:  Year of formation  xpath: /IRS990/FormationYr 

    PrncplOffcrNm = Column(String(length=35))
    # Line number:  F  Description:  Name of principal officer - Person  xpath: /IRS990/PrincipalOfficerNm 

    PrncplOfcrBsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  F  Description:  Business name line 1  xpath: /IRS990/PrincipalOfcrBusinessName/BusinessNameLine1Txt 

    PrncplOfcrBsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  F  Description:  Business name line 2  xpath: /IRS990/PrincipalOfcrBusinessName/BusinessNameLine2Txt 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  F  Description:  Address line 1  xpath: /IRS990/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  F  Description:  Address line 2  xpath: /IRS990/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  F  Description:  City  xpath: /IRS990/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  F  Description:  State  xpath: /IRS990/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  F  Description:  ZIP code  xpath: /IRS990/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  F  Description:  Address line 1  xpath: /IRS990/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  F  Description:  Address line 2  xpath: /IRS990/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  F  Description:  City  xpath: /IRS990/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  F  Description:  Province or state  xpath: /IRS990/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  F  Description:  Country  xpath: /IRS990/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  F  Description:  Postal code  xpath: /IRS990/ForeignAddress/ForeignPostalCd 

    Orgnztn501c3Ind = Column(String(length=1))
    # Line number:  I  Description:  Indicates a 501(c)(3) organization  xpath: /IRS990/Organization501c3Ind 

    Orgnztn501cInd = Column(Text)
    # Line number:  I  Description:  Indicates a 501(c) organization  xpath: /IRS990/Organization501cInd 

    Orgnztn49471NtPFInd = Column(String(length=1))
    # Line number:  I  Description:  Indicates a 4947(a)(1) organization  xpath: /IRS990/Organization4947a1NotPFInd 

    Orgnztn527Ind = Column(String(length=1))
    # Line number:  I  Description:  Indicates a 527 organization  xpath: /IRS990/Organization527Ind 

    LglDmclSttCd = Column(String(length=2))
    # Line number:  M  Description:  State of legal domicile  xpath: /IRS990/LegalDomicileStateCd 

    LglDmclCntryCd = Column(String(length=2))
    # Line number:  M  Description:  Country of legal domicile  xpath: /IRS990/LegalDomicileCountryCd 

#######
#
# IRS990 -  Part I Summary 
#
#######

class part_i(Base):
    __tablename__='part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    ActvtyOrMssnDsc = Column(Text)
    # Line number:  Part I Line 1  Description:  Activity or mission description  xpath: /IRS990/ActivityOrMissionDesc 

    CntrctTrmntnInd = Column(String(length=1))
    # Line number:  Part I Line 2  Description:  Termination or contraction  xpath: /IRS990/ContractTerminationInd 

    VtngMmbrsGvrnngBdyCnt = Column(BigInteger)
    # Line number:  Part I Line 3  Description:  Number voting members governing body  xpath: /IRS990/VotingMembersGoverningBodyCnt 

    VtngMmbrsIndpndntCnt = Column(BigInteger)
    # Line number:  Part I Line 4  Description:  Number independent voting members  xpath: /IRS990/VotingMembersIndependentCnt 

    TtlEmplyCnt = Column(BigInteger)
    # Line number:  Part I Line 5  Description:  total Number employees  xpath: /IRS990/TotalEmployeeCnt 

    TtlVlntrsCnt = Column(BigInteger)
    # Line number:  Part I Line 6  Description:  Total number volunteers  xpath: /IRS990/TotalVolunteersCnt 

    TtlGrssUBIAmt = Column(BigInteger)
    # Line number:  Part I Line 7a  Description:  Total gross UBI  xpath: /IRS990/TotalGrossUBIAmt 

    NtUnrltdBsTxblIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 7b  Description:  Net unrelated business taxable income  xpath: /IRS990/NetUnrelatedBusTxblIncmAmt 

    PYCntrbtnsGrntsAmt = Column(BigInteger)
    # Line number:  Part I Line 8  Description:  Contributions and grants - prior year  xpath: /IRS990/PYContributionsGrantsAmt 

    CYCntrbtnsGrntsAmt = Column(BigInteger)
    # Line number:  Part I Line 8  Description:  Contributions and grants - current year  xpath: /IRS990/CYContributionsGrantsAmt 

    PYPrgrmSrvcRvnAmt = Column(BigInteger)
    # Line number:  Part I Line 9  Description:  Program service revenue - prior year  xpath: /IRS990/PYProgramServiceRevenueAmt 

    CYPrgrmSrvcRvnAmt = Column(BigInteger)
    # Line number:  Part I Line 9  Description:  Program service revenue - current year  xpath: /IRS990/CYProgramServiceRevenueAmt 

    PYInvstmntIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 10  Description:  Investment income - prior year  xpath: /IRS990/PYInvestmentIncomeAmt 

    CYInvstmntIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 10  Description:  Investment income - current year  xpath: /IRS990/CYInvestmentIncomeAmt 

    PYOthrRvnAmt = Column(BigInteger)
    # Line number:  Part I Line 11  Description:  Other revenue - prior year  xpath: /IRS990/PYOtherRevenueAmt 

    CYOthrRvnAmt = Column(BigInteger)
    # Line number:  Part I Line 11  Description:  Other revenue - current year  xpath: /IRS990/CYOtherRevenueAmt 

    PYTtlRvnAmt = Column(BigInteger)
    # Line number:  Part I Line 12  Description:  Total revenue - prior year  xpath: /IRS990/PYTotalRevenueAmt 

    CYTtlRvnAmt = Column(BigInteger)
    # Line number:  Part I Line 12  Description:  Total revenue - current year  xpath: /IRS990/CYTotalRevenueAmt 

    PYGrntsAndSmlrPdAmt = Column(BigInteger)
    # Line number:  Part I Line 13  Description:  Grants and similar amounts - prior year  xpath: /IRS990/PYGrantsAndSimilarPaidAmt 

    CYGrntsAndSmlrPdAmt = Column(BigInteger)
    # Line number:  Part I Line 13  Description:  Grants and similar amounts - current year  xpath: /IRS990/CYGrantsAndSimilarPaidAmt 

    PYBnftsPdTMmbrsAmt = Column(BigInteger)
    # Line number:  Part I Line 14  Description:  Benefits paid to members - prior year  xpath: /IRS990/PYBenefitsPaidToMembersAmt 

    CYBnftsPdTMmbrsAmt = Column(BigInteger)
    # Line number:  Part I Line 14  Description:  Benefits paid to members - current year  xpath: /IRS990/CYBenefitsPaidToMembersAmt 

    PYSlrsCmpEmpBnftPdAmt = Column(BigInteger)
    # Line number:  Part I Line 15  Description:  Salaries, etc - prior year  xpath: /IRS990/PYSalariesCompEmpBnftPaidAmt 

    CYSlrsCmpEmpBnftPdAmt = Column(BigInteger)
    # Line number:  Part I Line 15  Description:  Salaries, etc - current year  xpath: /IRS990/CYSalariesCompEmpBnftPaidAmt 

    PYTtlPrfFndrsngExpnsAmt = Column(BigInteger)
    # Line number:  Part I Line 16a  Description:  Total professional fundraising expense - prior year  xpath: /IRS990/PYTotalProfFndrsngExpnsAmt 

    CYTtlPrfFndrsngExpnsAmt = Column(BigInteger)
    # Line number:  Part I Line 16a  Description:  Total professional fundraising expense - current year  xpath: /IRS990/CYTotalProfFndrsngExpnsAmt 

    CYTtlFndrsngExpnsAmt = Column(BigInteger)
    # Line number:  Part I Line 16b  Description:  Total fundraising expense - current year  xpath: /IRS990/CYTotalFundraisingExpenseAmt 

    PYOthrExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 17  Description:  Other expenses - prior year  xpath: /IRS990/PYOtherExpensesAmt 

    CYOthrExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 17  Description:  Other expenses - current year  xpath: /IRS990/CYOtherExpensesAmt 

    PYTtlExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 18  Description:  Total Expenses - prior year  xpath: /IRS990/PYTotalExpensesAmt 

    CYTtlExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 18  Description:  Total Expenses - current year  xpath: /IRS990/CYTotalExpensesAmt 

    PYRvnsLssExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 19  Description:  Revenues less expenses - prior year  xpath: /IRS990/PYRevenuesLessExpensesAmt 

    CYRvnsLssExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 19  Description:  Revenues less expenses - current year  xpath: /IRS990/CYRevenuesLessExpensesAmt 

    TtlAsstsBOYAmt = Column(BigInteger)
    # Line number:  Part I Line 20  Description:  Total Assets, BOY  xpath: /IRS990/TotalAssetsBOYAmt 

    TtlAsstsEOYAmt = Column(BigInteger)
    # Line number:  Part I Line 20  Description:  Total Assets, EOY  xpath: /IRS990/TotalAssetsEOYAmt 

    TtlLbltsBOYAmt = Column(BigInteger)
    # Line number:  Part I Line 21  Description:  Total Liabilities, BOY  xpath: /IRS990/TotalLiabilitiesBOYAmt 

    TtlLbltsEOYAmt = Column(BigInteger)
    # Line number:  Part I Line 21  Description:  Total Liabilities, EOY  xpath: /IRS990/TotalLiabilitiesEOYAmt 

    NtAsstsOrFndBlncsBOYAmt = Column(BigInteger)
    # Line number:  Part I Line 22  Description:  Net Assets or Fund Balances, BOY  xpath: /IRS990/NetAssetsOrFundBalancesBOYAmt 

    NtAsstsOrFndBlncsEOYAmt = Column(BigInteger)
    # Line number:  Part I Line 22  Description:  Net Assets or Fund Balances, EOY  xpath: /IRS990/NetAssetsOrFundBalancesEOYAmt 

#######
#
# IRS990 -  Part III Program Service Accomplishments 
#
#######

class part_iii(Base):
    __tablename__='part_iii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    InfInSkdOPrtIIIInd = Column(String(length=1))
    # Line number:  Part III  Description:  Schedule O contains a response to a question in Part III  xpath: /IRS990/InfoInScheduleOPartIIIInd 

    MssnDsc = Column(Text)
    # Line number:  Part III Line 1  Description:  Mission description  xpath: /IRS990/MissionDesc 

    SgnfcntNwPrgrmSrvcInd = Column(String(length=5))
    # Line number:  Part III Line 2  Description:  Significant new program services?  xpath: /IRS990/SignificantNewProgramSrvcInd 

    SgnfcntChngInd = Column(String(length=5))
    # Line number:  Part III Line 3  Description:  Significant change?  xpath: /IRS990/SignificantChangeInd 

    ActvtyCd = Column(BigInteger)
    # Line number:  Part III Line 4a  Description:  Activity code  xpath: /IRS990/ActivityCd 

    ExpnsAmt = Column(BigInteger)
    # Line number:  Part III Line 4a  Description:  Expense  xpath: /IRS990/ExpenseAmt 

    GrntAmt = Column(BigInteger)
    # Line number:  Part III Line 4a  Description:  Grants  xpath: /IRS990/GrantAmt 

    RvnAmt = Column(BigInteger)
    # Line number:  Part III Line 4a  Description:  Revenue  xpath: /IRS990/RevenueAmt 

    Dsc = Column(Text)
    # Line number:  Part III Line 4a  Description:  Description  xpath: /IRS990/Desc 

    PrgSrvcAccmActy2_ActvtyCd = Column(BigInteger)
    # Line number:  Part III  Description:  Activity code  xpath: /IRS990/ProgSrvcAccomActy2Grp/ActivityCd 

    PrgSrvcAccmActy2_ExpnsAmt = Column(BigInteger)
    # Line number:  Part III  Description:  Expense  xpath: /IRS990/ProgSrvcAccomActy2Grp/ExpenseAmt 

    PrgSrvcAccmActy2_GrntAmt = Column(BigInteger)
    # Line number:  Part III  Description:  Grants  xpath: /IRS990/ProgSrvcAccomActy2Grp/GrantAmt 

    PrgSrvcAccmActy2_RvnAmt = Column(BigInteger)
    # Line number:  Part III  Description:  Revenue  xpath: /IRS990/ProgSrvcAccomActy2Grp/RevenueAmt 

    PrgSrvcAccmActy2_Dsc = Column(Text)
    # Line number:  Part III  Description:  Description  xpath: /IRS990/ProgSrvcAccomActy2Grp/Desc 

    PrgSrvcAccmActy3_ActvtyCd = Column(BigInteger)
    # Line number:  Part III  Description:  Activity code  xpath: /IRS990/ProgSrvcAccomActy3Grp/ActivityCd 

    PrgSrvcAccmActy3_ExpnsAmt = Column(BigInteger)
    # Line number:  Part III  Description:  Expense  xpath: /IRS990/ProgSrvcAccomActy3Grp/ExpenseAmt 

    PrgSrvcAccmActy3_GrntAmt = Column(BigInteger)
    # Line number:  Part III  Description:  Grants  xpath: /IRS990/ProgSrvcAccomActy3Grp/GrantAmt 

    PrgSrvcAccmActy3_RvnAmt = Column(BigInteger)
    # Line number:  Part III  Description:  Revenue  xpath: /IRS990/ProgSrvcAccomActy3Grp/RevenueAmt 

    PrgSrvcAccmActy3_Dsc = Column(Text)
    # Line number:  Part III  Description:  Description  xpath: /IRS990/ProgSrvcAccomActy3Grp/Desc 

    TtlOthrPrgSrvcExpnsAmt = Column(BigInteger)
    # Line number:  Part III Line 4d  Description:  Total of other program service expense  xpath: /IRS990/TotalOtherProgSrvcExpenseAmt 

    TtlOthrPrgSrvcGrntAmt = Column(BigInteger)
    # Line number:  Part III Line 4d  Description:  Total of other program service grants  xpath: /IRS990/TotalOtherProgSrvcGrantAmt 

    TtlOthrPrgSrvcRvnAmt = Column(BigInteger)
    # Line number:  Part III Line 4d  Description:  Total of other program service revenue  xpath: /IRS990/TotalOtherProgSrvcRevenueAmt 

    TtlPrgrmSrvcExpnssAmt = Column(BigInteger)
    # Line number:  Part III Line 4e  Description:  Total program service expense  xpath: /IRS990/TotalProgramServiceExpensesAmt 

#######
#
# IRS990 -  Part IV Required Schedules 
#
#######

class part_iv(Base):
    __tablename__='part_iv'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    DscrbdInSctn501c3Ind = Column(Text)
    # Line number:  Part IV Line 1  Description:  Described in 501(c)(3)?  xpath: /IRS990/DescribedInSection501c3Ind 

    SkdBRqrdInd = Column(Text)
    # Line number:  Part IV Line 2  Description:  Schedule B required?  xpath: /IRS990/ScheduleBRequiredInd 

    PltclCmpgnActyInd = Column(Text)
    # Line number:  Part IV Line 3  Description:  Political activities?  xpath: /IRS990/PoliticalCampaignActyInd 

    LbbyngActvtsInd = Column(Text)
    # Line number:  Part IV Line 4  Description:  Lobbying activities?  xpath: /IRS990/LobbyingActivitiesInd 

    SbjctTPrxyTxInd = Column(Text)
    # Line number:  Part IV Line 5  Description:  Subject to proxy tax?  xpath: /IRS990/SubjectToProxyTaxInd 

    DnrAdvsdFndInd = Column(Text)
    # Line number:  Part IV Line 6  Description:  Donor advised funds?  xpath: /IRS990/DonorAdvisedFundInd 

    CnsrvtnEsmntsInd = Column(Text)
    # Line number:  Part IV Line 7  Description:  Conservation easements?  xpath: /IRS990/ConservationEasementsInd 

    CllctnsOfArtInd = Column(Text)
    # Line number:  Part IV Line 8  Description:  Collections of art?  xpath: /IRS990/CollectionsOfArtInd 

    CrdtCnslngInd = Column(Text)
    # Line number:  Part IV Line 9  Description:  Credit counseling?  xpath: /IRS990/CreditCounselingInd 

    TmpOrPrmnntEndwmntsInd = Column(Text)
    # Line number:  Part IV Line 10  Description:  Term or permanent endowments?  xpath: /IRS990/TempOrPermanentEndowmentsInd 

    RprtLndBldngEqpmntInd = Column(Text)
    # Line number:  Part IV Line 11a  Description:  Balance sheet land, buildings, equipment amounts reported?  xpath: /IRS990/ReportLandBuildingEquipmentInd 

    RprtInvstmntsOthrScInd = Column(Text)
    # Line number:  Part IV Line 11b  Description:  Balance sheet investments - other securities amounts reported?  xpath: /IRS990/ReportInvestmentsOtherSecInd 

    RprtPrgrmRltdInvstInd = Column(Text)
    # Line number:  Part IV Line 11c  Description:  Balance sheet investments - program related amounts reported?  xpath: /IRS990/ReportProgramRelatedInvstInd 

    RprtOthrAsstsInd = Column(Text)
    # Line number:  Part IV Line 11d  Description:  Balance sheet other assets amounts reported?  xpath: /IRS990/ReportOtherAssetsInd 

    RprtOthrLbltsInd = Column(Text)
    # Line number:  Part IV Line 11e  Description:  Balance sheet other liabilities amounts reported?  xpath: /IRS990/ReportOtherLiabilitiesInd 

    IncldFIN48FtntInd = Column(Text)
    # Line number:  Part IV Line 11f  Description:  Balance sheet footnote for liability under FIN 48?  xpath: /IRS990/IncludeFIN48FootnoteInd 

    IndpndntAdtFnclStmtInd = Column(Text)
    # Line number:  Part IV Line 12a  Description:  Independent audited financial statements?  xpath: /IRS990/IndependentAuditFinclStmtInd 

    CnsldtdAdtFnclStmtInd = Column(Text)
    # Line number:  Part IV Line 12b  Description:  Consolidated audited financial statement?  xpath: /IRS990/ConsolidatedAuditFinclStmtInd 

    SchlOprtngInd = Column(Text)
    # Line number:  Part IV Line 13  Description:  School?  xpath: /IRS990/SchoolOperatingInd 

    FrgnOffcInd = Column(String(length=5))
    # Line number:  Part IV Line 14a  Description:  Foreign office?  xpath: /IRS990/ForeignOfficeInd 

    FrgnActvtsInd = Column(Text)
    # Line number:  Part IV Line 14b  Description:  Foreign activities, etc?  xpath: /IRS990/ForeignActivitiesInd 

    MrThn5000KTOrgInd = Column(Text)
    # Line number:  Part IV Line 15  Description:  More than $5000 to organizations Part IX, line 3?  xpath: /IRS990/MoreThan5000KToOrgInd 

    MrThn5000KTIndvdlsInd = Column(Text)
    # Line number:  Part IV Line 16  Description:  More than $5000 to individuals Part IX, line 3?  xpath: /IRS990/MoreThan5000KToIndividualsInd 

    PrfssnlFndrsngInd = Column(Text)
    # Line number:  Part IV Line 17  Description:  Professional fundraising?  xpath: /IRS990/ProfessionalFundraisingInd 

    FndrsngActvtsInd = Column(Text)
    # Line number:  Part IV Line 18  Description:  Fundraising activities?  xpath: /IRS990/FundraisingActivitiesInd 

    GmngActvtsInd = Column(Text)
    # Line number:  Part IV Line 19  Description:  Gaming?  xpath: /IRS990/GamingActivitiesInd 

    OprtHsptlInd = Column(Text)
    # Line number:  Part IV Line 20a  Description:  Hospital?  xpath: /IRS990/OperateHospitalInd 

    AdtdFnnclStmtAttInd = Column(Text)
    # Line number:  Part IV Line 20b  Description:  Audited financial statement attached?  xpath: /IRS990/AuditedFinancialStmtAttInd 

    GrntsTOrgnztnsInd = Column(Text)
    # Line number:  Part IV Line 21  Description:  Grants to organizations?  xpath: /IRS990/GrantsToOrganizationsInd 

    GrntsTIndvdlsInd = Column(Text)
    # Line number:  Part IV Line 22  Description:  Grants to individuals?  xpath: /IRS990/GrantsToIndividualsInd 

    SkdJRqrdInd = Column(Text)
    # Line number:  Part IV Line 23  Description:  Part VII, Lines 3, 4, or 5 = "Yes"?  xpath: /IRS990/ScheduleJRequiredInd 

    TxExmptBndsInd = Column(Text)
    # Line number:  Part IV Line 24a  Description:  Tax exempt bonds?  xpath: /IRS990/TaxExemptBondsInd 

    InvstTxExmptBndsInd = Column(String(length=5))
    # Line number:  Part IV Line 24b  Description:  Investment income?  xpath: /IRS990/InvestTaxExemptBondsInd 

    EscrwAccntInd = Column(String(length=5))
    # Line number:  Part IV Line 24c  Description:  Escrow account?  xpath: /IRS990/EscrowAccountInd 

    OnBhlfOfIssrInd = Column(String(length=5))
    # Line number:  Part IV Line 24d  Description:  On behalf of issuer?  xpath: /IRS990/OnBehalfOfIssuerInd 

    EnggdInExcssBnftTrnsInd = Column(Text)
    # Line number:  Part IV Line 25a  Description:  Excess benefit transaction?  xpath: /IRS990/EngagedInExcessBenefitTransInd 

    PYExcssBnftTrnsInd = Column(Text)
    # Line number:  Part IV Line 25b  Description:  Prior excess benefit transaction?  xpath: /IRS990/PYExcessBenefitTransInd 

    LnOtstndngInd = Column(Text)
    # Line number:  Part IV Line 26  Description:  Loan to officer or DQP?  xpath: /IRS990/LoanOutstandingInd 

    GrntTRltdPrsnInd = Column(Text)
    # Line number:  Part IV Line 27  Description:  Grant to related person?  xpath: /IRS990/GrantToRelatedPersonInd 

    BsnssRlnWthOrgMmInd = Column(Text)
    # Line number:  Part IV Line 28a  Description:  Business relationship with organization?  xpath: /IRS990/BusinessRlnWithOrgMemInd 

    BsnssRlnWthFmMmInd = Column(Text)
    # Line number:  Part IV Line 28b  Description:  Business relationship thru family member?  xpath: /IRS990/BusinessRlnWithFamMemInd 

    BsnssRlnWthOffcrEntInd = Column(Text)
    # Line number:  Part IV Line 28c  Description:  Officer, etc. of entity with business relationship?  xpath: /IRS990/BusinessRlnWithOfficerEntInd 

    DdctblNnCshCntrInd = Column(Text)
    # Line number:  Part IV Line 29  Description:  Deductible non-cash contributions?  xpath: /IRS990/DeductibleNonCashContriInd 

    DdctblArtCntrbtnInd = Column(Text)
    # Line number:  Part IV Line 30  Description:  Deductible contributions of art, etc?  xpath: /IRS990/DeductibleArtContributionInd 

    TrmntOprtnsInd = Column(Text)
    # Line number:  Part IV Line 31  Description:  Terminated?  xpath: /IRS990/TerminateOperationsInd 

    PrtlLqdtnInd = Column(Text)
    # Line number:  Part IV Line 32  Description:  Partial liquidation?  xpath: /IRS990/PartialLiquidationInd 

    DsrgrddEnttyInd = Column(Text)
    # Line number:  Part IV Line 33  Description:  Disregarded entity?  xpath: /IRS990/DisregardedEntityInd 

    RltdEnttyInd = Column(Text)
    # Line number:  Part IV Line 34  Description:  Related entity?  xpath: /IRS990/RelatedEntityInd 

    RltdOrgnztnCtrlEntInd = Column(String(length=5))
    # Line number:  Part IV Line 35a  Description:  Related organization a controlled entity?  xpath: /IRS990/RelatedOrganizationCtrlEntInd 

    TrnsctnWthCntrlEntInd = Column(Text)
    # Line number:  Part IV Line 35b  Description:  Payment from or engage in transaction with a controlled entity?  xpath: /IRS990/TransactionWithControlEntInd 

    TrnsfrExmptNnChrtblRltdOrgInd = Column(Text)
    # Line number:  Part IV Line 36  Description:  Any transfers to exempt non-charitable org?  xpath: /IRS990/TrnsfrExmptNonChrtblRltdOrgInd 

    ActvtsCndctdPrtshpInd = Column(Text)
    # Line number:  Part IV Line 37  Description:  Activities conducted thru partnership?  xpath: /IRS990/ActivitiesConductedPrtshpInd 

    SkdORqrdInd = Column(String(length=5))
    # Line number:  Part IV Line 38  Description:  Governing body and public disclosure explained in Schedule O?  xpath: /IRS990/ScheduleORequiredInd 

#######
#
# IRS990 -  Part V Other Filings 
#
#######

class part_v(Base):
    __tablename__='part_v'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    InfInSkdOPrtVInd = Column(String(length=1))
    # Line number:  Part V  Description:  Schedule O contains a response to a question in Part V  xpath: /IRS990/InfoInScheduleOPartVInd 

    IRPDcmntCnt = Column(Integer)
    # Line number:  Part V Line 1a  Description:  Number forms transmitted with 1096  xpath: /IRS990/IRPDocumentCnt 

    IRPDcmntW2GCnt = Column(Integer)
    # Line number:  Part V Line 1b  Description:  Number W-2Gs included in 1a  xpath: /IRS990/IRPDocumentW2GCnt 

    BckpWthldCmplncInd = Column(String(length=5))
    # Line number:  Part V Line 1c  Description:  Compliance with backup witholding?  xpath: /IRS990/BackupWthldComplianceInd 

    EmplyCnt = Column(Integer)
    # Line number:  Part V Line 2a  Description:  Number of employees  xpath: /IRS990/EmployeeCnt 

    EmplymntTxRtrnsFldInd = Column(String(length=5))
    # Line number:  Part V Line 2b  Description:  Employment tax returns filed?  xpath: /IRS990/EmploymentTaxReturnsFiledInd 

    UnrltdBsIncmOvrLmtInd = Column(String(length=5))
    # Line number:  Part V Line 3a  Description:  Unrelated business income?  xpath: /IRS990/UnrelatedBusIncmOverLimitInd 

    Frm990TFldInd = Column(String(length=5))
    # Line number:  Part V Line 3b  Description:  Form 990-T filed?  xpath: /IRS990/Form990TFiledInd 

    FrgnFnnclAccntInd = Column(String(length=5))
    # Line number:  Part V Line 4a  Description:  Foreign financial account?  xpath: /IRS990/ForeignFinancialAccountInd 

    PrhbtdTxShltrTrnsInd = Column(String(length=5))
    # Line number:  Part V Line 5a  Description:  Prohibited tax shelter transaction?  xpath: /IRS990/ProhibitedTaxShelterTransInd 

    TxblPrtyNtfctnInd = Column(String(length=5))
    # Line number:  Part V Line 5b  Description:  Taxable party notification?  xpath: /IRS990/TaxablePartyNotificationInd 

    Frm8886TFldInd = Column(String(length=5))
    # Line number:  Part V Line 5c  Description:  Form 8886-T filed?  xpath: /IRS990/Form8886TFiledInd 

    NnddctblCntrbtnsInd = Column(String(length=5))
    # Line number:  Part V Line 6a  Description:  Non-deductible contributions?  xpath: /IRS990/NondeductibleContributionsInd 

    NnddctblCntrDsclInd = Column(String(length=5))
    # Line number:  Part V Line 6b  Description:  Non-deduct. disclosure?  xpath: /IRS990/NondeductibleContriDisclInd 

    QdPrQCntrbtnsInd = Column(String(length=5))
    # Line number:  Part V Line 7a  Description:  Quid pro quo contributions?  xpath: /IRS990/QuidProQuoContributionsInd 

    QdPrQCntrDsclInd = Column(String(length=5))
    # Line number:  Part V Line 7b  Description:  Quid pro quo disclosure?  xpath: /IRS990/QuidProQuoContriDisclInd 

    Frm8282PrprtyDspsdOfInd = Column(String(length=5))
    # Line number:  Part V Line 7c  Description:  Form 8282 property disposed of?  xpath: /IRS990/Form8282PropertyDisposedOfInd 

    Frm8282FldCnt = Column(Integer)
    # Line number:  Part V Line 7d  Description:  Number of 8282s filed  xpath: /IRS990/Form8282FiledCnt 

    RcvFndsTPyPrsnlBnftCntrctInd = Column(String(length=5))
    # Line number:  Part V Line 7e  Description:  Funds to pay premiums?  xpath: /IRS990/RcvFndsToPayPrsnlBnftCntrctInd 

    PyPrmmsPrsnlBnftCntrctInd = Column(String(length=5))
    # Line number:  Part V Line 7f  Description:  Premiums paid?  xpath: /IRS990/PayPremiumsPrsnlBnftCntrctInd 

    Frm8899Fldnd = Column(String(length=5))
    # Line number:  Part V Line 7g  Description:  Form 8899 filed?  xpath: /IRS990/Form8899Filedind 

    Frm1098CFldInd = Column(String(length=5))
    # Line number:  Part V Line 7h  Description:  Form 1098-C filed?  xpath: /IRS990/Form1098CFiledInd 

    DAFExcssBsnssHldngsInd = Column(String(length=5))
    # Line number:  Part V Line 8  Description:  Donor advised fund have excess business holdings?  xpath: /IRS990/DAFExcessBusinessHoldingsInd 

    TxblDstrbtnsInd = Column(String(length=5))
    # Line number:  Part V Line 9a  Description:  Taxable distributions?  xpath: /IRS990/TaxableDistributionsInd 

    DstrbtnTDnrInd = Column(String(length=5))
    # Line number:  Part V Line 9b  Description:  Distribution to donor?  xpath: /IRS990/DistributionToDonorInd 

    InttnFsAndCpCntrAmt = Column(BigInteger)
    # Line number:  Part V Line 10a  Description:  Initiation fees amount  xpath: /IRS990/InitiationFeesAndCapContriAmt 

    GrssRcptsFrPblcUsAmt = Column(BigInteger)
    # Line number:  Part V Line 10b  Description:  Gross receipts amount  xpath: /IRS990/GrossReceiptsForPublicUseAmt 

    MmbrsAndShrGrssIncmAmt = Column(BigInteger)
    # Line number:  Part V Line 11a  Description:  Gross income from members  xpath: /IRS990/MembersAndShrGrossIncomeAmt 

    OthrSrcsGrssIncmAmt = Column(BigInteger)
    # Line number:  Part V Line 11b  Description:  Gross income, other sources  xpath: /IRS990/OtherSourcesGrossIncomeAmt 

    OrgFldInLOfFrm1041Ind = Column(String(length=5))
    # Line number:  Part V Line 12a  Description:  Filed lieu 1041?  xpath: /IRS990/OrgFiledInLieuOfForm1041Ind 

    TxExmptIntrstAmt = Column(BigInteger)
    # Line number:  Part V Line 12b  Description:  Amount of tax exempt interest  xpath: /IRS990/TaxExemptInterestAmt 

    LcnsdMrThnOnSttInd = Column(String(length=5))
    # Line number:  Part V Line 13a  Description:  Is the organization licensed to issue qualified health plans in more than one state?  xpath: /IRS990/LicensedMoreThanOneStateInd 

    SttRqrdRsrvsAmt = Column(BigInteger)
    # Line number:  Part V Line 13b  Description:  State required reserves amount  xpath: /IRS990/StateRequiredReservesAmt 

    RsrvsMntndAmt = Column(BigInteger)
    # Line number:  Part V Line 13c  Description:  Reserves maintained amount  xpath: /IRS990/ReservesMaintainedAmt 

    IndrTnnngSrvcsInd = Column(String(length=5))
    # Line number:  Part V Line 14a  Description:  Payments received for indoor tanning services?  xpath: /IRS990/IndoorTanningServicesInd 

    Frm720FldInd = Column(String(length=5))
    # Line number:  Part V Line 14b  Description:  Form 720 filed and taxes paid on indoor tanning services?  xpath: /IRS990/Form720FiledInd 

#######
#
# IRS990 -  Part VI Governance 
#
#######

class part_vi(Base):
    __tablename__='part_vi'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    InfInSkdOPrtVIInd = Column(String(length=1))
    # Line number:  Part VI  Description:  Schedule O contains a response to a question in Part VI  xpath: /IRS990/InfoInScheduleOPartVIInd 

    GvrnngBdyVtngMmbrsCnt = Column(Integer)
    # Line number:  Part VI Section A Line 1a  Description:  Number of voting governing body members  xpath: /IRS990/GoverningBodyVotingMembersCnt 

    IndpndntVtngMmbrCnt = Column(Integer)
    # Line number:  Part VI Section A Line 1b  Description:  Number of independent voting members  xpath: /IRS990/IndependentVotingMemberCnt 

    FmlyOrBsnssRlnInd = Column(String(length=5))
    # Line number:  Part VI Section A Line 2  Description:  Family or business relationship?  xpath: /IRS990/FamilyOrBusinessRlnInd 

    DlgtnOfMgmtDtsInd = Column(String(length=5))
    # Line number:  Part VI Section A Line 3  Description:  Delegation of management duties?  xpath: /IRS990/DelegationOfMgmtDutiesInd 

    ChngTOrgDcmntsInd = Column(String(length=5))
    # Line number:  Part VI Section A Line 4  Description:  Changes to organizing docs?  xpath: /IRS990/ChangeToOrgDocumentsInd 

    MtrlDvrsnOrMssInd = Column(String(length=5))
    # Line number:  Part VI Section A Line 5  Description:  Material diversion or misuse?  xpath: /IRS990/MaterialDiversionOrMisuseInd 

    MmbrsOrStckhldrsInd = Column(String(length=5))
    # Line number:  Part VI Section A Line 6  Description:  Members or stockholders?  xpath: /IRS990/MembersOrStockholdersInd 

    ElctnOfBrdMmbrsInd = Column(String(length=5))
    # Line number:  Part VI Section A Line 7a  Description:  election of board members?  xpath: /IRS990/ElectionOfBoardMembersInd 

    DcsnsSbjctTApprvInd = Column(String(length=5))
    # Line number:  Part VI Section A Line 7b  Description:  decisions subject to approval?  xpath: /IRS990/DecisionsSubjectToApprovaInd 

    MntsOfGvrnngBdyInd = Column(String(length=5))
    # Line number:  Part VI Section A Line 8a  Description:  Minutes of governing body?  xpath: /IRS990/MinutesOfGoverningBodyInd 

    MntsOfCmmttsInd = Column(String(length=5))
    # Line number:  Part VI Section A Line 8b  Description:  Minutes of committees?  xpath: /IRS990/MinutesOfCommitteesInd 

    OffcrMlngAddrssInd = Column(String(length=5))
    # Line number:  Part VI Section A Line 9  Description:  Officer mailing address?  xpath: /IRS990/OfficerMailingAddressInd 

    LclChptrsInd = Column(String(length=5))
    # Line number:  Part VI Section B Line 10a  Description:  Local chapters?  xpath: /IRS990/LocalChaptersInd 

    PlcsRfrncChptrsInd = Column(String(length=5))
    # Line number:  Part VI Section B Line 10b  Description:  Policies reference chapters?  xpath: /IRS990/PoliciesReferenceChaptersInd 

    Frm990PrvddTGvrnBdyInd = Column(String(length=5))
    # Line number:  Part VI Section B Line 11  Description:  Form 990 provided to governing body?  xpath: /IRS990/Form990ProvidedToGvrnBodyInd 

    CnflctOfIntrstPlcyInd = Column(String(length=5))
    # Line number:  Part VI Section B Line 12a  Description:  Conflict of interest policy?  xpath: /IRS990/ConflictOfInterestPolicyInd 

    AnnlDsclsrCvrdPrsnInd = Column(String(length=5))
    # Line number:  Part VI Section B Line 12b  Description:  Annual disclosure by covered persons?  xpath: /IRS990/AnnualDisclosureCoveredPrsnInd 

    RglrMntrngEnfrcInd = Column(String(length=5))
    # Line number:  Part VI Section B Line 12c  Description:  Regular monitoring and enforcement?  xpath: /IRS990/RegularMonitoringEnfrcInd 

    WhstlblwrPlcyInd = Column(String(length=5))
    # Line number:  Part VI Section B Line 13  Description:  Whistleblower policy?  xpath: /IRS990/WhistleblowerPolicyInd 

    DcmntRtntnPlcyInd = Column(String(length=5))
    # Line number:  Part VI Section B Line 14  Description:  Document retention policy?  xpath: /IRS990/DocumentRetentionPolicyInd 

    CmpnstnPrcssCEOInd = Column(String(length=5))
    # Line number:  Part VI Section B Line 15a  Description:  Compensation process CEO?  xpath: /IRS990/CompensationProcessCEOInd 

    CmpnstnPrcssOthrInd = Column(String(length=5))
    # Line number:  Part VI Section B Line 15b  Description:  Compensation process other?  xpath: /IRS990/CompensationProcessOtherInd 

    InvstmntInJntVntrInd = Column(String(length=5))
    # Line number:  Part VI Section B Line 16a  Description:  Investment in joint venture?  xpath: /IRS990/InvestmentInJointVentureInd 

    WrttnPlcyOrPrcdrInd = Column(String(length=5))
    # Line number:  Part VI Section B Line 16b  Description:  Written policy or procedure?  xpath: /IRS990/WrittenPolicyOrProcedureInd 

    OwnWbstInd = Column(String(length=1))
    # Line number:  Part VI Section C Line 18  Description:  Own website  xpath: /IRS990/OwnWebsiteInd 

    OthrWbstInd = Column(String(length=1))
    # Line number:  Part VI Section C Line 18  Description:  Other website  xpath: /IRS990/OtherWebsiteInd 

    UpnRqstInd = Column(String(length=1))
    # Line number:  Part VI Section C Line 18  Description:  Upon request  xpath: /IRS990/UponRequestInd 

    OthrInd = Column(String(length=1))
    # Line number:  Part VI Section C Line 18  Description:  Other (Explain in Schedule O)  xpath: /IRS990/OtherInd 

    BksInCrOfDtl = Column(Text)
    # Description:  The books are in care of  xpath: /IRS990/BooksInCareOfDetail 

    BksInCrOfDtl_PrsnNm = Column(String(length=35))
    # Line number:  Part VI Section C Line 20  Description:  Name - Person  xpath: /IRS990/BooksInCareOfDetail/PersonNm 

    BsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part VI Section C Line 20  Description:  Business name line 1  xpath: /IRS990/BooksInCareOfDetail/BusinessName/BusinessNameLine1Txt 

    BsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part VI Section C Line 20  Description:  Business name line 2  xpath: /IRS990/BooksInCareOfDetail/BusinessName/BusinessNameLine2Txt 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VI Section C Line 20  Description:  Address line 1  xpath: /IRS990/BooksInCareOfDetail/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VI Section C Line 20  Description:  Address line 2  xpath: /IRS990/BooksInCareOfDetail/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part VI Section C Line 20  Description:  City  xpath: /IRS990/BooksInCareOfDetail/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part VI Section C Line 20  Description:  State  xpath: /IRS990/BooksInCareOfDetail/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part VI Section C Line 20  Description:  ZIP code  xpath: /IRS990/BooksInCareOfDetail/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VI Section C Line 20  Description:  Address line 1  xpath: /IRS990/BooksInCareOfDetail/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VI Section C Line 20  Description:  Address line 2  xpath: /IRS990/BooksInCareOfDetail/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part VI Section C Line 20  Description:  City  xpath: /IRS990/BooksInCareOfDetail/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part VI Section C Line 20  Description:  Province or state  xpath: /IRS990/BooksInCareOfDetail/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part VI Section C Line 20  Description:  Country  xpath: /IRS990/BooksInCareOfDetail/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part VI Section C Line 20  Description:  Postal code  xpath: /IRS990/BooksInCareOfDetail/ForeignAddress/ForeignPostalCd 

    BksInCrOfDtl_PhnNm = Column(String(length=10))
    # Line number:  Part VI Section C Line 20  Description:  Telephone number  xpath: /IRS990/BooksInCareOfDetail/PhoneNum 

#######
#
# IRS990 -  Part VII Compensation 
#
#######

class part_vii(Base):
    __tablename__='part_vii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    InfInSkdOPrtVIIInd = Column(String(length=1))
    # Line number:  Part VII  Description:  Schedule O contains a response to a question in Part VII  xpath: /IRS990/InfoInScheduleOPartVIIInd 

    NLstdPrsnsCmpnstdInd = Column(String(length=1))
    # Line number:  Part VII Section A  Description:  No listed persons compensated  xpath: /IRS990/NoListedPersonsCompensatedInd 

    TtlRprtblCmpFrmOrgAmt = Column(BigInteger)
    # Line number:  Part VII Section A Line 1d D  Description:  Total, column D  xpath: /IRS990/TotalReportableCompFromOrgAmt 

    TtRprtblCmpRltdOrgAmt = Column(BigInteger)
    # Line number:  Part VII Section A Line 1d E  Description:  Total, column E  xpath: /IRS990/TotReportableCompRltdOrgAmt 

    TtlOthrCmpnstnAmt = Column(BigInteger)
    # Line number:  Part VII Section A Line 1d F  Description:  Total, column F  xpath: /IRS990/TotalOtherCompensationAmt 

    IndvRcvdGrtrThn100KCnt = Column(Integer)
    # Line number:  Part VII Section A Line 2  Description:  Number individuals greater than $100K  xpath: /IRS990/IndivRcvdGreaterThan100KCnt 

    FrmrOfcrEmplysLstdInd = Column(String(length=5))
    # Line number:  Part VII Section A Line 3  Description:  Formers listed in 1a?  xpath: /IRS990/FormerOfcrEmployeesListedInd 

    TtlCmpGrtrThn150KInd = Column(String(length=5))
    # Line number:  Part VII Section A Line 4  Description:  Line1a, total greater than $150K?  xpath: /IRS990/TotalCompGreaterThan150KInd 

    CmpnstnFrmOthrSrcsInd = Column(String(length=5))
    # Line number:  Part VII Section A Line 5  Description:  Compensation from other sources?  xpath: /IRS990/CompensationFromOtherSrcsInd 

    CntrctRcvdGrtrThn100KCnt = Column(Integer)
    # Line number:  Part VII Section B Line 2  Description:  Number of contractors greater than $100K  xpath: /IRS990/CntrctRcvdGreaterThan100KCnt 

#######
#
# IRS990 -  Part VIII Revenue 
#
#######

class part_viii(Base):
    __tablename__='part_viii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    InfInSkdOPrtVIIIInd = Column(String(length=1))
    # Line number:  Part VIII  Description:  Schedule O contains a response to a question in Part VIII  xpath: /IRS990/InfoInScheduleOPartVIIIInd 

    FdrtdCmpgnsAmt = Column(BigInteger)
    # Line number:  Part VIII Line 1a  Description:  Federated campaigns  xpath: /IRS990/FederatedCampaignsAmt 

    MmbrshpDsAmt = Column(BigInteger)
    # Line number:  Part VIII Line 1b  Description:  Outside fundraising or commercial co-ventures  xpath: /IRS990/MembershipDuesAmt 

    FndrsngAmt = Column(BigInteger)
    # Line number:  Part VIII Line 1c  Description:  Fundraising events  xpath: /IRS990/FundraisingAmt 

    RltdOrgnztnsAmt = Column(BigInteger)
    # Line number:  Part VIII Line 1d  Description:  Related organizations  xpath: /IRS990/RelatedOrganizationsAmt 

    GvrnmntGrntsAmt = Column(BigInteger)
    # Line number:  Part VIII Line 1e  Description:  Government grants (contributions)  xpath: /IRS990/GovernmentGrantsAmt 

    AllOthrCntrbtnsAmt = Column(BigInteger)
    # Line number:  Part VIII Line 1f  Description:  All other contributions, gifts, grants, and similar amounts not included in above  xpath: /IRS990/AllOtherContributionsAmt 

    NncshCntrbtnsAmt = Column(BigInteger)
    # Line number:  Part VIII Line 1g  Description:  Noncash contributions  xpath: /IRS990/NoncashContributionsAmt 

    TtlCntrbtnsAmt = Column(BigInteger)
    # Line number:  Part VIII Line 1h Column (A)  Description:  Total contributions  xpath: /IRS990/TotalContributionsAmt 

    TtlPrgrmSrvcRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Line 2g  Description:  Program service revenue total  xpath: /IRS990/TotalProgramServiceRevenueAmt 

    GrssRnts_RlAmt = Column(BigInteger)
    # Line number:  Part VIII Column (i)  Description:  Real amount  xpath: /IRS990/GrossRentsGrp/RealAmt 

    GrssRnts_PrsnlAmt = Column(BigInteger)
    # Line number:  Part VIII Column (ii)  Description:  Amount  xpath: /IRS990/GrossRentsGrp/PersonalAmt 

    LssRntlExpnss_RlAmt = Column(BigInteger)
    # Line number:  Part VIII Column (i)  Description:  Real amount  xpath: /IRS990/LessRentalExpensesGrp/RealAmt 

    LssRntlExpnss_PrsnlAmt = Column(BigInteger)
    # Line number:  Part VIII Column (ii)  Description:  Amount  xpath: /IRS990/LessRentalExpensesGrp/PersonalAmt 

    RntlIncmOrLss_RlAmt = Column(BigInteger)
    # Line number:  Part VIII Column (i)  Description:  Real amount  xpath: /IRS990/RentalIncomeOrLossGrp/RealAmt 

    RntlIncmOrLss_PrsnlAmt = Column(BigInteger)
    # Line number:  Part VIII Column (ii)  Description:  Amount  xpath: /IRS990/RentalIncomeOrLossGrp/PersonalAmt 

    GrssAmntSlsAssts_ScrtsAmt = Column(BigInteger)
    # Line number:  Part VIII Column (i)  Description:  Securities amount  xpath: /IRS990/GrossAmountSalesAssetsGrp/SecuritiesAmt 

    GrssAmntSlsAssts_OthrAmt = Column(BigInteger)
    # Line number:  Part VIII Column (ii)  Description:  Other amount  xpath: /IRS990/GrossAmountSalesAssetsGrp/OtherAmt 

    LssCstOthBssSlsExpnss_ScrtsAmt = Column(BigInteger)
    # Line number:  Part VIII Column (i)  Description:  Securities amount  xpath: /IRS990/LessCostOthBasisSalesExpnssGrp/SecuritiesAmt 

    LssCstOthBssSlsExpnss_OthrAmt = Column(BigInteger)
    # Line number:  Part VIII Column (ii)  Description:  Other amount  xpath: /IRS990/LessCostOthBasisSalesExpnssGrp/OtherAmt 

    GnOrLss_ScrtsAmt = Column(BigInteger)
    # Line number:  Part VIII Column (i)  Description:  Securities amount  xpath: /IRS990/GainOrLossGrp/SecuritiesAmt 

    GnOrLss_OthrAmt = Column(BigInteger)
    # Line number:  Part VIII Column (ii)  Description:  Other amount  xpath: /IRS990/GainOrLossGrp/OtherAmt 

    FndrsngGrssIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Line 8a  Description:  Gross income from fundraising events, Line 8a box  xpath: /IRS990/FundraisingGrossIncomeAmt 

    CntrRptFndrsngEvntAmt = Column(BigInteger)
    # Line number:  Part VIII Line 8a  Description:  Contributions reported from fundraising events on line 1c, Line 8a underline  xpath: /IRS990/ContriRptFundraisingEventAmt 

    FndrsngDrctExpnssAmt = Column(BigInteger)
    # Line number:  Part VIII Line 8b  Description:  Direct expenses  xpath: /IRS990/FundraisingDirectExpensesAmt 

    NtIncmFrmFndrsngEvt_TtlRvnClmnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  xpath: /IRS990/NetIncmFromFundraisingEvtGrp/TotalRevenueColumnAmt 

    NtIncmFrmFndrsngEvt_UnrltdBsnssRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  xpath: /IRS990/NetIncmFromFundraisingEvtGrp/UnrelatedBusinessRevenueAmt 

    NtIncmFrmFndrsngEvt_ExclsnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  xpath: /IRS990/NetIncmFromFundraisingEvtGrp/ExclusionAmt 

    GmngGrssIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Line 9a  Description:  Gross income from gaming  xpath: /IRS990/GamingGrossIncomeAmt 

    GmngDrctExpnssAmt = Column(BigInteger)
    # Line number:  Part VIII Line 9b  Description:  Direct expenses  xpath: /IRS990/GamingDirectExpensesAmt 

    GrssSlsOfInvntryAmt = Column(BigInteger)
    # Line number:  Part VIII Line 10a  Description:  Gross sales of inventory, less returns and allowances  xpath: /IRS990/GrossSalesOfInventoryAmt 

    CstOfGdsSldAmt = Column(BigInteger)
    # Line number:  Part VIII Line 10b  Description:  Less cost of goods sold  xpath: /IRS990/CostOfGoodsSoldAmt 

    OthrRvnTtlAmt = Column(BigInteger)
    # Line number:  Part VIII Line 11e  Description:  Other miscellaneous revenue total  xpath: /IRS990/OtherRevenueTotalAmt 

    TtlRvn_TtlRvnClmnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  xpath: /IRS990/TotalRevenueGrp/TotalRevenueColumnAmt 

    TtlRvn_RltdOrExmptFncIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  xpath: /IRS990/TotalRevenueGrp/RelatedOrExemptFuncIncomeAmt 

    TtlRvn_UnrltdBsnssRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  xpath: /IRS990/TotalRevenueGrp/UnrelatedBusinessRevenueAmt 

    TtlRvn_ExclsnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  xpath: /IRS990/TotalRevenueGrp/ExclusionAmt 

    TtlOthPrgrmSrvcRv_TtlRvnClmnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  xpath: /IRS990/TotalOthProgramServiceRevGrp/TotalRevenueColumnAmt 

    NtIncmFrmGmng_TtlRvnClmnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  xpath: /IRS990/NetIncomeFromGamingGrp/TotalRevenueColumnAmt 

    NtRntlIncmOrLss_TtlRvnClmnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  xpath: /IRS990/NetRentalIncomeOrLossGrp/TotalRevenueColumnAmt 

    NtIncmOrLss_TtlRvnClmnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  xpath: /IRS990/NetIncomeOrLossGrp/TotalRevenueColumnAmt 

    MscRvn_TtlRvnClmnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  xpath: /IRS990/MiscellaneousRevenueGrp/TotalRevenueColumnAmt 

    IncmFrmInvstBndPrcds_TtlRvnClmnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  xpath: /IRS990/IncmFromInvestBondProceedsGrp/TotalRevenueColumnAmt 

    NtGnOrLssInvstmnts_TtlRvnClmnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  xpath: /IRS990/NetGainOrLossInvestmentsGrp/TotalRevenueColumnAmt 

    RyltsRvn_TtlRvnClmnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  xpath: /IRS990/RoyaltiesRevenueGrp/TotalRevenueColumnAmt 

    InvstmntIncm_TtlRvnClmnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  xpath: /IRS990/InvestmentIncomeGrp/TotalRevenueColumnAmt 

    RyltsRvn_RltdOrExmptFncIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  xpath: /IRS990/RoyaltiesRevenueGrp/RelatedOrExemptFuncIncomeAmt 

    TtlOthPrgrmSrvcRv_RltdOrExmptFncIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  xpath: /IRS990/TotalOthProgramServiceRevGrp/RelatedOrExemptFuncIncomeAmt 

    InvstmntIncm_RltdOrExmptFncIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  xpath: /IRS990/InvestmentIncomeGrp/RelatedOrExemptFuncIncomeAmt 

    NtGnOrLssInvstmnts_RltdOrExmptFncIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  xpath: /IRS990/NetGainOrLossInvestmentsGrp/RelatedOrExemptFuncIncomeAmt 

    NtIncmFrmGmng_RltdOrExmptFncIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  xpath: /IRS990/NetIncomeFromGamingGrp/RelatedOrExemptFuncIncomeAmt 

    NtIncmOrLss_RltdOrExmptFncIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  xpath: /IRS990/NetIncomeOrLossGrp/RelatedOrExemptFuncIncomeAmt 

    MscRvn_RltdOrExmptFncIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  xpath: /IRS990/MiscellaneousRevenueGrp/RelatedOrExemptFuncIncomeAmt 

    NtRntlIncmOrLss_RltdOrExmptFncIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  xpath: /IRS990/NetRentalIncomeOrLossGrp/RelatedOrExemptFuncIncomeAmt 

    IncmFrmInvstBndPrcds_RltdOrExmptFncIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  xpath: /IRS990/IncmFromInvestBondProceedsGrp/RelatedOrExemptFuncIncomeAmt 

    MscRvn_UnrltdBsnssRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  xpath: /IRS990/MiscellaneousRevenueGrp/UnrelatedBusinessRevenueAmt 

    NtIncmFrmGmng_UnrltdBsnssRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  xpath: /IRS990/NetIncomeFromGamingGrp/UnrelatedBusinessRevenueAmt 

    NtRntlIncmOrLss_UnrltdBsnssRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  xpath: /IRS990/NetRentalIncomeOrLossGrp/UnrelatedBusinessRevenueAmt 

    NtGnOrLssInvstmnts_UnrltdBsnssRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  xpath: /IRS990/NetGainOrLossInvestmentsGrp/UnrelatedBusinessRevenueAmt 

    RyltsRvn_UnrltdBsnssRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  xpath: /IRS990/RoyaltiesRevenueGrp/UnrelatedBusinessRevenueAmt 

    IncmFrmInvstBndPrcds_UnrltdBsnssRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  xpath: /IRS990/IncmFromInvestBondProceedsGrp/UnrelatedBusinessRevenueAmt 

    InvstmntIncm_UnrltdBsnssRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  xpath: /IRS990/InvestmentIncomeGrp/UnrelatedBusinessRevenueAmt 

    NtIncmOrLss_UnrltdBsnssRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  xpath: /IRS990/NetIncomeOrLossGrp/UnrelatedBusinessRevenueAmt 

    TtlOthPrgrmSrvcRv_UnrltdBsnssRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  xpath: /IRS990/TotalOthProgramServiceRevGrp/UnrelatedBusinessRevenueAmt 

    IncmFrmInvstBndPrcds_ExclsnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  xpath: /IRS990/IncmFromInvestBondProceedsGrp/ExclusionAmt 

    MscRvn_ExclsnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  xpath: /IRS990/MiscellaneousRevenueGrp/ExclusionAmt 

    NtGnOrLssInvstmnts_ExclsnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  xpath: /IRS990/NetGainOrLossInvestmentsGrp/ExclusionAmt 

    NtIncmFrmGmng_ExclsnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  xpath: /IRS990/NetIncomeFromGamingGrp/ExclusionAmt 

    NtIncmOrLss_ExclsnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  xpath: /IRS990/NetIncomeOrLossGrp/ExclusionAmt 

    NtRntlIncmOrLss_ExclsnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  xpath: /IRS990/NetRentalIncomeOrLossGrp/ExclusionAmt 

    RyltsRvn_ExclsnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  xpath: /IRS990/RoyaltiesRevenueGrp/ExclusionAmt 

    TtlOthPrgrmSrvcRv_ExclsnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  xpath: /IRS990/TotalOthProgramServiceRevGrp/ExclusionAmt 

    InvstmntIncm_ExclsnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  xpath: /IRS990/InvestmentIncomeGrp/ExclusionAmt 

#######
#
# IRS990 -  Part IX Functional Expense 
#
#######

class part_ix(Base):
    __tablename__='part_ix'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    InfInSkdOPrtIXInd = Column(String(length=1))
    # Line number:  Part IX  Description:  Schedule O contains a response to a question in Part IX  xpath: /IRS990/InfoInScheduleOPartIXInd 

    FsFrSrvcsPrfFndrsng = Column(Text)
    # Line number:  Part IX Line 11e  Description:  Fees for services (non-employees): Professional fundraising  xpath: /IRS990/FeesForServicesProfFundraising 

    FsFrSrvcsPrfFndrsng_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/FeesForServicesProfFundraising/TotalAmt 

    FsFrSrvcsPrfFndrsng_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/FeesForServicesProfFundraising/FundraisingAmt 

    JntCstsInd = Column(String(length=1))
    # Line number:  Part IX Line 26  Description:  Joint costs?  xpath: /IRS990/JointCostsInd 

    PyrllTxs_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/PayrollTaxesGrp/TotalAmt 

    DprctnDpltn_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/DepreciationDepletionGrp/TotalAmt 

    TtlFnctnlExpnss_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/TotalFunctionalExpensesGrp/TotalAmt 

    Insrnc_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/InsuranceGrp/TotalAmt 

    FsFrSrvcsAccntng_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/FeesForServicesAccountingGrp/TotalAmt 

    PymntsTAfflts_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/PaymentsToAffiliatesGrp/TotalAmt 

    Advrtsng_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/AdvertisingGrp/TotalAmt 

    Occpncy_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/OccupancyGrp/TotalAmt 

    FsFrSrvcsLgl_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/FeesForServicesLegalGrp/TotalAmt 

    OthrEmplyBnfts_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/OtherEmployeeBenefitsGrp/TotalAmt 

    FsFrSrvcsLbbyng_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/FeesForServicesLobbyingGrp/TotalAmt 

    OthrSlrsAndWgs_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/OtherSalariesAndWagesGrp/TotalAmt 

    GrntsTDmstcOrgs_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/GrantsToDomesticOrgsGrp/TotalAmt 

    AllOthrExpnss_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/AllOtherExpensesGrp/TotalAmt 

    FsFrSrvcsMngmnt_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/FeesForServicesManagementGrp/TotalAmt 

    OffcExpnss_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/OfficeExpensesGrp/TotalAmt 

    BnftsTMmbrs_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/BenefitsToMembersGrp/TotalAmt 

    Rylts_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/RoyaltiesGrp/TotalAmt 

    FsFrSrvcsOthr_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/FeesForServicesOtherGrp/TotalAmt 

    PnsnPlnCntrbtns_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/PensionPlanContributionsGrp/TotalAmt 

    FsFrSrvcInvstMgmntFs_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/FeesForSrvcInvstMgmntFeesGrp/TotalAmt 

    FrgnGrnts_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/ForeignGrantsGrp/TotalAmt 

    Intrst_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/InterestGrp/TotalAmt 

    CmpCrrntOfcrDrctrs_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/CompCurrentOfcrDirectorsGrp/TotalAmt 

    Trvl_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/TravelGrp/TotalAmt 

    CmpDsqlPrsns_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/CompDisqualPersonsGrp/TotalAmt 

    InfrmtnTchnlgy_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/InformationTechnologyGrp/TotalAmt 

    PymtTrvlEntrtnmntPbOfcl_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/PymtTravelEntrtnmntPubOfclGrp/TotalAmt 

    TtlJntCsts_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/TotalJointCostsGrp/TotalAmt 

    GrntsTDmstcIndvdls_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/GrantsToDomesticIndividualsGrp/TotalAmt 

    CnfrncsMtngs_TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/ConferencesMeetingsGrp/TotalAmt 

    FrgnGrnts_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/ForeignGrantsGrp/ProgramServicesAmt 

    GrntsTDmstcIndvdls_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/GrantsToDomesticIndividualsGrp/ProgramServicesAmt 

    GrntsTDmstcOrgs_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/GrantsToDomesticOrgsGrp/ProgramServicesAmt 

    OffcExpnss_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/OfficeExpensesGrp/ProgramServicesAmt 

    Insrnc_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/InsuranceGrp/ProgramServicesAmt 

    Intrst_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/InterestGrp/ProgramServicesAmt 

    Occpncy_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/OccupancyGrp/ProgramServicesAmt 

    PnsnPlnCntrbtns_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/PensionPlanContributionsGrp/ProgramServicesAmt 

    TtlJntCsts_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/TotalJointCostsGrp/ProgramServicesAmt 

    OthrSlrsAndWgs_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/OtherSalariesAndWagesGrp/ProgramServicesAmt 

    Advrtsng_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/AdvertisingGrp/ProgramServicesAmt 

    TtlFnctnlExpnss_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/TotalFunctionalExpensesGrp/ProgramServicesAmt 

    AllOthrExpnss_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/AllOtherExpensesGrp/ProgramServicesAmt 

    BnftsTMmbrs_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/BenefitsToMembersGrp/ProgramServicesAmt 

    CmpCrrntOfcrDrctrs_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/CompCurrentOfcrDirectorsGrp/ProgramServicesAmt 

    Rylts_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/RoyaltiesGrp/ProgramServicesAmt 

    CmpDsqlPrsns_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/CompDisqualPersonsGrp/ProgramServicesAmt 

    PymtTrvlEntrtnmntPbOfcl_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/PymtTravelEntrtnmntPubOfclGrp/ProgramServicesAmt 

    CnfrncsMtngs_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/ConferencesMeetingsGrp/ProgramServicesAmt 

    DprctnDpltn_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/DepreciationDepletionGrp/ProgramServicesAmt 

    PyrllTxs_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/PayrollTaxesGrp/ProgramServicesAmt 

    FsFrSrvcsAccntng_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/FeesForServicesAccountingGrp/ProgramServicesAmt 

    InfrmtnTchnlgy_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/InformationTechnologyGrp/ProgramServicesAmt 

    FsFrSrvcsLgl_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/FeesForServicesLegalGrp/ProgramServicesAmt 

    PymntsTAfflts_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/PaymentsToAffiliatesGrp/ProgramServicesAmt 

    FsFrSrvcsLbbyng_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/FeesForServicesLobbyingGrp/ProgramServicesAmt 

    FsFrSrvcsMngmnt_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/FeesForServicesManagementGrp/ProgramServicesAmt 

    OthrEmplyBnfts_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/OtherEmployeeBenefitsGrp/ProgramServicesAmt 

    Trvl_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/TravelGrp/ProgramServicesAmt 

    FsFrSrvcsOthr_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/FeesForServicesOtherGrp/ProgramServicesAmt 

    FsFrSrvcInvstMgmntFs_PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/FeesForSrvcInvstMgmntFeesGrp/ProgramServicesAmt 

    Insrnc_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/InsuranceGrp/ManagementAndGeneralAmt 

    PnsnPlnCntrbtns_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/PensionPlanContributionsGrp/ManagementAndGeneralAmt 

    FsFrSrvcInvstMgmntFs_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/FeesForSrvcInvstMgmntFeesGrp/ManagementAndGeneralAmt 

    InfrmtnTchnlgy_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/InformationTechnologyGrp/ManagementAndGeneralAmt 

    OthrSlrsAndWgs_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/OtherSalariesAndWagesGrp/ManagementAndGeneralAmt 

    Advrtsng_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/AdvertisingGrp/ManagementAndGeneralAmt 

    AllOthrExpnss_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/AllOtherExpensesGrp/ManagementAndGeneralAmt 

    CmpCrrntOfcrDrctrs_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/CompCurrentOfcrDirectorsGrp/ManagementAndGeneralAmt 

    CmpDsqlPrsns_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/CompDisqualPersonsGrp/ManagementAndGeneralAmt 

    CnfrncsMtngs_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/ConferencesMeetingsGrp/ManagementAndGeneralAmt 

    DprctnDpltn_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/DepreciationDepletionGrp/ManagementAndGeneralAmt 

    FsFrSrvcsAccntng_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/FeesForServicesAccountingGrp/ManagementAndGeneralAmt 

    FsFrSrvcsLgl_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/FeesForServicesLegalGrp/ManagementAndGeneralAmt 

    FsFrSrvcsLbbyng_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/FeesForServicesLobbyingGrp/ManagementAndGeneralAmt 

    FsFrSrvcsMngmnt_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/FeesForServicesManagementGrp/ManagementAndGeneralAmt 

    FsFrSrvcsOthr_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/FeesForServicesOtherGrp/ManagementAndGeneralAmt 

    Intrst_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/InterestGrp/ManagementAndGeneralAmt 

    Occpncy_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/OccupancyGrp/ManagementAndGeneralAmt 

    OffcExpnss_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/OfficeExpensesGrp/ManagementAndGeneralAmt 

    OthrEmplyBnfts_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/OtherEmployeeBenefitsGrp/ManagementAndGeneralAmt 

    PymntsTAfflts_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/PaymentsToAffiliatesGrp/ManagementAndGeneralAmt 

    PyrllTxs_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/PayrollTaxesGrp/ManagementAndGeneralAmt 

    PymtTrvlEntrtnmntPbOfcl_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/PymtTravelEntrtnmntPubOfclGrp/ManagementAndGeneralAmt 

    Rylts_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/RoyaltiesGrp/ManagementAndGeneralAmt 

    TtlFnctnlExpnss_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/TotalFunctionalExpensesGrp/ManagementAndGeneralAmt 

    TtlJntCsts_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/TotalJointCostsGrp/ManagementAndGeneralAmt 

    Trvl_MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/TravelGrp/ManagementAndGeneralAmt 

    FsFrSrvcsMngmnt_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/FeesForServicesManagementGrp/FundraisingAmt 

    PymntsTAfflts_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/PaymentsToAffiliatesGrp/FundraisingAmt 

    Trvl_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/TravelGrp/FundraisingAmt 

    FsFrSrvcsLbbyng_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/FeesForServicesLobbyingGrp/FundraisingAmt 

    FsFrSrvcsLgl_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/FeesForServicesLegalGrp/FundraisingAmt 

    PyrllTxs_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/PayrollTaxesGrp/FundraisingAmt 

    OthrEmplyBnfts_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/OtherEmployeeBenefitsGrp/FundraisingAmt 

    FsFrSrvcsAccntng_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/FeesForServicesAccountingGrp/FundraisingAmt 

    DprctnDpltn_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/DepreciationDepletionGrp/FundraisingAmt 

    PymtTrvlEntrtnmntPbOfcl_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/PymtTravelEntrtnmntPubOfclGrp/FundraisingAmt 

    Advrtsng_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/AdvertisingGrp/FundraisingAmt 

    CnfrncsMtngs_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/ConferencesMeetingsGrp/FundraisingAmt 

    Rylts_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/RoyaltiesGrp/FundraisingAmt 

    PnsnPlnCntrbtns_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/PensionPlanContributionsGrp/FundraisingAmt 

    CmpDsqlPrsns_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/CompDisqualPersonsGrp/FundraisingAmt 

    CmpCrrntOfcrDrctrs_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/CompCurrentOfcrDirectorsGrp/FundraisingAmt 

    TtlFnctnlExpnss_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/TotalFunctionalExpensesGrp/FundraisingAmt 

    FsFrSrvcInvstMgmntFs_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/FeesForSrvcInvstMgmntFeesGrp/FundraisingAmt 

    Occpncy_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/OccupancyGrp/FundraisingAmt 

    Intrst_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/InterestGrp/FundraisingAmt 

    OffcExpnss_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/OfficeExpensesGrp/FundraisingAmt 

    AllOthrExpnss_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/AllOtherExpensesGrp/FundraisingAmt 

    Insrnc_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/InsuranceGrp/FundraisingAmt 

    InfrmtnTchnlgy_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/InformationTechnologyGrp/FundraisingAmt 

    TtlJntCsts_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/TotalJointCostsGrp/FundraisingAmt 

    FsFrSrvcsOthr_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/FeesForServicesOtherGrp/FundraisingAmt 

    OthrSlrsAndWgs_FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/OtherSalariesAndWagesGrp/FundraisingAmt 

#######
#
# IRS990 -  Part X Balance Sheet 
#
#######

class part_x(Base):
    __tablename__='part_x'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    InfInSkdOPrtXInd = Column(String(length=1))
    # Line number:  Part X  Description:  Schedule O contains a response to a question in Part X  xpath: /IRS990/InfoInScheduleOPartXInd 

    CshNnIntrstBrng_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/CashNonInterestBearingGrp/BOYAmt 

    CshNnIntrstBrng_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/CashNonInterestBearingGrp/EOYAmt 

    SvngsAndTmpCshInvst_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/SavingsAndTempCashInvstGrp/BOYAmt 

    SvngsAndTmpCshInvst_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/SavingsAndTempCashInvstGrp/EOYAmt 

    PldgsAndGrntsRcvbl_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/PledgesAndGrantsReceivableGrp/BOYAmt 

    PldgsAndGrntsRcvbl_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/PledgesAndGrantsReceivableGrp/EOYAmt 

    AccntsRcvbl_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/AccountsReceivableGrp/BOYAmt 

    AccntsRcvbl_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/AccountsReceivableGrp/EOYAmt 

    RcvblsFrmOffcrsEtc_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/ReceivablesFromOfficersEtcGrp/BOYAmt 

    RcvblsFrmOffcrsEtc_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/ReceivablesFromOfficersEtcGrp/EOYAmt 

    RcvblFrmDsqlfdPrsn_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/RcvblFromDisqualifiedPrsnGrp/BOYAmt 

    RcvblFrmDsqlfdPrsn_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/RcvblFromDisqualifiedPrsnGrp/EOYAmt 

    OthNtsLnsRcvblNt_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/OthNotesLoansReceivableNetGrp/BOYAmt 

    OthNtsLnsRcvblNt_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/OthNotesLoansReceivableNetGrp/EOYAmt 

    InvntrsFrSlOrUs_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/InventoriesForSaleOrUseGrp/BOYAmt 

    InvntrsFrSlOrUs_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/InventoriesForSaleOrUseGrp/EOYAmt 

    PrpdExpnssDfrdChrgs_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/PrepaidExpensesDefrdChargesGrp/BOYAmt 

    PrpdExpnssDfrdChrgs_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/PrepaidExpensesDefrdChargesGrp/EOYAmt 

    LndBldgEqpCstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part X Line 10a  Description:  Land, buildings, and equipment basis  xpath: /IRS990/LandBldgEquipCostOrOtherBssAmt 

    LndBldgEqpAccmDprcAmt = Column(BigInteger)
    # Line number:  Part X Line 10b  Description:  Less: accumulated depreciation  xpath: /IRS990/LandBldgEquipAccumDeprecAmt 

    LndBldgEqpBssNt_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/LandBldgEquipBasisNetGrp/BOYAmt 

    LndBldgEqpBssNt_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/LandBldgEquipBasisNetGrp/EOYAmt 

    InvstmntsPbTrddSc_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/InvestmentsPubTradedSecGrp/BOYAmt 

    InvstmntsPbTrddSc_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/InvestmentsPubTradedSecGrp/EOYAmt 

    InvstmntsOthrScrts_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/InvestmentsOtherSecuritiesGrp/BOYAmt 

    InvstmntsOthrScrts_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/InvestmentsOtherSecuritiesGrp/EOYAmt 

    InvstmntsPrgrmRltd_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/InvestmentsProgramRelatedGrp/BOYAmt 

    InvstmntsPrgrmRltd_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/InvestmentsProgramRelatedGrp/EOYAmt 

    IntngblAssts_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/IntangibleAssetsGrp/BOYAmt 

    IntngblAssts_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/IntangibleAssetsGrp/EOYAmt 

    OthrAsstsTtl_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/OtherAssetsTotalGrp/BOYAmt 

    OthrAsstsTtl_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/OtherAssetsTotalGrp/EOYAmt 

    TtlAssts_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/TotalAssetsGrp/BOYAmt 

    TtlAssts_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/TotalAssetsGrp/EOYAmt 

    AccntsPyblAccrExpnss_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/AccountsPayableAccrExpnssGrp/BOYAmt 

    AccntsPyblAccrExpnss_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/AccountsPayableAccrExpnssGrp/EOYAmt 

    GrntsPybl_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/GrantsPayableGrp/BOYAmt 

    GrntsPybl_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/GrantsPayableGrp/EOYAmt 

    DfrrdRvn_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/DeferredRevenueGrp/BOYAmt 

    DfrrdRvn_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/DeferredRevenueGrp/EOYAmt 

    TxExmptBndLblts_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/TaxExemptBondLiabilitiesGrp/BOYAmt 

    TxExmptBndLblts_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/TaxExemptBondLiabilitiesGrp/EOYAmt 

    EscrwAccntLblty_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/EscrowAccountLiabilityGrp/BOYAmt 

    EscrwAccntLblty_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/EscrowAccountLiabilityGrp/EOYAmt 

    LnsFrmOffcrsDrctrs_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/LoansFromOfficersDirectorsGrp/BOYAmt 

    LnsFrmOffcrsDrctrs_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/LoansFromOfficersDirectorsGrp/EOYAmt 

    MrtgNtsPyblScrdInvstPrp_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/MortgNotesPyblScrdInvstPropGrp/BOYAmt 

    MrtgNtsPyblScrdInvstPrp_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/MortgNotesPyblScrdInvstPropGrp/EOYAmt 

    UnscrdNtsLnsPybl_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/UnsecuredNotesLoansPayableGrp/BOYAmt 

    UnscrdNtsLnsPybl_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/UnsecuredNotesLoansPayableGrp/EOYAmt 

    OthrLblts_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/OtherLiabilitiesGrp/BOYAmt 

    OthrLblts_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/OtherLiabilitiesGrp/EOYAmt 

    TtlLblts_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/TotalLiabilitiesGrp/BOYAmt 

    TtlLblts_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/TotalLiabilitiesGrp/EOYAmt 

    OrgnztnFllwsSFAS117Ind = Column(String(length=1))
    # Line number:  Part X  Description:  Organizations that follow SFAS 117, check here  xpath: /IRS990/OrganizationFollowsSFAS117Ind 

    UnrstrctdNtAssts_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/UnrestrictedNetAssetsGrp/BOYAmt 

    UnrstrctdNtAssts_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/UnrestrictedNetAssetsGrp/EOYAmt 

    TmprrlyRstrNtAssts_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/TemporarilyRstrNetAssetsGrp/BOYAmt 

    TmprrlyRstrNtAssts_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/TemporarilyRstrNetAssetsGrp/EOYAmt 

    PrmnntlyRstrNtAssts_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/PermanentlyRstrNetAssetsGrp/BOYAmt 

    PrmnntlyRstrNtAssts_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/PermanentlyRstrNetAssetsGrp/EOYAmt 

    OrgDsNtFllwSFAS117Ind = Column(String(length=1))
    # Line number:  Part X  Description:  Organizations that do not follow SFAS 117, check here  xpath: /IRS990/OrgDoesNotFollowSFAS117Ind 

    CpStkTrPrnCrrntFnds_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/CapStkTrPrinCurrentFundsGrp/BOYAmt 

    CpStkTrPrnCrrntFnds_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/CapStkTrPrinCurrentFundsGrp/EOYAmt 

    PdInCpSrplsLndBldgEqpFnd_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/PdInCapSrplsLandBldgEqpFundGrp/BOYAmt 

    PdInCpSrplsLndBldgEqpFnd_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/PdInCapSrplsLandBldgEqpFundGrp/EOYAmt 

    RtnErnEndwmntIncmOthFnds_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/RtnEarnEndowmentIncmOthFndsGrp/BOYAmt 

    RtnErnEndwmntIncmOthFnds_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/RtnEarnEndowmentIncmOthFndsGrp/EOYAmt 

    TtlNtAsstsFndBlnc_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/TotalNetAssetsFundBalanceGrp/BOYAmt 

    TtlNtAsstsFndBlnc_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/TotalNetAssetsFundBalanceGrp/EOYAmt 

    TtLbNtAsstsFndBlnc_BOYAmt = Column(BigInteger)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  xpath: /IRS990/TotLiabNetAssetsFundBalanceGrp/BOYAmt 

    TtLbNtAsstsFndBlnc_EOYAmt = Column(BigInteger)
    # Line number:  Part X Column (B)  Description:  Ending of year  xpath: /IRS990/TotLiabNetAssetsFundBalanceGrp/EOYAmt 

#######
#
# IRS990 -  Part XI Reconciliation of Net Assets 
#
#######

class part_xi(Base):
    __tablename__='part_xi'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    InfInSkdOPrtXIInd = Column(String(length=1))
    # Line number:  Part XI  Description:  Schedule O contains a response to a question in Part XI  xpath: /IRS990/InfoInScheduleOPartXIInd 

    RcncltnRvnExpnssAmt = Column(BigInteger)
    # Line number:  Part XI Line 3  Description:  Revenue less expenses  xpath: /IRS990/ReconcilationRevenueExpnssAmt 

    NtUnrlzdGnsLsssInvstAmt = Column(BigInteger)
    # Line number:  Part XI Line 5  Description:  Net unrealized gains (losses) on investments  xpath: /IRS990/NetUnrlzdGainsLossesInvstAmt 

    DntdSrvcsAndUsFcltsAmt = Column(BigInteger)
    # Line number:  Part XI Line 6  Description:  Donated services and use of facilities  xpath: /IRS990/DonatedServicesAndUseFcltsAmt 

    InvstmntExpnsAmt = Column(BigInteger)
    # Line number:  Part XI Line 7  Description:  Investment expenses  xpath: /IRS990/InvestmentExpenseAmt 

    PrrPrdAdjstmntsAmt = Column(BigInteger)
    # Line number:  Part XI Line 8  Description:  Prior period adjustments  xpath: /IRS990/PriorPeriodAdjustmentsAmt 

    OthrChngsInNtAsstsAmt = Column(BigInteger)
    # Line number:  Part XI Line 9  Description:  Other changes in net assets or fund balances  xpath: /IRS990/OtherChangesInNetAssetsAmt 

#######
#
# IRS990 -  Part XII Financial Statements and Reporting 
#
#######

class part_xii(Base):
    __tablename__='part_xii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    InfInSkdOPrtXIIInd = Column(String(length=1))
    # Line number:  Part XII  Description:  Schedule O contains a response to a question in Part XII  xpath: /IRS990/InfoInScheduleOPartXIIInd 

    AccntntCmplOrRvwInd = Column(String(length=5))
    # Line number:  Part XII Line 2a  Description:  Accountant provide compilation or review?  xpath: /IRS990/AccountantCompileOrReviewInd 

    AcctCmplOrRvwBss_SprtBssFnclStmtInd = Column(String(length=1))
    # Line number:  Part XII Lines 2a and 2b  Description:  Financial statement issued on separate basis  xpath: /IRS990/AcctCompileOrReviewBasisGrp/SeparateBasisFinclStmtInd 

    AcctCmplOrRvwBss_CnsldtdBssFnclStmtInd = Column(String(length=1))
    # Line number:  Part XII Lines 2a and 2b  Description:  Financial statement issued on consolidated basis  xpath: /IRS990/AcctCompileOrReviewBasisGrp/ConsolidatedBasisFinclStmtInd 

    AcctCmplOrRvwBss_CnslAndSpBssFnclStmtInd = Column(String(length=1))
    # Line number:  Part XII Lines 2a and 2b  Description:  Financial statement issued on consolidated and separate basis  xpath: /IRS990/AcctCompileOrReviewBasisGrp/ConsolAndSepBasisFinclStmtInd 

    FSAdtdInd = Column(String(length=5))
    # Line number:  Part XII Line 2b  Description:  Financial sheets audited?  xpath: /IRS990/FSAuditedInd 

    FSAdtdBss_SprtBssFnclStmtInd = Column(String(length=1))
    # Line number:  Part XII Lines 2a and 2b  Description:  Financial statement issued on separate basis  xpath: /IRS990/FSAuditedBasisGrp/SeparateBasisFinclStmtInd 

    FSAdtdBss_CnsldtdBssFnclStmtInd = Column(String(length=1))
    # Line number:  Part XII Lines 2a and 2b  Description:  Financial statement issued on consolidated basis  xpath: /IRS990/FSAuditedBasisGrp/ConsolidatedBasisFinclStmtInd 

    FSAdtdBss_CnslAndSpBssFnclStmtInd = Column(String(length=1))
    # Line number:  Part XII Lines 2a and 2b  Description:  Financial statement issued on consolidated and separate basis  xpath: /IRS990/FSAuditedBasisGrp/ConsolAndSepBasisFinclStmtInd 

    AdtCmmttInd = Column(String(length=5))
    # Line number:  Part XII Line 2c  Description:  Does the organization have an audit committee?  xpath: /IRS990/AuditCommitteeInd 

    FdrlGrntAdtRqrdInd = Column(String(length=5))
    # Line number:  Part XII Line 3a  Description:  Federal grant audit required?  xpath: /IRS990/FederalGrantAuditRequiredInd 

    FdrlGrntAdtPrfrmdInd = Column(String(length=5))
    # Line number:  Part XII Line 3b  Description:  Federal grant audit performed?  xpath: /IRS990/FederalGrantAuditPerformedInd 

    MthdOfAccntngCshInd = Column(String(length=1))
    # Line number:  Part XII Line 1  Description:  Method of accounting - Cash  xpath: /IRS990/MethodOfAccountingCashInd 

    MthdOfAccntngAccrlInd = Column(String(length=1))
    # Line number:  Part XII Line 1  Description:  Method of accounting - Accrual  xpath: /IRS990/MethodOfAccountingAccrualInd 

    MthdOfAccntngOthrInd = Column(Text)
    # Line number:  Part XII Line 1  Description:  Method of accounting - Other  xpath: /IRS990/MethodOfAccountingOtherInd 

#######
#
# IRS990 - Form990PartVIISectionAGrp
# A repeating structure from  Part VII Compensation 
#
#######

class Frm990PrtVIISctnA(Base):
    __tablename__='Frm990PrtVIISctnA'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Frm990PrtVIISctnA = Column(Text)
    # Description:  Section A, at least name required  xpath: /IRS990/Form990PartVIISectionAGrp 

    PrsnNm = Column(String(length=35))
    # Line number:  Part VII Section A Line 1a A  Description:  Name - Person  xpath: /IRS990/Form990PartVIISectionAGrp/PersonNm 

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part VII Section A Line 1a A  Description:  Business name line 1  xpath: /IRS990/Form990PartVIISectionAGrp/BusinessName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part VII Section A Line 1a A  Description:  Business name line 2  xpath: /IRS990/Form990PartVIISectionAGrp/BusinessName/BusinessNameLine2Txt 

    TtlTxt = Column(String(length=100))
    # Line number:  Part VII Section A Line 1a A  Description:  Title  xpath: /IRS990/Form990PartVIISectionAGrp/TitleTxt 

    AvrgHrsPrWkRt = Column(Text)
    # Line number:  Part VII Section A Line 1a B  Description:  Average hours per week  xpath: /IRS990/Form990PartVIISectionAGrp/AverageHoursPerWeekRt 

    AvrgHrsPrWkRltdOrgRt = Column(Text)
    # Line number:  Part VII Section A Line 1a B  Description:  Average hours per week for related organizations  xpath: /IRS990/Form990PartVIISectionAGrp/AverageHoursPerWeekRltdOrgRt 

    IndvdlTrstOrDrctrInd = Column(String(length=1))
    # Line number:  Part VII Section A Line 1a C  Description:  Individual trustee or director  xpath: /IRS990/Form990PartVIISectionAGrp/IndividualTrusteeOrDirectorInd 

    InstttnlTrstInd = Column(String(length=1))
    # Line number:  Part VII Section A Line 1a C  Description:  Institutional Trustee  xpath: /IRS990/Form990PartVIISectionAGrp/InstitutionalTrusteeInd 

    OffcrInd = Column(String(length=1))
    # Line number:  Part VII Section A Line 1a C  Description:  Officer  xpath: /IRS990/Form990PartVIISectionAGrp/OfficerInd 

    KyEmplyInd = Column(String(length=1))
    # Line number:  Part VII Section A Line 1a C  Description:  Key Employee  xpath: /IRS990/Form990PartVIISectionAGrp/KeyEmployeeInd 

    HghstCmpnstdEmplyInd = Column(String(length=1))
    # Line number:  Part VII Section A Line 1a C  Description:  Highest compensated employee  xpath: /IRS990/Form990PartVIISectionAGrp/HighestCompensatedEmployeeInd 

    FrmrOfcrDrctrTrstInd = Column(String(length=1))
    # Line number:  Part VII Section A Line 1a C  Description:  Former  xpath: /IRS990/Form990PartVIISectionAGrp/FormerOfcrDirectorTrusteeInd 

    RprtblCmpFrmOrgAmt = Column(BigInteger)
    # Line number:  Part VII Section A Line 1a D  Description:  Reportable compensation from organization  xpath: /IRS990/Form990PartVIISectionAGrp/ReportableCompFromOrgAmt 

    RprtblCmpFrmRltdOrgAmt = Column(BigInteger)
    # Line number:  Part VII Section A Line 1a E  Description:  Reportable compensation from related organizations  xpath: /IRS990/Form990PartVIISectionAGrp/ReportableCompFromRltdOrgAmt 

    OthrCmpnstnAmt = Column(BigInteger)
    # Line number:  Part VII Section A Line 1a F  Description:  Other compensation  xpath: /IRS990/Form990PartVIISectionAGrp/OtherCompensationAmt 

#######
#
# IRS990 - OtherExpensesGrp
# A repeating structure from  Part IX Functional Expense 
#
#######

class OthrExpnss(Base):
    __tablename__='OthrExpnss'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Dsc = Column(String(length=100))
    # Line number:  Part IX Line 24a - 24d  Description:  Description  xpath: /IRS990/OtherExpensesGrp/Desc 

    TtlAmt = Column(BigInteger)
    # Line number:  col (A)  Description:  Total  xpath: /IRS990/OtherExpensesGrp/TotalAmt 

    PrgrmSrvcsAmt = Column(BigInteger)
    # Line number:  col (B)  Description:  Program services  xpath: /IRS990/OtherExpensesGrp/ProgramServicesAmt 

    MngmntAndGnrlAmt = Column(BigInteger)
    # Line number:  col (C)  Description:  Management and general  xpath: /IRS990/OtherExpensesGrp/ManagementAndGeneralAmt 

    FndrsngAmt = Column(BigInteger)
    # Line number:  col (D)  Description:  Fundraising  xpath: /IRS990/OtherExpensesGrp/FundraisingAmt 

#######
#
# IRS990 - OtherRevenueMiscGrp
# A repeating structure from  Part VIII Revenue 
#
#######

class OthrRvnMsc(Base):
    __tablename__='OthrRvnMsc'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Dsc = Column(String(length=100))
    # Line number:  Part VIII Line 11a 11b 11c  Description:  Description  xpath: /IRS990/OtherRevenueMiscGrp/Desc 

    TtlRvnClmnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  xpath: /IRS990/OtherRevenueMiscGrp/TotalRevenueColumnAmt 

    RltdOrExmptFncIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  xpath: /IRS990/OtherRevenueMiscGrp/RelatedOrExemptFuncIncomeAmt 

    UnrltdBsnssRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  xpath: /IRS990/OtherRevenueMiscGrp/UnrelatedBusinessRevenueAmt 

    ExclsnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  xpath: /IRS990/OtherRevenueMiscGrp/ExclusionAmt 

    BsnssCd = Column(Text)
    # Line number:  Part VIII  Description:  Business code  xpath: /IRS990/OtherRevenueMiscGrp/BusinessCd 

#######
#
# IRS990 - ProgSrvcAccomActyOtherGrp
# A repeating structure from  Part III Program Service Accomplishments 
#
#######

class PrgSrvcAccmActyOthr(Base):
    __tablename__='PrgSrvcAccmActyOthr'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    ActvtyCd = Column(BigInteger)
    # Line number:  Part III  Description:  Activity code  xpath: /IRS990/ProgSrvcAccomActyOtherGrp/ActivityCd 

    ExpnsAmt = Column(BigInteger)
    # Line number:  Part III  Description:  Expense  xpath: /IRS990/ProgSrvcAccomActyOtherGrp/ExpenseAmt 

    GrntAmt = Column(BigInteger)
    # Line number:  Part III  Description:  Grants  xpath: /IRS990/ProgSrvcAccomActyOtherGrp/GrantAmt 

    RvnAmt = Column(BigInteger)
    # Line number:  Part III  Description:  Revenue  xpath: /IRS990/ProgSrvcAccomActyOtherGrp/RevenueAmt 

    Dsc = Column(Text)
    # Line number:  Part III  Description:  Description  xpath: /IRS990/ProgSrvcAccomActyOtherGrp/Desc 

#######
#
# IRS990 - ProgramServiceRevenueGrp
# A repeating structure from  Part VIII Revenue 
#
#######

class PrgrmSrvcRvn(Base):
    __tablename__='PrgrmSrvcRvn'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Dsc = Column(String(length=100))
    # Line number:  Part VIII Line 2a - 2e  Description:  Description  xpath: /IRS990/ProgramServiceRevenueGrp/Desc 

    TtlRvnClmnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  xpath: /IRS990/ProgramServiceRevenueGrp/TotalRevenueColumnAmt 

    RltdOrExmptFncIncmAmt = Column(BigInteger)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  xpath: /IRS990/ProgramServiceRevenueGrp/RelatedOrExemptFuncIncomeAmt 

    UnrltdBsnssRvnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  xpath: /IRS990/ProgramServiceRevenueGrp/UnrelatedBusinessRevenueAmt 

    ExclsnAmt = Column(BigInteger)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  xpath: /IRS990/ProgramServiceRevenueGrp/ExclusionAmt 

    BsnssCd = Column(Text)
    # Line number:  Part VIII  Description:  Business code  xpath: /IRS990/ProgramServiceRevenueGrp/BusinessCd 

#######
#
# IRS990 - ForeignCountryCd
# A repeating structure from  Part V Other Filings 
#
#######

class FrgnCntryCd(Base):
    __tablename__='FrgnCntryCd'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    FrgnCntryCd = Column(String(length=2))
    # Line number:  Part V Line 4b  Description:  Name of foreign country  xpath: /IRS990/ForeignCountryCd 

#######
#
# IRS990 - ContractorCompensationGrp
# A repeating structure from  Part VII Compensation 
#
#######

class CntrctrCmpnstn(Base):
    __tablename__='CntrctrCmpnstn'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    CntrctrCmpnstn_CntrctrNm = Column(Text)
    # Line number:  Part VII Section B  Description:  Name of contractor  xpath: /IRS990/ContractorCompensationGrp/ContractorName 

    CntrctrNm_PrsnNm = Column(String(length=35))
    # Line number:  Part VII Section B Line 1(A)  Description:  Name - Person  xpath: /IRS990/ContractorCompensationGrp/ContractorName/PersonNm 

    BsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part VII Section B Line 1(A)  Description:  Business name line 2  xpath: /IRS990/ContractorCompensationGrp/ContractorName/BusinessName/BusinessNameLine2Txt 

    BsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part VII Section B Line 1(A)  Description:  Business name line 1  xpath: /IRS990/ContractorCompensationGrp/ContractorName/BusinessName/BusinessNameLine1Txt 

    CntrctrCmpnstn_CntrctrAddrss = Column(Text)
    # Line number:  Part VII Section B  Description:  Address of contractor  xpath: /IRS990/ContractorCompensationGrp/ContractorAddress 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VII Section B Line 1(A)  Description:  Address line 1  xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VII Section B Line 1(A)  Description:  Address line 2  xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part VII Section B Line 1(A)  Description:  City  xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part VII Section B Line 1(A)  Description:  State  xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part VII Section B Line 1(A)  Description:  ZIP code  xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/USAddress/ZIPCd 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part VII Section B Line 1(A)  Description:  Province or state  xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VII Section B Line 1(A)  Description:  Address line 1  xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VII Section B Line 1(A)  Description:  Address line 2  xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part VII Section B Line 1(A)  Description:  City  xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/ForeignAddress/CityNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part VII Section B Line 1(A)  Description:  Country  xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part VII Section B Line 1(A)  Description:  Postal code  xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/ForeignAddress/ForeignPostalCd 

    CntrctrCmpnstn_SrvcsDsc = Column(String(length=100))
    # Line number:  Part VII Section B Line 1(B)  Description:  Description of services  xpath: /IRS990/ContractorCompensationGrp/ServicesDesc 

    CntrctrCmpnstn_CmpnstnAmt = Column(BigInteger)
    # Line number:  Part VII Section B Line 1(C)  Description:  Compensation  xpath: /IRS990/ContractorCompensationGrp/CompensationAmt 

#######
#
# IRS990 - StatesWhereCopyOfReturnIsFldCd
# A repeating structure from  Part VI Governance 
#
#######

class SttsWhrCpyOfRtrnIsFldCd(Base):
    __tablename__='SttsWhrCpyOfRtrnIsFldCd'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SttsWhrCpyOfRtrnIsFldCd = Column(String(length=2))
    # Line number:  Part VI Section C Line 17  Description:  States where return filed  xpath: /IRS990/StatesWhereCopyOfReturnIsFldCd 

#######
#
# IRS990 - SpecialConditionDesc
# A repeating structure from  Part 0 Prefatory material 
#
#######

class SpclCndtnDsc(Base):
    __tablename__='SpclCndtnDsc'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpclCndtnDsc = Column(Text)
    # Description:  Special condition description  xpath: /IRS990/SpecialConditionDesc 

#######
#
# IRS990EZ - EZ Part 0 Prefatory material 
#
#######

class ez_part_0(Base):
    __tablename__='ez_part_0'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    AddrssChngInd = Column(String(length=1))
    # Line number:  B  Description:  Indicates this return has an address change  xpath: /IRS990EZ/AddressChangeInd 

    IntlRtrnInd = Column(String(length=1))
    # Line number:  B  Description:  Indicates this is an initial return  xpath: /IRS990EZ/InitialReturnInd 

    FnlRtrnInd = Column(String(length=1))
    # Line number:  B  Description:  Final return  xpath: /IRS990EZ/FinalReturnInd 

    AmnddRtrnInd = Column(String(length=1))
    # Line number:  B  Description:  Amended return  xpath: /IRS990EZ/AmendedReturnInd 

    GrpExmptnNm = Column(Text)
    # Line number:  F  Description:  Group exempt number  xpath: /IRS990EZ/GroupExemptionNum 

    SkdBNtRqrdInd = Column(String(length=1))
    # Line number:  H  Description:  Indicates Schedule B is not required  xpath: /IRS990EZ/ScheduleBNotRequiredInd 

    WbstAddrssTxt = Column(String(length=100))
    # Line number:  I  Description:  Web site  xpath: /IRS990EZ/WebsiteAddressTxt 

    OfOrgnztnCrpInd = Column(String(length=1))
    # Line number:  K  Description:  Type of organization - corporation  xpath: /IRS990EZ/TypeOfOrganizationCorpInd 

    OfOrgnztnTrstInd = Column(String(length=1))
    # Line number:  K  Description:  Type of organization - trust  xpath: /IRS990EZ/TypeOfOrganizationTrustInd 

    OfOrgnztnAsscInd = Column(String(length=1))
    # Line number:  K  Description:  Type of organization - association  xpath: /IRS990EZ/TypeOfOrganizationAssocInd 

    OfOrgnztnOthrInd = Column(String(length=1))
    # Line number:  K  Description:  Type of organization - other  xpath: /IRS990EZ/TypeOfOrganizationOtherInd 

    OfOrgnztnOthrDsc = Column(String(length=100))
    # Line number:  K  Description:  Type of organization other description  xpath: /IRS990EZ/TypeOfOrganizationOtherDesc 

    GrssRcptsAmt = Column(BigInteger)
    # Line number:  L  Description:  Gross receipts  xpath: /IRS990EZ/GrossReceiptsAmt 

    MthdOfAccntngCshInd = Column(String(length=1))
    # Line number:  G  Description:  Method of accounting - Cash  xpath: /IRS990EZ/MethodOfAccountingCashInd 

    MthdOfAccntngAccrlInd = Column(String(length=1))
    # Line number:  G  Description:  Method of accounting - Accrual  xpath: /IRS990EZ/MethodOfAccountingAccrualInd 

    MthdOfAccntngOthrDsc = Column(String(length=100))
    # Line number:  G  Description:  Method of accounting - Other  xpath: /IRS990EZ/MethodOfAccountingOtherDesc 

    Orgnztn501c3Ind = Column(Text)
    # Line number:  J  Description:  Indicates a 501(c)(3) organization  xpath: /IRS990EZ/Organization501c3Ind 

    Orgnztn501cInd = Column(Text)
    # Line number:  J  Description:  Indicates a 501(c) organization  xpath: /IRS990EZ/Organization501cInd 

    Orgnztn49471NtPFInd = Column(Text)
    # Line number:  J  Description:  Indicates a 4947(a)(1) organization  xpath: /IRS990EZ/Organization4947a1NotPFInd 

    Orgnztn527Ind = Column(String(length=1))
    # Line number:  J  Description:  Indicates a 527 organization  xpath: /IRS990EZ/Organization527Ind 

#######
#
# IRS990EZ - EZ Part I Revenue, Expenses, and Changes in Net Assets or Fund Balances 
#
#######

class ez_part_i(Base):
    __tablename__='ez_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    InfInSkdOPrtIInd = Column(String(length=1))
    # Line number:  Part I  Description:  Schedule O contains a response to a question in Part I  xpath: /IRS990EZ/InfoInScheduleOPartIInd 

    CntrbtnsGftsGrntsEtcAmt = Column(BigInteger)
    # Line number:  Part I Line 1  Description:  Contributions, gifts, grants, and similar amounts received  xpath: /IRS990EZ/ContributionsGiftsGrantsEtcAmt 

    PrgrmSrvcRvnAmt = Column(BigInteger)
    # Line number:  Part I Line 2  Description:  ProgramServiceRevenue  xpath: /IRS990EZ/ProgramServiceRevenueAmt 

    MmbrshpDsAmt = Column(BigInteger)
    # Line number:  Part I Line 3  Description:  Membership dues and assessments  xpath: /IRS990EZ/MembershipDuesAmt 

    InvstmntIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 4  Description:  Investment income  xpath: /IRS990EZ/InvestmentIncomeAmt 

    SlOfAsstsGrssAmt = Column(BigInteger)
    # Line number:  Part I Line 5a  Description:  Gross amount from sale of assets other than inventory  xpath: /IRS990EZ/SaleOfAssetsGrossAmt 

    CstOrOthrBssExpnsSlAmt = Column(BigInteger)
    # Line number:  Part I Line 5b  Description:  Cost or other basis and sales expenses  xpath: /IRS990EZ/CostOrOtherBasisExpenseSaleAmt 

    GnOrLssFrmSlOfAsstsAmt = Column(BigInteger)
    # Line number:  Part I Line 5c  Description:  Gain or (loss) from sale of assets other than inventory  xpath: /IRS990EZ/GainOrLossFromSaleOfAssetsAmt 

    GmngGrssIncmAmt = Column(Text)
    # Line number:  Part I Line 6a  Description:  Special events Indicates revenue from gaming  xpath: /IRS990EZ/GamingGrossIncomeAmt 

    FndrsngGrssIncmAmt = Column(Text)
    # Line number:  Part I Line 6b  Description:  Fundraising gross income  xpath: /IRS990EZ/FundraisingGrossIncomeAmt 

    SpclEvntsDrctExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 6c  Description:  Special events direct expenses  xpath: /IRS990EZ/SpecialEventsDirectExpensesAmt 

    SpclEvntsNtIncmLssAmt = Column(BigInteger)
    # Line number:  Part I Line 6d  Description:  Special events net income (or loss)  xpath: /IRS990EZ/SpecialEventsNetIncomeLossAmt 

    GrssSlsOfInvntryAmt = Column(BigInteger)
    # Line number:  Part I Line 7a  Description:  Gross sales of inventory  xpath: /IRS990EZ/GrossSalesOfInventoryAmt 

    CstOfGdsSldAmt = Column(BigInteger)
    # Line number:  Part I Line 7b  Description:  Less: cost of goods sold  xpath: /IRS990EZ/CostOfGoodsSoldAmt 

    GrssPrftLssSlsOfInvntryAmt = Column(BigInteger)
    # Line number:  Part I Line 7c  Description:  Gross profit (or loss) from sales of inventory  xpath: /IRS990EZ/GrossProfitLossSlsOfInvntryAmt 

    OthrRvnTtlAmt = Column(BigInteger)
    # Line number:  Part I Line 8  Description:  Other revenue - total  xpath: /IRS990EZ/OtherRevenueTotalAmt 

    TtlRvnAmt = Column(BigInteger)
    # Line number:  Part I Line 9  Description:  Total revenue  xpath: /IRS990EZ/TotalRevenueAmt 

    GrntsAndSmlrAmntsPdAmt = Column(BigInteger)
    # Line number:  Part I Line 10  Description:  Grants and similar amounts paid  xpath: /IRS990EZ/GrantsAndSimilarAmountsPaidAmt 

    BnftsPdTOrFrMmbrsAmt = Column(BigInteger)
    # Line number:  Part I Line 11  Description:  Benefits paid to or for members  xpath: /IRS990EZ/BenefitsPaidToOrForMembersAmt 

    SlrsOthrCmpEmplBnftAmt = Column(BigInteger)
    # Line number:  Part I Line 12  Description:  Salaries, other compensation, and employee benefits  xpath: /IRS990EZ/SalariesOtherCompEmplBnftAmt 

    FsAndOthrPymtTIndCntrctAmt = Column(BigInteger)
    # Line number:  Part I Line 13  Description:  Professional fees and other payments to independent contractors  xpath: /IRS990EZ/FeesAndOtherPymtToIndCntrctAmt 

    OccpncyRntUtltsAndMntAmt = Column(BigInteger)
    # Line number:  Part I Line 14  Description:  Occupancy, rent, utilities, and maintenance  xpath: /IRS990EZ/OccupancyRentUtltsAndMaintAmt 

    PrntngPblctnsPstgAmt = Column(BigInteger)
    # Line number:  Part I Line 15  Description:  Printing, publications, postage, and shipping  xpath: /IRS990EZ/PrintingPublicationsPostageAmt 

    OthrExpnssTtlAmt = Column(BigInteger)
    # Line number:  Part I Line 16  Description:  Other expenses - total  xpath: /IRS990EZ/OtherExpensesTotalAmt 

    TtlExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 17  Description:  Total expenses  xpath: /IRS990EZ/TotalExpensesAmt 

    ExcssOrDfctFrYrAmt = Column(BigInteger)
    # Line number:  Part I Line 18  Description:  Excess or deficit  xpath: /IRS990EZ/ExcessOrDeficitForYearAmt 

    NtAsstsOrFndBlncsBOYAmt = Column(BigInteger)
    # Line number:  Part I Line 19  Description:  Net assets BOY  xpath: /IRS990EZ/NetAssetsOrFundBalancesBOYAmt 

    OthrChngsInNtAsstsAmt = Column(BigInteger)
    # Line number:  Part I Line 20  Description:  Other changes in net assets  xpath: /IRS990EZ/OtherChangesInNetAssetsAmt 

    NtAsstsOrFndBlncsEOYAmt = Column(BigInteger)
    # Line number:  Part I Line 21  Description:  Net assets EOY  xpath: /IRS990EZ/NetAssetsOrFundBalancesEOYAmt 

#######
#
# IRS990EZ - EZ Part II Balance Sheets 
#
#######

class ez_part_ii(Base):
    __tablename__='ez_part_ii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    EZ_InfInSkdOPrtIIInd = Column(String(length=1))
    # Line number:  Part II  Description:  Schedule O contains a response to a question in Part II  xpath: /IRS990EZ/InfoInScheduleOPartIIInd 

    CshSvngsAndInvstmnts_BOYAmt = Column(BigInteger)
    # Line number:  Part II - Column (A)  Description:  Beginnning of year  xpath: /IRS990EZ/CashSavingsAndInvestmentsGrp/BOYAmt 

    CshSvngsAndInvstmnts_EOYAmt = Column(BigInteger)
    # Line number:  Part II - Column (B)  Description:  Ending of year  xpath: /IRS990EZ/CashSavingsAndInvestmentsGrp/EOYAmt 

    LndAndBldngs_BOYAmt = Column(BigInteger)
    # Line number:  Part II - Column (A)  Description:  Beginnning of year  xpath: /IRS990EZ/LandAndBuildingsGrp/BOYAmt 

    LndAndBldngs_EOYAmt = Column(BigInteger)
    # Line number:  Part II - Column (B)  Description:  Ending of year  xpath: /IRS990EZ/LandAndBuildingsGrp/EOYAmt 

    OthrAsstsTtlDtl_BOYAmt = Column(BigInteger)
    # Line number:  Part II - Column (A)  Description:  Beginnning of year  xpath: /IRS990EZ/OtherAssetsTotalDetail/BOYAmt 

    OthrAsstsTtlDtl_EOYAmt = Column(BigInteger)
    # Line number:  Part II - Column (B)  Description:  Ending of year  xpath: /IRS990EZ/OtherAssetsTotalDetail/EOYAmt 

    Frm990TtlAssts_BOYAmt = Column(BigInteger)
    # Line number:  Part II - Column (A)  Description:  Beginnning of year  xpath: /IRS990EZ/Form990TotalAssetsGrp/BOYAmt 

    Frm990TtlAssts_EOYAmt = Column(BigInteger)
    # Line number:  Part II - Column (B)  Description:  Ending of year  xpath: /IRS990EZ/Form990TotalAssetsGrp/EOYAmt 

    SmOfTtlLblts_BOYAmt = Column(BigInteger)
    # Line number:  Part II - Column (A)  Description:  Beginnning of year  xpath: /IRS990EZ/SumOfTotalLiabilitiesGrp/BOYAmt 

    SmOfTtlLblts_EOYAmt = Column(BigInteger)
    # Line number:  Part II - Column (B)  Description:  Ending of year  xpath: /IRS990EZ/SumOfTotalLiabilitiesGrp/EOYAmt 

    EZ_NtAsstsOrFndBlncs = Column(Text)
    # Line number:  Part II Line 27  Description:  Net assets or fund balances  xpath: /IRS990EZ/NetAssetsOrFundBalancesGrp 

    NtAsstsOrFndBlncs_BOYAmt = Column(BigInteger)
    # Line number:  Part II Line 27 Column (A)  Description:  Beginnning of year  xpath: /IRS990EZ/NetAssetsOrFundBalancesGrp/BOYAmt 

    NtAsstsOrFndBlncs_EOYAmt = Column(BigInteger)
    # Line number:  Part II Line 27 Column (B)  Description:  Ending of year  xpath: /IRS990EZ/NetAssetsOrFundBalancesGrp/EOYAmt 

#######
#
# IRS990EZ - EZ Part III Program Service Accomplishments 
#
#######

class ez_part_iii(Base):
    __tablename__='ez_part_iii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    InfInSkdOPrtIIIInd = Column(String(length=1))
    # Line number:  Part III  Description:  Schedule O contains a response to a question in Part III  xpath: /IRS990EZ/InfoInScheduleOPartIIIInd 

    PrmryExmptPrpsTxt = Column(Text)
    # Line number:  Part III  Description:  Primary exempt purpose  xpath: /IRS990EZ/PrimaryExemptPurposeTxt 

    TtlPrgrmSrvcExpnssAmt = Column(BigInteger)
    # Line number:  Part III Line 32  Description:  Total Program Service Expenses  xpath: /IRS990EZ/TotalProgramServiceExpensesAmt 

#######
#
# IRS990EZ - EZ Part IV Compensation 
#
#######

class ez_part_iv(Base):
    __tablename__='ez_part_iv'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    InfInSkdOPrtIVInd = Column(String(length=1))
    # Line number:  Part IV  Description:  Schedule O contains a response to a question in Part IV  xpath: /IRS990EZ/InfoInScheduleOPartIVInd 

#######
#
# IRS990EZ - EZ Part V Other Information 
#
#######

class ez_part_v(Base):
    __tablename__='ez_part_v'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    EZ_InfInSkdOPrtVInd = Column(String(length=1))
    # Line number:  Part V  Description:  Schedule O contains a response to a question in Part V  xpath: /IRS990EZ/InfoInScheduleOPartVInd 

    EZ_ActvtsNtPrvslyRptInd = Column(String(length=5))
    # Line number:  Part V Line 33  Description:  Did the organization engage in any activity not previously reported to the IRS?  xpath: /IRS990EZ/ActivitiesNotPreviouslyRptInd 

    EZ_ChgMdTOrgnzngDcNtRptInd = Column(String(length=5))
    # Line number:  Part V Line 34  Description:  Were any changes made in the organizing or governing documents but not reported to the IRS?  xpath: /IRS990EZ/ChgMadeToOrgnzngDocNotRptInd 

    EZ_OrgnztnHdUBIInd = Column(String(length=5))
    # Line number:  Part V Line 35a  Description:  Did the organization have unrelated business gross income of $1,000 or more during the year covered by this return?  xpath: /IRS990EZ/OrganizationHadUBIInd 

    EZ_OrgnztnFld990TInd = Column(String(length=5))
    # Line number:  Part V Line 35b  Description:  If "Yes" for Line 35a, has it filed a tax return on Form 990-T for this year?  xpath: /IRS990EZ/OrganizationFiled990TInd 

    EZ_SbjctTPrxyTxInd = Column(Text)
    # Line number:  Part V Line 35c  Description:  Subject to proxy tax?  xpath: /IRS990EZ/SubjectToProxyTaxInd 

    EZ_OrgnztnDsslvdEtcInd = Column(Text)
    # Line number:  Part V Line 36  Description:  Was there a liquidation, dissolution, termination, or substantial contraction during the year?  xpath: /IRS990EZ/OrganizationDissolvedEtcInd 

    EZ_DrctIndrctPltclExpndAmt = Column(BigInteger)
    # Line number:  Part V Line 37a  Description:  Direct or indirect political expenditures.  xpath: /IRS990EZ/DirectIndirectPltclExpendAmt 

    EZ_Frm1120PlFldInd = Column(String(length=5))
    # Line number:  Part V Line 37b  Description:  Did the organization file Form 1120-POL for this year?  xpath: /IRS990EZ/Form1120PolFiledInd 

    EZ_MdLnsTFrmOffcrsInd = Column(String(length=5))
    # Line number:  Part V Line 38a  Description:  Did the organization borrow from, or make any loans to, any officer, director, trustee, or key employee or were any such loans made in a prior year and still unpaid at the start of the period caovered by this return?  xpath: /IRS990EZ/MadeLoansToFromOfficersInd 

    EZ_LnsTFrmOffcrsAmt = Column(Text)
    # Line number:  Part V Line 38b  Description:  Loans to/from officers amount  xpath: /IRS990EZ/LoansToFromOfficersAmt 

    EZ_InttnFsAndCpCntrAmt = Column(BigInteger)
    # Line number:  Part V Line 39a  Description:  501(c)(7) orgs: Initiation fees and capital contributions included on line 9  xpath: /IRS990EZ/InitiationFeesAndCapContriAmt 

    EZ_GrssRcptsFrPblcUsAmt = Column(BigInteger)
    # Line number:  Part V Line 39b  Description:  501(c)(7) orgs: Gross receipts, included on line 9, for public use of club facilities  xpath: /IRS990EZ/GrossReceiptsForPublicUseAmt 

    EZ_TxImpsdUndrIRC4911Amt = Column(BigInteger)
    # Line number:  Part V Line 40a  Description:  501(c)(3) Organizations: Amount of tax imposed on the organization furing the year under section 4911  xpath: /IRS990EZ/TaxImposedUnderIRC4911Amt 

    EZ_TxImpsdUndrIRC4912Amt = Column(BigInteger)
    # Line number:  Part V Line 40a  Description:  501(c)(3) Organizations: Amount of tax imposed on the organization furing the year under section 4912  xpath: /IRS990EZ/TaxImposedUnderIRC4912Amt 

    EZ_TxImpsdUndrIRC4955Amt = Column(BigInteger)
    # Line number:  Part V Line 40a  Description:  501(c)(3) Organizations: Amount of tax imposed on the organization furing the year under section 4955  xpath: /IRS990EZ/TaxImposedUnderIRC4955Amt 

    EZ_EnggdInExcssBnftTrnsInd = Column(Text)
    # Line number:  Part V Line 40b  Description:  501(c)(3) and 501(c)(4) orgs: Did the organization engage in any section 4958 excess benefit transaction during the year, etc?  xpath: /IRS990EZ/EngagedInExcessBenefitTransInd 

    EZ_TxImpsdOnOrgnztnMgrAmt = Column(BigInteger)
    # Line number:  Part V Line 40c  Description:  Amount of tax imposed on the organization managers etc during the year under sections 4912, 4955, and 4958  xpath: /IRS990EZ/TaxImposedOnOrganizationMgrAmt 

    EZ_TxRmbrsdByOrgnztnAmt = Column(BigInteger)
    # Line number:  Part V Line 40d  Description:  Amount of tax on line 40c, above, reimbursed by the organization  xpath: /IRS990EZ/TaxReimbursedByOrganizationAmt 

    EZ_PrhbtdTxShltrTrnsInd = Column(String(length=5))
    # Line number:  Part V Line 40e  Description:  At any time during the tax year, was the organization a party to a prohibited tax shelter transaction?  xpath: /IRS990EZ/ProhibitedTaxShelterTransInd 

    EZ_BksInCrOfDtl = Column(Text)
    # Description:  The books are in care of  xpath: /IRS990EZ/BooksInCareOfDetail 

    BksInCrOfDtl_PrsnNm = Column(String(length=35))
    # Line number:  Part V Line 42a  Description:  Name - Person  xpath: /IRS990EZ/BooksInCareOfDetail/PersonNm 

    BsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part V Line 42a  Description:  Business name line 1  xpath: /IRS990EZ/BooksInCareOfDetail/BusinessName/BusinessNameLine1Txt 

    BsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part V Line 42a  Description:  Business name line 2  xpath: /IRS990EZ/BooksInCareOfDetail/BusinessName/BusinessNameLine2Txt 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part V Line 42a  Description:  Address line 1  xpath: /IRS990EZ/BooksInCareOfDetail/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part V Line 42a  Description:  Address line 2  xpath: /IRS990EZ/BooksInCareOfDetail/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part V Line 42a  Description:  City  xpath: /IRS990EZ/BooksInCareOfDetail/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part V Line 42a  Description:  State  xpath: /IRS990EZ/BooksInCareOfDetail/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part V Line 42a  Description:  ZIP code  xpath: /IRS990EZ/BooksInCareOfDetail/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part V Line 42a  Description:  Address line 1  xpath: /IRS990EZ/BooksInCareOfDetail/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part V Line 42a  Description:  Address line 2  xpath: /IRS990EZ/BooksInCareOfDetail/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part V Line 42a  Description:  City  xpath: /IRS990EZ/BooksInCareOfDetail/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part V Line 42a  Description:  Province or state  xpath: /IRS990EZ/BooksInCareOfDetail/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part V Line 42a  Description:  Country  xpath: /IRS990EZ/BooksInCareOfDetail/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part V Line 42a  Description:  Postal code  xpath: /IRS990EZ/BooksInCareOfDetail/ForeignAddress/ForeignPostalCd 

    BksInCrOfDtl_PhnNm = Column(String(length=10))
    # Line number:  Part V Line 42a  Description:  Telephone number  xpath: /IRS990EZ/BooksInCareOfDetail/PhoneNum 

    EZ_FrgnFnnclAccntInd = Column(String(length=5))
    # Line number:  Part V Line 42b  Description:  Did the organization have an interest in or authority over a financial account in a foreign country?  xpath: /IRS990EZ/ForeignFinancialAccountInd 

    EZ_FrgnOffcInd = Column(String(length=5))
    # Line number:  Part V Line 42c  Description:  At any time during the calender year, did the organization maintain an office outside of the U.S.?  xpath: /IRS990EZ/ForeignOfficeInd 

    EZ_NECTFlngFrm990Ind = Column(Text)
    # Line number:  Part V Line 43  Description:  Indicates section 4947(a)(1) nonexempt charitable trusts filing Form 990 in lieu of Form 1041  xpath: /IRS990EZ/NECTFilingForm990Ind 

    EZ_DnrAdvsdFndsInd = Column(String(length=5))
    # Line number:  Part V Line 44a  Description:  Maintain any donor advised funds?  xpath: /IRS990EZ/DonorAdvisedFndsInd 

    EZ_OprtHsptlInd = Column(String(length=5))
    # Line number:  Part V Line 44b  Description:  Operate one or more hospital facilities?  xpath: /IRS990EZ/OperateHospitalInd 

    EZ_TnnngSrvcsPrvddInd = Column(String(length=5))
    # Line number:  Part V Line 44c  Description:  Payments received for indoor tanning services?  xpath: /IRS990EZ/TanningServicesProvidedInd 

    EZ_Frm720FldInd = Column(String(length=5))
    # Line number:  Part V Line 44d  Description:  Form 720 filed and taxes paid on indoor tanning services?  xpath: /IRS990EZ/Form720FiledInd 

    EZ_RltdOrgnztnCtrlEntInd = Column(String(length=5))
    # Line number:  Part V Line 45a  Description:  Is any related organization a controlled entity within the meaning of section 512(b)(13)?  xpath: /IRS990EZ/RelatedOrganizationCtrlEntInd 

    EZ_TrnsctnWthCntrlEntInd = Column(String(length=5))
    # Line number:  Part V Line 45b  Description:  Payment from or engage in transaction with a controlled entity?  xpath: /IRS990EZ/TransactionWithControlEntInd 

    EZ_PltclCmpgnActyInd = Column(Text)
    # Line number:  Part V Line 46  Description:  Did the organization engage in direct or indirect political campaign activities on behalf of or in opposition to candidates for public office?  xpath: /IRS990EZ/PoliticalCampaignActyInd 

#######
#
# IRS990EZ - EZ Part VI Section 501(c)(3) Organizations Only 
#
#######

class ez_part_vi(Base):
    __tablename__='ez_part_vi'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    InfInSkdOPrtVIInd = Column(String(length=1))
    # Line number:  Part VI  Description:  Schedule O contains a response to a question in Part VI  xpath: /IRS990EZ/InfoInScheduleOPartVIInd 

    LbbyngActvtsInd = Column(Text)
    # Line number:  Part VI Line 47  Description:  Did the organization engage in lobbying activities?  xpath: /IRS990EZ/LobbyingActivitiesInd 

    SchlOprtngInd = Column(Text)
    # Line number:  Part VI Line 48  Description:  Is the organization operating a school as described in section 170(b)(1)(A)(ii)?  xpath: /IRS990EZ/SchoolOperatingInd 

    TrnsfrExmptNnChrtblRltdOrgInd = Column(String(length=5))
    # Line number:  Part VI Line 49a  Description:  Did the organization make any transfers to an exempt non-charitable related organization?  xpath: /IRS990EZ/TrnsfrExmptNonChrtblRltdOrgInd 

    RltdOrgSct527OrgInd = Column(String(length=5))
    # Line number:  Part VI Line 49b  Description:  If "Yes," was the related organization(s) a section 527 organization?  xpath: /IRS990EZ/RelatedOrgSect527OrgInd 

    OthrEmplyPdOvr100kCnt = Column(Text)
    # Line number:  Part VI Line 50f  Description:  Total number of other employees paid over $100,000  xpath: /IRS990EZ/OtherEmployeePaidOver100kCnt 

    CntrctRcvdGrtrThn100KCnt = Column(Text)
    # Line number:  Part VI Line 51d  Description:  Total number of other independent contractors receiving over $100,000  xpath: /IRS990EZ/CntrctRcvdGreaterThan100KCnt 

    FldSkdAInd = Column(String(length=5))
    # Line number:  Part VI Line 52  Description:  Did the organization complete Schedule A?  xpath: /IRS990EZ/FiledScheduleAInd 

    PrtVIOfCmpOfHghstPdEmplTxt = Column(Text)
    # Line number:  Part VI Line 50  Description:  If there are none, enter "None"  xpath: /IRS990EZ/PartVIOfCompOfHghstPdEmplTxt 

    PrtVIHghstPdCntrctPrfSrvcTxt = Column(Text)
    # Line number:  Part VI Line 51  Description:  If there are none, enter "None"  xpath: /IRS990EZ/PartVIHghstPdCntrctProfSrvcTxt 

#######
#
# IRS990EZ - SpecialConditionDesc
# A repeating structure from EZ Part 0 Prefatory material 
#
#######

class EZSpclCndtnDsc(Base):
    __tablename__='EZSpclCndtnDsc'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpclCndtnDsc = Column(Text)
    # Description:  Special condition description  xpath: /IRS990EZ/SpecialConditionDesc 

#######
#
# IRS990EZ - CompensationOfHghstPdCntrctGrp
# A repeating structure from EZ Part VI Section 501(c)(3) Organizations Only 
#
#######

class EZCmpnstnOfHghstPdCntrct(Base):
    __tablename__='EZCmpnstnOfHghstPdCntrct'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    CmpnstnOfHghstPdCntrct_BsnssNm = Column(Text)
    # Line number:  Part VI Line 51 Column (a)  Description:  Highest paid contractor's name - Business  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/BusinessName 

    CmpnstnOfHghstPdCntrct_PrsnNm = Column(Text)
    # Line number:  Part VI Line 51 Column (a)  Description:  Highest paid contractor's name - Person  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/PersonNm 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VI Line 51 Column (a)  Description:  Address line 1  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VI Line 51 Column (a)  Description:  Address line 2  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part VI Line 51 Column (a)  Description:  City  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part VI Line 51 Column (a)  Description:  State  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part VI Line 51 Column (a)  Description:  ZIP code  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VI Line 51 Column (a)  Description:  Address line 1  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VI Line 51 Column (a)  Description:  Address line 2  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part VI Line 51 Column (a)  Description:  City  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part VI Line 51 Column (a)  Description:  Province or state  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part VI Line 51 Column (a)  Description:  Country  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part VI Line 51 Column (a)  Description:  Postal code  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ForeignAddress/ForeignPostalCd 

    CmpnstnOfHghstPdCntrct_SrvcTxt = Column(String(length=100))
    # Line number:  Part VI Line 51 Column (b)  Description:  Type of service  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ServiceTypeTxt 

    CmpnstnOfHghstPdCntrct_CmpnstnAmt = Column(BigInteger)
    # Line number:  Part VI Line 51 Column (c)  Description:  Compensation  xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/CompensationAmt 

#######
#
# IRS990EZ - ForeignOfficeCountryCd
# A repeating structure from EZ Part V Other Information 
#
#######

class EZFrgnOffcCntryCd(Base):
    __tablename__='EZFrgnOffcCntryCd'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    FrgnOffcCntryCd = Column(String(length=2))
    # Line number:  Part V Line 42c  Description:  Name of foreign country  xpath: /IRS990EZ/ForeignOfficeCountryCd 

#######
#
# IRS990EZ - ProgramSrvcAccomplishmentGrp
# A repeating structure from EZ Part III Program Service Accomplishments 
#
#######

class EZPrgrmSrvcAccmplshmnt(Base):
    __tablename__='EZPrgrmSrvcAccmplshmnt'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    DscrptnPrgrmSrvcAccmTxt = Column(Text)
    # Line number:  Part III  Description:  Description of program service accomplishments  xpath: /IRS990EZ/ProgramSrvcAccomplishmentGrp/DescriptionProgramSrvcAccomTxt 

    GrntsAndAllctnsAmt = Column(BigInteger)
    # Line number:  Part III  Description:  Grants and allocations  xpath: /IRS990EZ/ProgramSrvcAccomplishmentGrp/GrantsAndAllocationsAmt 

    FrgnGrntsInd = Column(String(length=1))
    # Line number:  Part III  Description:  Includes foreign grants?  xpath: /IRS990EZ/ProgramSrvcAccomplishmentGrp/ForeignGrantsInd 

    PrgrmSrvcExpnssAmt = Column(BigInteger)
    # Line number:  Part III  Description:  Program service expenses  xpath: /IRS990EZ/ProgramSrvcAccomplishmentGrp/ProgramServiceExpensesAmt 

#######
#
# IRS990EZ - StatesWhereCopyOfReturnIsFldCd
# A repeating structure from EZ Part V Other Information 
#
#######

class EZSttsWhrCpyOfRtrnIsFldCd(Base):
    __tablename__='EZSttsWhrCpyOfRtrnIsFldCd'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SttsWhrCpyOfRtrnIsFldCd = Column(String(length=2))
    # Line number:  Part V Line 41  Description:  States With Which a Copy of This Return is Filed  xpath: /IRS990EZ/StatesWhereCopyOfReturnIsFldCd 

#######
#
# IRS990EZ - ForeignFinancialAccountCntryCd
# A repeating structure from EZ Part V Other Information 
#
#######

class EZFrgnFnnclAccntCntryCd(Base):
    __tablename__='EZFrgnFnnclAccntCntryCd'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    FrgnFnnclAccntCntryCd = Column(String(length=2))
    # Line number:  Part V Line 42b  Description:  Name of foreign country  xpath: /IRS990EZ/ForeignFinancialAccountCntryCd 

#######
#
# IRS990EZ - OfficerDirectorTrusteeEmplGrp
# A repeating structure from EZ Part IV Compensation 
#
#######

class EZOffcrDrctrTrstEmpl(Base):
    __tablename__='EZOffcrDrctrTrstEmpl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    PrsnNm = Column(Text)
    # Line number:  Part IV - Column (a)  Description:  Person Name  xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/PersonNm 

    BsnssNm = Column(Text)
    # Line number:  Part IV - Column (a)  Description:  Business Name  xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/BusinessName 

    TtlTxt = Column(String(length=100))
    # Line number:  Part IV - Column (a)  Description:  Title  xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/TitleTxt 

    AvrgHrsPrWkDvtdTPsRt = Column(Text)
    # Line number:  Part IV - Column (b)  Description:  Average Hours per week devoted to position  xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/AverageHrsPerWkDevotedToPosRt 

    CmpnstnAmt = Column(BigInteger)
    # Line number:  Part IV - Column (c)  Description:  Compensation  xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/CompensationAmt 

    EmplyBnftPrgrmAmt = Column(BigInteger)
    # Line number:  Part IV - Column (d)  Description:  Contributions to employee benefit plans and deferred compensation  xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/EmployeeBenefitProgramAmt 

    ExpnsAccntOthrAllwncAmt = Column(BigInteger)
    # Line number:  Part IV - Column (e)  Description:  Expense account and other allowances  xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/ExpenseAccountOtherAllwncAmt 

#######
#
# IRS990EZ - CompensationHighestPaidEmplGrp
# A repeating structure from EZ Part VI Section 501(c)(3) Organizations Only 
#
#######

class EZCmpnstnHghstPdEmpl(Base):
    __tablename__='EZCmpnstnHghstPdEmpl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    PrsnNm = Column(Text)
    # Line number:  Part VI Line 50 Column (a)  Description:  Highest paid employee's name  xpath: /IRS990EZ/CompensationHighestPaidEmplGrp/PersonNm 

    TtlTxt = Column(String(length=100))
    # Line number:  Part VI Line 50 Column (a)  Description:  Title  xpath: /IRS990EZ/CompensationHighestPaidEmplGrp/TitleTxt 

    AvrgHrsPrWkRt = Column(Text)
    # Line number:  Part VI Line 50 Column (b)  Description:  Average hours per week  xpath: /IRS990EZ/CompensationHighestPaidEmplGrp/AverageHoursPerWeekRt 

    CmpnstnAmt = Column(BigInteger)
    # Line number:  Part VI Line 50 Column (c)  Description:  Compensation  xpath: /IRS990EZ/CompensationHighestPaidEmplGrp/CompensationAmt 

    EmplyBnftsAmt = Column(BigInteger)
    # Line number:  Part VI Line 50 Column (d)  Description:  Employee benefits  xpath: /IRS990EZ/CompensationHighestPaidEmplGrp/EmployeeBenefitsAmt 

    ExpnsAccntAmt = Column(BigInteger)
    # Line number:  Part VI Line 50 Column (e)  Description:  Expense Account  xpath: /IRS990EZ/CompensationHighestPaidEmplGrp/ExpenseAccountAmt 

#######
#
# IRS990PF - PF Part 0 Prefatory material 
#
#######

class pf_part_0(Base):
    __tablename__='pf_part_0'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    PFSttsTrmSct507b1AInd = Column(String(length=1))
    # Line number:  E  Description:  Indicates private foundation status terminated under section 507(b)(1)(A)  xpath: /IRS990PF/PFStatusTermSect507b1AInd 

    IntlRtrnInd = Column(String(length=1))
    # Line number:  G  Description:  Indicates this is an initial return  xpath: /IRS990PF/InitialReturnInd 

    IntlRtrnFrmrPbChrtyInd = Column(String(length=1))
    # Line number:  G  Description:  Indicates this is an initial return of a former public charity  xpath: /IRS990PF/InitialReturnFormerPubChrtyInd 

    FnlRtrnInd = Column(String(length=1))
    # Line number:  G  Description:  Final return  xpath: /IRS990PF/FinalReturnInd 

    AmnddRtrnInd = Column(String(length=1))
    # Line number:  G  Description:  Amended return  xpath: /IRS990PF/AmendedReturnInd 

    AddrssChngInd = Column(String(length=1))
    # Line number:  G  Description:  Indicates this return has an address change  xpath: /IRS990PF/AddressChangeInd 

    FMVAsstsEOYAmt = Column(BigInteger)
    # Line number:  I  Description:  Fair market value of all assets at end of year  xpath: /IRS990PF/FMVAssetsEOYAmt 

    Orgnztn501c3ExmptPFInd = Column(String(length=1))
    # Line number:  H  Description:  Section 501(c)(3) exempt private foundation  xpath: /IRS990PF/Organization501c3ExemptPFInd 

    Orgnztn49471TrtdPFInd = Column(String(length=1))
    # Line number:  H  Description:  Section 4947(a)(1) nonexempt charitable trust  xpath: /IRS990PF/Organization4947a1TrtdPFInd 

    Orgnztn501c3TxblPFInd = Column(String(length=1))
    # Line number:  H  Description:  Other taxable private foundation  xpath: /IRS990PF/Organization501c3TaxablePFInd 

    MthdOfAccntngCshInd = Column(String(length=1))
    # Line number:  J  Description:  Method of accounting - Cash  xpath: /IRS990PF/MethodOfAccountingCashInd 

    MthdOfAccntngAccrlInd = Column(String(length=1))
    # Line number:  J  Description:  Method of accounting - Accrual  xpath: /IRS990PF/MethodOfAccountingAccrualInd 

    MthdOfAccntngOthrInd = Column(Text)
    # Line number:  J  Description:  Method of accounting - Other  xpath: /IRS990PF/MethodOfAccountingOtherInd 

#######
#
# IRS990PF - PF Part I Analysis of Revenue and Expenses 
#
#######

class pf_part_i(Base):
    __tablename__='pf_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    AnlyssOfRvnAndExpnss = Column(Text)
    # xpath: /IRS990PF/AnalysisOfRevenueAndExpenses 

    CntrRcvdRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 1(a)  Description:  Contributions Received - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/ContriRcvdRevAndExpnssAmt 

    SkdBNtRqrdInd = Column(String(length=1))
    # Line number:  Part I Line 2  Description:  Not required to attach Schedule B  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/ScheduleBNotRequiredInd 

    IntrstOnSvRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 3(a)  Description:  Interest on Savings and Temporary Cash Investments - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestOnSavRevAndExpnssAmt 

    IntrstOnSvNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 3(b)  Description:  Interest on Savings and Temporary Cash Investments - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestOnSavNetInvstIncmAmt 

    IntrstOnSvngsAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 3(c)  Description:  Interest on Savings and Temporary Cash Investments - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestOnSavingsAdjNetIncmAmt 

    DvdndsRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 4(a)  Description:  Dividends and Interest from Securities - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/DividendsRevAndExpnssAmt 

    DvdndsNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 4(b)  Description:  Dividends and Interest from Securities - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/DividendsNetInvstIncmAmt 

    DvdndsAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 4(c)  Description:  Dividends and Interest from Securities - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/DividendsAdjNetIncmAmt 

    GrssRntsRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 5a(a)  Description:  Gross Rents - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossRentsRevAndExpnssAmt 

    GrssRntsNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 5a(b)  Description:  Gross Rents - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossRentsNetInvstIncmAmt 

    GrssRntsAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 5a(c)  Description:  Gross Rents - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossRentsAdjNetIncmAmt 

    NtRntlIncmOrLssAmt = Column(BigInteger)
    # Line number:  Part I Line 5b  Description:  Net Rental Income or Los  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/NetRentalIncomeOrLossAmt 

    NtGnSlAstRvAndExpnssAmt = Column(Text)
    # Line number:  Part I Line 6a(a)  Description:  Net Gain from Sale of Assets - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/NetGainSaleAstRevAndExpnssAmt 

    GrssSlsPrcAmt = Column(BigInteger)
    # Line number:  Part I Line 6b  Description:  Gross Sales Price  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossSalesPriceAmt 

    CpGnNtIncmNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 7(b)  Description:  Capital Gain Net Income - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/CapGainNetIncmNetInvstIncmAmt 

    NtSTCptlGnAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 8(c)  Description:  Net Short-Term Capital Gain - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/NetSTCapitalGainAdjNetIncmAmt 

    IncmMdfctnsAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 9(c)  Description:  Income Modifications - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/IncmModificationsAdjNetIncmAmt 

    GrssSlsLssRtAndAllwncAmt = Column(BigInteger)
    # Line number:  Part I Line 10a  Description:  Gross Sales Less Returns and Allowances  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossSalesLessRetAndAllwncAmt 

    CstOfGdsSldAmt = Column(BigInteger)
    # Line number:  Part I Line 10b  Description:  Cost of Goods Sold  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/CostOfGoodsSoldAmt 

    GrssPrftRvAndExpnssAmt = Column(Text)
    # Line number:  Part I Line 10c(a)  Description:  Gross Profit - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossProfitRevAndExpnssAmt 

    GrssPrftAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 10c(c)  Description:  Gross Profit - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossProfitAdjNetIncmAmt 

    OthrIncmRvAndExpnssAmt = Column(Text)
    # Line number:  Part I Line 11(a)  Description:  Other Income - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherIncomeRevAndExpnssAmt 

    OthrIncmNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 11(b)  Description:  Other Income - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherIncomeNetInvstIncmAmt 

    OthrIncmAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 11(c)  Description:  Other Income - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherIncomeAdjNetIncmAmt 

    TtlRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 12(a)  Description:  Total - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalRevAndExpnssAmt 

    TtlNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 12(b)  Description:  Total - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalNetInvstIncmAmt 

    TtlAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 12(c)  Description:  Total - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalAdjNetIncmAmt 

    CmpOfcrDrTrstRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 13(a)  Description:  Compensation of Officers, Directors, Trustees, etc. - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/CompOfcrDirTrstRevAndExpnssAmt 

    CmpOfcrDrTrstNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 13(b)  Description:  Compensation of Officers, Directors, Trustees, etc. - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/CompOfcrDirTrstNetInvstIncmAmt 

    CmpOfcrDrTrstAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 13(c)  Description:  Compensation of Officers, Directors, Trustees, etc. - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/CompOfcrDirTrstAdjNetIncmAmt 

    CmpOfcrDrTrstDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 13(d)  Description:  Compensation of Officers, Directors, Trustees, etc. - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/CompOfcrDirTrstDsbrsChrtblAmt 

    OthEmplSlrsWgsRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 14(a)  Description:  Other Employee Salaries and Wages - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OthEmplSlrsWgsRevAndExpnssAmt 

    OthEmplSlrsWgsNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 14(b)  Description:  Other Employee Salaries and Wages - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OthEmplSlrsWgsNetInvstIncmAmt 

    OthEmplSlrsWgsAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 14(c)  Description:  Other Employee Salaries and Wages - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OthEmplSlrsWgsAdjNetIncmAmt 

    OthEmplSlrsWgsDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 14(d)  Description:  Other Employee Salaries and Wages - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OthEmplSlrsWgsDsbrsChrtblAmt 

    PnsnEmplBnftRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 15(a)  Description:  Pension Plans, Employee Benefits - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PensionEmplBnftRevAndExpnssAmt 

    PnsnEmplBnftNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 15(b)  Description:  Pension Plans, Employee Benefits - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PensionEmplBnftNetInvstIncmAmt 

    PnsnEmplBnftAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 15(c)  Description:  Pension Plans, Employee Benefits - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PensionEmplBnftAdjNetIncmAmt 

    PnsnEmplBnftDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 15(d)  Description:  Pension Plans, Employee Benefits - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PensionEmplBnftDsbrsChrtblAmt 

    LglFsRvAndExpnssAmt = Column(Text)
    # Line number:  Part I Line 16a(a)  Description:  Legal Fees - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/LegalFeesRevAndExpnssAmt 

    LglFsNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 16a(b)  Description:  Legal Fees - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/LegalFeesNetInvstIncmAmt 

    LglFsAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 16a(c)  Description:  Legal Fees - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/LegalFeesAdjNetIncmAmt 

    LglFsDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 16a(d)  Description:  Legal Fees - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/LegalFeesDsbrsChrtblAmt 

    AccntngFsRvAndExpnssAmt = Column(Text)
    # Line number:  Part I Line 16b(a)  Description:  Accounting Fees - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/AccountingFeesRevAndExpnssAmt 

    AccntngFsNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 16b(b)  Description:  Accounting Fees - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/AccountingFeesNetInvstIncmAmt 

    AccntngFsAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 16b(c)  Description:  Accounting Fees - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/AccountingFeesAdjNetIncmAmt 

    AccntngFsChrtblPrpsAmt = Column(BigInteger)
    # Line number:  Part I Line 16b(d)  Description:  Accounting Fees - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/AccountingFeesChrtblPrpsAmt 

    OthrPrfFsRvAndExpnssAmt = Column(Text)
    # Line number:  Part I Line 16c(a)  Description:  Other Professional Fees - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherProfFeesRevAndExpnssAmt 

    OthrPrfFsNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 16c(b)  Description:  Other Professional Fees - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherProfFeesNetInvstIncmAmt 

    OthrPrfFsAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 16c(c)  Description:  Other Professional Fees - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherProfFeesAdjNetIncmAmt 

    OthrPrfFsDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 16c(d)  Description:  Other Professional Fees - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherProfFeesDsbrsChrtblAmt 

    IntrstRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 17(a)  Description:  Interest - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestRevAndExpnssAmt 

    IntrstNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 17(b)  Description:  Interest - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestNetInvstIncmAmt 

    IntrstAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 17(c)  Description:  Interest - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestAdjNetIncmAmt 

    IntrstDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 17(d)  Description:  Interest - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestDsbrsChrtblAmt 

    TxsRvAndExpnssAmt = Column(Text)
    # Line number:  Part I Line 18(a)  Description:  Taxes - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TaxesRevAndExpnssAmt 

    TxsNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 18(b)  Description:  Taxes - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TaxesNetInvstIncmAmt 

    TxsAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 18(c)  Description:  Taxes - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TaxesAdjNetIncmAmt 

    TxsDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 18(d)  Description:  Taxes - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TaxesDsbrsChrtblAmt 

    DprcAndDpltnRvAndExpnssAmt = Column(Text)
    # Line number:  Part I Line 19(a)  Description:  Depreciation and Depletion - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/DeprecAndDpltnRevAndExpnssAmt 

    DprcAndDpltnNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 19(b)  Description:  Depreciation and Depletion - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/DeprecAndDpltnNetInvstIncmAmt 

    DprcAndDpltnAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 19(c)  Description:  Depreciation and Depletion - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/DeprecAndDpltnAdjNetIncmAmt 

    OccpncyRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 20(a)  Description:  Occupancy - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OccupancyRevAndExpnssAmt 

    OccpncyNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 20(b)  Description:  Occupancy - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OccupancyNetInvstIncmAmt 

    OccpncyAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 20(c)  Description:  Occupancy - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OccupancyAdjNetIncmAmt 

    OccpncyDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 20(d)  Description:  Occupancy - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OccupancyDsbrsChrtblAmt 

    TrvCnfMtngRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 21(a)  Description:  Travel, Conferences, and Meetings - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TravConfMeetingRevAndExpnssAmt 

    TrvCnfMtngNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 21(b)  Description:  Travel, Conferences, and Meetings - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TravConfMeetingNetInvstIncmAmt 

    TrvCnfMtngAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 21(c)  Description:  Travel, Conferences, and Meetings - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TravConfMeetingAdjNetIncmAmt 

    TrvCnfMtngDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 21(d)  Description:  Travel, Conferences, and Meetings - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TravConfMeetingDsbrsChrtblAmt 

    PrntngAndPbRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 22(a)  Description:  Printing and Publications - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PrintingAndPubRevAndExpnssAmt 

    PrntngAndPbNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 22(b)  Description:  Printing and Publications - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PrintingAndPubNetInvstIncmAmt 

    PrntngAndPbAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 22(c)  Description:  Printing and Publications - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PrintingAndPubAdjNetIncmAmt 

    PrntngAndPbDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 22(d)  Description:  Printing and Publications - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PrintingAndPubDsbrsChrtblAmt 

    OthrExpnssRvAndExpnssAmt = Column(Text)
    # Line number:  Part I Line 23(a)  Description:  Other Expenses - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherExpensesRevAndExpnssAmt 

    OthrExpnssNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 23(b)  Description:  Other Expenses - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherExpensesNetInvstIncmAmt 

    OthrExpnssAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 23(c)  Description:  Other Expenses - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherExpensesAdjNetIncmAmt 

    OthrExpnssDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 23(d)  Description:  Other Expenses - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherExpensesDsbrsChrtblAmt 

    TtOprExpnssRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 24(a)  Description:  Total Operating and Administrative Expenses - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotOprExpensesRevAndExpnssAmt 

    TtOprExpnssNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 24(b)  Description:  Total Operating and Administrative Expenses - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotOprExpensesNetInvstIncmAmt 

    TtOprExpnssAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 24(c)  Description:  Total Operating and Administrative Expenses - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotOprExpensesAdjNetIncmAmt 

    TtOprExpnssDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 24(d)  Description:  Total Operating and Administrative Expenses - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotOprExpensesDsbrsChrtblAmt 

    CntrPdRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 25(a)  Description:  Contributions, Gifts, Grants Paid - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/ContriPaidRevAndExpnssAmt 

    CntrPdDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 25(d)  Description:  Contributions, Gifts, Grants Paid - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/ContriPaidDsbrsChrtblAmt 

    TtlExpnssRvAndExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 26(a)  Description:  Total Expenses and Disbursements - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalExpensesRevAndExpnssAmt 

    TtlExpnssNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 26(b)  Description:  Total Expenses and Disbursements - Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalExpensesNetInvstIncmAmt 

    TtlExpnssAdjNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 26(c)  Description:  Total Expenses and Disbursements - Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalExpensesAdjNetIncmAmt 

    TtlExpnssDsbrsChrtblAmt = Column(BigInteger)
    # Line number:  Part I Line 26(d)  Description:  Total Expenses and Disbursements - Disbursements for Charitable Purposes  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalExpensesDsbrsChrtblAmt 

    ExcssRvnOvrExpnssAmt = Column(BigInteger)
    # Line number:  Part I Line 27a(a)  Description:  Excess of Revenue Over Expenses and Disbursements - Revenue and Expenses per Books  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/ExcessRevenueOverExpensesAmt 

    NtInvstmntIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 27b(b)  Description:  Net Investment Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/NetInvestmentIncomeAmt 

    AdjstdNtIncmAmt = Column(BigInteger)
    # Line number:  Part I Line 27c(c)  Description:  Adjusted Net Income  xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/AdjustedNetIncomeAmt 

#######
#
# IRS990PF - PF Part II Balance Sheets 
#
#######

class pf_part_ii(Base):
    __tablename__='pf_part_ii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Frm990PFBlncShts = Column(Text)
    # xpath: /IRS990PF/Form990PFBalanceSheetsGrp 

    CshBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 1(a)  Description:  Cash - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CashBOYAmt 

    CshEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 1(b)  Description:  Cash - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CashEOYAmt 

    CshEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 1(c)  Description:  Cash - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CashEOYFMVAmt 

    SvAndTmpCshInvstBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 2(a)  Description:  Savings and Temporary Cash Investments - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/SavAndTempCashInvstBOYAmt 

    SvAndTmpCshInvstEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 2(b)  Description:  Savings and Temporary Cash Investments - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/SavAndTempCashInvstEOYAmt 

    SvAndTmpCshInvstEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 2(c)  Description:  Savings and Temporary Cash Investments - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/SavAndTempCashInvstEOYFMVAmt 

    AcctRcvblAmt = Column(BigInteger)
    # Line number:  Part II Line 3  Description:  Accounts Receivable  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AcctRcvblAmt 

    AcctRcvblAllwncDbtflAcctAmt = Column(BigInteger)
    # Line number:  Part II Line 3  Description:  Allowance for Doubtful Accounts (for Accounts Receivable)  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AcctRcvblAllwncDbtflAcctAmt 

    AcctRcvblBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 3(a)  Description:  Accounts Receivable - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AcctRcvblBOYAmt 

    AcctRcvblEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 3(b)  Description:  Accounts Receivable - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AcctRcvblEOYAmt 

    AcctRcvblEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 3(c)  Description:  Accounts Receivable - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AcctRcvblEOYFMVAmt 

    PldgsRcvblAmt = Column(BigInteger)
    # Line number:  Part II Line 4  Description:  Pledges Receivable  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PledgesRcvblAmt 

    PldgsRcvblAllwncDbtflAcctAmt = Column(BigInteger)
    # Line number:  Part II Line 4  Description:  Allowance for Doubtful Accounts (for Pledges Receivable)  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PledgesRcvblAllwncDbtflAcctAmt 

    PldgsRcvblBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 4(a)  Description:  Pledges Receivable - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PledgesRcvblBOYAmt 

    PldgsRcvblEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 4(b)  Description:  Pledges Receivable - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PledgesRcvblEOYAmt 

    PldgsRcvblEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 4(c)  Description:  Pledges Receivable - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PledgesRcvblEOYFMVAmt 

    GrntsRcvblBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 5(a)  Description:  Grants Receivable - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/GrantsReceivableBOYAmt 

    GrntsRcvblEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 5(b)  Description:  Grants Receivable - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/GrantsReceivableEOYAmt 

    GrntsRcvblEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 5(c)  Description:  Grants Receivable - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/GrantsReceivableEOYFMVAmt 

    RcvblFrmOffcrsBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 6(a)  Description:  Receivables from Officers - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/RcvblFromOfficersBOYAmt 

    RcvblFrmOffcrsEOYAmt = Column(Text)
    # Line number:  Part II Line 6(b)  Description:  Receivables from Officers - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/RcvblFromOfficersEOYAmt 

    RcvblFrmOffcrsEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 6(c)  Description:  Receivables from Officers - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/RcvblFromOfficersEOYFMVAmt 

    OthrNtsAndLnsRcvblAmt = Column(BigInteger)
    # Line number:  Part II Line 7  Description:  Other Notes and Loans Receivable  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherNtsAndLoansRcvblAmt 

    OthrRcvblAllwncDbtflAcctAmt = Column(BigInteger)
    # Line number:  Part II Line 7  Description:  Allowance for Doubtful Accounts (for Other Notes and Loans Receivable)  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherRcvblAllwncDbtflAcctAmt 

    OthrNtsAndLnsRcvblBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 7(a)  Description:  Other Notes and Loans Receivable - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherNtsAndLoansRcvblBOYAmt 

    OthrNtsAndLnsRcvblEOYAmt = Column(Text)
    # Line number:  Part II Line 7(b)  Description:  Other Notes and Loans Receivable - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherNtsAndLoansRcvblEOYAmt 

    OthrNtsAndLnsRcvblEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 7(c)  Description:  Other Notes and Loans Receivable - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherNtsAndLoansRcvblEOYFMVAmt 

    InvntrsBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 8(a)  Description:  Inventories for Sale or Use - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/InventoriesBOYAmt 

    InvntrsEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 8(b)  Description:  Inventories for Sale or Use - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/InventoriesEOYAmt 

    InvntrsEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 8(c)  Description:  Inventories for Sale or Use - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/InventoriesEOYFMVAmt 

    PrpdExpnssBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 9(a)  Description:  Prepaid Expenses - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PrepaidExpensesBOYAmt 

    PrpdExpnssEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 9(b)  Description:  Prepaid Expenses - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PrepaidExpensesEOYAmt 

    PrpdExpnssEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 9(c)  Description:  Prepaid Expenses - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PrepaidExpensesEOYFMVAmt 

    USGvrnmntOblgtnsBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 10a(a)  Description:  Investments, Government Obligations - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/USGovernmentObligationsBOYAmt 

    USGvrnmntOblgtnsEOYAmt = Column(Text)
    # Line number:  Part II Line 10a(b)  Description:  Investments, Government Obligations - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/USGovernmentObligationsEOYAmt 

    USGvtOblgtnsEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 10a(c)  Description:  Investments, Government Obligations - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/USGovtObligationsEOYFMVAmt 

    CrprtStckBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 10b(a)  Description:  Investments, Corporate Stock - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CorporateStockBOYAmt 

    CrprtStckEOYAmt = Column(Text)
    # Line number:  Part II Line 10b(b)  Description:  Investments, Corporate Stock - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CorporateStockEOYAmt 

    CrprtStckEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 10b(c)  Description:  Investments, Corporate Stock - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CorporateStockEOYFMVAmt 

    CrprtBndsBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 10c(a)  Description:  Investments, Corporate Bonds - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CorporateBondsBOYAmt 

    CrprtBndsEOYAmt = Column(Text)
    # Line number:  Part II Line 10c(b)  Description:  Investments, Corporate Bonds - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CorporateBondsEOYAmt 

    CrprtBndsEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 10c(c)  Description:  Investments, Corporate Bonds - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CorporateBondsEOYFMVAmt 

    InvstLndCstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part II Line 11  Description:  Investments, Land, Etc. Basis  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/InvstLandCostOrOtherBasisAmt 

    InvstLndAccmDprctnAmt = Column(BigInteger)
    # Line number:  Part II Line 11  Description:  Accumulated Depreciation (for Investments, Land, Etc.)  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/InvstLandAccumDepreciationAmt 

    LndBldgInvstmntsBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 11(a)  Description:  Investments, Land, Etc. - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandBldgInvestmentsBOYAmt 

    LndBldgInvstmntsEOYAmt = Column(Text)
    # Line number:  Part II Line 11(b)  Description:  Investments, Land, Etc. - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandBldgInvestmentsEOYAmt 

    LndBldgInvstmntsEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 11(c)  Description:  Investments, Land, Etc. - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandBldgInvestmentsEOYFMVAmt 

    MrtggLnsBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 12(a)  Description:  Investments, Mortgage Loans - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/MortgageLoansBOYAmt 

    MrtggLnsEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 12(b)  Description:  Investments, Mortgage Loans - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/MortgageLoansEOYAmt 

    MrtggLnsEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 12(c)  Description:  Investments, Mortgage Loans - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/MortgageLoansEOYFMVAmt 

    OthrInvstmntsBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 13(a)  Description:  Investments, Other - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherInvestmentsBOYAmt 

    OthrInvstmntsEOYAmt = Column(Text)
    # Line number:  Part II Line 13(b)  Description:  Investments, Other - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherInvestmentsEOYAmt 

    OthrInvstmntsEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 13(c)  Description:  Investments, Other - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherInvestmentsEOYFMVAmt 

    LndBldgEqpCstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part II Line 14  Description:  Land, Buildings, and Equipment - Basis  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandBldgEquipCostOrOtherBssAmt 

    LndBldgEqpAccmDprcAmt = Column(BigInteger)
    # Line number:  Part II Line 14  Description:  Accumulated Depreciation (for Land, Buildings, and Equipment)  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandBldgEquipAccumDeprecAmt 

    LndBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 14(a)  Description:  Land, Buildings, and Equipment - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandBOYAmt 

    LndEOYAmt = Column(Text)
    # Line number:  Part II Line 14(b)  Description:  Land, Buildings, and Equipment - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandEOYAmt 

    LndEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 14(c)  Description:  Land, Buildings, and Equipment - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandEOYFMVAmt 

    OthrAsstsBOYAmt = Column(Text)
    # Line number:  Part II Line 15(a)  Description:  Other Assets - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherAssetsBOYAmt 

    OthrAsstsEOYAmt = Column(Text)
    # Line number:  Part II Line 15(b)  Description:  Other Assets - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherAssetsEOYAmt 

    OthrAsstsEOYFMVAmt = Column(Text)
    # Line number:  Part II Line 15(c)  Description:  Other Assets - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherAssetsEOYFMVAmt 

    TtlAsstsBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 16(a)  Description:  Total Assets - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalAssetsBOYAmt 

    TtlAsstsEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 16(b)  Description:  Total Assets - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalAssetsEOYAmt 

    TtlAsstsEOYFMVAmt = Column(BigInteger)
    # Line number:  Part II Line 16(c)  Description:  Total Assets - End of Year - Fair Market Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalAssetsEOYFMVAmt 

    AccntsPyblBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 17(a)  Description:  Accounts Payable - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AccountsPayableBOYAmt 

    AccntsPyblEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 17(b)  Description:  Accounts Payable - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AccountsPayableEOYAmt 

    GrntsPyblBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 18(a)  Description:  Grants Payable - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/GrantsPayableBOYAmt 

    GrntsPyblEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 18(b)  Description:  Grants Payable - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/GrantsPayableEOYAmt 

    DfrrdRvnBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 19(a)  Description:  Deferred Revenue - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/DeferredRevenueBOYAmt 

    DfrrdRvnEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 19(b)  Description:  Deferred Revenue - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/DeferredRevenueEOYAmt 

    LnsFrmOffcrsBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 20(a)  Description:  Loans from Officers - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LoansFromOfficersBOYAmt 

    LnsFrmOffcrsEOYAmt = Column(Text)
    # Line number:  Part II Line 20(b)  Description:  Loans from Officers - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LoansFromOfficersEOYAmt 

    MrtggsAndNtsPyblBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 21(a)  Description:  Mortgages and Notes Payable - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/MortgagesAndNotesPayableBOYAmt 

    MrtggsAndNtsPyblEOYAmt = Column(Text)
    # Line number:  Part II Line 21(b)  Description:  Mortgages and Notes Payable - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/MortgagesAndNotesPayableEOYAmt 

    OthrLbltsBOYAmt = Column(Text)
    # Line number:  Part II Line 22(a)  Description:  Other Liabilities - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherLiabilitiesBOYAmt 

    OthrLbltsEOYAmt = Column(Text)
    # Line number:  Part II Line 22(b)  Description:  Other Liabilities - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherLiabilitiesEOYAmt 

    TtlLbltsBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 23(a)  Description:  Total Liabilities - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalLiabilitiesBOYAmt 

    TtlLbltsEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 23(b)  Description:  Total Liabilities - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalLiabilitiesEOYAmt 

    OrgnztnFllwsSFAS117Ind = Column(String(length=1))
    # Description:  Organizations That Follow SFAS 117  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OrganizationFollowsSFAS117Ind 

    UnrstrctdBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 24(a)  Description:  Unrestricted - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/UnrestrictedBOYAmt 

    UnrstrctdEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 24(b)  Description:  Unrestricted - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/UnrestrictedEOYAmt 

    TmprrlyRstrctdBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 25(a)  Description:  Temporarily Restricted - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TemporarilyRestrictedBOYAmt 

    TmprrlyRstrctdEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 25(b)  Description:  Temporarily Restricted - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TemporarilyRestrictedEOYAmt 

    PrmnntlyRstrctdBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 26(a)  Description:  Permanently Restricted - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PermanentlyRestrictedBOYAmt 

    PrmnntlyRstrctdEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 26(b)  Description:  Permanently Restricted - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PermanentlyRestrictedEOYAmt 

    OrgDsNtFllwSFAS117Ind = Column(String(length=1))
    # Description:  Organizations That Do Not Follow SFAS 117  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OrgDoesNotFollowSFAS117Ind 

    CptlStckBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 27(a)  Description:  Capital Stock - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CapitalStockBOYAmt 

    CptlStckEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 27(b)  Description:  Capital Stock - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CapitalStockEOYAmt 

    AddtnlPdInCptlBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 28(a)  Description:  Paid-in or Capital Surplus - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AdditionalPaidInCapitalBOYAmt 

    AddtnlPdInCptlEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 28(b)  Description:  Paid-in or Capital Surplus - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AdditionalPaidInCapitalEOYAmt 

    RtndErnngBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 29(a)  Description:  Retained Earnings - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/RetainedEarningBOYAmt 

    RtndErnngEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 29(b)  Description:  Retained Earnings - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/RetainedEarningEOYAmt 

    TtNtAstOrFndBlncsBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 30(a)  Description:  Total Net Assets or Fund Balances - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotNetAstOrFundBalancesBOYAmt 

    TtNtAstOrFndBlncsEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 30(b)  Description:  Total Net Assets or Fund Balances - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotNetAstOrFundBalancesEOYAmt 

    TtlLbltsNtAstBOYAmt = Column(BigInteger)
    # Line number:  Part II Line 31(a)  Description:  Total Liabilities and Net Assets - Beginning of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalLiabilitiesNetAstBOYAmt 

    TtlLbltsNtAstEOYAmt = Column(BigInteger)
    # Line number:  Part II Line 31(b)  Description:  Total Liabilities and Net Assets - End of Year - Book Value  xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalLiabilitiesNetAstEOYAmt 

#######
#
# IRS990PF - PF Part III Changes in Net Assets or Fund Balances 
#
#######

class pf_part_iii(Base):
    __tablename__='pf_part_iii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    ChgInNtAsstsFndBlncs = Column(Text)
    # xpath: /IRS990PF/ChgInNetAssetsFundBalancesGrp 

    TtNtAstOrFndBlncsBOYAmt = Column(BigInteger)
    # Line number:  Part III Line 1  Description:  Total Net Assets or Fund Balances at Beginning of Year  xpath: /IRS990PF/ChgInNetAssetsFundBalancesGrp/TotNetAstOrFundBalancesBOYAmt 

    ExcssRvnOvrExpnssAmt = Column(BigInteger)
    # Line number:  Part III Line 2  Description:  Excess of Revenue Over Expenses and Disbursements - Revenue and Expenses per Books  xpath: /IRS990PF/ChgInNetAssetsFundBalancesGrp/ExcessRevenueOverExpensesAmt 

    OthrIncrssAmt = Column(Text)
    # Line number:  Part III Line 3  Description:  Other Increases  xpath: /IRS990PF/ChgInNetAssetsFundBalancesGrp/OtherIncreasesAmt 

    SbttlAmt = Column(BigInteger)
    # Line number:  Part III Line 4  Description:  Subtotal  xpath: /IRS990PF/ChgInNetAssetsFundBalancesGrp/SubtotalAmt 

    OthrDcrssAmt = Column(Text)
    # Line number:  Part III Line 5  Description:  Other Decreases  xpath: /IRS990PF/ChgInNetAssetsFundBalancesGrp/OtherDecreasesAmt 

    TtNtAstOrFndBlncsEOYAmt = Column(BigInteger)
    # Line number:  Part III Line 6  Description:  Total Net Assets or Fund Balances at End of Year  xpath: /IRS990PF/ChgInNetAssetsFundBalancesGrp/TotNetAstOrFundBalancesEOYAmt 

#######
#
# IRS990PF - PF Part IV Capital Gains and Losses for Tax on Investment Income 
#
#######

class pf_part_iv(Base):
    __tablename__='pf_part_iv'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    CpGnsLssTxInvstIncmDtl = Column(Text)
    # xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail 

    CptlGnNtIncmAmt = Column(BigInteger)
    # Line number:  Part IV Line 2  Description:  Capital Gain Net Income  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapitalGainNetIncomeAmt 

    NtShrtTrmCptlGnLssAmt = Column(BigInteger)
    # Line number:  Part IV Line 3  Description:  Net Short-Term Capital Gain or Loss  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/NetShortTermCapitalGainLossAmt 

#######
#
# IRS990PF - PF Part V Qualification Under Section 4940(e) for Reduced Tax on Net Investment Income 
#
#######

class pf_part_v(Base):
    __tablename__='pf_part_v'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    QlfyUndSct4940RdcdTx = Column(Text)
    # xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp 

    LblSctn4942TxInd = Column(String(length=5))
    # Description:  Liable for 4942 Tax?  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/LiableSection4942TaxInd 

    AdjstdQlfyDstrYr1Amt = Column(BigInteger)
    # Line number:  Part V Line 1(b), row 1  Description:  Qualifying Distributions - Year 1  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/AdjustedQlfyDistriYr1Amt 

    NtVlNnchrtblAsstsYr1Amt = Column(BigInteger)
    # Line number:  Part V Line 1(c), row 1  Description:  Noncharitable Assets - Year 1  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/NetVlNoncharitableAssetsYr1Amt 

    DstrbtnYr1Rt = Column(Numeric(precision=9))
    # Line number:  Part V Line 1(d), row 1  Description:  Distribution Ratio - Year 1  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/DistributionYr1Rt 

    AdjstdQlfyDstrYr2Amt = Column(BigInteger)
    # Line number:  Part V Line 1(b), row 2  Description:  Qualifying Distributions - Year 2  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/AdjustedQlfyDistriYr2Amt 

    NtVlNnchrtblAsstsYr2Amt = Column(BigInteger)
    # Line number:  Part V Line 1(c), row 2  Description:  Noncharitable Assets - Year 2  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/NetVlNoncharitableAssetsYr2Amt 

    DstrbtnYr2Rt = Column(Numeric(precision=9))
    # Line number:  Part V Line 1(d), row 2  Description:  Distribution Ratio - Year 2  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/DistributionYr2Rt 

    AdjstdQlfyDstrYr3Amt = Column(BigInteger)
    # Line number:  Part V Line 1(b), row 3  Description:  Qualifying Distributions - Year 3  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/AdjustedQlfyDistriYr3Amt 

    NtVlNnchrtblAsstsYr3Amt = Column(BigInteger)
    # Line number:  Part V Line 1(c), row 3  Description:  Noncharitable Assets - Year 3  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/NetVlNoncharitableAssetsYr3Amt 

    DstrbtnYr3Rt = Column(Numeric(precision=9))
    # Line number:  Part V Line 1(d), row 3  Description:  Distribution Ratio - Year 3  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/DistributionYr3Rt 

    AdjstdQlfyDstrYr4Amt = Column(BigInteger)
    # Line number:  Part V Line 1(b), row 4  Description:  Qualifying Distributions - Year 4  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/AdjustedQlfyDistriYr4Amt 

    NtVlNnchrtblAsstsYr4Amt = Column(BigInteger)
    # Line number:  Part V Line 1(c), row 4  Description:  Noncharitable Assets - Year 4  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/NetVlNoncharitableAssetsYr4Amt 

    DstrbtnYr4Rt = Column(Numeric(precision=9))
    # Line number:  Part V Line 1(d), row 4  Description:  Distribution Ratio - Year 4  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/DistributionYr4Rt 

    AdjstdQlfyDstrYr5Amt = Column(BigInteger)
    # Line number:  Part V Line 1(b), row 5  Description:  Qualifying Distributions - Year 5  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/AdjustedQlfyDistriYr5Amt 

    NtVlNnchrtblAsstsYr5Amt = Column(BigInteger)
    # Line number:  Part V Line 1(c), row 5  Description:  Noncharitable Assets - Year 5  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/NetVlNoncharitableAssetsYr5Amt 

    DstrbtnYr5Rt = Column(Numeric(precision=9))
    # Line number:  Part V Line 1(d), row 5  Description:  Distribution Ratio - Year 5  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/DistributionYr5Rt 

    TtlDstrbtnRt = Column(Numeric(precision=9))
    # Line number:  Part V Line 2  Description:  Total Distribution Ratio  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/TotalDistributionRt 

    AvrgDstrbtnRt = Column(Numeric(precision=9))
    # Line number:  Part V Line 3  Description:  Average Distribution Ratio  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/AverageDistributionRt 

    NtVlNnchrtblAsstsAmt = Column(BigInteger)
    # Line number:  Part V Line 4  Description:  Net Noncharitable Assets  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/NetVlNoncharitableAssetsAmt 

    AdjNtVlNnchrtblAsstsAmt = Column(BigInteger)
    # Line number:  Part V Line 5  Description:  Adjusted Noncharitable Assets (multiply Line 4 by Line 3)  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/AdjNetVlNoncharitableAssetsAmt 

    NtInvstmntIncmPctAmt = Column(BigInteger)
    # Line number:  Part V Line 6  Description:  1% of Net Investment Income  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/NetInvestmentIncomePctAmt 

    AdjNnchrtblNtInvstIncmPctAmt = Column(BigInteger)
    # Line number:  Part V Line 7  Description:  Adjusted Noncharitable Assets and 1% of Net Investment Income (add lines 5 and 6)  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/AdjNonchrtblNetInvstIncmPctAmt 

    QlfyngDstrbtnsAmt = Column(BigInteger)
    # Line number:  Part V Line 8  Description:  Qualifying Distributions  xpath: /IRS990PF/QlfyUndSect4940eReducedTaxGrp/QualifyingDistributionsAmt 

#######
#
# IRS990PF - PF Part VI Excise Tax Based on Investment Income 
#
#######

class pf_part_vi(Base):
    __tablename__='pf_part_vi'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    ExcsTxBsdOnInvstIncm = Column(Text)
    # xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp 

    ExmptOprtngFndtnsInd = Column(String(length=1))
    # Line number:  Part VI Line 1a  Description:  Exempt Operating Foundations  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/ExemptOperatingFoundationsInd 

    RlngLttrDt = Column(String(length=31))
    # Line number:  Part VI Line 1a  Description:  Date of Ruling Letter  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/RulingLetterDt 

    DmstcOrgMtngSct4940Ind = Column(String(length=1))
    # Line number:  Part VI Line 1b  Description:  Domestic Organizations Meeting Section 4940(e) Requirements  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/DomesticOrgMeetingSect4940eInd 

    TxUndrSctn511Amt = Column(Text)
    # Line number:  Part VI Line 2  Description:  Tax Under Section 511  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/TaxUnderSection511Amt 

    SbttlAmt = Column(BigInteger)
    # Line number:  Part VI Line 3  Description:  Subtotal (add lines 1 and 2)  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/SubtotalAmt 

    SbttlATxAmt = Column(BigInteger)
    # Line number:  Part VI Line 4  Description:  Subtitle A Tax  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/SubtitleATaxAmt 

    TxBsdOnInvstmntIncmAmt = Column(BigInteger)
    # Line number:  Part VI Line 5  Description:  Tax Based on Investment Income  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/TaxBasedOnInvestmentIncomeAmt 

    EstmtdPlsOvpmtIncmTxAmt = Column(BigInteger)
    # Line number:  Part VI Line 6a  Description:  Estimated Tax Payments and Overpayment Credited  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/EstimatedPlusOvpmtIncmTxAmt 

    AppldTEsTxAmt = Column(BigInteger)
    # Line number:  Part VI Line 6c  Description:  Tax Paid with Extension  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/AppliedToEsTaxAmt 

    BckpWthhldngWthhldAmt = Column(BigInteger)
    # Line number:  Part VI Line 6d  Description:  Backup Withholding Erroneously Withheld  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/BackupWithholdingWithheldAmt 

    TtlPymntsAndCrdtsAmt = Column(BigInteger)
    # Line number:  Part VI Line 7  Description:  Total Credits and Payments  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/TotalPaymentsAndCreditsAmt 

    Frm2220AttchdInd = Column(Text)
    # Line number:  Part VI Line 8  Description:  Indicates Form 2220 is attached  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/Form2220AttachedInd 

    EsPnltyAmt = Column(BigInteger)
    # Line number:  Part VI Line 8  Description:  Penalty for Underpayment  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/EsPenaltyAmt 

    AppldTESTxAmt = Column(BigInteger)
    # Line number:  Part VI Line 11  Description:  Amount Credited to Next Year  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/AppliedToESTaxAmt 

    RfndAmt = Column(BigInteger)
    # Line number:  Part VI Line 11  Description:  Amount to be refunded  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/RefundAmt 

    InvstmntIncmExcsTxAmt = Column(BigInteger)
    # Line number:  Part VI Line 1  Description:  Investment Income Excise Tax - amount  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/InvestmentIncomeExciseTaxAmt 

    NtApplcblCd = Column(Text)
    # Line number:  Part VI Line 1  Description:  Investment Income Excise Tax - "N/A"  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/NotApplicableCd 

    OrgnlRtrnTxPdAmt = Column(BigInteger)
    # Line number:  Part VI Line 7 Tax Paid with Orig Return  Description:  Tax Paid with the Original Return  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/OriginalReturnTaxPaidAmt 

    OrgnlRtrnOvrpymntAmt = Column(BigInteger)
    # Line number:  Part VI Line 7 Orig Return Overpayment  Description:  Original Return Overpayment  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/OriginalReturnOverpaymentAmt 

    TxDAmt = Column(BigInteger)
    # Line number:  Part VI Line 9  Description:  Tax Due  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/TaxDueAmt 

    OvrpymntAmt = Column(BigInteger)
    # Line number:  Part VI Line 10  Description:  Overpayment  xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/OverpaymentAmt 

#######
#
# IRS990PF - PF Part VII-A Statements Regarding Activities 
#
#######

class pf_part_viia(Base):
    __tablename__='pf_part_viia'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    PF_SttmntsRgrdngActy = Column(Text)
    # xpath: /IRS990PF/StatementsRegardingActyGrp 

    SttmntsRgrdngActy_LgsltvPltclActyInd = Column(Text)
    # Line number:  Part VII-A Line 1a  Description:  Legislative and Political Activities?  xpath: /IRS990PF/StatementsRegardingActyGrp/LegislativePoliticalActyInd 

    SttmntsRgrdngActy_MrThn100SpntInd = Column(String(length=5))
    # Line number:  Part VII-A Line 1b  Description:  More Than $100 Spent?  xpath: /IRS990PF/StatementsRegardingActyGrp/MoreThan100SpentInd 

    SttmntsRgrdngActy_Frm1120POLFldInd = Column(String(length=5))
    # Line number:  Part VII-A Line 1c  Description:  Form 1120-POL Filed?  xpath: /IRS990PF/StatementsRegardingActyGrp/Form1120POLFiledInd 

    SttmntsRgrdngActy_Sctn4955OrgnztnTxAmt = Column(BigInteger)
    # Line number:  Part VII-A Line 1d(1)  Description:  Section 4955 Tax on Organization  xpath: /IRS990PF/StatementsRegardingActyGrp/Section4955OrganizationTaxAmt 

    SttmntsRgrdngActy_Sctn4955MngrsTxAmt = Column(BigInteger)
    # Line number:  Part VII-A Line 1d(2)  Description:  Section 4955 Tax on Managers  xpath: /IRS990PF/StatementsRegardingActyGrp/Section4955ManagersTaxAmt 

    SttmntsRgrdngActy_TxRmbrsdAmt = Column(BigInteger)
    # Line number:  Part VII-A Line 1e  Description:  Reimbursement of Tax  xpath: /IRS990PF/StatementsRegardingActyGrp/TaxReimbursedAmt 

    SttmntsRgrdngActy_ActvtsNtPrvslyRptInd = Column(Text)
    # Line number:  Part VII-A Line 2  Description:  Activities Not Previously Reported?  xpath: /IRS990PF/StatementsRegardingActyGrp/ActivitiesNotPreviouslyRptInd 

    SttmntsRgrdngActy_ChngsTArtclsOrBylwsInd = Column(Text)
    # Line number:  Part VII-A Line 3  Description:  Changes to Articles or Bylaws?  xpath: /IRS990PF/StatementsRegardingActyGrp/ChangesToArticlesOrBylawsInd 

    SttmntsRgrdngActy_UnrltdBsIncmOvrLmtInd = Column(String(length=5))
    # Line number:  Part VII-A Line 4a  Description:  Unrelated Business Income Over $1000?  xpath: /IRS990PF/StatementsRegardingActyGrp/UnrelatedBusIncmOverLimitInd 

    SttmntsRgrdngActy_Frm990TFldInd = Column(String(length=5))
    # Line number:  Part VII-A Line 4b  Description:  Form 990-T Filed?  xpath: /IRS990PF/StatementsRegardingActyGrp/Form990TFiledInd 

    SttmntsRgrdngActy_OrgnztnDsslvdEtcInd = Column(Text)
    # Line number:  Part VII-A Line 5  Description:  Termination, etc.?  xpath: /IRS990PF/StatementsRegardingActyGrp/OrganizationDissolvedEtcInd 

    SttmntsRgrdngActy_Sctn508RqrStsfdInd = Column(String(length=5))
    # Line number:  Part VII-A Line 6  Description:  Requirements of Section 508(e)?  xpath: /IRS990PF/StatementsRegardingActyGrp/Section508eRqrSatisfiedInd 

    SttmntsRgrdngActy_AtLst5000InAsstsInd = Column(String(length=5))
    # Line number:  Part VII-A Line 7  Description:  At least $5000 in Assets?  xpath: /IRS990PF/StatementsRegardingActyGrp/AtLeast5000InAssetsInd 

    SttmntsRgrdngActy_Frm990PFFldWthAttyGnInd = Column(Text)
    # Line number:  Part VII-A Line 8b  Description:  Form 990-PF Filed with Attorney General?  xpath: /IRS990PF/StatementsRegardingActyGrp/Form990PFFiledWithAttyGenInd 

    SttmntsRgrdngActy_PrvtOprtngFndtnInd = Column(String(length=5))
    # Line number:  Part VII-A Line 9  Description:  Private Operating Foundation?  xpath: /IRS990PF/StatementsRegardingActyGrp/PrivateOperatingFoundationInd 

    SttmntsRgrdngActy_NwSbstntlCntrbtrsInd = Column(Text)
    # Line number:  Part VII-A Line 10  Description:  New Substantial Contributors?  xpath: /IRS990PF/StatementsRegardingActyGrp/NewSubstantialContributorsInd 

    SttmntsRgrdngActy_OwnCntrlldEnttyInd = Column(Text)
    # Line number:  Part VII-A Line 11  Description:  At any time during the year, did the foundation, directly or indirectly, own a controlled entity within the meaning of section 51 2(b)(l3)?  xpath: /IRS990PF/StatementsRegardingActyGrp/OwnControlledEntityInd 

    SttmntsRgrdngActy_DnrAdvsdFndInd = Column(String(length=5))
    # Line number:  Part VII-A Line 12  Description:  Did Ihe organization acquire a direct or indirect interest in any applicable insurance contract?  xpath: /IRS990PF/StatementsRegardingActyGrp/DonorAdvisedFundInd 

    SttmntsRgrdngActy_CmplyWthPblcInspRqrInd = Column(String(length=5))
    # Line number:  Part VII-A Line 13  Description:  Comply with Public Inspection Requirements?  xpath: /IRS990PF/StatementsRegardingActyGrp/ComplyWithPublicInspRqrInd 

    SttmntsRgrdngActy_WbstAddrssTxt = Column(String(length=100))
    # Line number:  Part VII-A Line 13  Description:  Website Address  xpath: /IRS990PF/StatementsRegardingActyGrp/WebsiteAddressTxt 

    SttmntsRgrdngActy_PhnNm = Column(String(length=10))
    # Line number:  Part VII-A Line 14  Description:  Books In Care Of - Phone Number  xpath: /IRS990PF/StatementsRegardingActyGrp/PhoneNum 

    SttmntsRgrdngActy_NECTFlngInLOFFrm1041Ind = Column(String(length=1))
    # Line number:  Part VII-A Line 15  Description:  Section 4947(a)(1) Nonexempt Charitable Trusts Filing in lieu of Form 1041  xpath: /IRS990PF/StatementsRegardingActyGrp/NECTFilingInLieuOFForm1041Ind 

    SttmntsRgrdngActy_TxExmptIntrstAmt = Column(BigInteger)
    # Line number:  Part VII-A Line 15  Description:  Tax Exempt Interest Received  xpath: /IRS990PF/StatementsRegardingActyGrp/TaxExemptInterestAmt 

    SttmntsRgrdngActy_FrgnAccntsQstnInd = Column(String(length=5))
    # Line number:  Part VII-A Line 16  Description:  Interest or a signature or other authority over a bank, securities, or other financial account in a foreign country?  xpath: /IRS990PF/StatementsRegardingActyGrp/ForeignAccountsQuestionInd 

    PrsnsWthBksNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part VII-A Line 14  Description:  Business name line 1  xpath: /IRS990PF/StatementsRegardingActyGrp/PersonsWithBooksName/BusinessNameLine1Txt 

    PrsnsWthBksNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part VII-A Line 14  Description:  Business name line 2  xpath: /IRS990PF/StatementsRegardingActyGrp/PersonsWithBooksName/BusinessNameLine2Txt 

    SttmntsRgrdngActy_IndvdlWthBksNm = Column(String(length=35))
    # Line number:  Part VII-A Line 14  Description:  Books In Care Of - Person Name  xpath: /IRS990PF/StatementsRegardingActyGrp/IndividualWithBooksNm 

    LctnOfBksUSAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VII-A Line 14  Description:  Address line 1  xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksUSAddress/AddressLine1Txt 

    LctnOfBksUSAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VII-A Line 14  Description:  Address line 2  xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksUSAddress/AddressLine2Txt 

    LctnOfBksUSAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part VII-A Line 14  Description:  City  xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksUSAddress/CityNm 

    LctnOfBksUSAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part VII-A Line 14  Description:  State  xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksUSAddress/StateAbbreviationCd 

    LctnOfBksUSAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part VII-A Line 14  Description:  ZIP code  xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksUSAddress/ZIPCd 

    LctnOfBksFrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VII-A Line 14  Description:  Address line 1  xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksForeignAddress/AddressLine1Txt 

    LctnOfBksFrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VII-A Line 14  Description:  Address line 2  xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksForeignAddress/AddressLine2Txt 

    LctnOfBksFrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part VII-A Line 14  Description:  City  xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksForeignAddress/CityNm 

    LctnOfBksFrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part VII-A Line 14  Description:  Province or state  xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksForeignAddress/ProvinceOrStateNm 

    LctnOfBksFrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part VII-A Line 14  Description:  Country  xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksForeignAddress/CountryCd 

    LctnOfBksFrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part VII-A Line 14  Description:  Postal code  xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksForeignAddress/ForeignPostalCd 

#######
#
# IRS990PF - PF Part VII-B Statements Regarding Activities for Which Form 4720 May Be Required 
#
#######

class pf_part_viib(Base):
    __tablename__='pf_part_viib'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SttmntsRgrdngActy4720 = Column(Text)
    # xpath: /IRS990PF/StatementsRegardingActy4720Grp 

    SlOrExchDsqlfdPrsnInd = Column(String(length=5))
    # Line number:  Part VII-B Line 1a(1)  Description:  Sale or Exchange with a Disqualified Person?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/SaleOrExchDisqualifiedPrsnInd 

    BrrwOrLndDsqlfdPrsnInd = Column(String(length=5))
    # Line number:  Part VII-B Line 1a(2)  Description:  Borrow or Lend with a Disqualified Person?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/BrrwOrLendDisqualifiedPrsnInd 

    FrnGdsDsqlfdPrsnInd = Column(String(length=5))
    # Line number:  Part VII-B Line 1a(3)  Description:  Furnished Goods, etc. with a Disqualified Person?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/FurnGoodsDisqualifiedPrsnInd 

    PyCmpDsqlfdPrsnInd = Column(String(length=5))
    # Line number:  Part VII-B Line 1a(4)  Description:  Pay Compensation to a Disqualified Person?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/PayCompDisqualifiedPrsnInd 

    TrnsfrAstDsqlfdPrsnInd = Column(String(length=5))
    # Line number:  Part VII-B Line 1a(5)  Description:  Transfer Assets to a Disqualified Person?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/TransferAstDisqualifiedPrsnInd 

    PymntTGvrnmntOffclInd = Column(String(length=5))
    # Line number:  Part VII-B Line 1a(6)  Description:  Payment to a Government Official?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/PaymentToGovernmentOfficialInd 

    ActsFlTQlfyAsExcptnsInd = Column(String(length=5))
    # Line number:  Part VII-B Line 1b  Description:  Any Acts Fail to Qualify as Exceptions?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/ActsFailToQlfyAsExceptionsInd 

    RlyngCrrntNtcDsstrAsstInd = Column(String(length=1))
    # Line number:  Part VII-B Line 1b  Description:  Relying on Current Notice of Disaster Assistance  xpath: /IRS990PF/StatementsRegardingActy4720Grp/RelyingCurrentNtcDsstrAsstInd 

    UncrrctdPrrActsInd = Column(String(length=5))
    # Line number:  Part VII-B Line 1c  Description:  Uncorrected Prior Acts?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/UncorrectedPriorActsInd 

    UndstrbtdIncmPYInd = Column(String(length=5))
    # Line number:  Part VII-B Line 2a  Description:  Undistributed Income Prior Years?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistributedIncomePYInd 

    UndstrbtdIncmPY1Yr = Column(Integer)
    # Line number:  Part VII-B Line 2a  Description:  Undistributed Income Prior Year 1  xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistributedIncomePY1Yr 

    UndstrbtdIncmPY2Yr = Column(Integer)
    # Line number:  Part VII-B Line 2a  Description:  Undistributed Income Prior Year 2  xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistributedIncomePY2Yr 

    UndstrbtdIncmPY3Yr = Column(Integer)
    # Line number:  Part VII-B Line 2a  Description:  Undistributed Income Prior Year 3  xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistributedIncomePY3Yr 

    UndstrbtdIncmPY4Yr = Column(Integer)
    # Line number:  Part VII-B Line 2a  Description:  Undistributed Income Prior Year 4  xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistributedIncomePY4Yr 

    UndstrIncmSct49422NtAppInd = Column(Text)
    # Line number:  Part VII-B Line 2b  Description:  Undistributed Income 4942(a)(2) Not Applied?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistrIncmSect4942a2NotAppInd 

    UndstrIncmSct49422AppYr1Yr = Column(Integer)
    # Line number:  Part VII-B Line 2c  Description:  Undistributed Income 4942(a)(2) Applied Year 1  xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistrIncmSect4942a2AppYr1Yr 

    UndstrIncmSct49422AppYr2Yr = Column(Integer)
    # Line number:  Part VII-B Line 2c  Description:  Undistributed Income 4942(a)(2) Applied Year 2  xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistrIncmSect4942a2AppYr2Yr 

    UndstrIncmSct49422AppYr3Yr = Column(Integer)
    # Line number:  Part VII-B Line 2c  Description:  Undistributed Income 4942(a)(2) Applied Year 3  xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistrIncmSect4942a2AppYr3Yr 

    UndstrIncmSct49422AppYr4Yr = Column(Integer)
    # Line number:  Part VII-B Line 2c  Description:  Undistributed Income 4942(a)(2) Applied Year 4  xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistrIncmSect4942a2AppYr4Yr 

    BsnssHldngsInd = Column(String(length=5))
    # Line number:  Part VII-B Line 3a  Description:  Business Holdings?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/BusinessHoldingsInd 

    ExcssBsnssHldngsInd = Column(String(length=5))
    # Line number:  Part VII-B Line 3b  Description:  Excess Business Holdings?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/ExcessBusinessHoldingsInd 

    JprdyInvstmntsInd = Column(String(length=5))
    # Line number:  Part VII-B Line 4a  Description:  Jeopardy Investments?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/JeopardyInvestmentsInd 

    UncrrctdPYJprdyInvstInd = Column(String(length=5))
    # Line number:  Part VII-B Line 4b  Description:  Uncorrected Jeopardy Investments?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/UncorrectedPYJeopardyInvstInd 

    InflncLgsltnInd = Column(String(length=5))
    # Line number:  Part VII-B Line 5a(1)  Description:  Influence Legislation?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/InfluenceLegislationInd 

    InflncElctnInd = Column(String(length=5))
    # Line number:  Part VII-B Line 5a(2)  Description:  Influence Election?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/InfluenceElectionInd 

    GrntsTIndvdlsInd = Column(String(length=5))
    # Line number:  Part VII-B Line 5a(3)  Description:  Grants to Individuals?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/GrantsToIndividualsInd 

    GrntsTOrgnztnsInd = Column(String(length=5))
    # Line number:  Part VII-B Line 5a(4)  Description:  Grants to Organizations?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/GrantsToOrganizationsInd 

    NnchrtblPrpsInd = Column(String(length=5))
    # Line number:  Part VII-B Line 5a(5)  Description:  Noncharitable Purpose?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/NoncharitablePurposeInd 

    TrnsctnsFlTQlfyAsExcInd = Column(String(length=5))
    # Line number:  Part VII-B Line 5b  Description:  Any Transactions Fail to Qualify as Exceptions?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/TransactionsFailToQlfyAsExcInd 

    RlyngCrrntNtcDsstrAsst1Ind = Column(String(length=1))
    # Line number:  Part VII-B Line 5b  Description:  Relying on Current Notice of Disaster Assistance  xpath: /IRS990PF/StatementsRegardingActy4720Grp/RelyingCurrentNtcDsstrAsst1Ind 

    MntndExpndtrRspnsInd = Column(Text)
    # Line number:  Part VII-B Line 5c  Description:  Maintained Expenditure Responsibility?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/MaintainedExpenditureRspnsInd 

    RcvFndsTPyPrsnlBnftCntrctInd = Column(String(length=5))
    # Line number:  Part VII-B Line 6a  Description:  Receive Funds to Pay Premiums on a Personal Benefit Contract?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/RcvFndsToPayPrsnlBnftCntrctInd 

    PyPrmmsPrsnlBnftCntrctInd = Column(String(length=5))
    # Line number:  Part VII-B Line 6b  Description:  Pay Premiums on a Personal Benefit Contract?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/PayPremiumsPrsnlBnftCntrctInd 

    PrhbtdTxShltrTrnsInd = Column(String(length=5))
    # Line number:  Part VII-B Line 7a  Description:  Prohibited Tax Shelter Transaction?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/ProhibitedTaxShelterTransInd 

    PrcdsOrNtIncmInd = Column(String(length=5))
    # Line number:  Part VII-B Line 7b  Description:  Proceeds Or Net Income?  xpath: /IRS990PF/StatementsRegardingActy4720Grp/ProceedsOrNetIncomeInd 

#######
#
# IRS990PF - PF Part VIII Compensation 
#
#######

class pf_part_viii(Base):
    __tablename__='pf_part_viii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    OffcrDrTrstKyEmplInf = Column(Text)
    # xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp 

    OthrEmplyPdOvr50kCnt = Column(Text)
    # Line number:  Part VIII Line 2  Description:  Total number of other employees paid over $50,000  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OtherEmployeePaidOver50kCnt 

    CntrctrPdOvr50kCnt = Column(Text)
    # Line number:  Part VIII Line 3  Description:  Total number of other contractors paid over $50,000  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/ContractorPaidOver50kCnt 

    CmpOfHghstPdEmplOrNONETxt = Column(Text)
    # Line number:  Part VIII Line 2  Description:  If there are none, enter "None"  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompOfHghstPdEmplOrNONETxt 

    CmpOfHghstPdCntrctOrNONETxt = Column(Text)
    # Line number:  Part VIII Line 3  Description:  If there are none, enter "None"  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompOfHghstPdCntrctOrNONETxt 

#######
#
# IRS990PF - PF Part IX-A Summary of Charitable Activities 
#
#######

class pf_part_ixa(Base):
    __tablename__='pf_part_ixa'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SmmryOfDrctChrtblActy = Column(Text)
    # xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp 

    Dscrptn1Txt = Column(Text)
    # Line number:  Part IX-A Line 1  Description:  Description 1  xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Description1Txt 

    Expnss1Amt = Column(BigInteger)
    # Line number:  Part IX-A Line 1  Description:  Expenses 1  xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Expenses1Amt 

    Dscrptn2Txt = Column(Text)
    # Line number:  Part IX-A Line 2  Description:  Description 2  xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Description2Txt 

    Expnss2Amt = Column(BigInteger)
    # Line number:  Part IX-A Line 2  Description:  Expenses 2  xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Expenses2Amt 

    Dscrptn3Txt = Column(Text)
    # Line number:  Part IX-A Line 3  Description:  Description 3  xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Description3Txt 

    Expnss3Amt = Column(BigInteger)
    # Line number:  Part IX-A Line 3  Description:  Expenses 3  xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Expenses3Amt 

    Dscrptn4Txt = Column(Text)
    # Line number:  Part IX-A Line 4  Description:  Description 4  xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Description4Txt 

    Expnss4Amt = Column(BigInteger)
    # Line number:  Part IX-A Line 4  Description:  Expenses 4  xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Expenses4Amt 

#######
#
# IRS990PF - PF Part IX-B Summary of Program-Related Investments 
#
#######

class pf_part_ixb(Base):
    __tablename__='pf_part_ixb'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SmOfPrgrmRltdInvst = Column(Text)
    # xpath: /IRS990PF/SumOfProgramRelatedInvstGrp 

    Dscrptn1Txt = Column(Text)
    # Line number:  Part IX-B Line 1  Description:  Description 1  xpath: /IRS990PF/SumOfProgramRelatedInvstGrp/Description1Txt 

    Expnss1Amt = Column(BigInteger)
    # Line number:  Part IX-B Line 1  Description:  Amount 1  xpath: /IRS990PF/SumOfProgramRelatedInvstGrp/Expenses1Amt 

    Dscrptn2Txt = Column(Text)
    # Line number:  Part IX-B Line 2  Description:  Description 2  xpath: /IRS990PF/SumOfProgramRelatedInvstGrp/Description2Txt 

    Expnss2Amt = Column(BigInteger)
    # Line number:  Part IX-B Line 2  Description:  Amount 2  xpath: /IRS990PF/SumOfProgramRelatedInvstGrp/Expenses2Amt 

    AllOthrPrgrmRltdInvstTtAmt = Column(Text)
    # Line number:  Part IX-B Line 3  Description:  All Other Program-Related Investments Total  xpath: /IRS990PF/SumOfProgramRelatedInvstGrp/AllOtherProgramRltdInvstTotAmt 

    TtlAmt = Column(BigInteger)
    # Line number:  Part IX-B Total  Description:  Total  xpath: /IRS990PF/SumOfProgramRelatedInvstGrp/TotalAmt 

#######
#
# IRS990PF - PF Part X Minimum Investment Return 
#
#######

class pf_part_x(Base):
    __tablename__='pf_part_x'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    MnmmInvstmntRtrn = Column(Text)
    # xpath: /IRS990PF/MinimumInvestmentReturnGrp 

    AvrgMnthlyFMVOfScAmt = Column(BigInteger)
    # Line number:  Part X Line 1a  Description:  Average Monthly FMV of Securities  xpath: /IRS990PF/MinimumInvestmentReturnGrp/AverageMonthlyFMVOfSecAmt 

    AvrgMnthlyCshBlncsAmt = Column(BigInteger)
    # Line number:  Part X Line 1b  Description:  Average Monthly Cash Balances  xpath: /IRS990PF/MinimumInvestmentReturnGrp/AverageMonthlyCashBalancesAmt 

    FMVAllOthrNnchrtblAstAmt = Column(BigInteger)
    # Line number:  Part X Line 1c  Description:  FMV of All Other Noncharitable Assets  xpath: /IRS990PF/MinimumInvestmentReturnGrp/FMVAllOtherNoncharitableAstAmt 

    TtlFMVOfUnsdAsstsAmt = Column(BigInteger)
    # Line number:  Part X Line 1d  Description:  Total FMV of Unused Assets  xpath: /IRS990PF/MinimumInvestmentReturnGrp/TotalFMVOfUnusedAssetsAmt 

    RdctnClmdAmt = Column(Text)
    # Line number:  Part X Line 1e  Description:  Reduction Claimed  xpath: /IRS990PF/MinimumInvestmentReturnGrp/ReductionClaimedAmt 

    AcqstnIndbtdnssAmt = Column(BigInteger)
    # Line number:  Part X Line 2  Description:  Acquisition Indebtedness  xpath: /IRS990PF/MinimumInvestmentReturnGrp/AcquisitionIndebtednessAmt 

    AdjstdTtlFMVOfUnsdAstAmt = Column(BigInteger)
    # Line number:  Part X Line 3  Description:  Adjusted Total FMV of Unused Assets (subtract line 2 from line 1d)  xpath: /IRS990PF/MinimumInvestmentReturnGrp/AdjustedTotalFMVOfUnusedAstAmt 

    CshDmdChrtblAmt = Column(Text)
    # Line number:  Part X Line 4  Description:  Cash Deemed Charitable  xpath: /IRS990PF/MinimumInvestmentReturnGrp/CashDeemedCharitableAmt 

    NtVlNnchrtblAsstsAmt = Column(BigInteger)
    # Line number:  Part X Line 5  Description:  Net Noncharitable Assets  xpath: /IRS990PF/MinimumInvestmentReturnGrp/NetVlNoncharitableAssetsAmt 

    MnmmInvstmntRtrnAmt = Column(BigInteger)
    # Line number:  Part X Line 6  Description:  Minimum Investment Return  xpath: /IRS990PF/MinimumInvestmentReturnGrp/MinimumInvestmentReturnAmt 

#######
#
# IRS990PF - PF Part XI Distributable Amount 
#
#######

class pf_part_xi(Base):
    __tablename__='pf_part_xi'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    DstrbtblAmnt = Column(Text)
    # xpath: /IRS990PF/DistributableAmountGrp 

    Sct4942j3j5FndtnAndFrgnOrgInd = Column(String(length=1))
    # Description:  Section 4942(j)(3)&(j)(5) Private Operating Foundations and Certain Foreign Organizations  xpath: /IRS990PF/DistributableAmountGrp/Sect4942j3j5FndtnAndFrgnOrgInd 

    MnmmInvstmntRtrnAmt = Column(BigInteger)
    # Line number:  Part XI Line 1  Description:  Minimum Investment Return  xpath: /IRS990PF/DistributableAmountGrp/MinimumInvestmentReturnAmt 

    TxBsdOnInvstmntIncmAmt = Column(BigInteger)
    # Line number:  Part XI Line 2a  Description:  Tax Based on Investment Income  xpath: /IRS990PF/DistributableAmountGrp/TaxBasedOnInvestmentIncomeAmt 

    IncmTxAmt = Column(BigInteger)
    # Line number:  Part XI Line 2b  Description:  Income Tax for This Year  xpath: /IRS990PF/DistributableAmountGrp/IncomeTaxAmt 

    TtlTxAmt = Column(BigInteger)
    # Line number:  Part XI Line 2c  Description:  Total Tax (add lines 2a and 2b)  xpath: /IRS990PF/DistributableAmountGrp/TotalTaxAmt 

    DstrbtblBfrAdjAmt = Column(BigInteger)
    # Line number:  Part XI Line 3  Description:  Distributable Amount Before Adjustments  xpath: /IRS990PF/DistributableAmountGrp/DistributableBeforeAdjAmt 

    RcvrsQlfdDstrAmt = Column(BigInteger)
    # Line number:  Part XI Line 4  Description:  Recoveries of Qualified Distributions  xpath: /IRS990PF/DistributableAmountGrp/RecoveriesQualfiedDistriAmt 

    DstrbtblBfrDdAmt = Column(BigInteger)
    # Line number:  Part XI Line 5  Description:  Distributable Amount Before Deduction (add lines 3 and 4)  xpath: /IRS990PF/DistributableAmountGrp/DistributableBeforeDedAmt 

    DdctnFrmDstrbtblAmt = Column(BigInteger)
    # Line number:  Part XI Line 6  Description:  Deduction from Distributable Amount  xpath: /IRS990PF/DistributableAmountGrp/DeductionFromDistributableAmt 

    DstrbtblAsAdjstdAmt = Column(BigInteger)
    # Line number:  Part XI Line 7  Description:  Distributable Amount as Adjusted  xpath: /IRS990PF/DistributableAmountGrp/DistributableAsAdjustedAmt 

#######
#
# IRS990PF - PF Part XII Qualifying Distributions 
#
#######

class pf_part_xii(Base):
    __tablename__='pf_part_xii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    QlfyngDstrPrtXII = Column(Text)
    # xpath: /IRS990PF/QualifyingDistriPartXIIGrp 

    ExpnssAndCntrbtnsAmt = Column(Text)
    # Line number:  Part XII Line 1a  Description:  Expenses and Contributions  xpath: /IRS990PF/QualifyingDistriPartXIIGrp/ExpensesAndContributionsAmt 

    PrgrmRltdInvstTtlAmt = Column(BigInteger)
    # Line number:  Part XII Line 1b  Description:  Program Related Investments Total  xpath: /IRS990PF/QualifyingDistriPartXIIGrp/ProgramRelatedInvstTotalAmt 

    ChrtblAsstsAcqsPdAmt = Column(BigInteger)
    # Line number:  Part XII Line 2  Description:  Amounts Paid to Acquire Charitable Assets  xpath: /IRS990PF/QualifyingDistriPartXIIGrp/CharitableAssetsAcquisPaidAmt 

    StAsdStbltyTstAmt = Column(BigInteger)
    # Line number:  Part XII Line 3a  Description:  Amounts Set Aside - Suitability Test  xpath: /IRS990PF/QualifyingDistriPartXIIGrp/SetAsideSuitabilityTestAmt 

    StAsdCshDstrTstAmt = Column(Text)
    # Line number:  Part XII Line 3b  Description:  Amounts Set Aside - Cash Distribution Test  xpath: /IRS990PF/QualifyingDistriPartXIIGrp/SetAsideCashDistriTestAmt 

    QlfyngDstrbtnsAmt = Column(BigInteger)
    # Line number:  Part XII Line 4  Description:  Qualifying Distributions  xpath: /IRS990PF/QualifyingDistriPartXIIGrp/QualifyingDistributionsAmt 

    PctSct4940OrgNtInvstIncmAmt = Column(BigInteger)
    # Line number:  Part XII Line 5  Description:  1% of Section 4940(e) Organizations Net Investment Income  xpath: /IRS990PF/QualifyingDistriPartXIIGrp/PctSect4940eOrgNetInvstIncmAmt 

    AdjstdQlfyngDstrAmt = Column(BigInteger)
    # Line number:  Part XII Line 6  Description:  Adjusted Qualifying Distributions  xpath: /IRS990PF/QualifyingDistriPartXIIGrp/AdjustedQualifyingDistriAmt 

#######
#
# IRS990PF - PF Part XIII Undistributed Income 
#
#######

class pf_part_xiii(Base):
    __tablename__='pf_part_xiii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    UndstrbtdIncm = Column(Text)
    # xpath: /IRS990PF/UndistributedIncomeGrp 

    DstrbtblAsAdjstdAmt = Column(BigInteger)
    # Line number:  Part XIII Line 1(d)  Description:  Distributable Amount as Adjusted  xpath: /IRS990PF/UndistributedIncomeGrp/DistributableAsAdjustedAmt 

    UndstrbtdIncmPYAmt = Column(BigInteger)
    # Line number:  Part XIII Line 2a(c)  Description:  Undistributed Income Prior Year  xpath: /IRS990PF/UndistributedIncomeGrp/UndistributedIncomePYAmt 

    PrrYr1Yr = Column(Integer)
    # Line number:  Part XIII Line 2b  Description:  Prior Year 1  xpath: /IRS990PF/UndistributedIncomeGrp/PriorYear1Yr 

    PrrYr2Yr = Column(Integer)
    # Line number:  Part XIII Line 2b  Description:  Prior Year 2  xpath: /IRS990PF/UndistributedIncomeGrp/PriorYear2Yr 

    PrrYr3Yr = Column(Integer)
    # Line number:  Part XIII Line 2b  Description:  Prior Year 3  xpath: /IRS990PF/UndistributedIncomeGrp/PriorYear3Yr 

    TtlFrPrrYrsAmt = Column(BigInteger)
    # Line number:  Part XIII Line 2b(b)  Description:  Total for Prior Years  xpath: /IRS990PF/UndistributedIncomeGrp/TotalForPriorYearsAmt 

    ExcssDstrbtnCyvYr5Amt = Column(BigInteger)
    # Line number:  Part XIII Line 3a  Description:  Excess Distributions Carryover - Year 5  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistributionCyovYr5Amt 

    ExcssDstrbtnCyvYr4Amt = Column(BigInteger)
    # Line number:  Part XIII Line 3b  Description:  Excess Distributions Carryover - Year 4  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistributionCyovYr4Amt 

    ExcssDstrbtnCyvYr3Amt = Column(BigInteger)
    # Line number:  Part XIII Line 3c  Description:  Excess Distributions Carryover - Year 3  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistributionCyovYr3Amt 

    ExcssDstrbtnCyvYr2Amt = Column(BigInteger)
    # Line number:  Part XIII Line 3d  Description:  Excess Distributions Carryover - Year 2  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistributionCyovYr2Amt 

    ExcssDstrbtnCyvYr1Amt = Column(BigInteger)
    # Line number:  Part XIII Line 3e  Description:  Excess Distributions Carryover - Year 1  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistributionCyovYr1Amt 

    TtlExcssDstrbtnCyvAmt = Column(BigInteger)
    # Line number:  Part XIII Line 3f(a)  xpath: /IRS990PF/UndistributedIncomeGrp/TotalExcessDistributionCyovAmt 

    QlfyngDstrbtnsAmt = Column(BigInteger)
    # Line number:  Part XIII Line 4  Description:  Qualifying Distributions  xpath: /IRS990PF/UndistributedIncomeGrp/QualifyingDistributionsAmt 

    AppldTYr1Amt = Column(BigInteger)
    # Line number:  Part XIII Line 4a(c)  Description:  Applied to Year 1  xpath: /IRS990PF/UndistributedIncomeGrp/AppliedToYear1Amt 

    AppldTPrrYrsAmt = Column(Text)
    # Line number:  Part XIII Line 4b(b)  Description:  Applied to Prior Years  xpath: /IRS990PF/UndistributedIncomeGrp/AppliedToPriorYearsAmt 

    TrtdAsDstrFrmCrpsAmt = Column(Text)
    # Line number:  Part XIII Line 4c(a)  Description:  Treated as Distribution from Corpus  xpath: /IRS990PF/UndistributedIncomeGrp/TreatedAsDistriFromCorpusAmt 

    AppldTCrrntYrAmt = Column(BigInteger)
    # Line number:  Part XIII Line 4d(d)  Description:  Applied to Current Year  xpath: /IRS990PF/UndistributedIncomeGrp/AppliedToCurrentYearAmt 

    RmnngDstrFrmCrpsAmt = Column(BigInteger)
    # Line number:  Part XIII Line 4e(a)  Description:  Remaining Amount Distributed from Corpus  xpath: /IRS990PF/UndistributedIncomeGrp/RemainingDistriFromCorpusAmt 

    ExcssDstrCyvAppCYCrpsAmt = Column(BigInteger)
    # Line number:  Part XIII Line 5(a)  Description:  Excess Distributions Carryover Applied to Current Year - Corpus  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistriCyovAppCYCorpusAmt 

    ExcssDstrbtnCyvAppCYAmt = Column(BigInteger)
    # Line number:  Part XIII Line 5(d)  Description:  Excess Distributions Carryover Applied to Current Year  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistributionCyovAppCYAmt 

    TtlCrpsAmt = Column(BigInteger)
    # Line number:  Part XIII Line 6a(a)  Description:  Total Corpus  xpath: /IRS990PF/UndistributedIncomeGrp/TotalCorpusAmt 

    PrrYrUndstrbtdIncmAmt = Column(BigInteger)
    # Line number:  Part XIII Line 6b(b)  Description:  Prior Year's Undistributed Income  xpath: /IRS990PF/UndistributedIncomeGrp/PriorYearUndistributedIncmAmt 

    PrrYrDfcncyOrTxAmt = Column(BigInteger)
    # Line number:  Part XIII Line 6c(b)  Description:  Prior Year's Deficiency or Tax  xpath: /IRS990PF/UndistributedIncomeGrp/PriorYearDeficiencyOrTaxAmt 

    Txbl1Amt = Column(BigInteger)
    # Line number:  Part XIII Line 6d(b)  Description:  Taxable Amount 1  xpath: /IRS990PF/UndistributedIncomeGrp/Taxable1Amt 

    Txbl2Amt = Column(BigInteger)
    # Line number:  Part XIII Line 6e(c)  Description:  Taxable Amount 2  xpath: /IRS990PF/UndistributedIncomeGrp/Taxable2Amt 

    UndstrbtdIncmCYAmt = Column(BigInteger)
    # Line number:  Part XIII Line 6f(d)  Description:  Undistributed Income for Current Year  xpath: /IRS990PF/UndistributedIncomeGrp/UndistributedIncomeCYAmt 

    CrpsDstr170b1EOr4942g3Amt = Column(BigInteger)
    # Line number:  Part XIII Line 7(a)  Description:  Treated as Distribution from Corpus to Satisfy Requirements Imposed by Section 170(b)(1)(E) or 4942(g)(3)  xpath: /IRS990PF/UndistributedIncomeGrp/CorpusDistri170b1EOr4942g3Amt 

    ExcssDstrCyvFrmYr5Amt = Column(BigInteger)
    # Line number:  Part XIII Line 8(a)  Description:  Excess Distribution Carryover from Year 5  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistriCyovFromYr5Amt 

    ExcssDstrCyvTNxtYrAmt = Column(BigInteger)
    # Line number:  Part XIII Line 9(a)  Description:  Excess Distribution Carryover to Next Year  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistriCyovToNextYrAmt 

    ExcssFrmYr4Amt = Column(BigInteger)
    # Line number:  Part XIII Line 10a  Description:  Excess from Year 4  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessFromYear4Amt 

    ExcssFrmYr3Amt = Column(BigInteger)
    # Line number:  Part XIII Line 10b  Description:  Excess from Year 3  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessFromYear3Amt 

    ExcssFrmYr2Amt = Column(BigInteger)
    # Line number:  Part XIII Line 10c  Description:  Excess from Year 2  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessFromYear2Amt 

    ExcssFrmYr1Amt = Column(BigInteger)
    # Line number:  Part XIII Line 10d  Description:  Excess from Year 1  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessFromYear1Amt 

    ExcssFrmCrrntYrAmt = Column(BigInteger)
    # Line number:  Part XIII Line 10e  Description:  Excess from Current Year  xpath: /IRS990PF/UndistributedIncomeGrp/ExcessFromCurrentYearAmt 

#######
#
# IRS990PF - PF Part XIV Private Operating Foundations 
#
#######

class pf_part_xiv(Base):
    __tablename__='pf_part_xiv'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    PF_PrvtOprtngFndtns = Column(Text)
    # xpath: /IRS990PF/PrivateOperatingFoundationsGrp 

    PrvtOprtngFndtns_PrvtOprtngFndtnRlngDt = Column(String(length=31))
    # Line number:  Part XIV Line 1a  Description:  Date of Ruling  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/PrivateOperatingFndtnRulingDt 

    LssrAdjNtIncmMnInvstRt_CrrntYrAmt = Column(BigInteger)
    # Line number:  column (a)  Description:  Current Year  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LessorAdjNetIncmMinInvstRetGrp/CurrentYearAmt 

    LssrAdjNtIncmMnInvstRt_Yr1Amt = Column(BigInteger)
    # Line number:  column (b)  Description:  Year 1  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LessorAdjNetIncmMinInvstRetGrp/Year1Amt 

    LssrAdjNtIncmMnInvstRt_Yr2Amt = Column(BigInteger)
    # Line number:  column (c)  Description:  Year 2  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LessorAdjNetIncmMinInvstRetGrp/Year2Amt 

    LssrAdjNtIncmMnInvstRt_Yr3Amt = Column(BigInteger)
    # Line number:  column (d)  Description:  Year 3  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LessorAdjNetIncmMinInvstRetGrp/Year3Amt 

    LssrAdjNtIncmMnInvstRt_TtlAmt = Column(BigInteger)
    # Line number:  column (e)  Description:  Total  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LessorAdjNetIncmMinInvstRetGrp/TotalAmt 

    Pct85LssrAdjIncmOrMnRt_CrrntYrAmt = Column(BigInteger)
    # Line number:  column (a)  Description:  Current Year  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Pct85LessorAdjIncmOrMinRetGrp/CurrentYearAmt 

    Pct85LssrAdjIncmOrMnRt_Yr1Amt = Column(BigInteger)
    # Line number:  column (b)  Description:  Year 1  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Pct85LessorAdjIncmOrMinRetGrp/Year1Amt 

    Pct85LssrAdjIncmOrMnRt_Yr2Amt = Column(BigInteger)
    # Line number:  column (c)  Description:  Year 2  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Pct85LessorAdjIncmOrMinRetGrp/Year2Amt 

    Pct85LssrAdjIncmOrMnRt_Yr3Amt = Column(BigInteger)
    # Line number:  column (d)  Description:  Year 3  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Pct85LessorAdjIncmOrMinRetGrp/Year3Amt 

    Pct85LssrAdjIncmOrMnRt_TtlAmt = Column(BigInteger)
    # Line number:  column (e)  Description:  Total  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Pct85LessorAdjIncmOrMinRetGrp/TotalAmt 

    QlfyngDstrbtns_CrrntYrAmt = Column(BigInteger)
    # Line number:  column (a)  Description:  Current Year  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistributionsGrp/CurrentYearAmt 

    QlfyngDstrbtns_Yr1Amt = Column(BigInteger)
    # Line number:  column (b)  Description:  Year 1  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistributionsGrp/Year1Amt 

    QlfyngDstrbtns_Yr2Amt = Column(BigInteger)
    # Line number:  column (c)  Description:  Year 2  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistributionsGrp/Year2Amt 

    QlfyngDstrbtns_Yr3Amt = Column(BigInteger)
    # Line number:  column (d)  Description:  Year 3  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistributionsGrp/Year3Amt 

    QlfyngDstrbtns_TtlAmt = Column(BigInteger)
    # Line number:  column (e)  Description:  Total  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistributionsGrp/TotalAmt 

    QlfyngDstrNtUsdDrt_CrrntYrAmt = Column(BigInteger)
    # Line number:  column (a)  Description:  Current Year  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriNotUsedDrtGrp/CurrentYearAmt 

    QlfyngDstrNtUsdDrt_Yr1Amt = Column(BigInteger)
    # Line number:  column (b)  Description:  Year 1  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriNotUsedDrtGrp/Year1Amt 

    QlfyngDstrNtUsdDrt_Yr2Amt = Column(BigInteger)
    # Line number:  column (c)  Description:  Year 2  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriNotUsedDrtGrp/Year2Amt 

    QlfyngDstrNtUsdDrt_Yr3Amt = Column(BigInteger)
    # Line number:  column (d)  Description:  Year 3  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriNotUsedDrtGrp/Year3Amt 

    QlfyngDstrNtUsdDrt_TtlAmt = Column(BigInteger)
    # Line number:  column (e)  Description:  Total  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriNotUsedDrtGrp/TotalAmt 

    QlfyngDstrMdDrt_CrrntYrAmt = Column(BigInteger)
    # Line number:  column (a)  Description:  Current Year  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriMadeDrtGrp/CurrentYearAmt 

    QlfyngDstrMdDrt_Yr1Amt = Column(BigInteger)
    # Line number:  column (b)  Description:  Year 1  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriMadeDrtGrp/Year1Amt 

    QlfyngDstrMdDrt_Yr2Amt = Column(BigInteger)
    # Line number:  column (c)  Description:  Year 2  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriMadeDrtGrp/Year2Amt 

    QlfyngDstrMdDrt_Yr3Amt = Column(BigInteger)
    # Line number:  column (d)  Description:  Year 3  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriMadeDrtGrp/Year3Amt 

    QlfyngDstrMdDrt_TtlAmt = Column(BigInteger)
    # Line number:  column (e)  Description:  Total  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriMadeDrtGrp/TotalAmt 

    TtlAssts_CrrntYrAmt = Column(BigInteger)
    # Line number:  column (a)  Description:  Current Year  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsGrp/CurrentYearAmt 

    TtlAssts_Yr1Amt = Column(BigInteger)
    # Line number:  column (b)  Description:  Year 1  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsGrp/Year1Amt 

    TtlAssts_Yr2Amt = Column(BigInteger)
    # Line number:  column (c)  Description:  Year 2  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsGrp/Year2Amt 

    TtlAssts_Yr3Amt = Column(BigInteger)
    # Line number:  column (d)  Description:  Year 3  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsGrp/Year3Amt 

    TtlAssts_TtlAmt = Column(BigInteger)
    # Line number:  column (e)  Description:  Total  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsGrp/TotalAmt 

    TtlAsstsSct4942j3B_CrrntYrAmt = Column(BigInteger)
    # Line number:  column (a)  Description:  Current Year  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsSect4942j3BiGrp/CurrentYearAmt 

    TtlAsstsSct4942j3B_Yr1Amt = Column(BigInteger)
    # Line number:  column (b)  Description:  Year 1  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsSect4942j3BiGrp/Year1Amt 

    TtlAsstsSct4942j3B_Yr2Amt = Column(BigInteger)
    # Line number:  column (c)  Description:  Year 2  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsSect4942j3BiGrp/Year2Amt 

    TtlAsstsSct4942j3B_Yr3Amt = Column(BigInteger)
    # Line number:  column (d)  Description:  Year 3  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsSect4942j3BiGrp/Year3Amt 

    TtlAsstsSct4942j3B_TtlAmt = Column(BigInteger)
    # Line number:  column (e)  Description:  Total  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsSect4942j3BiGrp/TotalAmt 

    TwThrdsMnmmInvstRt_CrrntYrAmt = Column(BigInteger)
    # Line number:  column (a)  Description:  Current Year  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TwoThirdsMinimumInvstRetGrp/CurrentYearAmt 

    TwThrdsMnmmInvstRt_Yr1Amt = Column(BigInteger)
    # Line number:  column (b)  Description:  Year 1  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TwoThirdsMinimumInvstRetGrp/Year1Amt 

    TwThrdsMnmmInvstRt_Yr2Amt = Column(BigInteger)
    # Line number:  column (c)  Description:  Year 2  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TwoThirdsMinimumInvstRetGrp/Year2Amt 

    TwThrdsMnmmInvstRt_Yr3Amt = Column(BigInteger)
    # Line number:  column (d)  Description:  Year 3  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TwoThirdsMinimumInvstRetGrp/Year3Amt 

    TwThrdsMnmmInvstRt_TtlAmt = Column(BigInteger)
    # Line number:  column (e)  Description:  Total  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TwoThirdsMinimumInvstRetGrp/TotalAmt 

    TtlSpprt_CrrntYrAmt = Column(BigInteger)
    # Line number:  column (a)  Description:  Current Year  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalSupportGrp/CurrentYearAmt 

    TtlSpprt_Yr1Amt = Column(BigInteger)
    # Line number:  column (b)  Description:  Year 1  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalSupportGrp/Year1Amt 

    TtlSpprt_Yr2Amt = Column(BigInteger)
    # Line number:  column (c)  Description:  Year 2  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalSupportGrp/Year2Amt 

    TtlSpprt_Yr3Amt = Column(BigInteger)
    # Line number:  column (d)  Description:  Year 3  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalSupportGrp/Year3Amt 

    TtlSpprt_TtlAmt = Column(BigInteger)
    # Line number:  column (e)  Description:  Total  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalSupportGrp/TotalAmt 

    PblcSpprt_CrrntYrAmt = Column(BigInteger)
    # Line number:  column (a)  Description:  Current Year  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/PublicSupportType/CurrentYearAmt 

    PblcSpprt_Yr1Amt = Column(BigInteger)
    # Line number:  column (b)  Description:  Year 1  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/PublicSupportType/Year1Amt 

    PblcSpprt_Yr2Amt = Column(BigInteger)
    # Line number:  column (c)  Description:  Year 2  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/PublicSupportType/Year2Amt 

    PblcSpprt_Yr3Amt = Column(BigInteger)
    # Line number:  column (d)  Description:  Year 3  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/PublicSupportType/Year3Amt 

    PblcSpprt_TtlAmt = Column(BigInteger)
    # Line number:  column (e)  Description:  Total  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/PublicSupportType/TotalAmt 

    LrgstSpprtFrmEO_CrrntYrAmt = Column(BigInteger)
    # Line number:  column (a)  Description:  Current Year  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LargestSupportFromEOGrp/CurrentYearAmt 

    LrgstSpprtFrmEO_Yr1Amt = Column(BigInteger)
    # Line number:  column (b)  Description:  Year 1  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LargestSupportFromEOGrp/Year1Amt 

    LrgstSpprtFrmEO_Yr2Amt = Column(BigInteger)
    # Line number:  column (c)  Description:  Year 2  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LargestSupportFromEOGrp/Year2Amt 

    LrgstSpprtFrmEO_Yr3Amt = Column(BigInteger)
    # Line number:  column (d)  Description:  Year 3  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LargestSupportFromEOGrp/Year3Amt 

    LrgstSpprtFrmEO_TtlAmt = Column(BigInteger)
    # Line number:  column (e)  Description:  Total  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LargestSupportFromEOGrp/TotalAmt 

    GrssInvstmntIncm_CrrntYrAmt = Column(BigInteger)
    # Line number:  column (a)  Description:  Current Year  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/GrossInvestmentIncomeGrp/CurrentYearAmt 

    GrssInvstmntIncm_Yr1Amt = Column(BigInteger)
    # Line number:  column (b)  Description:  Year 1  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/GrossInvestmentIncomeGrp/Year1Amt 

    GrssInvstmntIncm_Yr2Amt = Column(BigInteger)
    # Line number:  column (c)  Description:  Year 2  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/GrossInvestmentIncomeGrp/Year2Amt 

    GrssInvstmntIncm_Yr3Amt = Column(BigInteger)
    # Line number:  column (d)  Description:  Year 3  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/GrossInvestmentIncomeGrp/Year3Amt 

    GrssInvstmntIncm_TtlAmt = Column(BigInteger)
    # Line number:  column (e)  Description:  Total  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/GrossInvestmentIncomeGrp/TotalAmt 

    PrvtOprtngFndtns_Sctn4942j3Ind = Column(String(length=1))
    # Line number:  Part XIV Line 1b  Description:  Section 4942(j)(3)  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Section4942j3Ind 

    PrvtOprtngFndtns_Sctn4942j5Ind = Column(String(length=1))
    # Line number:  Part XIV Line 1b  Description:  Section 4942(j)(5)  xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Section4942j5Ind 

#######
#
# IRS990PF - PF Part XV Supplementary Information 
#
#######

class pf_part_xv(Base):
    __tablename__='pf_part_xv'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntryInfrmtn = Column(Text)
    # xpath: /IRS990PF/SupplementaryInformationGrp 

    OnlyCntrTPrslctdInd = Column(String(length=1))
    # Line number:  Part XV Line 2  Description:  Only Contributes to Preselected Charitable Organizations  xpath: /IRS990PF/SupplementaryInformationGrp/OnlyContriToPreselectedInd 

    TtlGrntOrCntrPdDrYrAmt = Column(BigInteger)
    # Line number:  Part XV Line 3a Total  Description:  Total Grant or Contribution Paid During Year  xpath: /IRS990PF/SupplementaryInformationGrp/TotalGrantOrContriPdDurYrAmt 

    TtlGrntOrCntrApprvFtAmt = Column(BigInteger)
    # Line number:  Part XV Line 3b Total  Description:  Total Grant or Contribution Approved for Future Payment  xpath: /IRS990PF/SupplementaryInformationGrp/TotalGrantOrContriApprvFutAmt 

#######
#
# IRS990PF - PF Part XVI-A Analysis of Income-Producing Activities 
#
#######

class pf_part_xvia(Base):
    __tablename__='pf_part_xvia'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    PF_AnlyssIncmPrdcngActy = Column(Text)
    # xpath: /IRS990PF/AnalysisIncomeProducingActyGrp 

    AnlyssIncmPrdcngActy_SbttlsIncmPrdcngActy = Column(Text)
    # Line number:  Part XVI-A Line 12  Description:  Subtotal (add columns (B), (D), and (E))  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/SubtotalsIncmProducingActyGrp 

    SbttlsIncmPrdcngActy_UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/SubtotalsIncmProducingActyGrp/UnrelatedBusinessTaxblIncmAmt 

    SbttlsIncmPrdcngActy_ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/SubtotalsIncmProducingActyGrp/ExclusionAmt 

    SbttlsIncmPrdcngActy_RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/SubtotalsIncmProducingActyGrp/RelatedOrExemptFunctionIncmAmt 

    AnlyssIncmPrdcngActy_TtlIncmPrdcngActyAmt = Column(BigInteger)
    # Line number:  Part XVI-A Line 13  Description:  Total (add line 104, columns (B), (D), and (E))  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/TotalIncomeProducingActyAmt 

    NtRntlIncmRDbtFncdPrp_BsnssCd = Column(Text)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReDebtFincdPropGrp/BusinessCd 

    NtIncmLssFrmSpclEvt_BsnssCd = Column(Text)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetIncomeLossFromSpecialEvtGrp/BusinessCd 

    GrssPrftLssSlsOfInvntry_BsnssCd = Column(Text)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GrossProfitLossSlsOfInvntryGrp/BusinessCd 

    MmbrshpDsAndAssmnt_BsnssCd = Column(Text)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/MembershipDuesAndAssmntGrp/BusinessCd 

    OthrInvstmntIncmPrtVII_BsnssCd = Column(Text)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherInvestmentIncmPartVIIGrp/BusinessCd 

    NtRntlIncmPrsnlPrp_BsnssCd = Column(Text)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRentalIncomePersonalPropGrp/BusinessCd 

    IntOnSvAndTmpCshInvst_BsnssCd = Column(Text)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/IntOnSavAndTempCashInvstGrp/BusinessCd 

    DvAndIntFrmScPrtVII_BsnssCd = Column(Text)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/DivAndIntFromSecPartVIIGrp/BusinessCd 

    FsCntrctsFrmGvtAg_BsnssCd = Column(Text)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/FeesContractsFromGovtAgGrp/BusinessCd 

    GnSlsAstOthThnInvntry_BsnssCd = Column(Text)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GainSalesAstOthThanInvntryGrp/BusinessCd 

    NtRntlIncmRNtDbtFncdPrp_BsnssCd = Column(Text)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReNotDebtFincdProp/BusinessCd 

    NtRntlIncmRDbtFncdPrp_UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReDebtFincdPropGrp/UnrelatedBusinessTaxblIncmAmt 

    IntOnSvAndTmpCshInvst_UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/IntOnSavAndTempCashInvstGrp/UnrelatedBusinessTaxblIncmAmt 

    NtRntlIncmRNtDbtFncdPrp_UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReNotDebtFincdProp/UnrelatedBusinessTaxblIncmAmt 

    GnSlsAstOthThnInvntry_UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GainSalesAstOthThanInvntryGrp/UnrelatedBusinessTaxblIncmAmt 

    DvAndIntFrmScPrtVII_UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/DivAndIntFromSecPartVIIGrp/UnrelatedBusinessTaxblIncmAmt 

    FsCntrctsFrmGvtAg_UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/FeesContractsFromGovtAgGrp/UnrelatedBusinessTaxblIncmAmt 

    GrssPrftLssSlsOfInvntry_UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GrossProfitLossSlsOfInvntryGrp/UnrelatedBusinessTaxblIncmAmt 

    MmbrshpDsAndAssmnt_UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/MembershipDuesAndAssmntGrp/UnrelatedBusinessTaxblIncmAmt 

    NtIncmLssFrmSpclEvt_UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetIncomeLossFromSpecialEvtGrp/UnrelatedBusinessTaxblIncmAmt 

    NtRntlIncmPrsnlPrp_UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRentalIncomePersonalPropGrp/UnrelatedBusinessTaxblIncmAmt 

    OthrInvstmntIncmPrtVII_UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherInvestmentIncmPartVIIGrp/UnrelatedBusinessTaxblIncmAmt 

    NtRntlIncmRNtDbtFncdPrp_ExclsnCd = Column(Text)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReNotDebtFincdProp/ExclusionCd 

    GnSlsAstOthThnInvntry_ExclsnCd = Column(Text)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GainSalesAstOthThanInvntryGrp/ExclusionCd 

    GrssPrftLssSlsOfInvntry_ExclsnCd = Column(Text)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GrossProfitLossSlsOfInvntryGrp/ExclusionCd 

    IntOnSvAndTmpCshInvst_ExclsnCd = Column(Text)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/IntOnSavAndTempCashInvstGrp/ExclusionCd 

    NtIncmLssFrmSpclEvt_ExclsnCd = Column(Text)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetIncomeLossFromSpecialEvtGrp/ExclusionCd 

    MmbrshpDsAndAssmnt_ExclsnCd = Column(Text)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/MembershipDuesAndAssmntGrp/ExclusionCd 

    OthrInvstmntIncmPrtVII_ExclsnCd = Column(Text)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherInvestmentIncmPartVIIGrp/ExclusionCd 

    NtRntlIncmPrsnlPrp_ExclsnCd = Column(Text)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRentalIncomePersonalPropGrp/ExclusionCd 

    NtRntlIncmRDbtFncdPrp_ExclsnCd = Column(Text)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReDebtFincdPropGrp/ExclusionCd 

    DvAndIntFrmScPrtVII_ExclsnCd = Column(Text)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/DivAndIntFromSecPartVIIGrp/ExclusionCd 

    FsCntrctsFrmGvtAg_ExclsnCd = Column(Text)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/FeesContractsFromGovtAgGrp/ExclusionCd 

    MmbrshpDsAndAssmnt_ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/MembershipDuesAndAssmntGrp/ExclusionAmt 

    GnSlsAstOthThnInvntry_ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GainSalesAstOthThanInvntryGrp/ExclusionAmt 

    NtRntlIncmRDbtFncdPrp_ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReDebtFincdPropGrp/ExclusionAmt 

    FsCntrctsFrmGvtAg_ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/FeesContractsFromGovtAgGrp/ExclusionAmt 

    GrssPrftLssSlsOfInvntry_ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GrossProfitLossSlsOfInvntryGrp/ExclusionAmt 

    NtRntlIncmRNtDbtFncdPrp_ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReNotDebtFincdProp/ExclusionAmt 

    NtRntlIncmPrsnlPrp_ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRentalIncomePersonalPropGrp/ExclusionAmt 

    OthrInvstmntIncmPrtVII_ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherInvestmentIncmPartVIIGrp/ExclusionAmt 

    IntOnSvAndTmpCshInvst_ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/IntOnSavAndTempCashInvstGrp/ExclusionAmt 

    DvAndIntFrmScPrtVII_ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/DivAndIntFromSecPartVIIGrp/ExclusionAmt 

    NtIncmLssFrmSpclEvt_ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetIncomeLossFromSpecialEvtGrp/ExclusionAmt 

    IntOnSvAndTmpCshInvst_RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/IntOnSavAndTempCashInvstGrp/RelatedOrExemptFunctionIncmAmt 

    FsCntrctsFrmGvtAg_RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/FeesContractsFromGovtAgGrp/RelatedOrExemptFunctionIncmAmt 

    NtIncmLssFrmSpclEvt_RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetIncomeLossFromSpecialEvtGrp/RelatedOrExemptFunctionIncmAmt 

    OthrInvstmntIncmPrtVII_RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherInvestmentIncmPartVIIGrp/RelatedOrExemptFunctionIncmAmt 

    DvAndIntFrmScPrtVII_RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/DivAndIntFromSecPartVIIGrp/RelatedOrExemptFunctionIncmAmt 

    NtRntlIncmPrsnlPrp_RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRentalIncomePersonalPropGrp/RelatedOrExemptFunctionIncmAmt 

    GrssPrftLssSlsOfInvntry_RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GrossProfitLossSlsOfInvntryGrp/RelatedOrExemptFunctionIncmAmt 

    GnSlsAstOthThnInvntry_RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GainSalesAstOthThanInvntryGrp/RelatedOrExemptFunctionIncmAmt 

    NtRntlIncmRNtDbtFncdPrp_RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReNotDebtFincdProp/RelatedOrExemptFunctionIncmAmt 

    NtRntlIncmRDbtFncdPrp_RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReDebtFincdPropGrp/RelatedOrExemptFunctionIncmAmt 

    MmbrshpDsAndAssmnt_RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/MembershipDuesAndAssmntGrp/RelatedOrExemptFunctionIncmAmt 

#######
#
# IRS990PF - PF Part XVI-B Relationship of Activities to the Accomplishment of Exempt Purposes 
#
#######

class pf_part_xvib(Base):
    __tablename__='pf_part_xvib'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    RlnOfActyTAccmOfExmptPrps = Column(Text)
    # xpath: /IRS990PF/RlnOfActyToAccomOfExmptPrpsGrp 

#######
#
# IRS990PF - PF Part XVII Transfers, Transactions Relationships With Noncharitable Exempt Organizations 
#
#######

class pf_part_xvii(Base):
    __tablename__='pf_part_xvii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    TrnsfrTrnsRlnNnchrtblEO = Column(Text)
    # xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp 

    TrnsfrOfCshTNnchrtblEOInd = Column(String(length=5))
    # Line number:  Part XVII Line 1a(1)  Description:  Transfers of cash to noncharitable EO  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TrnsfrOfCashToNonchrtblEOInd 

    TrnsfrOthrAsstNnchrtblEOInd = Column(String(length=5))
    # Line number:  Part XVII Line 1a(2)  Description:  Transfers of other assets to noncharitable EO  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TrnsfrOtherAssetNonchrtblEOInd 

    SlsOrExchngsOfAsstsInd = Column(String(length=5))
    # Line number:  Part XVII Line 1b(1)  Description:  Other transactions : Sales or exchanges of assets with a noncharitable exempt organization  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/SalesOrExchangesOfAssetsInd 

    PrchsOfAsstsNnchrtblEOInd = Column(String(length=5))
    # Line number:  Part XVII Line 1b(2)  Description:  Other transactions : Purchases of assets from a noncharitable exempt organization  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/PurchaseOfAssetsNonchrtblEOInd 

    RntlOfFcltsOthAsstsInd = Column(String(length=5))
    # Line number:  Part XVII Line 1b(3)  Description:  Other transactions : Rental of facilities, equipment, or other assets  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/RentalOfFacilitiesOthAssetsInd 

    RmbrsmntArrngmntsInd = Column(String(length=5))
    # Line number:  Part XVII Line 1b(4)  Description:  Other transactions : Reimbursement arrangements  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/ReimbursementArrangementsInd 

    LnsOrLnGrntsInd = Column(String(length=5))
    # Line number:  Part XVII Line 1b(5)  Description:  Other transactions : Loans or loan guarantees  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/LoansOrLoanGuaranteesInd 

    PrfrmncOfSrvcsEtcInd = Column(String(length=5))
    # Line number:  Part XVII Line 1b(6)  Description:  Other transactions : Performance of Services or membership or fundraising solicitations  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/PerformanceOfServicesEtcInd 

    ShrngOfFcltsEtcInd = Column(String(length=5))
    # Line number:  Part XVII Line 1c  Description:  Other transactions : Sharing of facilities, equipment, mailing lists, other assets, or paid employees  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/SharingOfFacilitiesEtcInd 

    RltnshpsNnchrtblEOInd = Column(String(length=5))
    # Line number:  Part XVII Line 2a  Description:  Relationships with noncharitable EOs  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/RelationshipsNonchrtblEOInd 

#######
#
# IRS990PF - OrgReportOrRegisterStateCd
# A repeating structure from PF Part VII-A Statements Regarding Activities 
#
#######

class PFOrgRprtOrRgstrSttCd(Base):
    __tablename__='PFOrgRprtOrRgstrSttCd'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    OrgRprtOrRgstrSttCd = Column(String(length=2))
    # Line number:  Part VII-A Line 8a  Description:  States Filed With  xpath: /IRS990PF/StatementsRegardingActyGrp/OrgReportOrRegisterStateCd 

#######
#
# IRS990PF - OfficerDirTrstKeyEmplGrp
# A repeating structure from PF Part VIII Compensation 
#
#######

class PFOffcrDrTrstKyEmpl(Base):
    __tablename__='PFOffcrDrTrstKyEmpl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    OffcrDrTrstKyEmplInf_OffcrDrTrstKyEmpl = Column(Text)
    # Line number:  Part VIII Line 1  Description:  Officer, Director, Trustee, or Key Employee  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp 

    OffcrDrTrstKyEmpl_PrsnNm = Column(Text)
    # Line number:  Part VIII Line 1(a)  Description:  Person Name  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/PersonNm 

    OffcrDrTrstKyEmpl_BsnssNm = Column(Text)
    # Line number:  Part VIII Line 1(a)  Description:  Business Name  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/BusinessName 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part VIII Line 1(a)  Description:  State  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part VIII Line 1(a)  Description:  ZIP code  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/USAddress/ZIPCd 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VIII Line 1(a)  Description:  Address line 1  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VIII Line 1(a)  Description:  Address line 2  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part VIII Line 1(a)  Description:  City  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/USAddress/CityNm 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VIII Line 1(a)  Description:  Address line 1  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VIII Line 1(a)  Description:  Address line 2  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part VIII Line 1(a)  Description:  City  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ForeignAddress/CityNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part VIII Line 1(a)  Description:  Country  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part VIII Line 1(a)  Description:  Postal code  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ForeignAddress/ForeignPostalCd 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part VIII Line 1(a)  Description:  Province or state  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ForeignAddress/ProvinceOrStateNm 

    OffcrDrTrstKyEmpl_TtlTxt = Column(String(length=100))
    # Line number:  Part VIII Line 1(b)  Description:  Title  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/TitleTxt 

    OffcrDrTrstKyEmpl_AvrgHrsPrWkDvtdTPsRt = Column(Text)
    # Line number:  Part VIII Line 1(b)  Description:  Average Hours per week devoted to position  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/AverageHrsPerWkDevotedToPosRt 

    OffcrDrTrstKyEmpl_CmpnstnAmt = Column(BigInteger)
    # Line number:  Part VIII Line 1(c)  Description:  Compensation  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/CompensationAmt 

    OffcrDrTrstKyEmpl_EmplyBnftPrgrmAmt = Column(BigInteger)
    # Line number:  Part VIII Line 1(d)  Description:  Contributions to employee benefit plans and deferred compensation  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/EmployeeBenefitProgramAmt 

    OffcrDrTrstKyEmpl_ExpnsAccntOthrAllwncAmt = Column(BigInteger)
    # Line number:  Part VIII Line 1(e)  Description:  Expense account and other allowances  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ExpenseAccountOtherAllwncAmt 

#######
#
# IRS990PF - GrantOrContributionPdDurYrGrp
# A repeating structure from PF Part XV Supplementary Information 
#
#######

class PFGrntOrCntrbtnPdDrYr(Base):
    __tablename__='PFGrntOrCntrbtnPdDrYr'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    GrntOrCntrbtnPdDrYr_RcpntPrsnNm = Column(String(length=35))
    # Line number:  Part XV Line 3a  Description:  Recipient Person Name  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientPersonNm 

    RcpntBsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part XV Line 3a  Description:  Business name line 1  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientBusinessName/BusinessNameLine1Txt 

    RcpntBsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part XV Line 3a  Description:  Business name line 2  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientBusinessName/BusinessNameLine2Txt 

    RcpntUSAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part XV Line 3a  Description:  ZIP code  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientUSAddress/ZIPCd 

    RcpntUSAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part XV Line 3a  Description:  Address line 1  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientUSAddress/AddressLine1Txt 

    RcpntUSAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part XV Line 3a  Description:  Address line 2  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientUSAddress/AddressLine2Txt 

    RcpntUSAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part XV Line 3a  Description:  City  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientUSAddress/CityNm 

    RcpntUSAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part XV Line 3a  Description:  State  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientUSAddress/StateAbbreviationCd 

    RcpntFrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part XV Line 3a  Description:  City  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientForeignAddress/CityNm 

    RcpntFrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part XV Line 3a  Description:  Postal code  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientForeignAddress/ForeignPostalCd 

    RcpntFrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part XV Line 3a  Description:  Province or state  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientForeignAddress/ProvinceOrStateNm 

    RcpntFrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part XV Line 3a  Description:  Address line 2  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientForeignAddress/AddressLine2Txt 

    RcpntFrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part XV Line 3a  Description:  Address line 1  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientForeignAddress/AddressLine1Txt 

    RcpntFrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part XV Line 3a  Description:  Country  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientForeignAddress/CountryCd 

    GrntOrCntrbtnPdDrYr_RcpntRltnshpTxt = Column(String(length=100))
    # Line number:  Part XV Line 3a  Description:  Recipient Relationship to Foundation Manager or Substantial Contributor  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientRelationshipTxt 

    GrntOrCntrbtnPdDrYr_RcpntFndtnSttsTxt = Column(String(length=20))
    # Line number:  Part XV Line 3a  Description:  Recipient's Foundation Status  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientFoundationStatusTxt 

    GrntOrCntrbtnPdDrYr_GrntOrCntrbtnPrpsTxt = Column(Text)
    # Line number:  Part XV Line 3a  Description:  Purpose of Grant or Contribution  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/GrantOrContributionPurposeTxt 

    GrntOrCntrbtnPdDrYr_Amt = Column(BigInteger)
    # Line number:  Part XV Line 3a  Description:  Amount  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/Amt 

#######
#
# IRS990PF - TransferScheduleDetail
# A repeating structure from PF Part XVII Transfers, Transactions Relationships With Noncharitable Exempt Organizations 
#
#######

class PFTrnsfrSkdDtl(Base):
    __tablename__='PFTrnsfrSkdDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    LnNmbrTxt = Column(Text)
    # Line number:  Part XVII Line 1d Column (a)  Description:  Line number  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TransferScheduleDetail/LineNumberTxt 

    InvlvdAmt = Column(BigInteger)
    # Line number:  Part XVII Line 1d Column (b)  Description:  Amount involved  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TransferScheduleDetail/InvolvedAmt 

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part XVII Line 1d Column (c)  Description:  Business name line 1  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TransferScheduleDetail/NoncharitableExemptOrgName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part XVII Line 1d Column (c)  Description:  Business name line 2  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TransferScheduleDetail/NoncharitableExemptOrgName/BusinessNameLine2Txt 

    TrnsfrsTrnsAndShrArrngmDsc = Column(Text)
    # Line number:  Part XVII Line 1d Column (d)  Description:  Description of transfers, transactions, and sharing arrangements  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TransferScheduleDetail/TransfersTransAndShrArrngmDesc 

#######
#
# IRS990PF - ShareholderManagerNm
# A repeating structure from PF Part XV Supplementary Information 
#
#######

class PFShrhldrMngrNm(Base):
    __tablename__='PFShrhldrMngrNm'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    ShrhldrMngrNm = Column(String(length=35))
    # Line number:  Part XV Line 1b  Description:  Shareholder Manager  xpath: /IRS990PF/SupplementaryInformationGrp/ShareholderManagerNm 

#######
#
# IRS990PF - CompensationHighestPaidEmplGrp
# A repeating structure from PF Part VIII Compensation 
#
#######

class PFCmpnstnHghstPdEmpl(Base):
    __tablename__='PFCmpnstnHghstPdEmpl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    OffcrDrTrstKyEmplInf_CmpnstnHghstPdEmpl = Column(Text)
    # Line number:  Part VIII Line 2  Description:  Compensation of the five highest paid employees other than officers, directors, and trustees  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp 

    CmpnstnHghstPdEmpl_PrsnNm = Column(Text)
    # Line number:  Part VIII Line 2(a)  Description:  Highest paid employee's name  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/PersonNm 

    CmpnstnHghstPdEmpl_TtlTxt = Column(String(length=20))
    # Line number:  Part VIII Line 2(b)  Description:  Title  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/TitleTxt 

    CmpnstnHghstPdEmpl_AvrgHrsPrWkDvtdTPsRt = Column(Text)
    # Line number:  Part VIII Line 2(b)  Description:  Average hours per week  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/AverageHrsPerWkDevotedToPosRt 

    CmpnstnHghstPdEmpl_CmpnstnAmt = Column(BigInteger)
    # Line number:  Part VIII Line 2(c)  Description:  Compensation  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/CompensationAmt 

    CmpnstnHghstPdEmpl_EmplyBnftsAmt = Column(BigInteger)
    # Line number:  Part VIII Line 2(d)  Description:  Employee benefits  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/EmployeeBenefitsAmt 

    CmpnstnHghstPdEmpl_ExpnsAccntAmt = Column(BigInteger)
    # Line number:  Part VIII Line 2(e)  Description:  Expense Account  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ExpenseAccountAmt 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part VIII Line 2(a)  Description:  ZIP code  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/USAddress/ZIPCd 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VIII Line 2(a)  Description:  Address line 1  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VIII Line 2(a)  Description:  Address line 2  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part VIII Line 2(a)  Description:  City  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part VIII Line 2(a)  Description:  State  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/USAddress/StateAbbreviationCd 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part VIII Line 2(a)  Description:  Province or state  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part VIII Line 2(a)  Description:  Postal code  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ForeignAddress/ForeignPostalCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VIII Line 2(a)  Description:  Address line 1  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VIII Line 2(a)  Description:  Address line 2  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part VIII Line 2(a)  Description:  Country  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ForeignAddress/CountryCd 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part VIII Line 2(a)  Description:  City  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ForeignAddress/CityNm 

#######
#
# IRS990PF - OtherRevenueDescribedGrp
# A repeating structure from PF Part XVI-A Analysis of Income-Producing Activities 
#
#######

class PFOthrRvnDscrbd(Base):
    __tablename__='PFOthrRvnDscrbd'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Dsc = Column(String(length=100))
    # Line number:  Part XVI-A Line 11  Description:  Description  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherRevenueDescribedGrp/Desc 

    BsnssCd = Column(Text)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherRevenueDescribedGrp/BusinessCd 

    UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherRevenueDescribedGrp/UnrelatedBusinessTaxblIncmAmt 

    ExclsnCd = Column(Text)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherRevenueDescribedGrp/ExclusionCd 

    ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherRevenueDescribedGrp/ExclusionAmt 

    RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherRevenueDescribedGrp/RelatedOrExemptFunctionIncmAmt 

#######
#
# IRS990PF - SpecialConditionDesc
# A repeating structure from PF Part 0 Prefatory material 
#
#######

class PFSpclCndtnDsc(Base):
    __tablename__='PFSpclCndtnDsc'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpclCndtnDsc = Column(Text)
    # Description:  Special condition description  xpath: /IRS990PF/SpecialConditionDesc 

#######
#
# IRS990PF - ApplicationSubmissionInfoGrp
# A repeating structure from PF Part XV Supplementary Information 
#
#######

class PFApplctnSbmssnInf(Base):
    __tablename__='PFApplctnSbmssnInf'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntryInfrmtn_ApplctnSbmssnInf = Column(Text)
    # xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp 

    ApplctnSbmssnInf_RcpntPrsnNm = Column(String(length=35))
    # Line number:  Part XV Line 2a  Description:  Name of Person to Receive Applications  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientPersonNm 

    ApplctnSbmssnInf_RcpntPhnNm = Column(String(length=10))
    # Line number:  Part XV Line 2a  Description:  Phone Number of Person to Receive Applications  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientPhoneNum 

    ApplctnSbmssnInf_RcpntEmlAddrssTxt = Column(String(length=100))
    # Line number:  Part XV Line 2a  Description:  Recipient Email Address  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientEmailAddressTxt 

    ApplctnSbmssnInf_FrmAndInfAndMtrlsTxt = Column(Text)
    # Line number:  Part XV Line 2b  Description:  Form and Information and Materials To Include  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/FormAndInfoAndMaterialsTxt 

    ApplctnSbmssnInf_SbmssnDdlnsTxt = Column(String(length=100))
    # Line number:  Part XV Line 2c  Description:  Subsmission Deadlines  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/SubmissionDeadlinesTxt 

    ApplctnSbmssnInf_RstrctnsOnAwrdsTxt = Column(Text)
    # Line number:  Part XV Line 2d  Description:  Restrictions on Awards  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RestrictionsOnAwardsTxt 

    RcpntUSAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part XV Line 2a  Description:  Address line 2  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientUSAddress/AddressLine2Txt 

    RcpntUSAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part XV Line 2a  Description:  City  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientUSAddress/CityNm 

    RcpntUSAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part XV Line 2a  Description:  State  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientUSAddress/StateAbbreviationCd 

    RcpntUSAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part XV Line 2a  Description:  ZIP code  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientUSAddress/ZIPCd 

    RcpntUSAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part XV Line 2a  Description:  Address line 1  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientUSAddress/AddressLine1Txt 

    RcpntFrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part XV Line 2a  Description:  City  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientForeignAddress/CityNm 

    RcpntFrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part XV Line 2a  Description:  Address line 1  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientForeignAddress/AddressLine1Txt 

    RcpntFrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part XV Line 2a  Description:  Country  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientForeignAddress/CountryCd 

    RcpntFrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part XV Line 2a  Description:  Postal code  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientForeignAddress/ForeignPostalCd 

    RcpntFrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part XV Line 2a  Description:  Province or state  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientForeignAddress/ProvinceOrStateNm 

    RcpntFrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part XV Line 2a  Description:  Address line 2  xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientForeignAddress/AddressLine2Txt 

#######
#
# IRS990PF - CompensationOfHghstPdCntrctGrp
# A repeating structure from PF Part VIII Compensation 
#
#######

class PFCmpnstnOfHghstPdCntrct(Base):
    __tablename__='PFCmpnstnOfHghstPdCntrct'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    OffcrDrTrstKyEmplInf_CmpnstnOfHghstPdCntrct = Column(Text)
    # Line number:  Part VIII Line 3  Description:  Compensation of the five highest paid independent contractors for professional services  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp 

    CmpnstnOfHghstPdCntrct_BsnssNm = Column(Text)
    # Line number:  Part VIII Line 3(a)  Description:  Highest paid contractor's name - Business  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/BusinessName 

    CmpnstnOfHghstPdCntrct_PrsnNm = Column(Text)
    # Line number:  Part VIII Line 3(a)  Description:  Highest paid contractor's name - Person  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/PersonNm 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part VIII Line 3(a)  Description:  ZIP code  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/USAddress/ZIPCd 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part VIII Line 3(a)  Description:  City  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/USAddress/CityNm 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VIII Line 3(a)  Description:  Address line 2  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/USAddress/AddressLine2Txt 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VIII Line 3(a)  Description:  Address line 1  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/USAddress/AddressLine1Txt 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part VIII Line 3(a)  Description:  State  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/USAddress/StateAbbreviationCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part VIII Line 3(a)  Description:  Postal code  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ForeignAddress/ForeignPostalCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VIII Line 3(a)  Description:  Address line 1  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part VIII Line 3(a)  Description:  City  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ForeignAddress/CityNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part VIII Line 3(a)  Description:  Country  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ForeignAddress/CountryCd 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VIII Line 3(a)  Description:  Address line 2  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part VIII Line 3(a)  Description:  Province or state  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ForeignAddress/ProvinceOrStateNm 

    CmpnstnOfHghstPdCntrct_SrvcTxt = Column(String(length=100))
    # Line number:  Part VIII Line 3(b)  Description:  Type of service  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ServiceTypeTxt 

    CmpnstnOfHghstPdCntrct_CmpnstnAmt = Column(BigInteger)
    # Line number:  Part VIII Line 3(c)  Description:  Compensation  xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/CompensationAmt 

#######
#
# IRS990PF - RelationshipScheduleDetail
# A repeating structure from PF Part XVII Transfers, Transactions Relationships With Noncharitable Exempt Organizations 
#
#######

class PFRltnshpSkdDtl(Base):
    __tablename__='PFRltnshpSkdDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part XVII Line 2b Column (a)  Description:  Business name line 1  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/RelationshipScheduleDetail/OrganizationBusinessName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part XVII Line 2b Column (a)  Description:  Business name line 2  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/RelationshipScheduleDetail/OrganizationBusinessName/BusinessNameLine2Txt 

    OrgnztnDsc = Column(String(length=20))
    # Line number:  Part XVII Line 2b Column (b)  Description:  Type of organization  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/RelationshipScheduleDetail/OrganizationTypeDesc 

    RltnshpDscrptnTxt = Column(Text)
    # Line number:  Part XVII Line 2b Column (c)  Description:  Description of relationship  xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/RelationshipScheduleDetail/RelationshipDescriptionTxt 

#######
#
# IRS990PF - ContributingManagerNm
# A repeating structure from PF Part XV Supplementary Information 
#
#######

class PFCntrbtngMngrNm(Base):
    __tablename__='PFCntrbtngMngrNm'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    CntrbtngMngrNm = Column(String(length=35))
    # Line number:  Part XV Line 1a  Description:  Contributing Manager  xpath: /IRS990PF/SupplementaryInformationGrp/ContributingManagerNm 

#######
#
# IRS990PF - RlnOfActyToAccomOfExmptPrpsGrp
# A repeating structure from PF Part XVI-B Relationship of Activities to the Accomplishment of Exempt Purposes 
#
#######

class PFRlnOfActyTAccmOfExmptPrps(Base):
    __tablename__='PFRlnOfActyTAccmOfExmptPrps'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    RlnOfActyTAccmOfExmptPrps = Column(Text)
    # Line number:  Part XVI-B  Description:  Relationship of activities to the accomplishment of exempt purposes  xpath: /IRS990PF/RlnOfActyToAccomOfExmptPrpsGrp/RlnOfActyToAccomOfExmptPrpsGrp 

    LnNmbrTxt = Column(Text)
    # Line number:  Part XVI-B  Description:  Line number  xpath: /IRS990PF/RlnOfActyToAccomOfExmptPrpsGrp/RlnOfActyToAccomOfExmptPrpsGrp/LineNumberTxt 

    RltnshpSttmntTxt = Column(Text)
    # Line number:  Part XVI-B  Description:  Relationship statement  xpath: /IRS990PF/RlnOfActyToAccomOfExmptPrpsGrp/RlnOfActyToAccomOfExmptPrpsGrp/RelationshipStatementTxt 

#######
#
# IRS990PF - ProgramServiceRevPartVIIGrp
# A repeating structure from PF Part XVI-A Analysis of Income-Producing Activities 
#
#######

class PFPrgrmSrvcRvPrtVII(Base):
    __tablename__='PFPrgrmSrvcRvPrtVII'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Dsc = Column(String(length=100))
    # Line number:  Part XVI-A Line 1  Description:  Description  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/ProgramServiceRevPartVIIGrp/Desc 

    BsnssCd = Column(Text)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/ProgramServiceRevPartVIIGrp/BusinessCd 

    UnrltdBsnssTxblIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/ProgramServiceRevPartVIIGrp/UnrelatedBusinessTaxblIncmAmt 

    ExclsnCd = Column(Text)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/ProgramServiceRevPartVIIGrp/ExclusionCd 

    ExclsnAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/ProgramServiceRevPartVIIGrp/ExclusionAmt 

    RltdOrExmptFnctnIncmAmt = Column(BigInteger)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/ProgramServiceRevPartVIIGrp/RelatedOrExemptFunctionIncmAmt 

#######
#
# IRS990PF - ForeignCountryCd
# A repeating structure from PF Part VII-A Statements Regarding Activities 
#
#######

class PFFrgnCntryCd(Base):
    __tablename__='PFFrgnCntryCd'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    FrgnCntryCd = Column(String(length=2))
    # Line number:  Part VII-A Line 16  Description:  Name of foreign country  xpath: /IRS990PF/StatementsRegardingActyGrp/ForeignCountryCd 

#######
#
# IRS990PF - GrantOrContriApprvForFutGrp
# A repeating structure from PF Part XV Supplementary Information 
#
#######

class PFGrntOrCntrApprvFrFt(Base):
    __tablename__='PFGrntOrCntrApprvFrFt'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    GrntOrCntrApprvFrFt_RcpntPrsnNm = Column(String(length=35))
    # Line number:  Part XV Line 3b  Description:  Recipient Person Name  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientPersonNm 

    RcpntBsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part XV Line 3b  Description:  Business name line 1  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientBusinessName/BusinessNameLine1Txt 

    RcpntBsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part XV Line 3b  Description:  Business name line 2  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientBusinessName/BusinessNameLine2Txt 

    RcpntUSAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part XV Line 3b  Description:  State  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientUSAddress/StateAbbreviationCd 

    RcpntUSAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part XV Line 3b  Description:  ZIP code  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientUSAddress/ZIPCd 

    RcpntUSAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part XV Line 3b  Description:  Address line 1  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientUSAddress/AddressLine1Txt 

    RcpntUSAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part XV Line 3b  Description:  Address line 2  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientUSAddress/AddressLine2Txt 

    RcpntUSAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part XV Line 3b  Description:  City  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientUSAddress/CityNm 

    RcpntFrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part XV Line 3b  Description:  Address line 2  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientForeignAddress/AddressLine2Txt 

    RcpntFrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part XV Line 3b  Description:  Country  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientForeignAddress/CountryCd 

    RcpntFrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part XV Line 3b  Description:  Postal code  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientForeignAddress/ForeignPostalCd 

    RcpntFrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part XV Line 3b  Description:  Province or state  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientForeignAddress/ProvinceOrStateNm 

    RcpntFrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part XV Line 3b  Description:  Address line 1  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientForeignAddress/AddressLine1Txt 

    RcpntFrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part XV Line 3b  Description:  City  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientForeignAddress/CityNm 

    GrntOrCntrApprvFrFt_RcpntRltnshpTxt = Column(String(length=100))
    # Line number:  Part XV Line 3b  Description:  Recipient Relationship to Foundation Manager or Substantial Contributor  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientRelationshipTxt 

    GrntOrCntrApprvFrFt_RcpntFndtnSttsTxt = Column(String(length=20))
    # Line number:  Part XV Line 3b  Description:  Recipient's Foundation Status  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientFoundationStatusTxt 

    GrntOrCntrApprvFrFt_GrntOrCntrbtnPrpsTxt = Column(Text)
    # Line number:  Part XV Line 3b  Description:  Purpose of Grant or Contribution  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/GrantOrContributionPurposeTxt 

    GrntOrCntrApprvFrFt_Amt = Column(BigInteger)
    # Line number:  Part XV Line 3b  Description:  Amount  xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/Amt 

#######
#
# IRS990PF - CapGainsLossTxInvstIncmGrp
# A repeating structure from PF Part IV Capital Gains and Losses for Tax on Investment Income 
#
#######

class PFCpGnsLssTxInvstIncm(Base):
    __tablename__='PFCpGnsLssTxInvstIncm'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    CpGnsLssTxInvstIncm = Column(Text)
    # xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp 

    PrprtyDsc = Column(String(length=100))
    # Line number:  Part IV Line 1(a)  Description:  Description of Asset  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/PropertyDesc 

    HwAcqrdCd = Column(Text)
    # Line number:  Part IV Line 1(b)  Description:  How Acquired  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/HowAcquiredCd 

    AcqrdDt = Column(String(length=31))
    # Line number:  Part IV Line 1(c)  Description:  Date Acquired  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/AcquiredDt 

    SldDt = Column(String(length=31))
    # Line number:  Part IV Line 1(d)  Description:  Date Sold  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/SoldDt 

    GrssSlsPrcAmt = Column(BigInteger)
    # Line number:  Part IV Line 1(e)  Description:  Gross Sales Price  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/GrossSalesPriceAmt 

    DprctnAmt = Column(BigInteger)
    # Line number:  Part IV Line 1(f)  Description:  Depreciation  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/DepreciationAmt 

    CstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part IV Line 1(g)  Description:  Cost or Other Basis  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/CostOrOtherBasisAmt 

    GnOrLssAmt = Column(BigInteger)
    # Line number:  Part IV Line 1(h)  Description:  Gain or Loss  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/GainOrLossAmt 

    FMVAsOf123169Amt = Column(BigInteger)
    # Line number:  Part IV Line 1(i)  Description:  FMV as of 12/31/69  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/FMVAsOf123169Amt 

    AdjstdBssAsOf123169Amt = Column(BigInteger)
    # Line number:  Part IV Line 1(j)  Description:  Adjusted Basis as of 12/31/69  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/AdjustedBasisAsOf123169Amt 

    ExcssFMVOvrAdjstdBssAmt = Column(BigInteger)
    # Line number:  Part IV Line 1(k)  Description:  Excess of FMV Over Adjusted Basis  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/ExcessFMVOverAdjustedBssAmt 

    GnsMnsExcssOrLsssAmt = Column(BigInteger)
    # Line number:  Part IV Line 1(l)  Description:  Gains Minus Excess or Losses  xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/GainsMinusExcessOrLossesAmt 

#######
#
# IRS990ScheduleA - ScheduleA Part I Reason for Non-Private Foundation Status 
#
#######

class skeda_part_i(Base):
    __tablename__='skeda_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    ChrchInd = Column(String(length=1))
    # Line number:  Part I Line 1  Description:  A church, convention of churches, or association of churches. Section 170(b)(1)(A)(i)  xpath: /IRS990ScheduleA/ChurchInd 

    SchlInd = Column(String(length=1))
    # Line number:  Part I Line 2  Description:  A school. Section 170(b)(1)(A)(ii)  xpath: /IRS990ScheduleA/SchoolInd 

    HsptlInd = Column(String(length=1))
    # Line number:  Part I Line 3  Description:  A hospital or a cooperative hospital service organization. Section 170(b)(1)(A)(iii)  xpath: /IRS990ScheduleA/HospitalInd 

    CllgOrgnztnInd = Column(String(length=1))
    # Line number:  Part I Line 5  Description:  An organization operated for the benefit of a college or university owned or operated by a governmental unit. Section 170(b)(1)(A)(iv).  xpath: /IRS990ScheduleA/CollegeOrganizationInd 

    GvrnmntlUntInd = Column(String(length=1))
    # Line number:  Part I Line 6  Description:  A Federal, state, or local government or governmental unit. Section 170(b)(1)(A)(v)  xpath: /IRS990ScheduleA/GovernmentalUnitInd 

    PblcOrgnztn170Ind = Column(String(length=1))
    # Line number:  Part I Line 7  Description:  An organization that normally receives a substantial part of its support from a governmental unit or from the general public. 			Section 170(b)(1)(A)(vi)  xpath: /IRS990ScheduleA/PublicOrganization170Ind 

    CmmntyTrstInd = Column(String(length=1))
    # Line number:  Part I Line 8  Description:  A community trust. Section 170(b)(1)(A)(vi)  xpath: /IRS990ScheduleA/CommunityTrustInd 

    PblclySpprtdOrg5092Ind = Column(String(length=1))
    # Line number:  Part I Line 9  Description:  Publicly supported organization 509(a)(2)  xpath: /IRS990ScheduleA/PubliclySupportedOrg509a2Ind 

    TstPblcSftyInd = Column(String(length=1))
    # Line number:  Part I Line 10  Description:  An organization organized and operated to test for public safety. Section 509(a)(4)  xpath: /IRS990ScheduleA/TestPublicSafetyInd 

    MdclRsrchOrgnztnInd = Column(String(length=1))
    # Line number:  Part I Line 4  Description:  A medical research organization operated in conjunction with a hospital. Section 170(b)(1)(A)(iii)  xpath: /IRS990ScheduleA/MedicalResearchOrganizationInd 

    SpprtngOrgnztn5093Ind = Column(String(length=1))
    # Line number:  Part I Line 11  Description:  Supporting organization 509(a)(3)  xpath: /IRS990ScheduleA/SupportingOrganization509a3Ind 

    SpprtngOrg1Ind = Column(String(length=1))
    # Line number:  Part I Line 11a  Description:  Supporting organization 509(a)(3) - Type 1  xpath: /IRS990ScheduleA/SupportingOrgType1Ind 

    SpprtngOrg2Ind = Column(String(length=1))
    # Line number:  Part I Line 11b  Description:  Supporting organization 509(a)(3) - Type 2  xpath: /IRS990ScheduleA/SupportingOrgType2Ind 

    SpprtngOrg3FncIntInd = Column(String(length=1))
    # Line number:  Part I Line 11c  Description:  Supporting organization 509(a)(3) - Type 3 functionally integrated  xpath: /IRS990ScheduleA/SupportingOrgType3FuncIntInd 

    SpprtngOrg3NnFncInd = Column(String(length=1))
    # Line number:  Part I Line 11d  Description:  Supporting organization 509(a)(3) - Type 3 Non-functionally integrated  xpath: /IRS990ScheduleA/SupportingOrgType3NonFuncInd 

    IRSWrttnDtrmntnInd = Column(String(length=1))
    # Line number:  Part I Line 11e  Description:  Does the organization have a written determination from the IRS that it is a Type I, Type II or Type III supporting organization?  xpath: /IRS990ScheduleA/IRSWrittenDeterminationInd 

    SpprtdOrgnztnsCnt = Column(BigInteger)
    # Line number:  Part I Line 11f  Description:  Number of supported organizations  xpath: /IRS990ScheduleA/SupportedOrganizationsCnt 

    SpprtdOrgnztnsTtlCnt = Column(BigInteger)
    # Line number:  Part I Line 11g(i), Total  Description:  Total number of supported organizations  xpath: /IRS990ScheduleA/SupportedOrganizationsTotalCnt 

    SpprtSmAmt = Column(BigInteger)
    # Line number:  Part I Line 11g(v), Total  Description:  Sum of amounts of support  xpath: /IRS990ScheduleA/SupportSumAmt 

    OthrSpprtSmAmt = Column(BigInteger)
    # Line number:  Part I Line 11g(vi) Total  Description:  Sum of amounts of other support  xpath: /IRS990ScheduleA/OtherSupportSumAmt 

#######
#
# IRS990ScheduleA - ScheduleA Part II Support Schedule for Organizations described in IRC 170(b)(1)(A)(iv) and 170(b)(1)(A)(vi) 
#
#######

class skeda_part_ii(Base):
    __tablename__='skeda_part_ii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    GftsGrntsCntrRcvd170_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/GiftsGrantsContriRcvd170Grp/CurrentTaxYearMinus4YearsAmt 

    GftsGrntsCntrRcvd170_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/GiftsGrantsContriRcvd170Grp/CurrentTaxYearMinus3YearsAmt 

    GftsGrntsCntrRcvd170_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/GiftsGrantsContriRcvd170Grp/CurrentTaxYearMinus2YearsAmt 

    GftsGrntsCntrRcvd170_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/GiftsGrantsContriRcvd170Grp/CurrentTaxYearMinus1YearAmt 

    GftsGrntsCntrRcvd170_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/GiftsGrantsContriRcvd170Grp/CurrentTaxYearAmt 

    GftsGrntsCntrRcvd170_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/GiftsGrantsContriRcvd170Grp/TotalAmt 

    TxRvLvdOrgnztnlBnft170_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft170Grp/CurrentTaxYearMinus4YearsAmt 

    TxRvLvdOrgnztnlBnft170_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft170Grp/CurrentTaxYearMinus3YearsAmt 

    TxRvLvdOrgnztnlBnft170_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft170Grp/CurrentTaxYearMinus2YearsAmt 

    TxRvLvdOrgnztnlBnft170_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft170Grp/CurrentTaxYearMinus1YearAmt 

    TxRvLvdOrgnztnlBnft170_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft170Grp/CurrentTaxYearAmt 

    TxRvLvdOrgnztnlBnft170_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft170Grp/TotalAmt 

    GvtFrnSrvcFcltsVl170_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl170Grp/CurrentTaxYearMinus4YearsAmt 

    GvtFrnSrvcFcltsVl170_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl170Grp/CurrentTaxYearMinus3YearsAmt 

    GvtFrnSrvcFcltsVl170_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl170Grp/CurrentTaxYearMinus2YearsAmt 

    GvtFrnSrvcFcltsVl170_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl170Grp/CurrentTaxYearMinus1YearAmt 

    GvtFrnSrvcFcltsVl170_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl170Grp/CurrentTaxYearAmt 

    GvtFrnSrvcFcltsVl170_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl170Grp/TotalAmt 

    TtlClndrYr170_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/TotalCalendarYear170Grp/CurrentTaxYearMinus4YearsAmt 

    TtlClndrYr170_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/TotalCalendarYear170Grp/CurrentTaxYearMinus3YearsAmt 

    TtlClndrYr170_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/TotalCalendarYear170Grp/CurrentTaxYearMinus2YearsAmt 

    TtlClndrYr170_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/TotalCalendarYear170Grp/CurrentTaxYearMinus1YearAmt 

    TtlClndrYr170_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/TotalCalendarYear170Grp/CurrentTaxYearAmt 

    TtlClndrYr170_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/TotalCalendarYear170Grp/TotalAmt 

    SkdA_SbstntlCntrbtrsTtAmt = Column(BigInteger)
    # Line number:  Part II Line 5(f)  Description:  Amounts from substantial contributors total  xpath: /IRS990ScheduleA/SubstantialContributorsTotAmt 

    SkdA_PblcSpprtTtl170Amt = Column(BigInteger)
    # Line number:  Part II Line 6(f)  Description:  Public Support Total  xpath: /IRS990ScheduleA/PublicSupportTotal170Amt 

    GrssInvstmntIncm170_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/GrossInvestmentIncome170Grp/CurrentTaxYearMinus4YearsAmt 

    GrssInvstmntIncm170_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/GrossInvestmentIncome170Grp/CurrentTaxYearMinus3YearsAmt 

    GrssInvstmntIncm170_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/GrossInvestmentIncome170Grp/CurrentTaxYearMinus2YearsAmt 

    GrssInvstmntIncm170_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/GrossInvestmentIncome170Grp/CurrentTaxYearMinus1YearAmt 

    GrssInvstmntIncm170_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/GrossInvestmentIncome170Grp/CurrentTaxYearAmt 

    GrssInvstmntIncm170_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/GrossInvestmentIncome170Grp/TotalAmt 

    UnrltdBsnssNtIncm170_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/UnrelatedBusinessNetIncm170Grp/CurrentTaxYearMinus4YearsAmt 

    UnrltdBsnssNtIncm170_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/UnrelatedBusinessNetIncm170Grp/CurrentTaxYearMinus3YearsAmt 

    UnrltdBsnssNtIncm170_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/UnrelatedBusinessNetIncm170Grp/CurrentTaxYearMinus2YearsAmt 

    UnrltdBsnssNtIncm170_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/UnrelatedBusinessNetIncm170Grp/CurrentTaxYearMinus1YearAmt 

    UnrltdBsnssNtIncm170_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/UnrelatedBusinessNetIncm170Grp/CurrentTaxYearAmt 

    UnrltdBsnssNtIncm170_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/UnrelatedBusinessNetIncm170Grp/TotalAmt 

    OthrIncm170_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/OtherIncome170Grp/CurrentTaxYearMinus4YearsAmt 

    OthrIncm170_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/OtherIncome170Grp/CurrentTaxYearMinus3YearsAmt 

    OthrIncm170_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/OtherIncome170Grp/CurrentTaxYearMinus2YearsAmt 

    OthrIncm170_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/OtherIncome170Grp/CurrentTaxYearMinus1YearAmt 

    OthrIncm170_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/OtherIncome170Grp/CurrentTaxYearAmt 

    OthrIncm170_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/OtherIncome170Grp/TotalAmt 

    SkdA_TtlSpprtAmt = Column(BigInteger)
    # Line number:  Part II Line 11(f)  Description:  Total support  xpath: /IRS990ScheduleA/TotalSupportAmt 

    SkdA_GrssRcptsRltdActvtsAmt = Column(BigInteger)
    # Line number:  Part II Line 12  Description:  Gross receipts from admissions, merchandise sold or services performed, or furnishing of facilities in any activity that is related to the organization's tax-exempt purpose  xpath: /IRS990ScheduleA/GrossReceiptsRltdActivitiesAmt 

    SkdA_Frst5Yrs170Ind = Column(String(length=1))
    # Line number:  Part II Line 13  Description:  First five years  xpath: /IRS990ScheduleA/First5Years170Ind 

    SkdA_PblcSpprtCY170Pct = Column(Numeric(precision=6))
    # Line number:  Part II Line 14  Description:  Public support percentage (line 6 column (f) divided by line 12 column (f)  xpath: /IRS990ScheduleA/PublicSupportCY170Pct 

    SkdA_PblcSpprtPY170Pct = Column(Numeric(precision=6))
    # Line number:  Part II Line 15  Description:  Public support percentage from prior year's Schedule A, Part II, line 14  xpath: /IRS990ScheduleA/PublicSupportPY170Pct 

    SkdA_ThrtyThrPctSprtTstsCY170Ind = Column(String(length=1))
    # Line number:  Part II Line 16a  Description:  Thirty three and one third test for the current year  xpath: /IRS990ScheduleA/ThirtyThrPctSuprtTestsCY170Ind 

    SkdA_ThrtyThrPctSprtTstsPY170Ind = Column(String(length=1))
    # Line number:  Part II Line 16b  Description:  Thirty three and one third test for the prior year  xpath: /IRS990ScheduleA/ThirtyThrPctSuprtTestsPY170Ind 

    SkdA_TnPctFctsCrcmstncsTstCYInd = Column(String(length=1))
    # Line number:  Part II Line 17a  Description:  Ten percent facts and circumstances test for the current year  xpath: /IRS990ScheduleA/TenPctFactsCrcmstncsTestCYInd 

    SkdA_TnPctFctsCrcmstncsTstPYInd = Column(String(length=1))
    # Line number:  Part II Line 17b  Description:  Ten percent facts and circumstances test for the prior year  xpath: /IRS990ScheduleA/TenPctFactsCrcmstncsTestPYInd 

    SkdA_PrvtFndtn170Ind = Column(String(length=1))
    # Line number:  Part II Line 18  Description:  If the organization did not check a box on line 13, 16a, 16b, 17a or 17b, check this box and see instructions  xpath: /IRS990ScheduleA/PrivateFoundation170Ind 

#######
#
# IRS990ScheduleA - ScheduleA Part III Support Schedule for Organizations described in IRC 509(a)(2) 
#
#######

class skeda_part_iii(Base):
    __tablename__='skeda_part_iii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    GftsGrntsCntrsRcvd509_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/GiftsGrantsContrisRcvd509Grp/CurrentTaxYearMinus4YearsAmt 

    GftsGrntsCntrsRcvd509_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/GiftsGrantsContrisRcvd509Grp/CurrentTaxYearMinus3YearsAmt 

    GftsGrntsCntrsRcvd509_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/GiftsGrantsContrisRcvd509Grp/CurrentTaxYearMinus2YearsAmt 

    GftsGrntsCntrsRcvd509_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/GiftsGrantsContrisRcvd509Grp/CurrentTaxYearMinus1YearAmt 

    GftsGrntsCntrsRcvd509_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/GiftsGrantsContrisRcvd509Grp/CurrentTaxYearAmt 

    GftsGrntsCntrsRcvd509_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/GiftsGrantsContrisRcvd509Grp/TotalAmt 

    GrssRcptsAdmssns_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/GrossReceiptsAdmissionsGrp/CurrentTaxYearMinus4YearsAmt 

    GrssRcptsAdmssns_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/GrossReceiptsAdmissionsGrp/CurrentTaxYearMinus3YearsAmt 

    GrssRcptsAdmssns_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/GrossReceiptsAdmissionsGrp/CurrentTaxYearMinus2YearsAmt 

    GrssRcptsAdmssns_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/GrossReceiptsAdmissionsGrp/CurrentTaxYearMinus1YearAmt 

    GrssRcptsAdmssns_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/GrossReceiptsAdmissionsGrp/CurrentTaxYearAmt 

    GrssRcptsAdmssns_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/GrossReceiptsAdmissionsGrp/TotalAmt 

    GrssRcptsNnUnrltBs_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/GrossReceiptsNonUnrltBusGrp/CurrentTaxYearMinus4YearsAmt 

    GrssRcptsNnUnrltBs_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/GrossReceiptsNonUnrltBusGrp/CurrentTaxYearMinus3YearsAmt 

    GrssRcptsNnUnrltBs_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/GrossReceiptsNonUnrltBusGrp/CurrentTaxYearMinus2YearsAmt 

    GrssRcptsNnUnrltBs_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/GrossReceiptsNonUnrltBusGrp/CurrentTaxYearMinus1YearAmt 

    GrssRcptsNnUnrltBs_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/GrossReceiptsNonUnrltBusGrp/CurrentTaxYearAmt 

    GrssRcptsNnUnrltBs_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/GrossReceiptsNonUnrltBusGrp/TotalAmt 

    TxRvLvdOrgnztnlBnft509_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft509Grp/CurrentTaxYearMinus4YearsAmt 

    TxRvLvdOrgnztnlBnft509_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft509Grp/CurrentTaxYearMinus3YearsAmt 

    TxRvLvdOrgnztnlBnft509_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft509Grp/CurrentTaxYearMinus2YearsAmt 

    TxRvLvdOrgnztnlBnft509_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft509Grp/CurrentTaxYearMinus1YearAmt 

    TxRvLvdOrgnztnlBnft509_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft509Grp/CurrentTaxYearAmt 

    TxRvLvdOrgnztnlBnft509_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft509Grp/TotalAmt 

    GvtFrnSrvcFcltsVl509_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl509Grp/CurrentTaxYearMinus4YearsAmt 

    GvtFrnSrvcFcltsVl509_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl509Grp/CurrentTaxYearMinus3YearsAmt 

    GvtFrnSrvcFcltsVl509_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl509Grp/CurrentTaxYearMinus2YearsAmt 

    GvtFrnSrvcFcltsVl509_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl509Grp/CurrentTaxYearMinus1YearAmt 

    GvtFrnSrvcFcltsVl509_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl509Grp/CurrentTaxYearAmt 

    GvtFrnSrvcFcltsVl509_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl509Grp/TotalAmt 

    Ttl509_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/Total509Grp/CurrentTaxYearMinus4YearsAmt 

    Ttl509_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/Total509Grp/CurrentTaxYearMinus3YearsAmt 

    Ttl509_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/Total509Grp/CurrentTaxYearMinus2YearsAmt 

    Ttl509_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/Total509Grp/CurrentTaxYearMinus1YearAmt 

    Ttl509_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/Total509Grp/CurrentTaxYearAmt 

    Ttl509_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/Total509Grp/TotalAmt 

    AmntsRcvdDsqlfyPrsn_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/AmountsRcvdDsqlfyPersonGrp/CurrentTaxYearMinus4YearsAmt 

    AmntsRcvdDsqlfyPrsn_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/AmountsRcvdDsqlfyPersonGrp/CurrentTaxYearMinus3YearsAmt 

    AmntsRcvdDsqlfyPrsn_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/AmountsRcvdDsqlfyPersonGrp/CurrentTaxYearMinus2YearsAmt 

    AmntsRcvdDsqlfyPrsn_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/AmountsRcvdDsqlfyPersonGrp/CurrentTaxYearMinus1YearAmt 

    AmntsRcvdDsqlfyPrsn_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/AmountsRcvdDsqlfyPersonGrp/CurrentTaxYearAmt 

    AmntsRcvdDsqlfyPrsn_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/AmountsRcvdDsqlfyPersonGrp/TotalAmt 

    SbstntlCntrbtrsAmt_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/SubstantialContributorsAmtGrp/CurrentTaxYearMinus4YearsAmt 

    SbstntlCntrbtrsAmt_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/SubstantialContributorsAmtGrp/CurrentTaxYearMinus3YearsAmt 

    SbstntlCntrbtrsAmt_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/SubstantialContributorsAmtGrp/CurrentTaxYearMinus2YearsAmt 

    SbstntlCntrbtrsAmt_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/SubstantialContributorsAmtGrp/CurrentTaxYearMinus1YearAmt 

    SbstntlCntrbtrsAmt_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/SubstantialContributorsAmtGrp/CurrentTaxYearAmt 

    SbstntlCntrbtrsAmt_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/SubstantialContributorsAmtGrp/TotalAmt 

    SbstAndDsqlfyPrsnsTt_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/SubstAndDsqlfyPrsnsTotGrp/CurrentTaxYearMinus4YearsAmt 

    SbstAndDsqlfyPrsnsTt_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/SubstAndDsqlfyPrsnsTotGrp/CurrentTaxYearMinus3YearsAmt 

    SbstAndDsqlfyPrsnsTt_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/SubstAndDsqlfyPrsnsTotGrp/CurrentTaxYearMinus2YearsAmt 

    SbstAndDsqlfyPrsnsTt_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/SubstAndDsqlfyPrsnsTotGrp/CurrentTaxYearMinus1YearAmt 

    SbstAndDsqlfyPrsnsTt_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/SubstAndDsqlfyPrsnsTotGrp/CurrentTaxYearAmt 

    SbstAndDsqlfyPrsnsTt_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/SubstAndDsqlfyPrsnsTotGrp/TotalAmt 

    SkdA_PblcSpprtTtl509Amt = Column(BigInteger)
    # Line number:  Part III Line 8(f)  Description:  Public support total  xpath: /IRS990ScheduleA/PublicSupportTotal509Amt 

    GrssInvstmntIncm509_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/GrossInvestmentIncome509Grp/CurrentTaxYearMinus4YearsAmt 

    GrssInvstmntIncm509_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/GrossInvestmentIncome509Grp/CurrentTaxYearMinus3YearsAmt 

    GrssInvstmntIncm509_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/GrossInvestmentIncome509Grp/CurrentTaxYearMinus2YearsAmt 

    GrssInvstmntIncm509_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/GrossInvestmentIncome509Grp/CurrentTaxYearMinus1YearAmt 

    GrssInvstmntIncm509_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/GrossInvestmentIncome509Grp/CurrentTaxYearAmt 

    GrssInvstmntIncm509_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/GrossInvestmentIncome509Grp/TotalAmt 

    Pst1975UBTI_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/Post1975UBTIGrp/CurrentTaxYearMinus4YearsAmt 

    Pst1975UBTI_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/Post1975UBTIGrp/CurrentTaxYearMinus3YearsAmt 

    Pst1975UBTI_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/Post1975UBTIGrp/CurrentTaxYearMinus2YearsAmt 

    Pst1975UBTI_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/Post1975UBTIGrp/CurrentTaxYearMinus1YearAmt 

    Pst1975UBTI_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/Post1975UBTIGrp/CurrentTaxYearAmt 

    Pst1975UBTI_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/Post1975UBTIGrp/TotalAmt 

    InvstmntIncmAndUBTI_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/InvestmentIncomeAndUBTIGrp/CurrentTaxYearMinus4YearsAmt 

    InvstmntIncmAndUBTI_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/InvestmentIncomeAndUBTIGrp/CurrentTaxYearMinus3YearsAmt 

    InvstmntIncmAndUBTI_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/InvestmentIncomeAndUBTIGrp/CurrentTaxYearMinus2YearsAmt 

    InvstmntIncmAndUBTI_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/InvestmentIncomeAndUBTIGrp/CurrentTaxYearMinus1YearAmt 

    InvstmntIncmAndUBTI_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/InvestmentIncomeAndUBTIGrp/CurrentTaxYearAmt 

    InvstmntIncmAndUBTI_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/InvestmentIncomeAndUBTIGrp/TotalAmt 

    NtIncmFrmOthrUBI_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/NetIncomeFromOtherUBIGrp/CurrentTaxYearMinus4YearsAmt 

    NtIncmFrmOthrUBI_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/NetIncomeFromOtherUBIGrp/CurrentTaxYearMinus3YearsAmt 

    NtIncmFrmOthrUBI_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/NetIncomeFromOtherUBIGrp/CurrentTaxYearMinus2YearsAmt 

    NtIncmFrmOthrUBI_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/NetIncomeFromOtherUBIGrp/CurrentTaxYearMinus1YearAmt 

    NtIncmFrmOthrUBI_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/NetIncomeFromOtherUBIGrp/CurrentTaxYearAmt 

    NtIncmFrmOthrUBI_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/NetIncomeFromOtherUBIGrp/TotalAmt 

    OthrIncm509_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/OtherIncome509Grp/CurrentTaxYearMinus4YearsAmt 

    OthrIncm509_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/OtherIncome509Grp/CurrentTaxYearMinus3YearsAmt 

    OthrIncm509_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/OtherIncome509Grp/CurrentTaxYearMinus2YearsAmt 

    OthrIncm509_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/OtherIncome509Grp/CurrentTaxYearMinus1YearAmt 

    OthrIncm509_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/OtherIncome509Grp/CurrentTaxYearAmt 

    OthrIncm509_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/OtherIncome509Grp/TotalAmt 

    TtlSpprtClndrYr_CrrntTxYrMns4YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  xpath: /IRS990ScheduleA/TotalSupportCalendarYearGrp/CurrentTaxYearMinus4YearsAmt 

    TtlSpprtClndrYr_CrrntTxYrMns3YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  xpath: /IRS990ScheduleA/TotalSupportCalendarYearGrp/CurrentTaxYearMinus3YearsAmt 

    TtlSpprtClndrYr_CrrntTxYrMns2YrsAmt = Column(BigInteger)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  xpath: /IRS990ScheduleA/TotalSupportCalendarYearGrp/CurrentTaxYearMinus2YearsAmt 

    TtlSpprtClndrYr_CrrntTxYrMns1YrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  xpath: /IRS990ScheduleA/TotalSupportCalendarYearGrp/CurrentTaxYearMinus1YearAmt 

    TtlSpprtClndrYr_CrrntTxYrAmt = Column(BigInteger)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  xpath: /IRS990ScheduleA/TotalSupportCalendarYearGrp/CurrentTaxYearAmt 

    TtlSpprtClndrYr_TtlAmt = Column(BigInteger)
    # Line number:  Part II and III Column (f)  Description:  Total  xpath: /IRS990ScheduleA/TotalSupportCalendarYearGrp/TotalAmt 

    SkdA_Frst5Yrs509Ind = Column(String(length=1))
    # Line number:  Part III Line 14  Description:  First five years?  xpath: /IRS990ScheduleA/First5Years509Ind 

    SkdA_PblcSpprtCY509Pct = Column(Numeric(precision=6))
    # Line number:  Part III Line 15  Description:  Public support percentage (line 8 column(f) divided by line 13 column(f))  xpath: /IRS990ScheduleA/PublicSupportCY509Pct 

    SkdA_PblcSpprtPY509Pct = Column(Numeric(precision=6))
    # Line number:  Part III Line 16  Description:  Public support percentage from prior year's Schedule A, Part III, line 14a  xpath: /IRS990ScheduleA/PublicSupportPY509Pct 

    SkdA_InvstmntIncmCYPct = Column(Numeric(precision=6))
    # Line number:  Part III Line 17  Description:  Investment income percentage (line 10c column (f) divided by line 13 column(f))  xpath: /IRS990ScheduleA/InvestmentIncomeCYPct 

    SkdA_InvstmntIncmPYPct = Column(Numeric(precision=6))
    # Line number:  Part III Line 18  Description:  Investment income percentage from prior year's Schedule A, Part III, line 15a  xpath: /IRS990ScheduleA/InvestmentIncomePYPct 

    SkdA_ThrtyThrPctSprtTstsCY509Ind = Column(String(length=1))
    # Line number:  Part III Line 19a  Description:  33.33 % Tests - Current Year. If the organization did not check the box on line17, and line 14a is more than 33.33% and line 15a is less than 33.33%, check this box and stop here  xpath: /IRS990ScheduleA/ThirtyThrPctSuprtTestsCY509Ind 

    SkdA_ThrtyThrPctSprtTstsPY509Ind = Column(String(length=1))
    # Line number:  Part III Line 19b  Description:  33.33 % Tests - Prior Year. If the organization did not check the boxes on line 17 and line 18, and line 14b is more than 33.33% and line 15a is less than 33.33%, check this box and stop here  xpath: /IRS990ScheduleA/ThirtyThrPctSuprtTestsPY509Ind 

    SkdA_PrvtFndtn509Ind = Column(String(length=1))
    # Line number:  Part III Line 20  Description:  Private Foundation. If the organization did not check the box on either line 14, 19a or 19b, check this box and see instructions  xpath: /IRS990ScheduleA/PrivateFoundation509Ind 

#######
#
# IRS990ScheduleA - ScheduleA Part IV Supporting Organizations 
#
#######

class skeda_part_iv(Base):
    __tablename__='skeda_part_iv'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Frm990SchASpprtngOrg = Column(Text)
    # Line number:  Part IV Section A Group  Description:  All supporting organizations  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp 

    LstdByNmGvrnngDcInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 1  Description:  All supported organizations listed by name in governing documents?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ListedByNameGoverningDocInd 

    SprtOrgNIRSDtrmntnInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 2  Description:  Any supported organization that does not have IRS determination?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SuprtOrgNoIRSDeterminationInd 

    SpprtdOrgSctnC456Ind = Column(String(length=5))
    # Line number:  Part IV Section A Line 3a  Description:  Supported org described in Section 501(c)(4), (5), (6)?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SupportedOrgSectionC456Ind 

    SpprtdOrgQlfdInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 3b  Description:  Confirmed supported org qualified?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SupportedOrgQualifiedInd 

    SprtExclsvlySc170c2BInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 3c  Description:  Ensure support used exclusively for section 170(c)(2)(B) purposes?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SuprtExclusivelySec170c2BInd 

    SpprtdOrgNtOrgnzdUSInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 4a  Description:  Any supported organized not organized in the United States?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SupportedOrgNotOrganizedUSInd 

    CntrlDcdngGrntFrgnOrgInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 4b  Description:  Ultimate control in deciding whether to make grants to foreign supported org?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ControlDecidingGrntFrgnOrgInd 

    SpprtFrgnOrgNDtrmInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 4c  Description:  Support any foreign organizations that does not have IRS determination?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SupportForeignOrgNoDetermInd 

    OrgnztnChngSprtOrgInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 5a  Description:  Organization add, substitute or remove any supported org during the year?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/OrganizationChangeSuprtOrgInd 

    SpprtdOrgClssDsgntdInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 5b  Description:  Supported organization part of a class already designated in orgs organizing document?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SupportedOrgClassDesignatedInd 

    SbstttnByndOrgCntlInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 5c  Description:  Substitution the result of an event beyond the organization's control?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SubstitutionBeyondOrgCntlInd 

    SpprtNnSpprtdOrgInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 6  Description:  Support anyone other than supported organizations?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SupportNonSupportedOrgInd 

    PymntSbstntlCntrbtrInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 7  Description:  Provide grant, loan, compensation to a substantial contributor?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/PaymentSubstantialContribtrInd 

    LnDsqlfdPrsnInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 8  Description:  Loan to disqualified person?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/LoanDisqualifiedPersonInd 

    CntrlldDsqlfdPrsnInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 9a  Description:  Controlled by one or more disqualified persons?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ControlledDisqualifiedPrsnInd 

    DsqlfdPrsnCntrllIntInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 9b  Description:  Disqualified person hold controlling interest in any entity which supporting org had an interest?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/DisqualifiedPrsnControllIntInd 

    DsqlfdPrsnOwnrIntInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 9c  Description:  Disqualified person have an ownership interest in assets which supporting org had an interest?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/DisqualifiedPrsnOwnrIntInd 

    ExcssBsnssHldngsRlsInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 10a  Description:  Subject to excess business holding rules?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ExcessBusinessHoldingsRulesInd 

    ExcssBsnssHldngsInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 10b  Description:  Excess business holdings in the tax year?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ExcessBusinessHoldingsInd 

    CntrbtnCntrllrInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 11a  Description:  A person who controls, alone or together with persons in (ii) and (iii) below, the governing body of the supported organization?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ContributionControllerInd 

    CntrbtnFmlyInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 11b  Description:  A family member of a party described in (i) above?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ContributionFamilyInd 

    Cntrbtn35CntrlldInd = Column(String(length=5))
    # Line number:  Part IV Section A Line 11c  Description:  A 35% controlled entity of a person described in (i) or (ii) above?  xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/Contribution35ControlledInd 

    Frm990SchA1SprtOrg = Column(Text)
    # Line number:  Part IV Section B Group  Description:  Type I supporting organizations  xpath: /IRS990ScheduleA/Form990SchAType1SuprtOrgGrp 

    PwrAppntMjrtyDrTrstInd = Column(String(length=5))
    # Line number:  Part IV Section B Line 1  Description:  Directors, trustees, or membership of supported org have power to regularly appoint or elect at least majority of orgs directors or trustees?  xpath: /IRS990ScheduleA/Form990SchAType1SuprtOrgGrp/PowerAppointMajorityDirTrstInd 

    OprtBnftNnSprtOrgInd = Column(String(length=5))
    # Line number:  Part IV Section B Line 2  Description:  Operate for the benefit of any other supported organization?  xpath: /IRS990ScheduleA/Form990SchAType1SuprtOrgGrp/OperateBenefitNonSuprtOrgInd 

    MjrtyDrTrstSpprtdOrgInd = Column(String(length=5))
    # Line number:  Part IV Section C Line 1  Description:  Also a majority of the directors or trustees of each of the organizations supported orgs?  xpath: /IRS990ScheduleA/MajorityDirTrstSupportedOrgInd 

    Frm990SchA3SprtOrgAll = Column(Text)
    # Line number:  Part IV Section D Group  Description:  All type III supporting organizations  xpath: /IRS990ScheduleA/Form990SchAType3SprtOrgAllGrp 

    TmlyPrvddDcmntsInd = Column(String(length=5))
    # Line number:  Part IV Section D Line 1  Description:  Timely provided written notice, copy of Form 990, and governing documents?  xpath: /IRS990ScheduleA/Form990SchAType3SprtOrgAllGrp/TimelyProvidedDocumentsInd 

    OffcrsClsRltnshpInd = Column(String(length=5))
    # Line number:  Part IV Section D Line 2  Description:  Maintained close and continuous working relationship with the supported organization?  xpath: /IRS990ScheduleA/Form990SchAType3SprtOrgAllGrp/OfficersCloseRelationshipInd 

    SpprtdOrgVcInvstmntInd = Column(String(length=5))
    # Line number:  Part IV Section D Line 3  Description:  Supported organizations have significant voice in the organizations investment policies?  xpath: /IRS990ScheduleA/Form990SchAType3SprtOrgAllGrp/SupportedOrgVoiceInvestmentInd 

    Frm990SchA3FncInt = Column(Text)
    # Line number:  Part IV Section E Group  Description:  Type III functionally-integrated supporting organizations  xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp 

    ActvtsTstInd = Column(String(length=1))
    # Line number:  Part IV Section E Line 1a  Description:  Satisfied activities test  xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/ActivitiesTestInd 

    PrntSpprtdOrgInd = Column(String(length=1))
    # Line number:  Part IV Section E Line 1b  Description:  Parent of each of its supported organizations  xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/ParentSupportedOrgInd 

    GvrnmntlEnttyInd = Column(String(length=1))
    # Line number:  Part IV Section E Line 1c  Description:  Supported a governmental entity  xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/GovernmentalEntityInd 

    ActvtsFrthrExmptPrpsInd = Column(String(length=5))
    # Line number:  Part IV Section E Line 2a  Description:  Substantially all activities during the year directly further exempt purposes of the supported organization?  xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/ActivitiesFurtherExemptPrpsInd 

    ActvtsEnggdOrgInvlmntInd = Column(String(length=5))
    # Line number:  Part IV Section E Line 2b  Description:  Constitute activities that, but for the organization's involvement, supported org would have been engaged?  xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/ActivitiesEngagedOrgInvlmntInd 

    AppntElctMjrtyOffcrInd = Column(String(length=5))
    # Line number:  Part IV Section E Line 3a  Description:  Power to regularly appoint or elect majority of the officers of each supported organization?  xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/AppointElectMajorityOfficerInd 

    ExrcsDrctnPlcsInd = Column(String(length=5))
    # Line number:  Part IV Section E Line 3b  Description:  Exercise a substantial degree of direction over policies, programs or activities of each supported org?  xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/ExerciseDirectionPoliciesInd 

#######
#
# IRS990ScheduleA - ScheduleA Part V Type III Non-Functionally Integrated 509(a)(3) Supporting Organizations 
#
#######

class skeda_part_v(Base):
    __tablename__='skeda_part_v'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SkdA_TrstIntgrlPrtTstInd = Column(String(length=1))
    # Line number:  Part V Line 1  Description:  Organization satisfied Integral Part Test as qualifying trust  xpath: /IRS990ScheduleA/TrustIntegralPartTestInd 

    SkdA_AdjstdNtIncm = Column(Text)
    # Line number:  Part V Section A Group  Description:  Adjusted net income group  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp 

    NtSTCptlGnAdjNtIncm_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/NetSTCapitalGainAdjNetIncmGrp/PriorYearAmt 

    NtSTCptlGnAdjNtIncm_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/NetSTCapitalGainAdjNetIncmGrp/CurrentYearAmt 

    RcvrsPYDstrbtns_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/RecoveriesPYDistributionsGrp/PriorYearAmt 

    RcvrsPYDstrbtns_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/RecoveriesPYDistributionsGrp/CurrentYearAmt 

    OthrGrssIncm_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/OtherGrossIncomeGrp/PriorYearAmt 

    OthrGrssIncm_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/OtherGrossIncomeGrp/CurrentYearAmt 

    AdjstdGrssIncm_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/AdjustedGrossIncomeGrp/PriorYearAmt 

    AdjstdGrssIncm_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/AdjustedGrossIncomeGrp/CurrentYearAmt 

    DprctnDpltn_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/DepreciationDepletionGrp/PriorYearAmt 

    DprctnDpltn_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/DepreciationDepletionGrp/CurrentYearAmt 

    PrdctnIncm_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/ProductionIncomeGrp/PriorYearAmt 

    PrdctnIncm_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/ProductionIncomeGrp/CurrentYearAmt 

    OthrExpnss_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/OtherExpensesGrp/PriorYearAmt 

    OthrExpnss_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/OtherExpensesGrp/CurrentYearAmt 

    TtlAdjstdNtIncm_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/TotalAdjustedNetIncomeGrp/PriorYearAmt 

    TtlAdjstdNtIncm_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/TotalAdjustedNetIncomeGrp/CurrentYearAmt 

    SkdA_MnmmAsstAmnt = Column(Text)
    # Line number:  Part V Section B Group  Description:  Minimum asset amount group  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp 

    AvrgMnthlyFMVOfSc_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AverageMonthlyFMVOfSecGrp/PriorYearAmt 

    AvrgMnthlyFMVOfSc_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AverageMonthlyFMVOfSecGrp/CurrentYearAmt 

    AvrgMnthlyCshBlncs_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AverageMonthlyCashBalancesGrp/PriorYearAmt 

    AvrgMnthlyCshBlncs_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AverageMonthlyCashBalancesGrp/CurrentYearAmt 

    FMVOthrNnExmptUsAsst_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/FMVOtherNonExemptUseAssetGrp/PriorYearAmt 

    FMVOthrNnExmptUsAsst_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/FMVOtherNonExemptUseAssetGrp/CurrentYearAmt 

    TtlFMVOfNnExmptUsAsst_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/TotalFMVOfNonExemptUseAssetGrp/PriorYearAmt 

    TtlFMVOfNnExmptUsAsst_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/TotalFMVOfNonExemptUseAssetGrp/CurrentYearAmt 

    MnmmAsstAmnt_DscntClmdAmt = Column(BigInteger)
    # Line number:  Part V Section B Line 1e  Description:  Discount claimed for blockage or other factors  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/DiscountClaimedAmt 

    AcqstnIndbtdnss_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AcquisitionIndebtednessGrp/PriorYearAmt 

    AcqstnIndbtdnss_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AcquisitionIndebtednessGrp/CurrentYearAmt 

    AdjstdFMVLssIndbtdnss_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AdjustedFMVLessIndebtednessGrp/PriorYearAmt 

    AdjstdFMVLssIndbtdnss_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AdjustedFMVLessIndebtednessGrp/CurrentYearAmt 

    CshDmdChrtbl_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/CashDeemedCharitableGrp/PriorYearAmt 

    CshDmdChrtbl_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/CashDeemedCharitableGrp/CurrentYearAmt 

    NtVlNnExmptUsAssts_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/NetVlNonExemptUseAssetsGrp/PriorYearAmt 

    NtVlNnExmptUsAssts_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/NetVlNonExemptUseAssetsGrp/CurrentYearAmt 

    PctOfNtVlNnExmptUsAst_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/PctOfNetVlNonExemptUseAstGrp/PriorYearAmt 

    PctOfNtVlNnExmptUsAst_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/PctOfNetVlNonExemptUseAstGrp/CurrentYearAmt 

    RcvrsPYDstrMnAsst_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/RecoveriesPYDistriMinAssetGrp/PriorYearAmt 

    RcvrsPYDstrMnAsst_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/RecoveriesPYDistriMinAssetGrp/CurrentYearAmt 

    TtlMnmmAsst_PrrYrAmt = Column(BigInteger)
    # Line number:  Part V Column A  Description:  Prior year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/TotalMinimumAssetGrp/PriorYearAmt 

    TtlMnmmAsst_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part V Column B  Description:  Current year amount  xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/TotalMinimumAssetGrp/CurrentYearAmt 

    SkdA_DstrbtblAmnt = Column(Text)
    # Line number:  Part V Section C  Description:  Distributable amount group  xpath: /IRS990ScheduleA/DistributableAmountGrp 

    DstrbtblAmnt_CYAdjNtIncmDstrbtblAmt = Column(BigInteger)
    # Line number:  Part V Section C Line 1(B)  Description:  Adjusted net income amount for prior year - distributable amount (from Section A, line 8, Column A)  xpath: /IRS990ScheduleA/DistributableAmountGrp/CYAdjNetIncomeDistributableAmt 

    DstrbtblAmnt_CYPct85AdjstdNtIncmAmt = Column(BigInteger)
    # Line number:  Part V Section C Line 2(B)  Description:  85% Percent of adjusted net income amount - distributable amount  xpath: /IRS990ScheduleA/DistributableAmountGrp/CYPct85AdjustedNetIncomeAmt 

    DstrbtblAmnt_CYTtlMnAstDstrbtblAmt = Column(BigInteger)
    # Line number:  Part V Section C Line 3(B)  Description:  Minimum asset amount for prior year - distributable amount (from Section B, line 8, Column A)  xpath: /IRS990ScheduleA/DistributableAmountGrp/CYTotalMinAstDistributableAmt 

    DstrbtblAmnt_CYGrtrAdjstdMnmmAmt = Column(BigInteger)
    # Line number:  Part V Section C Line 4(B)  Description:  Greater of 85% adjusted net income amount and minimum assets amount  xpath: /IRS990ScheduleA/DistributableAmountGrp/CYGreaterAdjustedMinimumAmt 

    DstrbtblAmnt_CYIncmTxImpsdPYAmt = Column(BigInteger)
    # Line number:  Part V Section C Line 5(B)  Description:  Income tax imposed in prior year  xpath: /IRS990ScheduleA/DistributableAmountGrp/CYIncomeTaxImposedPYAmt 

    DstrbtblAmnt_CYDstrbtblAsAdjstdAmt = Column(BigInteger)
    # Line number:  Part V Section C Line 6(B)  Description:  Distributable amount as adjusted unless subject to emergency temporary reduction  xpath: /IRS990ScheduleA/DistributableAmountGrp/CYDistributableAsAdjustedAmt 

    DstrbtblAmnt_FrstYr3NnFncInd = Column(String(length=1))
    # Line number:  Part V Section C Line 7  Description:  First year as a non-functionally-integrated Type III supporting organization  xpath: /IRS990ScheduleA/DistributableAmountGrp/FirstYearType3NonFuncInd 

    SkdA_Dstrbtns = Column(Text)
    # Line number:  Part V Section D Group  xpath: /IRS990ScheduleA/DistributionsGrp 

    Dstrbtns_CYPdAccmplshExmptPrpsAmt = Column(BigInteger)
    # Line number:  Part V Section D Line 1  Description:  Amounts paid to supported organizations to accomplish exempt purpose - Current Year  xpath: /IRS990ScheduleA/DistributionsGrp/CYPaidAccomplishExemptPrpsAmt 

    Dstrbtns_CYPdInExcssIncmActvtyAmt = Column(BigInteger)
    # Line number:  Part V Section D Line 2  Description:  Amounts paid to perform activity that directly furthers exempt purpose - in excess of income from activity  xpath: /IRS990ScheduleA/DistributionsGrp/CYPdInExcessIncomeActivityAmt 

    Dstrbtns_CYAdmnstrtvExpnsPdAmt = Column(BigInteger)
    # Line number:  Part V Section D Line 3  Description:  Administrative expenses paid to accomplish exempt purposes  xpath: /IRS990ScheduleA/DistributionsGrp/CYAdministrativeExpensePaidAmt 

    Dstrbtns_ExmptUsAsstsAcqsPdAmt = Column(BigInteger)
    # Line number:  Part V Section D Line 4  Description:  Amounts paid to acquire exempt-use assets  xpath: /IRS990ScheduleA/DistributionsGrp/ExemptUseAssetsAcquisPaidAmt 

    Dstrbtns_QlfdStAsdAmt = Column(BigInteger)
    # Line number:  Part V Section D Line 5  Description:  Qualified set-aside amounts  xpath: /IRS990ScheduleA/DistributionsGrp/QualifiedSetAsideAmt 

    Dstrbtns_CYOthrDstrbtnsAmt = Column(BigInteger)
    # Line number:  Part V Section D Line 6  Description:  Other distributions - Current Year  xpath: /IRS990ScheduleA/DistributionsGrp/CYOtherDistributionsAmt 

    Dstrbtns_CYTtlAnnlDstrbtnsAmt = Column(BigInteger)
    # Line number:  Part V Section D Line 7  Description:  Total annual distributions - Current Year  xpath: /IRS990ScheduleA/DistributionsGrp/CYTotalAnnualDistributionsAmt 

    Dstrbtns_CYDstrAttntvSprtOrgAmt = Column(BigInteger)
    # Line number:  Part V Section D Line 8  Description:  Distributions to attentive supported organizations to which the org is responsive  xpath: /IRS990ScheduleA/DistributionsGrp/CYDistriAttentiveSuprtOrgAmt 

    Dstrbtns_CYDstrbtblAsAdjstdAmt = Column(BigInteger)
    # Line number:  Part V Section D Line 9  Description:  Distributable amount for current year (from Section C, line 6)  xpath: /IRS990ScheduleA/DistributionsGrp/CYDistributableAsAdjustedAmt 

    Dstrbtns_CYDstrbtnYrRt = Column(Text)
    # Line number:  Part V Section D Line 10  Description:  Distributions to attentive supported org divided by Distributable amount  xpath: /IRS990ScheduleA/DistributionsGrp/CYDistributionYrRt 

    SkdA_DstrbtnAllctns = Column(Text)
    # Line number:  Part V Section E Group  Description:  Distribution allocations  xpath: /IRS990ScheduleA/DistributionAllocationsGrp 

    DstrbtnAllctns_CYDstrbtblAsAdjstdAmt = Column(BigInteger)
    # Line number:  Part V Section E Line 1(iii)  Description:  Distributable amount for current year (from Section C, line 6)  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/CYDistributableAsAdjustedAmt 

    DstrbtnAllctns_UndrdstrbtnsAmt = Column(BigInteger)
    # Line number:  Part V Section E Line 2(ii)  Description:  Underdistributions for years prior to current year  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/UnderdistributionsAmt 

    DstrbtnAllctns_ExcssDstrbtnCyvYr2Amt = Column(BigInteger)
    # Line number:  Part V Section E Line 3(d)  Description:  Excess distributions carryover - year 2  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistributionCyovYr2Amt 

    DstrbtnAllctns_ExcssDstrbtnCyvYr1Amt = Column(BigInteger)
    # Line number:  Part V Section E Line 3(e)  Description:  Excess distributions carryover - year 1  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistributionCyovYr1Amt 

    DstrbtnAllctns_TtlExcssDstrbtnCyvAmt = Column(BigInteger)
    # Line number:  Part V Section E Line 3(f)(i)  Description:  Excess distributions carryover amount  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/TotalExcessDistributionCyovAmt 

    DstrbtnAllctns_CyvAppldUndrdstrPYAmt = Column(BigInteger)
    # Line number:  Part V Section E Line 3(g)(ii)  Description:  Carryover applied to underdistributions of prior years  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/CyovAppliedUnderdistriPYAmt 

    DstrbtnAllctns_CyvAppldUndrdstrCPYAmt = Column(BigInteger)
    # Line number:  Part V Section E Line 3(h)(iii)  Description:  Carryover applied to current year  distributable amount  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/CyovAppliedUnderdistrCPYAmt 

    DstrbtnAllctns_ExcssDstrbtnCyvAmt = Column(BigInteger)
    # Line number:  Part V Section E Line 3(j)  Description:  Excess distributions carryover amount  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistributionCyovAmt 

    DstrbtnAllctns_CYTtlAnnlDstrbtnsAmt = Column(BigInteger)
    # Line number:  Part V Section E Line 4  Description:  Total annual distributions from current year (from Section D, line 7)  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/CYTotalAnnualDistributionsAmt 

    DstrbtnAllctns_CYDstrbAppUndrdstrPYAmt = Column(BigInteger)
    # Line number:  Part V Section E Line 4a(ii)  Description:  Current year distributions applied to underdistributions of prior years  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/CYDistribAppUnderdistriPYAmt 

    DstrbtnAllctns_CYDstrAppDstrbtblAmt = Column(BigInteger)
    # Line number:  Part V Section E Line 4b(iii)  Description:  Current year distributions applied to distributable amount  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/CYDistriAppDistributableAmt 

    DstrbtnAllctns_ExcssDstrbtnAmt = Column(BigInteger)
    # Line number:  Part V Section E Line 4c(i)  Description:  Excess distributions current year amount  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistributionAmt 

    DstrbtnAllctns_RmnngUndrdstrPYAmt = Column(BigInteger)
    # Line number:  Part V Section E Line 5(ii)  Description:  Remaining underdistributions - prior years  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/RemainingUnderdistriPYAmt 

    DstrbtnAllctns_RmnngUndrdstrCYAmt = Column(BigInteger)
    # Line number:  Part V Section E Line 6(iii)  Description:  Remaining underdistributions - current years  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/RemainingUnderdistriCYAmt 

    DstrbtnAllctns_ExcssDstrCyvTNxtYrAmt = Column(BigInteger)
    # Line number:  Part V Section E Line 7(i)  Description:  Excess distribution carryover to next year  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistriCyovToNextYrAmt 

    DstrbtnAllctns_ExcssFrmYr3Amt = Column(BigInteger)
    # Line number:  Part V Section E Line 8c  Description:  Excess from year 3  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessFromYear3Amt 

    DstrbtnAllctns_ExcssFrmYr2Amt = Column(BigInteger)
    # Line number:  Part V Section E Line 8d  Description:  Excess from year 2  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessFromYear2Amt 

    DstrbtnAllctns_ExcssFrmYr1Amt = Column(BigInteger)
    # Line number:  Part V Section E Line 8e  Description:  Excess from year 1  xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessFromYear1Amt 

#######
#
# IRS990ScheduleA - ScheduleA Part VI Supplemental Information 
#
#######

class skeda_part_vi(Base):
    __tablename__='skeda_part_vi'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    FctsAndCrcmstncsTstTxt = Column(Text)
    # Line number:  Part VI  Description:  Facts and circumstances test  xpath: /IRS990ScheduleA/FactsAndCircumstancesTestTxt 

#######
#
# IRS990ScheduleA - HospitalNameAndAddressGrp
# A repeating structure from ScheduleA Part I Reason for Non-Private Foundation Status 
#
#######

class SkdAHsptlNmAndAddrss(Base):
    __tablename__='SkdAHsptlNmAndAddrss'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part I Line 4  Description:  Business name line 1  xpath: /IRS990ScheduleA/HospitalNameAndAddressGrp/SupportedOrganizationName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part I Line 4  Description:  Business name line 2  xpath: /IRS990ScheduleA/HospitalNameAndAddressGrp/SupportedOrganizationName/BusinessNameLine2Txt 

    CtyNm = Column(String(length=22))
    # Line number:  Part I Line 4  Description:  US city or foreign city  xpath: /IRS990ScheduleA/HospitalNameAndAddressGrp/CityNm 

    SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part I Line 4  Description:  US address State  xpath: /IRS990ScheduleA/HospitalNameAndAddressGrp/StateAbbreviationCd 

    CntryCd = Column(String(length=2))
    # Line number:  Part I Line 4  Description:  Foreign address Country  xpath: /IRS990ScheduleA/HospitalNameAndAddressGrp/CountryCd 

#######
#
# IRS990ScheduleA - SupportedOrgInformationGrp
# A repeating structure from ScheduleA Part I Reason for Non-Private Foundation Status 
#
#######

class SkdASpprtdOrgInfrmtn(Base):
    __tablename__='SkdASpprtdOrgInfrmtn'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part I Line 11g Column (i)  Description:  Business name line 1  xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/SupportedOrganizationName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part I Line 11g Column (i)  Description:  Business name line 2  xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/SupportedOrganizationName/BusinessNameLine2Txt 

    EIN = Column(String(length=9))
    # Line number:  Part I Line 11g Column (ii)  Description:  EIN of supported organization  xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/EIN 

    OrgnztnCd = Column(Text)
    # Line number:  Part I Line 11g(iii)  Description:  Type of organization  xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/OrganizationTypeCd 

    GvrnngDcmntLstdInd = Column(String(length=5))
    # Line number:  Part I Line 11g Column (iv)  Description:  Is the supported organization listed in your governing documents?  xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/GoverningDocumentListedInd 

    SpprtAmt = Column(BigInteger)
    # Line number:  Part I Line 11g Column (v)  Description:  Amount of support  xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/SupportAmt 

    OthrSpprtAmt = Column(BigInteger)
    # Line number:  Part I Line 11g Column (vi)  Description:  Estimated value of diversion  xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/OtherSupportAmt 

#######
#
# IRS990ScheduleA - Form990ScheduleAPartVIGrp
# A repeating structure from ScheduleA Part VI Supplemental Information 
#
#######

class SkdAFrm990SkdAPrtVI(Base):
    __tablename__='SkdAFrm990SkdAPrtVI'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Frm990SkdAPrtVI = Column(Text)
    # Line number:  Schedule A, Part VI  Description:  Supplemental information for schedule A  xpath: /IRS990ScheduleA/Form990ScheduleAPartVIGrp 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Schedule A Part VI  Description:  Form, part and line number reference  xpath: /IRS990ScheduleA/Form990ScheduleAPartVIGrp/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Schedule A Part VI  Description:  Form, part and line number reference explanation  xpath: /IRS990ScheduleA/Form990ScheduleAPartVIGrp/ExplanationTxt 

#######
#
# IRS990ScheduleB - ScheduleB Part 0 Prefatory material 
#
#######

class skedb_part_0(Base):
    __tablename__='skedb_part_0'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Orgnztn501cInd = Column(Text)
    # Description:  Indicates a 501(c) organization  xpath: /IRS990ScheduleB/Organization501cInd 

    Orgnztn49471NtPFInd = Column(String(length=1))
    # Description:  Indicates a 4947(a)(1) organization not treated as a private foundation  xpath: /IRS990ScheduleB/Organization4947a1NotPFInd 

    Orgnztn527Ind = Column(String(length=1))
    # Description:  Indicates a 527 organization  xpath: /IRS990ScheduleB/Organization527Ind 

    Orgnztn501c3ExmptPFInd = Column(String(length=1))
    # Description:  Organization 501(c)(3) exempt PF  xpath: /IRS990ScheduleB/Organization501c3ExemptPFInd 

    Orgnztn49471TrtdPFInd = Column(String(length=1))
    # Description:  Organization 4947(a)(1) treated as PF  xpath: /IRS990ScheduleB/Organization4947a1TrtdPFInd 

    Orgnztn501c3TxblPFInd = Column(String(length=1))
    # Description:  Indicates a 501(c)(3) taxable private foundation  xpath: /IRS990ScheduleB/Organization501c3TaxablePFInd 

    GnrlRlInd = Column(String(length=1))
    # Description:  For organizations filing Form 990, or 990-EZ that received, during the year, $5000 or more (in money or property) from any one contributor  xpath: /IRS990ScheduleB/GeneralRuleInd 

    SpclRlMtOn3rdSprtTstInd = Column(String(length=1))
    # Description:  For a section 501(c)(3) organization filing Form 990, or Form 990-EZ, that met the 33 1/3 % support test of the regulations under sections 509(a)(1)/170(b)(1)(A)(vi) and received from any one contributor, during the year, a contribution of the greater of $5,000 or 2% of the amount on line 1 of these forms  xpath: /IRS990ScheduleB/SpclRuleMetOne3rdSuprtTestInd 

    TtCntrRcvdMr1000Ind = Column(String(length=1))
    # Description:  For a section 501(c)(7), (8), or (10) organization filing Form 990, or Form 990-EZ, that received from any one contributor, during the year, aggregate contributions or bequests of more than $1,000 for use exclusively for religious, charitable, scientific, literary, or educational purposes, or the prevention of cruelty to children or animals  xpath: /IRS990ScheduleB/TotContriRcvdMore1000Ind 

    TtCntrRcvdUpT1000Ind = Column(Text)
    # Description:  For a section 501(c)(7), (8), or (10) organization filing Form 990, or Form 990-EZ, that received from any one contributor, during the year, some contributions for use exclusively for religious, charitable, etc., purposes, but these contributions did not aggregate to more than $1,000  xpath: /IRS990ScheduleB/TotContriRcvdUpTo1000Ind 

#######
#
# IRS990ScheduleB - ScheduleB Part II - Noncash Property 
#
#######

class skedb_part_ii(Base):
    __tablename__='skedb_part_ii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    TtlUndr1000CntrbtnsAmt = Column(BigInteger)
    # Line number:  Part III  Description:  Total of contributions of $1,000 or less  xpath: /IRS990ScheduleB/TotalUnder1000ContributionsAmt 

#######
#
# IRS990ScheduleB - NonCashPropertyContributionGrp
# A repeating structure from ScheduleB Part II - Noncash Property 
#
#######

class SkdBNnCshPrprtyCntrbtn(Base):
    __tablename__='SkdBNnCshPrprtyCntrbtn'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    CntrbtrNm = Column(BigInteger)
    # Line number:  Part II Column (a)  Description:  Contributor number from Part I  xpath: /IRS990ScheduleB/NonCashPropertyContributionGrp/ContributorNum 

    NncshPrprtyDsc = Column(String(length=100))
    # Line number:  Part II Column (b)  Description:  Description of noncash property given  xpath: /IRS990ScheduleB/NonCashPropertyContributionGrp/NoncashPropertyDesc 

    FrMrktVlAmt = Column(BigInteger)
    # Line number:  Part II Column (c)  Description:  FMV (or estimate)  xpath: /IRS990ScheduleB/NonCashPropertyContributionGrp/FairMarketValueAmt 

    RcvdDt = Column(String(length=31))
    # Line number:  Part II Column (d)  Description:  Date received  xpath: /IRS990ScheduleB/NonCashPropertyContributionGrp/ReceivedDt 

#######
#
# IRS990ScheduleB - CharitableContributionsDetail
# A repeating structure from ScheduleB Part II - Noncash Property 
#
#######

class SkdBChrtblCntrbtnsDtl(Base):
    __tablename__='SkdBChrtblCntrbtnsDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    ChrtblCntrbtnsDtl_CntrbtrNm = Column(BigInteger)
    # Line number:  Part III Column (a)  Description:  Contributor number from Part I  xpath: /IRS990ScheduleB/CharitableContributionsDetail/ContributorNum 

    ChrtblCntrbtnsDtl_GftPrpsTxt = Column(String(length=100))
    # Line number:  Part III Column (b)  Description:  Purpose of gift  xpath: /IRS990ScheduleB/CharitableContributionsDetail/GiftPurposeTxt 

    ChrtblCntrbtnsDtl_GftUsTxt = Column(String(length=100))
    # Line number:  Part III Column (c)  Description:  Use of gift  xpath: /IRS990ScheduleB/CharitableContributionsDetail/GiftUseTxt 

    ChrtblCntrbtnsDtl_HwGftIsHldDsc = Column(String(length=100))
    # Line number:  Part III Column (d)  Description:  Description of how gift is held  xpath: /IRS990ScheduleB/CharitableContributionsDetail/HowGiftIsHeldDesc 

    ChrtblCntrbtnsDtl_RlnOfTrnsfrrTTrnsfrTxt = Column(String(length=100))
    # Line number:  Part III Column (e)  Description:  Relationship of transferor to transferee  xpath: /IRS990ScheduleB/CharitableContributionsDetail/RlnOfTransferorToTransfereeTxt 

    TrnsfrNmBsnss_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part III Column (e)  Description:  Business name line 1  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeNameBusiness/BusinessNameLine1Txt 

    TrnsfrNmBsnss_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part III Column (e)  Description:  Business name line 2  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeNameBusiness/BusinessNameLine2Txt 

    ChrtblCntrbtnsDtl_TrnsfrNmIndvdl = Column(String(length=35))
    # Line number:  Part III Column (e)  Description:  Transferee name - Individual  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeNameIndividual 

    TrnsfrUSAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part III Column (e)  Description:  Address line 1  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeUSAddress/AddressLine1Txt 

    TrnsfrUSAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part III Column (e)  Description:  Address line 2  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeUSAddress/AddressLine2Txt 

    TrnsfrUSAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part III Column (e)  Description:  City  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeUSAddress/CityNm 

    TrnsfrUSAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part III Column (e)  Description:  State  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeUSAddress/StateAbbreviationCd 

    TrnsfrUSAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part III Column (e)  Description:  ZIP code  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeUSAddress/ZIPCd 

    TrnsfrFrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part III Column (e)  Description:  Address line 1  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeForeignAddress/AddressLine1Txt 

    TrnsfrFrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part III Column (e)  Description:  Address line 2  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeForeignAddress/AddressLine2Txt 

    TrnsfrFrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part III Column (e)  Description:  City  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeForeignAddress/CityNm 

    TrnsfrFrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part III Column (e)  Description:  Province or state  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeForeignAddress/ProvinceOrStateNm 

    TrnsfrFrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part III Column (e)  Description:  Country  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeForeignAddress/CountryCd 

    TrnsfrFrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part III Column (e)  Description:  Postal code  xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeForeignAddress/ForeignPostalCd 

#######
#
# IRS990ScheduleB - ContributorInformationGrp
# A repeating structure from ScheduleB Part I - Contributors 
#
#######

class SkdBCntrbtrInfrmtn(Base):
    __tablename__='SkdBCntrbtrInfrmtn'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    CntrbtrInfrmtn_CntrbtrNm = Column(BigInteger)
    # Line number:  Part I Column (a)  Description:  Cotributor number  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorNum 

    CntrbtrInfrmtn_TtlCntrbtnsAmt = Column(BigInteger)
    # Line number:  Part I Column (c)  Description:  Aggregate contributions  xpath: /IRS990ScheduleB/ContributorInformationGrp/TotalContributionsAmt 

    CntrbtrInfrmtn_PrsnCntrbtnInd = Column(String(length=1))
    # Line number:  Part I Column (d)  Description:  Type of contribution - Person  xpath: /IRS990ScheduleB/ContributorInformationGrp/PersonContributionInd 

    CntrbtrInfrmtn_PyrllCntrbtnInd = Column(String(length=1))
    # Line number:  Part I Column (d)  Description:  Type of contribution - Payroll  xpath: /IRS990ScheduleB/ContributorInformationGrp/PayrollContributionInd 

    CntrbtrInfrmtn_NncshCntrbtnInd = Column(String(length=1))
    # Line number:  Part I Column (d)  Description:  Type of contribution - Noncash  xpath: /IRS990ScheduleB/ContributorInformationGrp/NoncashContributionInd 

    CntrbtrBsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part I Column (b)  Description:  Business name line 1  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorBusinessName/BusinessNameLine1Txt 

    CntrbtrBsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part I Column (b)  Description:  Business name line 2  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorBusinessName/BusinessNameLine2Txt 

    CntrbtrInfrmtn_CntrbtrPrsnNm = Column(String(length=35))
    # Line number:  Part I Column (b)  Description:  Contributor name - Individual  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorPersonNm 

    CntrbtrInfrmtn_Pd527j1Ind = Column(String(length=1))
    # Line number:  Part I Column (b)  Description:  Pd. 527(j)(1)  xpath: /IRS990ScheduleB/ContributorInformationGrp/Paid527j1Ind 

    CntrbtrUSAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part I Column (b)  Description:  Address line 1  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorUSAddress/AddressLine1Txt 

    CntrbtrUSAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part I Column (b)  Description:  Address line 2  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorUSAddress/AddressLine2Txt 

    CntrbtrUSAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part I Column (b)  Description:  City  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorUSAddress/CityNm 

    CntrbtrUSAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part I Column (b)  Description:  State  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorUSAddress/StateAbbreviationCd 

    CntrbtrUSAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part I Column (b)  Description:  ZIP code  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorUSAddress/ZIPCd 

    CntrbtrFrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part I Column (b)  Description:  Address line 1  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorForeignAddress/AddressLine1Txt 

    CntrbtrFrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part I Column (b)  Description:  Address line 2  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorForeignAddress/AddressLine2Txt 

    CntrbtrFrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part I Column (b)  Description:  City  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorForeignAddress/CityNm 

    CntrbtrFrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part I Column (b)  Description:  Province or state  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorForeignAddress/ProvinceOrStateNm 

    CntrbtrFrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part I Column (b)  Description:  Country  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorForeignAddress/CountryCd 

    CntrbtrFrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part I Column (b)  Description:  Postal code  xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorForeignAddress/ForeignPostalCd 

#######
#
# IRS990ScheduleC - ScheduleC Part 0 Prefatory material 
#
#######

class skedc_part_0(Base):
    __tablename__='skedc_part_0'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    PltclExpndtrsAmt = Column(BigInteger)
    # Line number:  Part I-A Line 2  Description:  Political expenditures  xpath: /IRS990ScheduleC/PoliticalExpendituresAmt 

    VlntrHrsCnt = Column(BigInteger)
    # Line number:  Part I-A Line 3  Description:  Volunteer hours  xpath: /IRS990ScheduleC/VolunteerHoursCnt 

    Sctn4955OrgnztnTxAmt = Column(BigInteger)
    # Line number:  Part I-B Line 1  Description:  Enter the amount of any excise tax incurred under section 4955  xpath: /IRS990ScheduleC/Section4955OrganizationTaxAmt 

    Sctn4955MngrsTxAmt = Column(BigInteger)
    # Line number:  Part I-B Line 2  Description:  Enter the amount of any excise tax incurred by organization managers under section 4955  xpath: /IRS990ScheduleC/Section4955ManagersTaxAmt 

    Frm4720FldSctn4955TxInd = Column(String(length=5))
    # Line number:  Part I-B Line 3  xpath: /IRS990ScheduleC/Form4720FiledSection4955TaxInd 

    CrrctnMdInd = Column(String(length=5))
    # Line number:  Part I-B Line 4a  Description:  If the filing organization incurred in a section 4955 tax, did it file Form 4720 for this year?  xpath: /IRS990ScheduleC/CorrectionMadeInd 

    Expndd527ActvtsAmt = Column(BigInteger)
    # Line number:  Part I-C Line 1  Description:  Enter the amount directly expended by the filing organization for section 527 exempt function activities  xpath: /IRS990ScheduleC/Expended527ActivitiesAmt 

    IntrnlFndsCntrbtdAmt = Column(BigInteger)
    # Line number:  Part I-C Line 2  Description:  Enter the amount of the filing organization's own internal funds contributed to other organizations for section 527 exempt function activities  xpath: /IRS990ScheduleC/InternalFundsContributedAmt 

    TtlExmptFnctnExpndAmt = Column(BigInteger)
    # Line number:  Part I-C Line 3  Description:  Total of direct and indirect exempt function expenditures. Add lines 1 and 2  xpath: /IRS990ScheduleC/TotalExemptFunctionExpendAmt 

    Frm1120POLFldInd = Column(String(length=5))
    # Line number:  Part I-C Line 4  Description:  Did the filing organization file Form 1120-POL for this year?  xpath: /IRS990ScheduleC/Form1120POLFiledInd 

#######
#
# IRS990ScheduleC - ScheduleC Part II-A : Political Campaign and Lobbying Activities 
#
#######

class skedc_part_iia(Base):
    __tablename__='skedc_part_iia'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SkdC_OrgnztnBlngsAffltInd = Column(Text)
    # Line number:  Part II-A Line A  Description:  Check if the organization belongs to an affiliated group  xpath: /IRS990ScheduleC/OrganizationBelongsAffltGrpInd 

    SkdC_LmtdCntrlPrvsnsAppInd = Column(String(length=1))
    # Line number:  Part II-A Line B  Description:  Check if "A" is checked and "limited control" provisions apply  xpath: /IRS990ScheduleC/LimitedControlProvisionsAppInd 

    TtlGrssrtsLbbyng_FlngOrgnztnsTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  xpath: /IRS990ScheduleC/TotalGrassrootsLobbyingGrp/FilingOrganizationsTotalAmt 

    TtlGrssrtsLbbyng_AffltdGrpTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  xpath: /IRS990ScheduleC/TotalGrassrootsLobbyingGrp/AffiliatedGroupTotalAmt 

    TtlDrctLbbyng_FlngOrgnztnsTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  xpath: /IRS990ScheduleC/TotalDirectLobbyingGrp/FilingOrganizationsTotalAmt 

    TtlDrctLbbyng_AffltdGrpTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  xpath: /IRS990ScheduleC/TotalDirectLobbyingGrp/AffiliatedGroupTotalAmt 

    TtlLbbyngExpnd_FlngOrgnztnsTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  xpath: /IRS990ScheduleC/TotalLobbyingExpendGrp/FilingOrganizationsTotalAmt 

    TtlLbbyngExpnd_AffltdGrpTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  xpath: /IRS990ScheduleC/TotalLobbyingExpendGrp/AffiliatedGroupTotalAmt 

    OthrExmptPrpsExpnd_FlngOrgnztnsTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  xpath: /IRS990ScheduleC/OtherExemptPurposeExpendGrp/FilingOrganizationsTotalAmt 

    OthrExmptPrpsExpnd_AffltdGrpTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  xpath: /IRS990ScheduleC/OtherExemptPurposeExpendGrp/AffiliatedGroupTotalAmt 

    TtlExmptPrpsExpnd_FlngOrgnztnsTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  xpath: /IRS990ScheduleC/TotalExemptPurposeExpendGrp/FilingOrganizationsTotalAmt 

    TtlExmptPrpsExpnd_AffltdGrpTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  xpath: /IRS990ScheduleC/TotalExemptPurposeExpendGrp/AffiliatedGroupTotalAmt 

    LbbyngNntxblAmnt_FlngOrgnztnsTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  xpath: /IRS990ScheduleC/LobbyingNontaxableAmountGrp/FilingOrganizationsTotalAmt 

    LbbyngNntxblAmnt_AffltdGrpTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  xpath: /IRS990ScheduleC/LobbyingNontaxableAmountGrp/AffiliatedGroupTotalAmt 

    GrssrtsNntxbl_FlngOrgnztnsTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  xpath: /IRS990ScheduleC/GrassrootsNontaxableGrp/FilingOrganizationsTotalAmt 

    GrssrtsNntxbl_AffltdGrpTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  xpath: /IRS990ScheduleC/GrassrootsNontaxableGrp/AffiliatedGroupTotalAmt 

    TtLbbyngGrssrtMnsNnTx_FlngOrgnztnsTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  xpath: /IRS990ScheduleC/TotLbbyngGrassrootMnsNonTxGrp/FilingOrganizationsTotalAmt 

    TtLbbyngGrssrtMnsNnTx_AffltdGrpTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  xpath: /IRS990ScheduleC/TotLbbyngGrassrootMnsNonTxGrp/AffiliatedGroupTotalAmt 

    TtLbbyExpndMnsLbbyngNnTx_FlngOrgnztnsTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  xpath: /IRS990ScheduleC/TotLbbyExpendMnsLbbyngNonTxGrp/FilingOrganizationsTotalAmt 

    TtLbbyExpndMnsLbbyngNnTx_AffltdGrpTtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  xpath: /IRS990ScheduleC/TotLbbyExpendMnsLbbyngNonTxGrp/AffiliatedGroupTotalAmt 

    SkdC_Frm4720FldInd = Column(String(length=5))
    # Line number:  Part II-A Line 1j  Description:  If there is an amount other than zero on either line h or line i, did the organization file Form 4720 reporting section 4911 tax for this year?  xpath: /IRS990ScheduleC/Form4720FiledInd 

    AvgLbbyngNntxblAmnt_CrrntYrMns3Amt = Column(BigInteger)
    # Line number:  Part II-A Column (a)  Description:  Current year minus 3  xpath: /IRS990ScheduleC/AvgLobbyingNontaxableAmountGrp/CurrentYearMinus3Amt 

    AvgLbbyngNntxblAmnt_CrrntYrMns2Amt = Column(BigInteger)
    # Line number:  Part II-A Column (b)  Description:  Current year minus 2  xpath: /IRS990ScheduleC/AvgLobbyingNontaxableAmountGrp/CurrentYearMinus2Amt 

    AvgLbbyngNntxblAmnt_CrrntYrMns1Amt = Column(BigInteger)
    # Line number:  Part II-A Column (c)  Description:  Current year minus 1  xpath: /IRS990ScheduleC/AvgLobbyingNontaxableAmountGrp/CurrentYearMinus1Amt 

    AvgLbbyngNntxblAmnt_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part II-A Column (d)  Description:  Current year  xpath: /IRS990ScheduleC/AvgLobbyingNontaxableAmountGrp/CurrentYearAmt 

    AvgLbbyngNntxblAmnt_TtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (e)  Description:  Total  xpath: /IRS990ScheduleC/AvgLobbyingNontaxableAmountGrp/TotalAmt 

    SkdC_LbbyngClngAmt = Column(BigInteger)
    # Line number:  Part II-A Line 2b(e)  Description:  Lobbying ceiling amount (150% of line 2a(e))  xpath: /IRS990ScheduleC/LobbyingCeilingAmt 

    AvgTtlLbbyngExpnd_CrrntYrMns3Amt = Column(BigInteger)
    # Line number:  Part II-A Column (a)  Description:  Current year minus 3  xpath: /IRS990ScheduleC/AvgTotalLobbyingExpendGrp/CurrentYearMinus3Amt 

    AvgTtlLbbyngExpnd_CrrntYrMns2Amt = Column(BigInteger)
    # Line number:  Part II-A Column (b)  Description:  Current year minus 2  xpath: /IRS990ScheduleC/AvgTotalLobbyingExpendGrp/CurrentYearMinus2Amt 

    AvgTtlLbbyngExpnd_CrrntYrMns1Amt = Column(BigInteger)
    # Line number:  Part II-A Column (c)  Description:  Current year minus 1  xpath: /IRS990ScheduleC/AvgTotalLobbyingExpendGrp/CurrentYearMinus1Amt 

    AvgTtlLbbyngExpnd_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part II-A Column (d)  Description:  Current year  xpath: /IRS990ScheduleC/AvgTotalLobbyingExpendGrp/CurrentYearAmt 

    AvgTtlLbbyngExpnd_TtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (e)  Description:  Total  xpath: /IRS990ScheduleC/AvgTotalLobbyingExpendGrp/TotalAmt 

    AvgGrssrtsNntxbl_CrrntYrMns3Amt = Column(BigInteger)
    # Line number:  Part II-A Column (a)  Description:  Current year minus 3  xpath: /IRS990ScheduleC/AvgGrassrootsNontaxableGrp/CurrentYearMinus3Amt 

    AvgGrssrtsNntxbl_CrrntYrMns2Amt = Column(BigInteger)
    # Line number:  Part II-A Column (b)  Description:  Current year minus 2  xpath: /IRS990ScheduleC/AvgGrassrootsNontaxableGrp/CurrentYearMinus2Amt 

    AvgGrssrtsNntxbl_CrrntYrMns1Amt = Column(BigInteger)
    # Line number:  Part II-A Column (c)  Description:  Current year minus 1  xpath: /IRS990ScheduleC/AvgGrassrootsNontaxableGrp/CurrentYearMinus1Amt 

    AvgGrssrtsNntxbl_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part II-A Column (d)  Description:  Current year  xpath: /IRS990ScheduleC/AvgGrassrootsNontaxableGrp/CurrentYearAmt 

    AvgGrssrtsNntxbl_TtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (e)  Description:  Total  xpath: /IRS990ScheduleC/AvgGrassrootsNontaxableGrp/TotalAmt 

    SkdC_GrssrtsClngAmt = Column(BigInteger)
    # Line number:  Part II-A Line 2e(e)  Description:  Grassroots ceiling amount (150% of line 2d(e))  xpath: /IRS990ScheduleC/GrassrootsCeilingAmt 

    AvgGrssrtsLbbyngExpnd_CrrntYrMns3Amt = Column(BigInteger)
    # Line number:  Part II-A Column (a)  Description:  Current year minus 3  xpath: /IRS990ScheduleC/AvgGrassrootsLobbyingExpendGrp/CurrentYearMinus3Amt 

    AvgGrssrtsLbbyngExpnd_CrrntYrMns2Amt = Column(BigInteger)
    # Line number:  Part II-A Column (b)  Description:  Current year minus 2  xpath: /IRS990ScheduleC/AvgGrassrootsLobbyingExpendGrp/CurrentYearMinus2Amt 

    AvgGrssrtsLbbyngExpnd_CrrntYrMns1Amt = Column(BigInteger)
    # Line number:  Part II-A Column (c)  Description:  Current year minus 1  xpath: /IRS990ScheduleC/AvgGrassrootsLobbyingExpendGrp/CurrentYearMinus1Amt 

    AvgGrssrtsLbbyngExpnd_CrrntYrAmt = Column(BigInteger)
    # Line number:  Part II-A Column (d)  Description:  Current year  xpath: /IRS990ScheduleC/AvgGrassrootsLobbyingExpendGrp/CurrentYearAmt 

    AvgGrssrtsLbbyngExpnd_TtlAmt = Column(BigInteger)
    # Line number:  Part II-A Column (e)  Description:  Total  xpath: /IRS990ScheduleC/AvgGrassrootsLobbyingExpendGrp/TotalAmt 

#######
#
# IRS990ScheduleC - ScheduleC Part II-B : Political Campaign and Lobbying Activities 
#
#######

class skedc_part_iib(Base):
    __tablename__='skedc_part_iib'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    VlntrsInd = Column(String(length=5))
    # Line number:  Part II-B Line 1a Column (a)  Description:  Volunteers?  xpath: /IRS990ScheduleC/VolunteersInd 

    PdStffOrMngmntInd = Column(String(length=5))
    # Line number:  Part II-B Line 1b Column (a)  Description:  Paid staff or management?  xpath: /IRS990ScheduleC/PaidStaffOrManagementInd 

    MdAdvrtsmntsInd = Column(String(length=5))
    # Line number:  Part II-B Line 1c Column(a)  Description:  Media advertisements?  xpath: /IRS990ScheduleC/MediaAdvertisementsInd 

    MdAdvrtsmntsAmt = Column(BigInteger)
    # Line number:  Part II-B Line 1c Column (b)  Description:  Media advertisements amount (only for section 501(c)(3))  xpath: /IRS990ScheduleC/MediaAdvertisementsAmt 

    MlngsMmbrsInd = Column(String(length=5))
    # Line number:  Part II-B Line 1d Column (a)  Description:  Mailings to members, legislators, or to the public?  xpath: /IRS990ScheduleC/MailingsMembersInd 

    MlngsMmbrsAmt = Column(BigInteger)
    # Line number:  Part II-B Line 1d Column (b)  Description:  Media advertisements amount (only for section 501(c)(3))  xpath: /IRS990ScheduleC/MailingsMembersAmt 

    PblctnsOrBrdcstInd = Column(String(length=5))
    # Line number:  Part II-B Line 1e Column(a)  Description:  Publications, or published or broadcast statements?  xpath: /IRS990ScheduleC/PublicationsOrBroadcastInd 

    PblctnsOrBrdcstAmt = Column(BigInteger)
    # Line number:  Part II-B Line 1e Column (b)  Description:  Publications, or published or broadcast statements (only for section 501(c)(3))  xpath: /IRS990ScheduleC/PublicationsOrBroadcastAmt 

    GrntsOthrOrgnztnsInd = Column(String(length=5))
    # Line number:  Part II-B Line 1f Column (a)  Description:  Grants to other organizations for lobbying purposes?  xpath: /IRS990ScheduleC/GrantsOtherOrganizationsInd 

    GrntsOthrOrgnztnsAmt = Column(BigInteger)
    # Line number:  Part II-B Line 1f Column (b)  Description:  Grants to other organizations for lobbying purposes (only for section 501(c)(3))  xpath: /IRS990ScheduleC/GrantsOtherOrganizationsAmt 

    DrctCntctLgsltrsInd = Column(String(length=5))
    # Line number:  Part II-B Line 1g Column (a)  Description:  Direct contact with legislators, their staffs, government officials, or a legislative body?  xpath: /IRS990ScheduleC/DirectContactLegislatorsInd 

    DrctCntctLgsltrsAmt = Column(BigInteger)
    # Line number:  Part II-B Line 1g Column (b)  Description:  Direct contact with legislators, their staffs, government officials, or a legislative body (only for section 501(c)(3))  xpath: /IRS990ScheduleC/DirectContactLegislatorsAmt 

    RllsDmnstrtnsInd = Column(String(length=5))
    # Line number:  Part II-B Line 1h Column (a)  Description:  Rallies, demonstrations, seminars, conventions, speeches, lectures, or any other means?  xpath: /IRS990ScheduleC/RalliesDemonstrationsInd 

    RllsDmnstrtnsAmt = Column(BigInteger)
    # Line number:  Part II-B Line 1h Column (b)  Description:  Rallies, demonstrations, seminars, conventions, speeches, lectures, or any other means (only for section 501(c)(3))  xpath: /IRS990ScheduleC/RalliesDemonstrationsAmt 

    OthrActvtsInd = Column(String(length=5))
    # Line number:  Part II-B Line 1i Column (a)  Description:  Other activities?  xpath: /IRS990ScheduleC/OtherActivitiesInd 

    OthrActvtsAmt = Column(BigInteger)
    # Line number:  Part II-B Line 1i Column (b)  Description:  Other activities amount  xpath: /IRS990ScheduleC/OtherActivitiesAmt 

    TtlLbbyngExpndtrsAmt = Column(BigInteger)
    # Line number:  Part II-B Line 1j Column (b)  Description:  Total Line 1c through 1i (only for section 501(c)(3))  xpath: /IRS990ScheduleC/TotalLobbyingExpendituresAmt 

    NtDscrbdSctn501c3Ind = Column(String(length=5))
    # Line number:  Part II-B Line 2a Column (a)  Description:  Did the activities in line 1 cause the organization to be not described in section 501(c)(3)?  xpath: /IRS990ScheduleC/NotDescribedSection501c3Ind 

    Tx4912Amt = Column(BigInteger)
    # Line number:  Part II-B Line 2b Column (b)  Description:  If "Yes," enter the amount of any tax incurred under section 4912  xpath: /IRS990ScheduleC/Tax4912Amt 

    Mngrs4912TxAmt = Column(BigInteger)
    # Line number:  Part II-B Line 2c Column (b)  Description:  If "Yes," enter the amount of any tax incurred by organization managers under section 4912  xpath: /IRS990ScheduleC/Managers4912TaxAmt 

    Frm4720Fld4912TxInd = Column(String(length=5))
    # Line number:  Part II-B Line 2d Column (a)  Description:  If the filing organization incurred a section 4912 tax, did it file Form 4720 for this year?  xpath: /IRS990ScheduleC/Form4720Filed4912TaxInd 

#######
#
# IRS990ScheduleC - ScheduleC Part III-A : Political Campaign and Lobbying Activities 
#
#######

class skedc_part_iiia(Base):
    __tablename__='skedc_part_iiia'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SbstntllyAllDsNnddInd = Column(String(length=5))
    # Line number:  Part III-A Line 1  Description:  Were substantially all (90% or more) dues received nondeductible by members?  xpath: /IRS990ScheduleC/SubstantiallyAllDuesNondedInd 

    OnlyInHsLbbyngInd = Column(String(length=5))
    # Line number:  Part III-A Line 2  Description:  Did the organization make only in-house lobbying expenditures of $2,000 or less?  xpath: /IRS990ScheduleC/OnlyInHouseLobbyingInd 

    AgrCrryvrPrrYrInd = Column(String(length=5))
    # Line number:  Part III-A Line 3  Description:  Did the organization agree to carryover lobbying and political expenditures from the prior year?  xpath: /IRS990ScheduleC/AgreeCarryoverPriorYearInd 

#######
#
# IRS990ScheduleC - ScheduleC Part III-B : Political Campaign and Lobbying Activities 
#
#######

class skedc_part_iiib(Base):
    __tablename__='skedc_part_iiib'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    DsAssssmntsAmt = Column(BigInteger)
    # Line number:  Part III-B Line 1  Description:  Dues, assessments and similar amounts from members  xpath: /IRS990ScheduleC/DuesAssessmentsAmt 

    NnDdctblLbbyngPltclCYAmt = Column(BigInteger)
    # Line number:  Part III-B Line 2a  Description:  Current year  xpath: /IRS990ScheduleC/NonDeductibleLbbyngPltclCYAmt 

    NnDdLbbyngPltclCyvAmt = Column(BigInteger)
    # Line number:  Part III-B Line 2b  Description:  Carryover from last year  xpath: /IRS990ScheduleC/NonDedLbbyngPltclCyovAmt 

    NnDdctblLbbyngPltclTtAmt = Column(BigInteger)
    # Line number:  Part III-B Line 2c  Description:  Total  xpath: /IRS990ScheduleC/NonDeductibleLbbyngPltclTotAmt 

    AggrgtRprtdDsNtcAmt = Column(BigInteger)
    # Line number:  Part III-B Line 3  Description:  Aggregate amount reported in section 6033(e)(1)(A) notices of nondeductible section 162(e) dues  xpath: /IRS990ScheduleC/AggregateReportedDuesNtcAmt 

    CrrdOvrAmt = Column(BigInteger)
    # Line number:  Part III-B Line 4  Description:  If notices were sent and the amount on line 2c exceeds the amount on line 3, what portion of that amount does the organization agree to carryover to the reasonable estimate of nondeductible lobbying and political expenditure next year?  xpath: /IRS990ScheduleC/CarriedOverAmt 

    TxblAmt = Column(BigInteger)
    # Line number:  Part III-B Line 5  Description:  Taxable amount of lobbying and political expenditures (line 2c total minus 3 and 4)  xpath: /IRS990ScheduleC/TaxableAmt 

#######
#
# IRS990ScheduleC - SupplementalInformationDetail
# A repeating structure from ScheduleC Part IV : Explanations 
#
#######

class SkdCSpplmntlInfrmtnDtl(Base):
    __tablename__='SkdCSpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtnDtl = Column(Text)
    # Description:  Part IV contents  xpath: /IRS990ScheduleC/SupplementalInformationDetail 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part IV  Description:  Form, part and line number reference  xpath: /IRS990ScheduleC/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part IV  Description:  Form, part and line number reference explanation  xpath: /IRS990ScheduleC/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleC - Section527PoliticalOrgGrp
# A repeating structure from ScheduleC Part 0 Prefatory material 
#
#######

class SkdCSctn527PltclOrg(Base):
    __tablename__='SkdCSctn527PltclOrg'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SkdC_Sctn527PltclOrg = Column(Text)
    # Description:  State the names, addresses and Employer Identification Number (EIN) of all section 527 political organizations to which payments were made  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp 

    OrgnztnBsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part I-C Line 5(a)  Description:  Business name line 1  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/OrganizationBusinessName/BusinessNameLine1Txt 

    OrgnztnBsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part I-C Line 5(a)  Description:  Business name line 2  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/OrganizationBusinessName/BusinessNameLine2Txt 

    Sctn527PltclOrg_EIN = Column(String(length=9))
    # Line number:  Part I-C Line 5(c)  Description:  EIN  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/EIN 

    Sctn527PltclOrg_PdIntrnlFndsAmt = Column(BigInteger)
    # Line number:  Part I-C Line 5(d)  Description:  Amount paid from internal funds  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/PaidInternalFundsAmt 

    Sctn527PltclOrg_CntrbtnsRcvdDlvrAmt = Column(BigInteger)
    # Line number:  Part I-C Line 5(e)  Description:  Amount of contributions received and delivered  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ContributionsRcvdDlvrAmt 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part I-C Line 5(b)  Description:  Address line 1  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part I-C Line 5(b)  Description:  Address line 2  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part I-C Line 5(b)  Description:  City  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part I-C Line 5(b)  Description:  State  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part I-C Line 5(b)  Description:  ZIP code  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part I-C Line 5(b)  Description:  Address line 1  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part I-C Line 5(b)  Description:  Address line 2  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part I-C Line 5(b)  Description:  City  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part I-C Line 5(b)  Description:  Province or state  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part I-C Line 5(b)  Description:  Country  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part I-C Line 5(b)  Description:  Postal code  xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ForeignAddress/ForeignPostalCd 

#######
#
# IRS990ScheduleD - ScheduleD Part I Organizations Maintaining Donor Advised Funds or Other Similar Funds or Accounts 
#
#######

class skedd_part_i(Base):
    __tablename__='skedd_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    DnrAdvsdFndsHldCnt = Column(BigInteger)
    # Line number:  Part I Line 1 Column (a)  Description:  Enter the total number of donor advised funds maintained at the end of the tax year  xpath: /IRS990ScheduleD/DonorAdvisedFundsHeldCnt 

    FndsAndOthrAccntsHldCnt = Column(BigInteger)
    # Line number:  Part I Line 1 Column (b)  Description:  Enter the total number of separate accounts for participating donors where donors have the right to provide advice on the use or distribution of funds owned at the end of the tax year  xpath: /IRS990ScheduleD/FundsAndOtherAccountsHeldCnt 

    DnrAdvsdFndsCntrAmt = Column(BigInteger)
    # Line number:  Part I Line 2 Column (a)  Description:  Contributions, gifts, grants, and similar amounts received: donor advised funds  xpath: /IRS990ScheduleD/DonorAdvisedFundsContriAmt 

    FndsAndOthrAccntsCntrAmt = Column(BigInteger)
    # Line number:  Part I Line 2 Column (b)  Description:  Contributions, gifts, grants, and similar amounts received: funds and other accounts  xpath: /IRS990ScheduleD/FundsAndOtherAccountsContriAmt 

    DnrAdvsdFndsGrntsAmt = Column(BigInteger)
    # Line number:  Part I Line 3 Column (a)  Description:  Grants and allocations from donor advised funds  xpath: /IRS990ScheduleD/DonorAdvisedFundsGrantsAmt 

    FndsAndOthrAccntsGrntsAmt = Column(BigInteger)
    # Line number:  Part I Line 3 Column (b)  Description:  Grants from funds and other accounts  xpath: /IRS990ScheduleD/FundsAndOtherAccountsGrantsAmt 

    DnrAdvsdFndsVlEOYAmt = Column(BigInteger)
    # Line number:  Part I Line 4 Column (a)  Description:  Enter the aggregate value of assets held in all donor advised funds at the end of the tax year  xpath: /IRS990ScheduleD/DonorAdvisedFundsVlEOYAmt 

    FndsAndOthrAccntsVlEOYAmt = Column(BigInteger)
    # Line number:  Part I Line 4 Column (b)  Description:  Enter the aggregate value of assets held in all funds and other accounts at the end of the tax year  xpath: /IRS990ScheduleD/FundsAndOtherAccountsVlEOYAmt 

    DsclsdOrgLgCtrlInd = Column(String(length=5))
    # Line number:  Part I Line 5  Description:  Did the organization inform all donors and donor advisors in writing that the assets held in DAFs are the organization's property, subject to the organization's exclusive legal control?  xpath: /IRS990ScheduleD/DisclosedOrgLegCtrlInd 

    DsclsdFrChrtblPrpsInd = Column(String(length=5))
    # Line number:  Part I Line 6  Description:  Did the organization inform all grantees, donors, and donor advisors in writing that grant funds may be used only for charitable purposes and not for the benefit of the donor or donor advisor?  xpath: /IRS990ScheduleD/DisclosedForCharitablePrpsInd 

#######
#
# IRS990ScheduleD - ScheduleD Part II Conservation Easements 
#
#######

class skedd_part_ii(Base):
    __tablename__='skedd_part_ii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    PrsrvtnPblcUsInd = Column(String(length=1))
    # Line number:  Part II Line 1  Description:  Preservation for  public use  xpath: /IRS990ScheduleD/PreservationPublicUseInd 

    PrtctnNtrlHbttInd = Column(String(length=1))
    # Line number:  Part II Line 1  Description:  Protection of natural habitat  xpath: /IRS990ScheduleD/ProtectionNaturalHabitatInd 

    PrsrvtnOpnSpcInd = Column(String(length=1))
    # Line number:  Part II Line 1  Description:  Preservation of open space  xpath: /IRS990ScheduleD/PreservationOpenSpaceInd 

    HstrcLndArInd = Column(String(length=1))
    # Line number:  Part II Line 1  Description:  Historic land area  xpath: /IRS990ScheduleD/HistoricLandAreaInd 

    HstrcStrctrInd = Column(String(length=1))
    # Line number:  Part II Line 1  Description:  Historic structure  xpath: /IRS990ScheduleD/HistoricStructureInd 

    TtlEsmntsCnt = Column(BigInteger)
    # Line number:  Part II Line 2a  Description:  Total number of easements  xpath: /IRS990ScheduleD/TotalEasementsCnt 

    TtlAcrgCnt = Column(Numeric(precision=22))
    # Line number:  Part II Line 2b  Description:  Total acreage subject to easements  xpath: /IRS990ScheduleD/TotalAcreageCnt 

    HstrcStrctrEsmntsCnt = Column(BigInteger)
    # Line number:  Part II Line 2c  Description:  Number of easements on a certified historic structure included in (a)  xpath: /IRS990ScheduleD/HistoricStructureEasementsCnt 

    HstrcStrctrEsmntsAftrCnt = Column(BigInteger)
    # Line number:  Part II Line 2d  Description:  Number of historic structure easements acquired after 8-17-2006  xpath: /IRS990ScheduleD/HistoricStrctrEasementsAftrCnt 

    MdfdEsmntsCnt = Column(BigInteger)
    # Line number:  Part II Line 3  Description:  Number of conservation easements modified, transferred, released, or terminated by the organization during the taxable year  xpath: /IRS990ScheduleD/ModifiedEasementsCnt 

    SttsEsmntsHldCnt = Column(BigInteger)
    # Line number:  Part II Line 4  Description:  Number of states in which the organization held an easement  xpath: /IRS990ScheduleD/StatesEasementsHeldCnt 

    WrttnPlcyMntrngInd = Column(String(length=5))
    # Line number:  Part II Line 5  Description:  Does the organization have a written policy regarding the periodic monitoring, inspection, and enforcement of the easements it holds?  xpath: /IRS990ScheduleD/WrittenPolicyMonitoringInd 

    StffHrsSpntEnfrcmntCnt = Column(Numeric(precision=22))
    # Line number:  Part II Line 6  Description:  Staff hours devoted to monitoring or enforcing easements during the year  xpath: /IRS990ScheduleD/StaffHoursSpentEnforcementCnt 

    ExpnssIncrrdEnfrcmntAmt = Column(BigInteger)
    # Line number:  Part II Line 7  Description:  Amount of expenses incurred in monitoring or enforcing easements during the taxable year  xpath: /IRS990ScheduleD/ExpensesIncurredEnforcementAmt 

    Sctn170hRqrStsfdInd = Column(String(length=5))
    # Line number:  Part II Line 8  Description:  Does each conservation easement reported on line 2(d) above satisfy the requirements of section 170(h)(4)(B)(i) and 170(h)(4)(B)(ii)?  xpath: /IRS990ScheduleD/Section170hRqrStsfdInd 

#######
#
# IRS990ScheduleD - ScheduleD Part III Organizations Maintaining Collections of Art, Historical Treasures, or Other Similar Assets 
#
#######

class skedd_part_iii(Base):
    __tablename__='skedd_part_iii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    ArtPblcExhbtnAmnts_RvnsInclddAmt = Column(BigInteger)
    # Line number:  Part III Line 1b(i) OR Line 2a  Description:  Revenues on Form 990, Part VIII, line 1  xpath: /IRS990ScheduleD/ArtPublicExhibitionAmountsGrp/RevenuesIncludedAmt 

    ArtPblcExhbtnAmnts_AsstsInclddAmt = Column(BigInteger)
    # Line number:  Part III Line 1b(ii) OR Line 2b  Description:  Assets in Form 990, Part X  xpath: /IRS990ScheduleD/ArtPublicExhibitionAmountsGrp/AssetsIncludedAmt 

    HldWrksArt_RvnsInclddAmt = Column(BigInteger)
    # Line number:  Part III Line 1b(i) OR Line 2a  Description:  Revenues on Form 990, Part VIII, line 1  xpath: /IRS990ScheduleD/HeldWorksArtGrp/RevenuesIncludedAmt 

    HldWrksArt_AsstsInclddAmt = Column(BigInteger)
    # Line number:  Part III Line 1b(ii) OR Line 2b  Description:  Assets in Form 990, Part X  xpath: /IRS990ScheduleD/HeldWorksArtGrp/AssetsIncludedAmt 

    SkdD_CllctnUsdPbExhbtnInd = Column(String(length=1))
    # Line number:  Part III Line 3a  Description:  Collection used for public exhibition  xpath: /IRS990ScheduleD/CollectionUsedPubExhibitionInd 

    SkdD_CllUsdSchlrlyRsrchInd = Column(String(length=1))
    # Line number:  Part III Line 3b  Description:  Collection used for scholarly research  xpath: /IRS990ScheduleD/CollUsedScholarlyRsrchInd 

    SkdD_CllctnUsdPrsrvtnInd = Column(String(length=1))
    # Line number:  Part III Line 3c  Description:  Collection used for preservation  xpath: /IRS990ScheduleD/CollectionUsedPreservationInd 

    SkdD_CllUsdLnOrExchPrgInd = Column(String(length=1))
    # Line number:  Part III Line 3d  Description:  Collection used for loan or exchange programs  xpath: /IRS990ScheduleD/CollUsedLoanOrExchProgInd 

    SkdD_CllctnUsdOthrPrpss = Column(Text)
    # Line number:  Part III Line 3e  Description:  Collection used for other purposes and description  xpath: /IRS990ScheduleD/CollectionUsedOtherPurposesGrp 

    CllctnUsdOthrPrpss_CllctnUsdOthrPrpssInd = Column(String(length=1))
    # Line number:  Part III Line 3e  Description:  Collection used for other purposes and description  xpath: /IRS990ScheduleD/CollectionUsedOtherPurposesGrp/CollectionUsedOtherPurposesInd 

    CllctnUsdOthrPrpss_OthrPrpssDsc = Column(String(length=100))
    # Line number:  Part III Line 3e  Description:  Collection used for other purposes and description  xpath: /IRS990ScheduleD/CollectionUsedOtherPurposesGrp/OtherPurposesDesc 

    SkdD_SlctdAsstsSlInd = Column(String(length=5))
    # Line number:  Part III Line 5  Description:  During the year, did the organization solicit or receive donations of art, historical treasures or other similar assets to be sold to raise funds rather than to be maintained as part of the organization's collection?  xpath: /IRS990ScheduleD/SolicitedAssetsSaleInd 

#######
#
# IRS990ScheduleD - ScheduleD Part IV Trust, Escrow and Custodial Arrangements 
#
#######

class skedd_part_iv(Base):
    __tablename__='skedd_part_iv'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    AgntTrstEtcInd = Column(String(length=5))
    # Line number:  Part IV Line 1a  Description:  Is the organization an agent, trustee, custodian or other intermediary for contributions or other assets not included on Form 990, Part X?  xpath: /IRS990ScheduleD/AgentTrusteeEtcInd 

    BgnnngBlncAmt = Column(BigInteger)
    # Line number:  Part IV Line 1c  Description:  Beginning balance  xpath: /IRS990ScheduleD/BeginningBalanceAmt 

    AddtnsDrngYrAmt = Column(BigInteger)
    # Line number:  Part IV Line 1d  Description:  Additions during the year  xpath: /IRS990ScheduleD/AdditionsDuringYearAmt 

    DstrbtnsDrngYrAmt = Column(BigInteger)
    # Line number:  Part IV Line 1e  Description:  Distributions during the year  xpath: /IRS990ScheduleD/DistributionsDuringYearAmt 

    EndngBlncAmt = Column(BigInteger)
    # Line number:  Part IV Line 1f  Description:  Ending balance  xpath: /IRS990ScheduleD/EndingBalanceAmt 

    InclEscrwCstdlAcctLbInd = Column(String(length=5))
    # Line number:  Part IV Line 2a  Description:  Did the organization include an amount on Form 990, Part X, line 21?  xpath: /IRS990ScheduleD/InclEscrowCustodialAcctLiabInd 

    ExplntnPrvddInd = Column(String(length=1))
    # Line number:  Part IV Line 2b  Description:  Part XIII contains an explanation for Part IV, Line 2b  xpath: /IRS990ScheduleD/ExplanationProvidedInd 

#######
#
# IRS990ScheduleD - ScheduleD Part V Endowment Funds 
#
#######

class skedd_part_v(Base):
    __tablename__='skedd_part_v'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    CYEndwmtFnd_BgnnngYrBlncAmt = Column(BigInteger)
    # Line number:  Part V Line 1a  Description:  Beginning of year balance  xpath: /IRS990ScheduleD/CYEndwmtFundGrp/BeginningYearBalanceAmt 

    CYEndwmtFnd_CntrbtnsAmt = Column(BigInteger)
    # Line number:  Part V Line 1b  Description:  Contributions  xpath: /IRS990ScheduleD/CYEndwmtFundGrp/ContributionsAmt 

    CYEndwmtFnd_InvstmntErnngsOrLsssAmt = Column(BigInteger)
    # Line number:  Part V Line 1c  Description:  Investment earnings or losses  xpath: /IRS990ScheduleD/CYEndwmtFundGrp/InvestmentEarningsOrLossesAmt 

    CYEndwmtFnd_GrntsOrSchlrshpsAmt = Column(BigInteger)
    # Line number:  Part V Line 1d  Description:  Grants or scholarships  xpath: /IRS990ScheduleD/CYEndwmtFundGrp/GrantsOrScholarshipsAmt 

    CYEndwmtFnd_OthrExpndtrsAmt = Column(BigInteger)
    # Line number:  Part V Line 1e  Description:  Other expenditures  xpath: /IRS990ScheduleD/CYEndwmtFundGrp/OtherExpendituresAmt 

    CYEndwmtFnd_AdmnstrtvExpnssAmt = Column(BigInteger)
    # Line number:  Part V Line 1f  Description:  Administrative expenses  xpath: /IRS990ScheduleD/CYEndwmtFundGrp/AdministrativeExpensesAmt 

    CYEndwmtFnd_EndYrBlncAmt = Column(BigInteger)
    # Line number:  Part V Line 1g  Description:  End of year balance  xpath: /IRS990ScheduleD/CYEndwmtFundGrp/EndYearBalanceAmt 

    CYMns1YrEndwmtFnd_BgnnngYrBlncAmt = Column(BigInteger)
    # Line number:  Part V Line 1a  Description:  Beginning of year balance  xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/BeginningYearBalanceAmt 

    CYMns1YrEndwmtFnd_CntrbtnsAmt = Column(BigInteger)
    # Line number:  Part V Line 1b  Description:  Contributions  xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/ContributionsAmt 

    CYMns1YrEndwmtFnd_InvstmntErnngsOrLsssAmt = Column(BigInteger)
    # Line number:  Part V Line 1c  Description:  Investment earnings or losses  xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/InvestmentEarningsOrLossesAmt 

    CYMns1YrEndwmtFnd_GrntsOrSchlrshpsAmt = Column(BigInteger)
    # Line number:  Part V Line 1d  Description:  Grants or scholarships  xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/GrantsOrScholarshipsAmt 

    CYMns1YrEndwmtFnd_OthrExpndtrsAmt = Column(BigInteger)
    # Line number:  Part V Line 1e  Description:  Other expenditures  xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/OtherExpendituresAmt 

    CYMns1YrEndwmtFnd_AdmnstrtvExpnssAmt = Column(BigInteger)
    # Line number:  Part V Line 1f  Description:  Administrative expenses  xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/AdministrativeExpensesAmt 

    CYMns1YrEndwmtFnd_EndYrBlncAmt = Column(BigInteger)
    # Line number:  Part V Line 1g  Description:  End of year balance  xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/EndYearBalanceAmt 

    CYMns2YrEndwmtFnd_BgnnngYrBlncAmt = Column(BigInteger)
    # Line number:  Part V Line 1a  Description:  Beginning of year balance  xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/BeginningYearBalanceAmt 

    CYMns2YrEndwmtFnd_CntrbtnsAmt = Column(BigInteger)
    # Line number:  Part V Line 1b  Description:  Contributions  xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/ContributionsAmt 

    CYMns2YrEndwmtFnd_InvstmntErnngsOrLsssAmt = Column(BigInteger)
    # Line number:  Part V Line 1c  Description:  Investment earnings or losses  xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/InvestmentEarningsOrLossesAmt 

    CYMns2YrEndwmtFnd_GrntsOrSchlrshpsAmt = Column(BigInteger)
    # Line number:  Part V Line 1d  Description:  Grants or scholarships  xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/GrantsOrScholarshipsAmt 

    CYMns2YrEndwmtFnd_OthrExpndtrsAmt = Column(BigInteger)
    # Line number:  Part V Line 1e  Description:  Other expenditures  xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/OtherExpendituresAmt 

    CYMns2YrEndwmtFnd_AdmnstrtvExpnssAmt = Column(BigInteger)
    # Line number:  Part V Line 1f  Description:  Administrative expenses  xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/AdministrativeExpensesAmt 

    CYMns2YrEndwmtFnd_EndYrBlncAmt = Column(BigInteger)
    # Line number:  Part V Line 1g  Description:  End of year balance  xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/EndYearBalanceAmt 

    CYMns3YrEndwmtFnd_BgnnngYrBlncAmt = Column(BigInteger)
    # Line number:  Part V Line 1a  Description:  Beginning of year balance  xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/BeginningYearBalanceAmt 

    CYMns3YrEndwmtFnd_CntrbtnsAmt = Column(BigInteger)
    # Line number:  Part V Line 1b  Description:  Contributions  xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/ContributionsAmt 

    CYMns3YrEndwmtFnd_InvstmntErnngsOrLsssAmt = Column(BigInteger)
    # Line number:  Part V Line 1c  Description:  Investment earnings or losses  xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/InvestmentEarningsOrLossesAmt 

    CYMns3YrEndwmtFnd_GrntsOrSchlrshpsAmt = Column(BigInteger)
    # Line number:  Part V Line 1d  Description:  Grants or scholarships  xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/GrantsOrScholarshipsAmt 

    CYMns3YrEndwmtFnd_OthrExpndtrsAmt = Column(BigInteger)
    # Line number:  Part V Line 1e  Description:  Other expenditures  xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/OtherExpendituresAmt 

    CYMns3YrEndwmtFnd_AdmnstrtvExpnssAmt = Column(BigInteger)
    # Line number:  Part V Line 1f  Description:  Administrative expenses  xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/AdministrativeExpensesAmt 

    CYMns3YrEndwmtFnd_EndYrBlncAmt = Column(BigInteger)
    # Line number:  Part V Line 1g  Description:  End of year balance  xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/EndYearBalanceAmt 

    CYMns4YrEndwmtFnd_BgnnngYrBlncAmt = Column(BigInteger)
    # Line number:  Part V Line 1a  Description:  Beginning of year balance  xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/BeginningYearBalanceAmt 

    CYMns4YrEndwmtFnd_CntrbtnsAmt = Column(BigInteger)
    # Line number:  Part V Line 1b  Description:  Contributions  xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/ContributionsAmt 

    CYMns4YrEndwmtFnd_InvstmntErnngsOrLsssAmt = Column(BigInteger)
    # Line number:  Part V Line 1c  Description:  Investment earnings or losses  xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/InvestmentEarningsOrLossesAmt 

    CYMns4YrEndwmtFnd_GrntsOrSchlrshpsAmt = Column(BigInteger)
    # Line number:  Part V Line 1d  Description:  Grants or scholarships  xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/GrantsOrScholarshipsAmt 

    CYMns4YrEndwmtFnd_OthrExpndtrsAmt = Column(BigInteger)
    # Line number:  Part V Line 1e  Description:  Other expenditures  xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/OtherExpendituresAmt 

    CYMns4YrEndwmtFnd_AdmnstrtvExpnssAmt = Column(BigInteger)
    # Line number:  Part V Line 1f  Description:  Administrative expenses  xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/AdministrativeExpensesAmt 

    CYMns4YrEndwmtFnd_EndYrBlncAmt = Column(BigInteger)
    # Line number:  Part V Line 1g  Description:  End of year balance  xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/EndYearBalanceAmt 

    SkdD_BrdDsgntdBlncEOYPct = Column(Numeric(precision=6))
    # Line number:  Part V Line 2a  Description:  Board designated EOY balance  xpath: /IRS990ScheduleD/BoardDesignatedBalanceEOYPct 

    SkdD_PrmnntEndwmntBlncEOYPct = Column(Numeric(precision=6))
    # Line number:  Part V Line 2b  Description:  Permanent endowment EOY balance  xpath: /IRS990ScheduleD/PrmnntEndowmentBalanceEOYPct 

    SkdD_TrmEndwmntBlncEOYPct = Column(Numeric(precision=6))
    # Line number:  Part V Line 2c  Description:  Term endowment EOY balance  xpath: /IRS990ScheduleD/TermEndowmentBalanceEOYPct 

    SkdD_EndwmntsHldUnrltdOrgInd = Column(String(length=5))
    # Line number:  Part V Line 3a(i)  Description:  Endowments held by unrelated organizations?  xpath: /IRS990ScheduleD/EndowmentsHeldUnrelatedOrgInd 

    SkdD_EndwmntsHldRltdOrgInd = Column(String(length=5))
    # Line number:  Part V Line 3a(ii)  Description:  Endowments held by related organizations?  xpath: /IRS990ScheduleD/EndowmentsHeldRelatedOrgInd 

    SkdD_RltdOrgLstSchRInd = Column(String(length=5))
    # Line number:  Part V Line 3b  Description:  Are related orgs listed on Schedule R?  xpath: /IRS990ScheduleD/RelatedOrgListSchRInd 

#######
#
# IRS990ScheduleD - ScheduleD Part VI Land, Buildings and Equipment 
#
#######

class skedd_part_vi(Base):
    __tablename__='skedd_part_vi'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Bldngs_DprctnAmt = Column(BigInteger)
    # Line number:  Part VI Column (c)  Description:  Depreciation  xpath: /IRS990ScheduleD/BuildingsGrp/DepreciationAmt 

    LshldImprvmnts_DprctnAmt = Column(BigInteger)
    # Line number:  Part VI Column (c)  Description:  Depreciation  xpath: /IRS990ScheduleD/LeaseholdImprovementsGrp/DepreciationAmt 

    Eqpmnt_DprctnAmt = Column(BigInteger)
    # Line number:  Part VI Column (c)  Description:  Depreciation  xpath: /IRS990ScheduleD/EquipmentGrp/DepreciationAmt 

    OthrLndBldngs_DprctnAmt = Column(BigInteger)
    # Line number:  Part VI Column (c)  Description:  Depreciation  xpath: /IRS990ScheduleD/OtherLandBuildingsGrp/DepreciationAmt 

    SkdD_TtlBkVlLndBldngsAmt = Column(BigInteger)
    # Line number:  Part VI Line 1  Description:  Total of book value  xpath: /IRS990ScheduleD/TotalBookValueLandBuildingsAmt 

    Lnd_InvstmntCstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part VI Column (a)  Description:  Investment cost or other basis  xpath: /IRS990ScheduleD/LandGrp/InvestmentCostOrOtherBasisAmt 

    Bldngs_InvstmntCstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part VI Column (a)  Description:  Investment cost or other basis  xpath: /IRS990ScheduleD/BuildingsGrp/InvestmentCostOrOtherBasisAmt 

    Eqpmnt_InvstmntCstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part VI Column (a)  Description:  Investment cost or other basis  xpath: /IRS990ScheduleD/EquipmentGrp/InvestmentCostOrOtherBasisAmt 

    LshldImprvmnts_InvstmntCstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part VI Column (a)  Description:  Investment cost or other basis  xpath: /IRS990ScheduleD/LeaseholdImprovementsGrp/InvestmentCostOrOtherBasisAmt 

    OthrLndBldngs_InvstmntCstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part VI Column (a)  Description:  Investment cost or other basis  xpath: /IRS990ScheduleD/OtherLandBuildingsGrp/InvestmentCostOrOtherBasisAmt 

    LshldImprvmnts_OthrCstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part VI Column (b)  Description:  Other cost or other basis  xpath: /IRS990ScheduleD/LeaseholdImprovementsGrp/OtherCostOrOtherBasisAmt 

    OthrLndBldngs_OthrCstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part VI Column (b)  Description:  Other cost or other basis  xpath: /IRS990ScheduleD/OtherLandBuildingsGrp/OtherCostOrOtherBasisAmt 

    Bldngs_OthrCstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part VI Column (b)  Description:  Other cost or other basis  xpath: /IRS990ScheduleD/BuildingsGrp/OtherCostOrOtherBasisAmt 

    Lnd_OthrCstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part VI Column (b)  Description:  Other cost or other basis  xpath: /IRS990ScheduleD/LandGrp/OtherCostOrOtherBasisAmt 

    Eqpmnt_OthrCstOrOthrBssAmt = Column(BigInteger)
    # Line number:  Part VI Column (b)  Description:  Other cost or other basis  xpath: /IRS990ScheduleD/EquipmentGrp/OtherCostOrOtherBasisAmt 

    Bldngs_BkVlAmt = Column(BigInteger)
    # Line number:  Part VI Column (d)  Description:  Book value  xpath: /IRS990ScheduleD/BuildingsGrp/BookValueAmt 

    Lnd_BkVlAmt = Column(BigInteger)
    # Line number:  Part VI Column (d)  Description:  Book value  xpath: /IRS990ScheduleD/LandGrp/BookValueAmt 

    LshldImprvmnts_BkVlAmt = Column(BigInteger)
    # Line number:  Part VI Column (d)  Description:  Book value  xpath: /IRS990ScheduleD/LeaseholdImprovementsGrp/BookValueAmt 

    OthrLndBldngs_BkVlAmt = Column(BigInteger)
    # Line number:  Part VI Column (d)  Description:  Book value  xpath: /IRS990ScheduleD/OtherLandBuildingsGrp/BookValueAmt 

    Eqpmnt_BkVlAmt = Column(BigInteger)
    # Line number:  Part VI Column (d)  Description:  Book value  xpath: /IRS990ScheduleD/EquipmentGrp/BookValueAmt 

#######
#
# IRS990ScheduleD - ScheduleD Part VII Investments, Other Securities
#
#######

class skedd_part_vii(Base):
    __tablename__='skedd_part_vii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SkdD_TtlBkVlScrtsAmt = Column(BigInteger)
    # Line number:  Part VII Column (b)  Description:  Total of book value  xpath: /IRS990ScheduleD/TotalBookValueSecuritiesAmt 

    ClslyHldEqtyIntrsts_BkVlAmt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Book value  xpath: /IRS990ScheduleD/CloselyHeldEquityInterestsGrp/BookValueAmt 

    FnnclDrvtvs_BkVlAmt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Book value  xpath: /IRS990ScheduleD/FinancialDerivativesGrp/BookValueAmt 

    ClslyHldEqtyIntrsts_MthdVltnCd = Column(Text)
    # Line number:  Column (c)  Description:  Method of valuation  xpath: /IRS990ScheduleD/CloselyHeldEquityInterestsGrp/MethodValuationCd 

    FnnclDrvtvs_MthdVltnCd = Column(Text)
    # Line number:  Column (c)  Description:  Method of valuation  xpath: /IRS990ScheduleD/FinancialDerivativesGrp/MethodValuationCd 

#######
#
# IRS990ScheduleD - ScheduleD Part VIII Investments - Program Related 
#
#######

class skedd_part_viii(Base):
    __tablename__='skedd_part_viii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    TtlBkVlPrgrmRltdAmt = Column(BigInteger)
    # Line number:  Part VIII Column (b)  Description:  Total of book value  xpath: /IRS990ScheduleD/TotalBookValueProgramRltdAmt 

#######
#
# IRS990ScheduleD - ScheduleD Part IX Other Assets 
#
#######

class skedd_part_ix(Base):
    __tablename__='skedd_part_ix'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    TtlBkVlOthrAsstsAmt = Column(BigInteger)
    # Line number:  Part IX Column (b)  Description:  Total book value  xpath: /IRS990ScheduleD/TotalBookValueOtherAssetsAmt 

#######
#
# IRS990ScheduleD - ScheduleD Part X Other Liabilities 
#
#######

class skedd_part_x(Base):
    __tablename__='skedd_part_x'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    FdrlIncmTxLbltyAmt = Column(BigInteger)
    # Line number:  Part X Column (b)  Description:  Federal income tax liability  xpath: /IRS990ScheduleD/FederalIncomeTaxLiabilityAmt 

    TtlLbltyAmt = Column(BigInteger)
    # Line number:  Part X Column (b)  Description:  Total of liability amounts  xpath: /IRS990ScheduleD/TotalLiabilityAmt 

    FtntTxtInd = Column(String(length=1))
    # Line number:  Part X Line 2  Description:  Part XIII contains the text of the footnote for Part X, Line 2  xpath: /IRS990ScheduleD/FootnoteTextInd 

#######
#
# IRS990ScheduleD - ScheduleD Part XI Reconciliation of Revenue per Audited Financial Statements with Revenue per Return 
#
#######

class skedd_part_xi(Base):
    __tablename__='skedd_part_xi'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    TtlRvEtcAdtdFnclStmtAmt = Column(BigInteger)
    # Line number:  Part XI Line 1  Description:  Total revenue, gains and other support per audited financial statments  xpath: /IRS990ScheduleD/TotalRevEtcAuditedFinclStmtAmt 

    NtUnrlzdGnsInvstAmt = Column(BigInteger)
    # Line number:  Part XI Line 2a  Description:  Net unrealized gains on investments  xpath: /IRS990ScheduleD/NetUnrealizedGainsInvstAmt 

    DntdSrvcsAndUsFcltsAmt = Column(BigInteger)
    # Line number:  Part XI Line 2b  Description:  Donated services and use of facilities  xpath: /IRS990ScheduleD/DonatedServicesAndUseFcltsAmt 

    RcvrsPrrYrGrntsAmt = Column(BigInteger)
    # Line number:  Part XI Line 2c  Description:  Recoveries of prior year grants  xpath: /IRS990ScheduleD/RecoveriesPriorYearGrantsAmt 

    OthrRvnAmt = Column(BigInteger)
    # Line number:  Part XI Line 2d  Description:  Other revenues  xpath: /IRS990ScheduleD/OtherRevenueAmt 

    RvnNtRprtdAmt = Column(BigInteger)
    # Line number:  Part XI Line 2e  Description:  Total amounts, add lines 2a through 2d  xpath: /IRS990ScheduleD/RevenueNotReportedAmt 

    RvnSbttlAmt = Column(BigInteger)
    # Line number:  Part XI Line 3  Description:  Part XI line 1 minus Part XI line 2e  xpath: /IRS990ScheduleD/RevenueSubtotalAmt 

    InvstmntExpnssNtIncldAmt = Column(BigInteger)
    # Line number:  Part XI Line 4a  Description:  Investment expenses not included on Form 990, Part VIII, line 7b  xpath: /IRS990ScheduleD/InvestmentExpensesNotIncldAmt 

    OthrRvnsNtInclddAmt = Column(BigInteger)
    # Line number:  Part XI Line 4b  Description:  Other revenues not included  xpath: /IRS990ScheduleD/OtherRevenuesNotIncludedAmt 

    RvnNtRprtdFnclStmtAmt = Column(BigInteger)
    # Line number:  Part XI Line 4c  Description:  Total amounts, add lines 4a and 4b  xpath: /IRS990ScheduleD/RevenueNotReportedFinclStmtAmt 

    TtlRvnPrFrm990Amt = Column(BigInteger)
    # Line number:  Part XI Line 5  Description:  Total revenue (Form 990, Part 1, Line 12). Add lines 3 and 4c  xpath: /IRS990ScheduleD/TotalRevenuePerForm990Amt 

#######
#
# IRS990ScheduleD - ScheduleD Part XII Reconciliation of Expenses per Audited Financial Statements with Expenses per Return 
#
#######

class skedd_part_xii(Base):
    __tablename__='skedd_part_xii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    TtExpnsEtcAdtdFnclStmtAmt = Column(BigInteger)
    # Line number:  Part XII Line 1  Description:  Total Expenses, and Losses per audited financial statments  xpath: /IRS990ScheduleD/TotExpnsEtcAuditedFinclStmtAmt 

    DntdSrvcsUsFcltsAmt = Column(BigInteger)
    # Line number:  Part XII Line 2a  Description:  Donated Services and Use of Facilities  xpath: /IRS990ScheduleD/DonatedServicesUseFcltsAmt 

    PrrYrAdjstmntsAmt = Column(BigInteger)
    # Line number:  Part XII Line 2b  Description:  Prior year adjustments  xpath: /IRS990ScheduleD/PriorYearAdjustmentsAmt 

    LsssRprtdAmt = Column(BigInteger)
    # Line number:  Part XII Line 2c  Description:  Losses reported  xpath: /IRS990ScheduleD/LossesReportedAmt 

    OthrExpnssInclddAmt = Column(BigInteger)
    # Line number:  Part XII Line 2d  Description:  Other expenses included  xpath: /IRS990ScheduleD/OtherExpensesIncludedAmt 

    ExpnssNtRprtdAmt = Column(BigInteger)
    # Line number:  Part XII Line 2e  Description:  Total amounts, add lines 2a through 2d  xpath: /IRS990ScheduleD/ExpensesNotReportedAmt 

    ExpnssSbttlAmt = Column(BigInteger)
    # Line number:  Part XII Line 3  Description:  Part XII line 1 minus Part XII line 2e  xpath: /IRS990ScheduleD/ExpensesSubtotalAmt 

    InvstmntExpnssNtIncld2Amt = Column(BigInteger)
    # Line number:  Part XII Line 4a  Description:  Investment expenses not included on Form 990, Part VIII, line 7b  xpath: /IRS990ScheduleD/InvestmentExpensesNotIncld2Amt 

    OthrExpnssNtInclddAmt = Column(BigInteger)
    # Line number:  Part XII Line 4b  Description:  Other expenses  xpath: /IRS990ScheduleD/OtherExpensesNotIncludedAmt 

    ExpnssNtRptFnclStmtAmt = Column(BigInteger)
    # Line number:  Part XII Line 4c  Description:  Total amounts, add lines 4a through 4b  xpath: /IRS990ScheduleD/ExpensesNotRptFinclStmtAmt 

    TtlExpnssPrFrm990Amt = Column(BigInteger)
    # Line number:  Part XII Line 5  Description:  Total expenses (Form 990, Part I, Line 18). Add lines 3 and 4c  xpath: /IRS990ScheduleD/TotalExpensesPerForm990Amt 

#######
#
# IRS990ScheduleD - OtherSecuritiesGrp
# A repeating structure from ScheduleD Part VII Investments, Other Securities
#
#######

class SkdDOthrScrts(Base):
    __tablename__='SkdDOthrScrts'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Dsc = Column(String(length=100))
    # Line number:  Column (a)  Description:  Description  xpath: /IRS990ScheduleD/OtherSecuritiesGrp/Desc 

    BkVlAmt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Book value  xpath: /IRS990ScheduleD/OtherSecuritiesGrp/BookValueAmt 

    MthdVltnCd = Column(Text)
    # Line number:  Column (c)  Description:  Method of valuation  xpath: /IRS990ScheduleD/OtherSecuritiesGrp/MethodValuationCd 

#######
#
# IRS990ScheduleD - SupplementalInformationDetail
# A repeating structure from ScheduleD Part XIII Supplemental Information 
#
#######

class SkdDSpplmntlInfrmtnDtl(Base):
    __tablename__='SkdDSpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtnDtl = Column(Text)
    # Description:  Part XIII contents  xpath: /IRS990ScheduleD/SupplementalInformationDetail 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part XIII  Description:  Form part and line number reference  xpath: /IRS990ScheduleD/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part XIII  Description:  Form part and line number reference explanation  xpath: /IRS990ScheduleD/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleD - InvstProgramRelatedOrgGrp
# A repeating structure from ScheduleD Part VIII Investments - Program Related 
#
#######

class SkdDInvstPrgrmRltdOrg(Base):
    __tablename__='SkdDInvstPrgrmRltdOrg'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Dsc = Column(String(length=100))
    # Line number:  Column (a)  Description:  Description  xpath: /IRS990ScheduleD/InvstProgramRelatedOrgGrp/Desc 

    BkVlAmt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Book value  xpath: /IRS990ScheduleD/InvstProgramRelatedOrgGrp/BookValueAmt 

    MthdVltnCd = Column(Text)
    # Line number:  Column (c)  Description:  Method of valuation  xpath: /IRS990ScheduleD/InvstProgramRelatedOrgGrp/MethodValuationCd 

#######
#
# IRS990ScheduleD - OtherLiabilitiesOrgGrp
# A repeating structure from ScheduleD Part X Other Liabilities 
#
#######

class SkdDOthrLbltsOrg(Base):
    __tablename__='SkdDOthrLbltsOrg'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Dsc = Column(String(length=100))
    # Line number:  Column (a)  Description:  Description  xpath: /IRS990ScheduleD/OtherLiabilitiesOrgGrp/Desc 

    Amt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Amount  xpath: /IRS990ScheduleD/OtherLiabilitiesOrgGrp/Amt 

#######
#
# IRS990ScheduleD - OtherAssetsOrgGrp
# A repeating structure from ScheduleD Part IX Other Assets 
#
#######

class SkdDOthrAsstsOrg(Base):
    __tablename__='SkdDOthrAsstsOrg'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Dsc = Column(String(length=100))
    # Line number:  Column (a)  Description:  Description  xpath: /IRS990ScheduleD/OtherAssetsOrgGrp/Desc 

    BkVlAmt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Book value  xpath: /IRS990ScheduleD/OtherAssetsOrgGrp/BookValueAmt 

#######
#
# IRS990ScheduleE - ScheduleE Part I 
#
#######

class skede_part_i(Base):
    __tablename__='skede_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    NndscrmntryPlcyStmtInd = Column(String(length=5))
    # Line number:  Line 1  Description:  Does the organization have a racially nondiscriminatory policy statement?  xpath: /IRS990ScheduleE/NondiscriminatoryPolicyStmtInd 

    PlcyStmtInBrchrsEtcInd = Column(String(length=5))
    # Line number:  Line 2  Description:  Does the organization have policy statement in brochures, etc?  xpath: /IRS990ScheduleE/PolicyStmtInBrochuresEtcInd 

    PlcyPblczdVBrdcstMdInd = Column(String(length=5))
    # Line number:  Line 3  Description:  Has the organization publicized the policy through broadcast media?  xpath: /IRS990ScheduleE/PlcyPblczdViaBroadcastMediaInd 

    MntnRclCmpRcsInd = Column(String(length=5))
    # Line number:  Line 4a  Description:  Does the organization maintain racial composition records?  xpath: /IRS990ScheduleE/MaintainRacialCompRecsInd 

    MntnSchlrshpsRcsInd = Column(String(length=5))
    # Line number:  Line 4b  Description:  Does the organization maintain scholarships records?  xpath: /IRS990ScheduleE/MaintainScholarshipsRecsInd 

    MntnCpyOfBrchrsEtcInd = Column(String(length=5))
    # Line number:  Line 4c  Description:  Does the organization maintain copies of brochures, etc?  xpath: /IRS990ScheduleE/MaintainCpyOfBrochuresEtcInd 

    MntnCpyOfAllSlInd = Column(String(length=5))
    # Line number:  Line 4d  Description:  Does the organization maintain copies of all solicitations?  xpath: /IRS990ScheduleE/MaintainCpyOfAllSolInd 

    DscrmntRcStdntsRghtsInd = Column(String(length=5))
    # Line number:  Line 5a  Description:  Does the organization discriminate by race in any way students' rights or privileges?  xpath: /IRS990ScheduleE/DiscriminateRaceStdntsRghtsInd 

    DscrmntRcAdmssPlcyInd = Column(String(length=5))
    # Line number:  Line 5b  Description:  Does the organization discriminate by race in any way admissions policies?  xpath: /IRS990ScheduleE/DiscriminateRaceAdmissPlcyInd 

    DscrmntRcEmplmFcltyInd = Column(String(length=5))
    # Line number:  Line 5c  Description:  Does the organization discriminate by race in any way employment of faculty or administrative staff?  xpath: /IRS990ScheduleE/DiscriminateRaceEmplmFcultyInd 

    DscrmntRcSchsInd = Column(String(length=5))
    # Line number:  Line 5d  Description:  Does the organization discriminate by race in any way scholarships or other financial assistance?  xpath: /IRS990ScheduleE/DiscriminateRaceSchsInd 

    DscrmntRcEdcPlcyInd = Column(String(length=5))
    # Line number:  Line 5e  Description:  Does the organization discriminate by race in any way educational policies?  xpath: /IRS990ScheduleE/DiscriminateRaceEducPlcyInd 

    DscrmntRcUsOfFcltsInd = Column(String(length=5))
    # Line number:  Line 5f  Description:  Does the organization discriminate by race in any way use of facilities?  xpath: /IRS990ScheduleE/DiscriminateRaceUseOfFcltsInd 

    DscrmntRcAthltPrgInd = Column(String(length=5))
    # Line number:  Line 5g  Description:  Does the organization discriminate by race in any way athletic programs?  xpath: /IRS990ScheduleE/DiscriminateRaceAthltProgInd 

    DscrmntRcOthrActyInd = Column(String(length=5))
    # Line number:  Line 5h  Description:  Does the organization discriminate by race in any way other extracurricular activities?  xpath: /IRS990ScheduleE/DiscriminateRaceOtherActyInd 

    GvrnmntFnnclAdRcvdInd = Column(String(length=5))
    # Line number:  Line 6a  Description:  Does the organization receive any financial aid or assistance from a governmental agency?  xpath: /IRS990ScheduleE/GovernmentFinancialAidRcvdInd 

    GvrnmntFnnclAdRvkdInd = Column(String(length=5))
    # Line number:  Line 6b  Description:  Has the organization's right to such aid ever been revoked or suspended?  xpath: /IRS990ScheduleE/GovernmentFinancialAidRvkdInd 

    CmplncWthRvPrc7550Ind = Column(String(length=5))
    # Line number:  Line 7  Description:  Compliance with Rev. Proc. 75-50, 1975-2 C.B. 587?  xpath: /IRS990ScheduleE/ComplianceWithRevProc7550Ind 

#######
#
# IRS990ScheduleE - SupplementalInformationDetail
# A repeating structure from ScheduleE Part II Supplemental Information 
#
#######

class SkdESpplmntlInfrmtnDtl(Base):
    __tablename__='SkdESpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtnDtl = Column(Text)
    # Description:  Part II contents  xpath: /IRS990ScheduleE/SupplementalInformationDetail 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part II  Description:  Form, part and line number reference  xpath: /IRS990ScheduleE/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part II  Description:  Form, part, and line number reference explanation  xpath: /IRS990ScheduleE/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleF - ScheduleF Part I General Activities Outside the U.S. 
#
#######

class skedf_part_i(Base):
    __tablename__='skedf_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    GrntRcrdsMntndInd = Column(String(length=5))
    # Line number:  Part I Line 1  Description:  For grantmakers: Does the organization maintain records to substantiate the amount of the grants or assistance, the grantees' eligibility for the grants or assistance, and the selection criteria used to award the grants or assistance?  xpath: /IRS990ScheduleF/GrantRecordsMaintainedInd 

    SbttlOffcsCnt = Column(BigInteger)
    # Line number:  Part I Line 3a Column (b)  Description:  Subtotal number of offices  xpath: /IRS990ScheduleF/SubtotalOfficesCnt 

    SbttlEmplysCnt = Column(BigInteger)
    # Line number:  Part I Line 3a Column (c)  Description:  Subtotal number of employees  xpath: /IRS990ScheduleF/SubtotalEmployeesCnt 

    CntnttnTtlOffcCnt = Column(BigInteger)
    # Line number:  Part I Line 3b Column (b)  Description:  Total offices from continuation sheets to Part I  xpath: /IRS990ScheduleF/ContinutationTotalOfficeCnt 

    CntnttnTtlEmplyCnt = Column(BigInteger)
    # Line number:  Part I Line 3b Column (c)  Description:  Total employees from continuation sheets to Part I  xpath: /IRS990ScheduleF/ContinutationTotalEmployeeCnt 

    TtlOffcCnt = Column(BigInteger)
    # Line number:  Part I Line 3c Column (b)  Description:  Total number of offices  xpath: /IRS990ScheduleF/TotalOfficeCnt 

    TtlEmplyCnt = Column(BigInteger)
    # Line number:  Part I Line 3c Column (c)  Description:  Total number of employees  xpath: /IRS990ScheduleF/TotalEmployeeCnt 

    SbttlSpntAmt = Column(BigInteger)
    # Line number:  Part I Line 3a Column (f)  Description:  Subtotal amount spent  xpath: /IRS990ScheduleF/SubtotalSpentAmt 

    CntntnSpntAmt = Column(BigInteger)
    # Line number:  Part I Line 3b Column (f)  Description:  Total amouunt from continuation sheets to Part I  xpath: /IRS990ScheduleF/ContinuationSpentAmt 

    TtlSpntAmt = Column(BigInteger)
    # Line number:  Part I Line 3c Column (f)  Description:  Total amount spent  xpath: /IRS990ScheduleF/TotalSpentAmt 

#######
#
# IRS990ScheduleF - ScheduleF Part II Grants and Other Assistance to Organizations or Entities Outside the United States 
#
#######

class skedf_part_ii(Base):
    __tablename__='skedf_part_ii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Ttl501c3OrgCnt = Column(BigInteger)
    # Line number:  Part II line 2  Description:  Total number of 501(c)(3) organizations  xpath: /IRS990ScheduleF/Total501c3OrgCnt 

    TtlOthrOrgCnt = Column(BigInteger)
    # Line number:  Part II line 3  Description:  Total number of other organizations or entities  xpath: /IRS990ScheduleF/TotalOtherOrgCnt 

#######
#
# IRS990ScheduleF - ScheduleF Part IV Foreign Forms 
#
#######

class skedf_part_iv(Base):
    __tablename__='skedf_part_iv'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    TrnsfrTFrgnCrpInd = Column(String(length=5))
    # Line number:  Part IV Line 1  Description:  Was the organization a U.S. transferor of property to a foreign corporation during the tax year?  xpath: /IRS990ScheduleF/TransferToForeignCorpInd 

    IntrstInFrgnTrstInd = Column(String(length=5))
    # Line number:  Part IV Line 2  Description:  Did the organization have an interest in a foreign trust during the tax year?  xpath: /IRS990ScheduleF/InterestInForeignTrustInd 

    FrgnCrpOwnrshpInd = Column(String(length=5))
    # Line number:  Part IV Line 3  Description:  Did the organization have an ownership interest in a foreign corporation during the tax year?  xpath: /IRS990ScheduleF/ForeignCorpOwnershipInd 

    PssvFrgnInvstmstCInd = Column(String(length=5))
    # Line number:  Part IV Line 4  Description:  Was the organization a direct or indirect shareholder of a passive foreign investment company or a qualified electing fund during the tax year?  xpath: /IRS990ScheduleF/PassiveForeignInvestmestCoInd 

    FrgnPrtnrshpInd = Column(String(length=5))
    # Line number:  Part IV Line 5  Description:  Did the organization have an ownership interest in a foreign partnership during the tax year?  xpath: /IRS990ScheduleF/ForeignPartnershipInd 

    BycttCntrsInd = Column(String(length=5))
    # Line number:  Part IV Line 6  Description:  Did the organization have any operations in or related to any boycotting countries during the tax year?  xpath: /IRS990ScheduleF/BoycottCountriesInd 

#######
#
# IRS990ScheduleF - SupplementalInformationDetail
# A repeating structure from ScheduleF Part V  Supplemental Information 
#
#######

class SkdFSpplmntlInfrmtnDtl(Base):
    __tablename__='SkdFSpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtnDtl = Column(Text)
    # Description:  Part V contents  xpath: /IRS990ScheduleF/SupplementalInformationDetail 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part V  Description:  Form, part and line number reference  xpath: /IRS990ScheduleF/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part V  Description:  Form, part and line number reference explanation  xpath: /IRS990ScheduleF/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleF - ForeignIndividualsGrantsGrp
# A repeating structure from ScheduleF Part III Grants and Other Assistance to Individuals Outside the United States 
#
#######

class SkdFFrgnIndvdlsGrnts(Base):
    __tablename__='SkdFFrgnIndvdlsGrnts'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    OfAssstncTxt = Column(Text)
    # Line number:  Column (a)  Description:  Type of assistance  xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/TypeOfAssistanceTxt 

    RgnTxt = Column(String(length=100))
    # Line number:  Column (b)  Description:  Region  xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/RegionTxt 

    RcpntCnt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Number of recipients  xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/RecipientCnt 

    CshGrntAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Amount of cash grant  xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/CashGrantAmt 

    MnnrOfCshDsbrsmntTxt = Column(String(length=100))
    # Line number:  Column (e)  Description:  Manner of cash disbursement  xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/MannerOfCashDisbursementTxt 

    NnCshAssstncAmt = Column(BigInteger)
    # Line number:  Column (f)  Description:  Amount of non-cash assistance  xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/NonCashAssistanceAmt 

    DscrptnOfNnCshAsstTxt = Column(Text)
    # Line number:  Column (g)  Description:  Description of non-cash assistance  xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/DescriptionOfNonCashAsstTxt 

    VltnMthdUsdDsc = Column(String(length=100))
    # Line number:  Column (h)  Description:  Method of valuation  xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/ValuationMethodUsedDesc 

#######
#
# IRS990ScheduleF - AccountActivitiesOutsideUSGrp
# A repeating structure from ScheduleF Part I General Activities Outside the U.S. 
#
#######

class SkdFAccntActvtsOtsdUS(Base):
    __tablename__='SkdFAccntActvtsOtsdUS'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    RgnTxt = Column(String(length=100))
    # Line number:  Part I Line 3 Column (a)  Description:  Region  xpath: /IRS990ScheduleF/AccountActivitiesOutsideUSGrp/RegionTxt 

    OffcsCnt = Column(BigInteger)
    # Line number:  Part I Line 3 Column (b)  Description:  Number of offices in the region  xpath: /IRS990ScheduleF/AccountActivitiesOutsideUSGrp/OfficesCnt 

    EmplyCnt = Column(BigInteger)
    # Line number:  Part I Line 3 Column (c)  Description:  Number of employees or agents in region  xpath: /IRS990ScheduleF/AccountActivitiesOutsideUSGrp/EmployeeCnt 

    OfActvtsCndctdTxt = Column(String(length=100))
    # Line number:  Part I Line 3 Column (d)  Description:  Activities conducted in region (by type) (i.e., fundraising, program services, grants to recipients located in the region)  xpath: /IRS990ScheduleF/AccountActivitiesOutsideUSGrp/TypeOfActivitiesConductedTxt 

    SpcfcSrvcsPrvddTxt = Column(Text)
    # Line number:  Part I Line 3 Column (e)  Description:  If activity listed in (d) is a program service, describe specific type of service(s) in region  xpath: /IRS990ScheduleF/AccountActivitiesOutsideUSGrp/SpecificServicesProvidedTxt 

    RgnTtlExpndtrsAmt = Column(BigInteger)
    # Line number:  Part I Line 3 Column (f)  Description:  Total expenditures in region  xpath: /IRS990ScheduleF/AccountActivitiesOutsideUSGrp/RegionTotalExpendituresAmt 

#######
#
# IRS990ScheduleF - GrantsToOrgOutsideUSGrp
# A repeating structure from ScheduleF Part II Grants and Other Assistance to Organizations or Entities Outside the United States 
#
#######

class SkdFGrntsTOrgOtsdUS(Base):
    __tablename__='SkdFGrntsTOrgOtsdUS'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    RgnTxt = Column(String(length=100))
    # Line number:  Column (c)  Description:  Region  xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/RegionTxt 

    PrpsOfGrntTxt = Column(Text)
    # Line number:  Column (d)  Description:  Purpose of grant  xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/PurposeOfGrantTxt 

    CshGrntAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Amount of cash grant  xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/CashGrantAmt 

    MnnrOfCshDsbrsmntTxt = Column(String(length=100))
    # Line number:  Column (f)  Description:  Manner of cash disbursement  xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/MannerOfCashDisbursementTxt 

    NnCshAssstncAmt = Column(BigInteger)
    # Line number:  Column (g)  Description:  Amount of non-cash assistance  xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/NonCashAssistanceAmt 

    DscrptnOfNnCshAsstTxt = Column(Text)
    # Line number:  Column (h)  Description:  Description of non-cash assistance  xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/DescriptionOfNonCashAsstTxt 

    VltnMthdUsdDsc = Column(String(length=100))
    # Line number:  Column (i)  Description:  Method of valuation  xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/ValuationMethodUsedDesc 

#######
#
# IRS990ScheduleG - ScheduleG Part I Fundraising Activities 
#
#######

class skedg_part_i(Base):
    __tablename__='skedg_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    MlSlcttnsInd = Column(String(length=1))
    # Line number:  Part I Line 1  Description:  Mail solicitations  xpath: /IRS990ScheduleG/MailSolicitationsInd 

    EmlSlcttnsInd = Column(String(length=1))
    # Line number:  Part I Line 1  Description:  Email solicitations  xpath: /IRS990ScheduleG/EmailSolicitationsInd 

    PhnSlcttnsInd = Column(String(length=1))
    # Line number:  Part I Line 1  Description:  Phone solicitations  xpath: /IRS990ScheduleG/PhoneSolicitationsInd 

    InPrsnSlcttnsInd = Column(String(length=1))
    # Line number:  Part I Line 1  Description:  In-person solicitations  xpath: /IRS990ScheduleG/InPersonSolicitationsInd 

    SlcttnOfNnGvtGrntsInd = Column(String(length=1))
    # Line number:  Part I Line 1  Description:  Solicitation of non-govt grants  xpath: /IRS990ScheduleG/SolicitationOfNonGovtGrantsInd 

    SlcttnOfGvtGrntsInd = Column(String(length=1))
    # Line number:  Part I Line 1  Description:  Solicitation of government grants  xpath: /IRS990ScheduleG/SolicitationOfGovtGrantsInd 

    SpclFndrsngEvntsInd = Column(String(length=1))
    # Line number:  Part I Line 1  Description:  Special fundraising events  xpath: /IRS990ScheduleG/SpecialFundraisingEventsInd 

    AgrmtPrfFndrsngActyInd = Column(String(length=5))
    # Line number:  Part I Line 2a  Description:  Did the organization have a written or oral agreement with any individual (including officers, directors, trustees or key employees listed in Form 990, Part VII) or entity in connection with professional fundraising activities?  xpath: /IRS990ScheduleG/AgrmtProfFundraisingActyInd 

    TtlGrssRcptsAmt = Column(BigInteger)
    # Line number:  Part I Line 2b(iv)  Description:  Total gross receipts  xpath: /IRS990ScheduleG/TotalGrossReceiptsAmt 

    TtlRtndByCntrctrsAmt = Column(BigInteger)
    # Line number:  Part I Line 2b(v)  Description:  Total retained by contractors  xpath: /IRS990ScheduleG/TotalRetainedByContractorsAmt 

    TtlNtTOrgnztnAmt = Column(BigInteger)
    # Line number:  Part I Line 2b(vi)  Description:  Total net to organization  xpath: /IRS990ScheduleG/TotalNetToOrganizationAmt 

    AllSttsCd = Column(Text)
    # Line number:  Part I Line 3  Description:  Literal for all states  xpath: /IRS990ScheduleG/AllStatesCd 

#######
#
# IRS990ScheduleG - ScheduleG Part II Events 
#
#######

class skedg_part_ii(Base):
    __tablename__='skedg_part_ii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Evnt1Nm = Column(String(length=100))
    # Line number:  Column (a)  Description:  Name of event no.1  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/Event1Nm 

    GrssRcptsEvnt1Amt = Column(BigInteger)
    # Line number:  Line 1 Column (a)  Description:  Gross receipts, event no.1  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossReceiptsEvent1Amt 

    ChrtblCntrEvnt1Amt = Column(BigInteger)
    # Line number:  Line 2 Column (a)  Description:  Charitable contributions, event no.1  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CharitableContriEvent1Amt 

    GrssRvnEvnt1Amt = Column(BigInteger)
    # Line number:  Line 3 Column (a)  Description:  Gross revenue, event no.1  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossRevenueEvent1Amt 

    CshPrzsEvnt1Amt = Column(BigInteger)
    # Line number:  Line 4 Column (a)  Description:  Cash prizes, event no.1  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CashPrizesEvent1Amt 

    NnCshPrzsEvnt1Amt = Column(BigInteger)
    # Line number:  Line 5 Column (a)  Description:  Non-cash prizes, event no.1  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/NonCashPrizesEvent1Amt 

    RntFcltyCstsEvnt1Amt = Column(BigInteger)
    # Line number:  Line 6 Column (a)  Description:  Rent or facility costs, event no.1  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/RentFacilityCostsEvent1Amt 

    FdAndBvrgEvnt1Amt = Column(BigInteger)
    # Line number:  Line 7 Column (a)  Description:  Food and beverage expenses, event no.1  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/FoodAndBeverageEvent1Amt 

    EntrtnmntEvnt1Amt = Column(BigInteger)
    # Line number:  Line 8 Column (a)  Description:  Entertainment expenses, event no.1  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/EntertainmentEvent1Amt 

    OthrDrctExpnssEvnt1Amt = Column(BigInteger)
    # Line number:  Line 9 Column (a)  Description:  Other direct expenses, event no.1  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/OtherDirectExpensesEvent1Amt 

    Evnt2Nm = Column(String(length=100))
    # Line number:  Column (b)  Description:  Name of event no.2  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/Event2Nm 

    GrssRcptsEvnt2Amt = Column(BigInteger)
    # Line number:  Line 1 Column (b)  Description:  Gross receipts, event no.2  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossReceiptsEvent2Amt 

    ChrtblCntrEvnt2Amt = Column(BigInteger)
    # Line number:  Line 2 Column (b)  Description:  Charitable contributions, event no.2  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CharitableContriEvent2Amt 

    GrssRvnEvnt2Amt = Column(BigInteger)
    # Line number:  Line 3 Column (b)  Description:  Gross revenue, event no.2  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossRevenueEvent2Amt 

    CshPrzsEvnt2Amt = Column(BigInteger)
    # Line number:  Line 4 Column (b)  Description:  Cash prizes, event no.2  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CashPrizesEvent2Amt 

    NnCshPrzsEvnt2Amt = Column(BigInteger)
    # Line number:  Line 5 Column (b)  Description:  Non-cash prizes, event no.2  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/NonCashPrizesEvent2Amt 

    RntFcltyCstsEvnt2Amt = Column(BigInteger)
    # Line number:  Line 6 Column (b)  Description:  Rent or facility costs, event no.2  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/RentFacilityCostsEvent2Amt 

    FdAndBvrgEvnt2Amt = Column(BigInteger)
    # Line number:  Line 7 Column (b)  Description:  Food and beverage expenses, event no.2  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/FoodAndBeverageEvent2Amt 

    EntrtnmntEvnt2Amt = Column(BigInteger)
    # Line number:  Line 8 Column (b)  Description:  Entertainment expenses, event no.2  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/EntertainmentEvent2Amt 

    OthrDrctExpnssEvnt2Amt = Column(BigInteger)
    # Line number:  Line 9 Column (b)  Description:  Other direct expenses, event no.2  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/OtherDirectExpensesEvent2Amt 

    OthrEvntsTtlCnt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Other events: total number  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/OtherEventsTotalCnt 

    GrssRcptsOthrEvntsAmt = Column(BigInteger)
    # Line number:  Line 1 Column (c)  Description:  Gross receipts, other events  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossReceiptsOtherEventsAmt 

    ChrtblCntrOthrEvntsAmt = Column(BigInteger)
    # Line number:  Line 2 Column (c)  Description:  Charitable contributions, other events  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CharitableContriOtherEventsAmt 

    GrssRvnOthrEvntsAmt = Column(BigInteger)
    # Line number:  Line 3 Column (c)  Description:  Gross revenue, other events  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossRevenueOtherEventsAmt 

    CshPrzsOthrEvntsAmt = Column(BigInteger)
    # Line number:  Line 4 Column (c)  Description:  Cash prizes, other events  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CashPrizesOtherEventsAmt 

    NnCshPrzsOthrEvntsAmt = Column(BigInteger)
    # Line number:  Line 5 Column (c)  Description:  Non-cash prizes, other events  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/NonCashPrizesOtherEventsAmt 

    RntFcltyCstsOthrEvntsAmt = Column(BigInteger)
    # Line number:  Line 6 Column (c)  Description:  Rent or facility costs, other events  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/RentFcltyCostsOtherEventsAmt 

    FdAndBvrgOthrEvntsAmt = Column(BigInteger)
    # Line number:  Line 7 Column (c)  Description:  Food and beverage expenses, other events  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/FoodAndBeverageOtherEventsAmt 

    EntrtnmntOthrEvntsAmt = Column(BigInteger)
    # Line number:  Line 8 Column (c)  Description:  Entertainment expenses, other events  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/EntertainmentOtherEventsAmt 

    OthDrctExpnssOthrEvntsAmt = Column(BigInteger)
    # Line number:  Line 9 Column (c)  Description:  Other direct expenses, other events  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/OthDirectExpnssOtherEventsAmt 

    GrssRcptsTtlAmt = Column(BigInteger)
    # Line number:  Line 1 Column (d)  Description:  Gross receipts, total  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossReceiptsTotalAmt 

    ChrtblCntrbtnsTtAmt = Column(BigInteger)
    # Line number:  Line 2 Column (d)  Description:  Charitable contributions, total  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CharitableContributionsTotAmt 

    GrssRvnTtlEvntsAmt = Column(BigInteger)
    # Line number:  Line 3 Column (d)  Description:  Gross revenue, total  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossRevenueTotalEventsAmt 

    CshPrzsTtlEvntsAmt = Column(BigInteger)
    # Line number:  Line 4 Column (d)  Description:  Cash prizes, total  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CashPrizesTotalEventsAmt 

    NnCshPrzsTtlEvntsAmt = Column(BigInteger)
    # Line number:  Line 5 Column (d)  Description:  Non-cash prizes, total  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/NonCashPrizesTotalEventsAmt 

    RntFcltyCstsTtlEvntsAmt = Column(BigInteger)
    # Line number:  Line 6 Column (d)  Description:  Rent or facility costs, total  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/RentFcltyCostsTotalEventsAmt 

    FdAndBvrgTtlEvntsAmt = Column(BigInteger)
    # Line number:  Line 7 Column (d)  Description:  Food and beverage costs, total  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/FoodAndBeverageTotalEventsAmt 

    EntrtnmntTtlEvntsAmt = Column(BigInteger)
    # Line number:  Line 8 Column (d)  Description:  Entertainment costs, total  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/EntertainmentTotalEventsAmt 

    OthDrctExpnssTtlEvntsAmt = Column(BigInteger)
    # Line number:  Line 9 Column (d)  Description:  Other direct expenses, total  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/OthDirectExpnssTotalEventsAmt 

    DrctExpnsSmmryEvntsAmt = Column(BigInteger)
    # Line number:  Line 10 Column (d)  Description:  Direct expense summary  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/DirectExpenseSummaryEventsAmt 

    NtIncmSmmryAmt = Column(BigInteger)
    # Line number:  Line 11 Column (d)  Description:  Net income summary  xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/NetIncomeSummaryAmt 

#######
#
# IRS990ScheduleG - ScheduleG Part III Gaming Information 
#
#######

class skedg_part_iii(Base):
    __tablename__='skedg_part_iii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    GmngInfrmtn_GrssRvnBngAmt = Column(BigInteger)
    # Line number:  Line 1 Column (a)  Description:  Gross revenue, bingo  xpath: /IRS990ScheduleG/GamingInformationGrp/GrossRevenueBingoAmt 

    GmngInfrmtn_CshPrzsBngAmt = Column(BigInteger)
    # Line number:  Line 2 Column (a)  Description:  Cash prizes, bingo  xpath: /IRS990ScheduleG/GamingInformationGrp/CashPrizesBingoAmt 

    GmngInfrmtn_NnCshPrzsBngAmt = Column(BigInteger)
    # Line number:  Line 3 Column (a)  Description:  Non-cash prizes, bingo  xpath: /IRS990ScheduleG/GamingInformationGrp/NonCashPrizesBingoAmt 

    GmngInfrmtn_RntFcltyCstsBngAmt = Column(BigInteger)
    # Line number:  Line 4 Column (a)  Description:  Rent or facility costs, bingo  xpath: /IRS990ScheduleG/GamingInformationGrp/RentFacilityCostsBingoAmt 

    GmngInfrmtn_OthrDrctExpnssBngAmt = Column(BigInteger)
    # Line number:  Line 5 Column (a)  Description:  Other direct expenses, bingo  xpath: /IRS990ScheduleG/GamingInformationGrp/OtherDirectExpensesBingoAmt 

    GmngInfrmtn_VlntrLbrBngInd = Column(String(length=5))
    # Line number:  Line 6 Column (a)  Description:  volunteer labor, bingo  xpath: /IRS990ScheduleG/GamingInformationGrp/VolunteerLaborBingoInd 

    GmngInfrmtn_VlntrLbrBngPct = Column(Numeric(precision=6))
    # Line number:  Line 6 Column (a)  Description:  volunteer labor percentage, bingo  xpath: /IRS990ScheduleG/GamingInformationGrp/VolunteerLaborBingoPct 

    GmngInfrmtn_GrssRvnPllTbsAmt = Column(BigInteger)
    # Line number:  Line 1 Column (b)  Description:  Gross revenue, pull tabs  xpath: /IRS990ScheduleG/GamingInformationGrp/GrossRevenuePullTabsAmt 

    GmngInfrmtn_CshPrzsPllTbsAmt = Column(BigInteger)
    # Line number:  Line 2 Column (b)  Description:  Cash prizes, pull tabs  xpath: /IRS990ScheduleG/GamingInformationGrp/CashPrizesPullTabsAmt 

    GmngInfrmtn_NnCshPrzsPllTbsAmt = Column(BigInteger)
    # Line number:  Line 3 Column (b)  Description:  Non-cash prizes, pull tabs  xpath: /IRS990ScheduleG/GamingInformationGrp/NonCashPrizesPullTabsAmt 

    GmngInfrmtn_RntFcltyCstsPllTbsAmt = Column(BigInteger)
    # Line number:  Line 4 Column (b)  Description:  Rent or facility costs, pull tabs  xpath: /IRS990ScheduleG/GamingInformationGrp/RentFacilityCostsPullTabsAmt 

    GmngInfrmtn_OthrDrctExpnssPllTbsAmt = Column(BigInteger)
    # Line number:  Line 5 Column (b)  Description:  Other direct expenses, pull tabs  xpath: /IRS990ScheduleG/GamingInformationGrp/OtherDirectExpensesPullTabsAmt 

    GmngInfrmtn_VlntrLbrPllTbsInd = Column(String(length=5))
    # Line number:  Line 6 Column (b)  Description:  volunteer labor, pull tabs  xpath: /IRS990ScheduleG/GamingInformationGrp/VolunteerLaborPullTabsInd 

    GmngInfrmtn_VlntrLbrPllTbsPct = Column(Numeric(precision=6))
    # Line number:  Line 6 Column (b)  Description:  volunteer labor percentage, pull tabs  xpath: /IRS990ScheduleG/GamingInformationGrp/VolunteerLaborPullTabsPct 

    GmngInfrmtn_GrssRvnOthrGmngAmt = Column(BigInteger)
    # Line number:  Line 1 Column (c)  Description:  Gross revenue, other gaming  xpath: /IRS990ScheduleG/GamingInformationGrp/GrossRevenueOtherGamingAmt 

    GmngInfrmtn_CshPrzsOthrGmngAmt = Column(BigInteger)
    # Line number:  Line 2 Column (c)  Description:  Cash prizes, other gaming  xpath: /IRS990ScheduleG/GamingInformationGrp/CashPrizesOtherGamingAmt 

    GmngInfrmtn_NnCshPrzsOthrGmngAmt = Column(BigInteger)
    # Line number:  Line 3 Column (c)  Description:  Non-cash prizes, other gaming  xpath: /IRS990ScheduleG/GamingInformationGrp/NonCashPrizesOtherGamingAmt 

    GmngInfrmtn_RntFcltyCstsOthrGmngAmt = Column(BigInteger)
    # Line number:  Line 4 Column (c)  Description:  Rent or facility costs, other gaming  xpath: /IRS990ScheduleG/GamingInformationGrp/RentFcltyCostsOtherGamingAmt 

    GmngInfrmtn_OthDrctExpnssOthrGmngAmt = Column(BigInteger)
    # Line number:  Line 5 Column (c)  Description:  Other direct expenses, other gaming  xpath: /IRS990ScheduleG/GamingInformationGrp/OthDirectExpnssOtherGamingAmt 

    GmngInfrmtn_VlntrLbrOthrGmngInd = Column(String(length=5))
    # Line number:  Line 6 Column (c)  Description:  volunteer labor, other gaming  xpath: /IRS990ScheduleG/GamingInformationGrp/VolunteerLaborOtherGamingInd 

    GmngInfrmtn_VlntrLbrOthrGmngPct = Column(Numeric(precision=6))
    # Line number:  Line 6 Column (c)  Description:  volunteer labor percentage, other gaming  xpath: /IRS990ScheduleG/GamingInformationGrp/VolunteerLaborOtherGamingPct 

    GmngInfrmtn_GrssRvnTtlGmngAmt = Column(BigInteger)
    # Line number:  Line 1 Column (d)  Description:  Gross revenue, total  xpath: /IRS990ScheduleG/GamingInformationGrp/GrossRevenueTotalGamingAmt 

    GmngInfrmtn_CshPrzsTtlGmngAmt = Column(BigInteger)
    # Line number:  Line 2 Column (d)  Description:  Cash prizes, total  xpath: /IRS990ScheduleG/GamingInformationGrp/CashPrizesTotalGamingAmt 

    GmngInfrmtn_NnCshPrzsTtlGmngAmt = Column(BigInteger)
    # Line number:  Line 3 Column (d)  Description:  Non-cash prizes, total  xpath: /IRS990ScheduleG/GamingInformationGrp/NonCashPrizesTotalGamingAmt 

    GmngInfrmtn_RntFcltyCstsTtlGmngAmt = Column(BigInteger)
    # Line number:  Line 4 Column (d)  Description:  Rent or facility costs, total  xpath: /IRS990ScheduleG/GamingInformationGrp/RentFcltyCostsTotalGamingAmt 

    GmngInfrmtn_OthDrctExpnssTtlGmngAmt = Column(BigInteger)
    # Line number:  Line 5 Column (d)  Description:  Other direct expenses, total  xpath: /IRS990ScheduleG/GamingInformationGrp/OthDirectExpnssTotalGamingAmt 

    GmngInfrmtn_DrctExpnsSmmryGmngAmt = Column(BigInteger)
    # Line number:  Line 7  Description:  Direct expense summary  xpath: /IRS990ScheduleG/GamingInformationGrp/DirectExpenseSummaryGamingAmt 

    GmngInfrmtn_NtGmngIncmSmmryAmt = Column(BigInteger)
    # Line number:  Line 8  Description:  Net gaming income summary  xpath: /IRS990ScheduleG/GamingInformationGrp/NetGamingIncomeSummaryAmt 

    SkdG_LcnsdInd = Column(String(length=5))
    # Line number:  Part III Line 9a  Description:  Is organization licensed in each state?  xpath: /IRS990ScheduleG/LicensedInd 

    SkdG_ExplntnIfNTxt = Column(Text)
    # Line number:  Part III Line 9b  Description:  Explanation if no license  xpath: /IRS990ScheduleG/ExplanationIfNoTxt 

    SkdG_LcnsSspnddEtcInd = Column(String(length=5))
    # Line number:  Part III Line 10a  Description:  Were any gaming licenses revoked, suspended, or terminated during the tax year?  xpath: /IRS990ScheduleG/LicenseSuspendedEtcInd 

    SkdG_ExplntnIfYsTxt = Column(Text)
    # Line number:  Part III Line 10b  Description:  Explanation if license revoked, suspended, or termination  xpath: /IRS990ScheduleG/ExplanationIfYesTxt 

    SkdG_GmngWthNnmmbrsInd = Column(String(length=5))
    # Line number:  Part III Line 11  Description:  Does organization operate gaming activities with nonmembers?  xpath: /IRS990ScheduleG/GamingWithNonmembersInd 

    SkdG_MmbrOfOthrEnttyInd = Column(String(length=5))
    # Line number:  Part III Line 12  Description:  Is organization formed to administer charitable gaming?  xpath: /IRS990ScheduleG/MemberOfOtherEntityInd 

    SkdG_GmngOwnFcltyPct = Column(Numeric(precision=6))
    # Line number:  Part III Line 13a  Description:  Percentage of gaming in own facility  xpath: /IRS990ScheduleG/GamingOwnFacilityPct 

    SkdG_GmngOthrFcltyPct = Column(Numeric(precision=6))
    # Line number:  Part III Line 13b  Description:  Percentage of gaming in other facility  xpath: /IRS990ScheduleG/GamingOtherFacilityPct 

    SkdG_CntrctWth3rdPrtyFrGmRvInd = Column(String(length=5))
    # Line number:  Part III Line 15a  Description:  Is there a third party contract for gaming revenue?  xpath: /IRS990ScheduleG/CntrctWith3rdPrtyForGameRevInd 

    SkdG_GmngRvnRcvdByOrgAmt = Column(BigInteger)
    # Line number:  Part III Line 15b  Description:  Amount of gaming revenue received by organization  xpath: /IRS990ScheduleG/GamingRevenueReceivedByOrgAmt 

    SkdG_GmngRvnRtnBy3PrtyAmt = Column(BigInteger)
    # Line number:  Part III Line 15b  Description:  Amount of gaming revenue retained by 3rd party  xpath: /IRS990ScheduleG/GamingRevenueRtnBy3PrtyAmt 

    SkdG_GmngMngrCmpnstnAmt = Column(BigInteger)
    # Line number:  Part III Line 16  Description:  Gaming manager compensation  xpath: /IRS990ScheduleG/GamingManagerCompensationAmt 

    SkdG_GmngMngrSrvcsPrvTxt = Column(Text)
    # Line number:  Part III Line 16  Description:  Gamaing manager services provided  xpath: /IRS990ScheduleG/GamingManagerServicesProvTxt 

    SkdG_GmngMngrIsDrctrOfcrInd = Column(String(length=1))
    # Line number:  Part III Line 16  Description:  Gaming manager is a director or officer  xpath: /IRS990ScheduleG/GamingManagerIsDirectorOfcrInd 

    SkdG_GmngMngrIsEmplyInd = Column(String(length=1))
    # Line number:  Part III Line 16  Description:  Gaming manager is an employee  xpath: /IRS990ScheduleG/GamingManagerIsEmployeeInd 

    SkdG_GmngMngrIsIndCntrctInd = Column(String(length=1))
    # Line number:  Part III Line 16  Description:  Gaming manager is an independent contractor  xpath: /IRS990ScheduleG/GamingManagerIsIndCntrctInd 

    SkdG_ChrtblDstrbtnRqrInd = Column(String(length=5))
    # Line number:  Part III Line 17a  Description:  Charitable distributions required?  xpath: /IRS990ScheduleG/CharitableDistributionRqrInd 

    SkdG_DstrbtdAmt = Column(BigInteger)
    # Line number:  Part III Line 17b  Description:  Amount distributed  xpath: /IRS990ScheduleG/DistributedAmt 

    SkdG_IndvdlWthBksNm = Column(String(length=35))
    # Line number:  Part III Line 14  Description:  Person name of gaming records keeper  xpath: /IRS990ScheduleG/IndividualWithBooksNm 

    PrsnsWthBksNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part III Line 14  Description:  Business name line 1  xpath: /IRS990ScheduleG/PersonsWithBooksName/BusinessNameLine1Txt 

    PrsnsWthBksNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part III Line 14  Description:  Business name line 2  xpath: /IRS990ScheduleG/PersonsWithBooksName/BusinessNameLine2Txt 

    PrsnsWthBksUSAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part III Line 14  Description:  Address line 1  xpath: /IRS990ScheduleG/PersonsWithBooksUSAddress/AddressLine1Txt 

    PrsnsWthBksUSAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part III Line 14  Description:  Address line 2  xpath: /IRS990ScheduleG/PersonsWithBooksUSAddress/AddressLine2Txt 

    PrsnsWthBksUSAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part III Line 14  Description:  City  xpath: /IRS990ScheduleG/PersonsWithBooksUSAddress/CityNm 

    PrsnsWthBksUSAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part III Line 14  Description:  State  xpath: /IRS990ScheduleG/PersonsWithBooksUSAddress/StateAbbreviationCd 

    PrsnsWthBksUSAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part III Line 14  Description:  ZIP code  xpath: /IRS990ScheduleG/PersonsWithBooksUSAddress/ZIPCd 

    PrsnsWthBksFrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part III Line 14  Description:  Address line 1  xpath: /IRS990ScheduleG/PersonsWithBooksForeignAddress/AddressLine1Txt 

    PrsnsWthBksFrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part III Line 14  Description:  Address line 2  xpath: /IRS990ScheduleG/PersonsWithBooksForeignAddress/AddressLine2Txt 

    PrsnsWthBksFrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part III Line 14  Description:  City  xpath: /IRS990ScheduleG/PersonsWithBooksForeignAddress/CityNm 

    PrsnsWthBksFrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part III Line 14  Description:  Province or state  xpath: /IRS990ScheduleG/PersonsWithBooksForeignAddress/ProvinceOrStateNm 

    PrsnsWthBksFrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part III Line 14  Description:  Country  xpath: /IRS990ScheduleG/PersonsWithBooksForeignAddress/CountryCd 

    PrsnsWthBksFrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part III Line 14  Description:  Postal code  xpath: /IRS990ScheduleG/PersonsWithBooksForeignAddress/ForeignPostalCd 

    SkdG_ThrdPrtyPrsnNm = Column(String(length=35))
    # Line number:  Part III Line 15c  Description:  Person name of third party  xpath: /IRS990ScheduleG/ThirdPartyPersonNm 

    ThrdPrtyBsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part III Line 15c  Description:  Business name line 1  xpath: /IRS990ScheduleG/ThirdPartyBusinessName/BusinessNameLine1Txt 

    ThrdPrtyBsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part III Line 15c  Description:  Business name line 2  xpath: /IRS990ScheduleG/ThirdPartyBusinessName/BusinessNameLine2Txt 

    ThrdPrtyUSAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part III Line 15c  Description:  Address line 1  xpath: /IRS990ScheduleG/ThirdPartyUSAddress/AddressLine1Txt 

    ThrdPrtyUSAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part III Line 15c  Description:  Address line 2  xpath: /IRS990ScheduleG/ThirdPartyUSAddress/AddressLine2Txt 

    ThrdPrtyUSAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part III Line 15c  Description:  City  xpath: /IRS990ScheduleG/ThirdPartyUSAddress/CityNm 

    ThrdPrtyUSAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part III Line 15c  Description:  State  xpath: /IRS990ScheduleG/ThirdPartyUSAddress/StateAbbreviationCd 

    ThrdPrtyUSAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part III Line 15c  Description:  ZIP code  xpath: /IRS990ScheduleG/ThirdPartyUSAddress/ZIPCd 

    ThrdPrtyFrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part III Line 15c  Description:  Address line 1  xpath: /IRS990ScheduleG/ThirdPartyForeignAddress/AddressLine1Txt 

    ThrdPrtyFrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part III Line 15c  Description:  Address line 2  xpath: /IRS990ScheduleG/ThirdPartyForeignAddress/AddressLine2Txt 

    ThrdPrtyFrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part III Line 15c  Description:  City  xpath: /IRS990ScheduleG/ThirdPartyForeignAddress/CityNm 

    ThrdPrtyFrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part III Line 15c  Description:  Province or state  xpath: /IRS990ScheduleG/ThirdPartyForeignAddress/ProvinceOrStateNm 

    ThrdPrtyFrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part III Line 15c  Description:  Country  xpath: /IRS990ScheduleG/ThirdPartyForeignAddress/CountryCd 

    ThrdPrtyFrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part III Line 15c  Description:  Postal code  xpath: /IRS990ScheduleG/ThirdPartyForeignAddress/ForeignPostalCd 

    SkdG_GmngMngrPrsnNm = Column(String(length=35))
    # Line number:  Part III Line 16  Description:  Gaming manager person name  xpath: /IRS990ScheduleG/GamingManagerPersonNm 

    GmngMngrBsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part III Line 16  Description:  Business name line 1  xpath: /IRS990ScheduleG/GamingManagerBusinessName/BusinessNameLine1Txt 

    GmngMngrBsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part III Line 16  Description:  Business name line 2  xpath: /IRS990ScheduleG/GamingManagerBusinessName/BusinessNameLine2Txt 

#######
#
# IRS990ScheduleG - SupplementalInformationDetail
# A repeating structure from ScheduleG Part IV Supplemental Information 
#
#######

class SkdGSpplmntlInfrmtnDtl(Base):
    __tablename__='SkdGSpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtnDtl = Column(Text)
    # Description:  Part IV contents  xpath: /IRS990ScheduleG/SupplementalInformationDetail 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part IV  Description:  Form, part and line number reference  xpath: /IRS990ScheduleG/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part IV  Description:  Form, part and line number reference explanation  xpath: /IRS990ScheduleG/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleG - StatesWhereGamingConductedCd
# A repeating structure from ScheduleG Part III Gaming Information 
#
#######

class SkdGSttsWhrGmngCndctdCd(Base):
    __tablename__='SkdGSttsWhrGmngCndctdCd'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SttsWhrGmngCndctdCd = Column(String(length=2))
    # Line number:  Part III Line 9  Description:  Enter state where organization conducts gaming activities  xpath: /IRS990ScheduleG/StatesWhereGamingConductedCd 

#######
#
# IRS990ScheduleG - LicensedStatesCd
# A repeating structure from ScheduleG Part I Fundraising Activities 
#
#######

class SkdGLcnsdSttsCd(Base):
    __tablename__='SkdGLcnsdSttsCd'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    LcnsdSttsCd = Column(String(length=2))
    # Line number:  Part I Line 3  Description:  List all states in which the organization is registered or licensed to solicit funds or has been notified it is exempt from registration or licensing  xpath: /IRS990ScheduleG/LicensedStatesCd 

#######
#
# IRS990ScheduleG - FundraiserActivityInfoGrp
# A repeating structure from ScheduleG Part I Fundraising Activities 
#
#######

class SkdGFndrsrActvtyInf(Base):
    __tablename__='SkdGFndrsrActvtyInf'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    FndrsrActvtyInf_PrsnNm = Column(String(length=35))
    # Line number:  Line 2b Column (i)  Description:  Name of individual  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/PersonNm 

    OrgnztnBsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Line 2b Column (i)  Description:  Business name line 1  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/OrganizationBusinessName/BusinessNameLine1Txt 

    OrgnztnBsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Line 2b Column (i)  Description:  Business name line 2  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/OrganizationBusinessName/BusinessNameLine2Txt 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Line 2b Column (i)  Description:  Address line 1  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Line 2b Column (i)  Description:  Address line 2  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Line 2b Column (i)  Description:  City  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Line 2b Column (i)  Description:  State  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Line 2b Column (i)  Description:  ZIP code  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Line 2b Column (i)  Description:  Address line 1  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Line 2b Column (i)  Description:  Address line 2  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Line 2b Column (i)  Description:  City  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Line 2b Column (i)  Description:  Province or state  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Line 2b Column (i)  Description:  Country  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Line 2b Column (i)  Description:  Postal code  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ForeignAddress/ForeignPostalCd 

    FndrsrActvtyInf_ActvtyTxt = Column(Text)
    # Line number:  Line 2b Column (ii)  Description:  Activity  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ActivityTxt 

    FndrsrActvtyInf_FndrsrCntrlOfFndsInd = Column(String(length=5))
    # Line number:  Line 2b Column (iii)  Description:  Fundraiser control of funds?  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/FundraiserControlOfFundsInd 

    FndrsrActvtyInf_GrssRcptsAmt = Column(BigInteger)
    # Line number:  Part I Line 2b(iv)  Description:  Gross receipts from activity  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/GrossReceiptsAmt 

    FndrsrActvtyInf_RtndByCntrctrAmt = Column(BigInteger)
    # Line number:  Part I Line 2b(v)  Description:  Amount paid to (or retained by) fundraiser listed in (i)  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/RetainedByContractorAmt 

    FndrsrActvtyInf_NtTOrgnztnAmt = Column(BigInteger)
    # Line number:  Part I Line 2b(vi)  Description:  Amount paid to (or retained by) organization  xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/NetToOrganizationAmt 

#######
#
# IRS990ScheduleH - ScheduleH Part I - Community Benefit Report 
#
#######

class skedh_part_i(Base):
    __tablename__='skedh_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SkdH_FnnclAssstncPlcyInd = Column(String(length=5))
    # Line number:  Part I Line 1a  Description:  Financial assistance policy?  xpath: /IRS990ScheduleH/FinancialAssistancePolicyInd 

    SkdH_WrttnPlcyInd = Column(String(length=5))
    # Line number:  Part I Line 1b  Description:  Written policy?  xpath: /IRS990ScheduleH/WrittenPolicyInd 

    SkdH_FPGRfrncFrCrInd = Column(String(length=5))
    # Line number:  Part I Line 3a  Description:  FPG reference free care?  xpath: /IRS990ScheduleH/FPGReferenceFreeCareInd 

    SkdH_FPGRfrncDscntdCrInd = Column(String(length=5))
    # Line number:  Part I Line 3b  Description:  FPG reference discounted care  xpath: /IRS990ScheduleH/FPGReferenceDiscountedCareInd 

    SkdH_FrCrMdcllyIndgntInd = Column(String(length=5))
    # Line number:  Part I Line 4  Description:  Free or discounted care to medically indigent?  xpath: /IRS990ScheduleH/FreeCareMedicallyIndigentInd 

    SkdH_FnnclAssstncBdgtInd = Column(String(length=5))
    # Line number:  Part I Line 5a  Description:  Amounts budgeted for financial assistance?  xpath: /IRS990ScheduleH/FinancialAssistanceBudgetInd 

    SkdH_ExpnssExcdBdgtInd = Column(String(length=5))
    # Line number:  Part I Line 5b  Description:  Expenses exceeded budget?  xpath: /IRS990ScheduleH/ExpensesExceedBudgetInd 

    SkdH_UnblTPrvdCrInd = Column(String(length=5))
    # Line number:  Part I Line 5c  Description:  Unable to provide care?  xpath: /IRS990ScheduleH/UnableToProvideCareInd 

    SkdH_AnnlCmmntyBnftRprtInd = Column(String(length=5))
    # Line number:  Part I Line 6a  Description:  Annual community benefit report?  xpath: /IRS990ScheduleH/AnnualCommunityBnftReportInd 

    SkdH_RprtPblcllyAvlblInd = Column(String(length=5))
    # Line number:  Part I Line 6b  Description:  Report publically available?  xpath: /IRS990ScheduleH/ReportPublicallyAvailableInd 

    FnnclAssstncAtCstTyp_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/FinancialAssistanceAtCostTyp/ActivitiesOrProgramsCnt 

    FnnclAssstncAtCstTyp_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/FinancialAssistanceAtCostTyp/PersonsServedCnt 

    FnnclAssstncAtCstTyp_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community benefit expense  xpath: /IRS990ScheduleH/FinancialAssistanceAtCostTyp/TotalCommunityBenefitExpnsAmt 

    FnnclAssstncAtCstTyp_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/FinancialAssistanceAtCostTyp/DirectOffsettingRevenueAmt 

    FnnclAssstncAtCstTyp_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community benefit expense  xpath: /IRS990ScheduleH/FinancialAssistanceAtCostTyp/NetCommunityBenefitExpnsAmt 

    FnnclAssstncAtCstTyp_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/FinancialAssistanceAtCostTyp/TotalExpensePct 

    UnrmbrsdMdcd_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/UnreimbursedMedicaidGrp/ActivitiesOrProgramsCnt 

    UnrmbrsdMdcd_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/UnreimbursedMedicaidGrp/PersonsServedCnt 

    UnrmbrsdMdcd_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community benefit expense  xpath: /IRS990ScheduleH/UnreimbursedMedicaidGrp/TotalCommunityBenefitExpnsAmt 

    UnrmbrsdMdcd_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/UnreimbursedMedicaidGrp/DirectOffsettingRevenueAmt 

    UnrmbrsdMdcd_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community benefit expense  xpath: /IRS990ScheduleH/UnreimbursedMedicaidGrp/NetCommunityBenefitExpnsAmt 

    UnrmbrsdMdcd_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/UnreimbursedMedicaidGrp/TotalExpensePct 

    UnrmbrsdCsts_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/UnreimbursedCostsGrp/ActivitiesOrProgramsCnt 

    UnrmbrsdCsts_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/UnreimbursedCostsGrp/PersonsServedCnt 

    UnrmbrsdCsts_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community benefit expense  xpath: /IRS990ScheduleH/UnreimbursedCostsGrp/TotalCommunityBenefitExpnsAmt 

    UnrmbrsdCsts_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/UnreimbursedCostsGrp/DirectOffsettingRevenueAmt 

    UnrmbrsdCsts_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community benefit expense  xpath: /IRS990ScheduleH/UnreimbursedCostsGrp/NetCommunityBenefitExpnsAmt 

    UnrmbrsdCsts_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/UnreimbursedCostsGrp/TotalExpensePct 

    TtlFnnclAssstncTyp_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/TotalFinancialAssistanceTyp/ActivitiesOrProgramsCnt 

    TtlFnnclAssstncTyp_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/TotalFinancialAssistanceTyp/PersonsServedCnt 

    TtlFnnclAssstncTyp_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community benefit expense  xpath: /IRS990ScheduleH/TotalFinancialAssistanceTyp/TotalCommunityBenefitExpnsAmt 

    TtlFnnclAssstncTyp_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/TotalFinancialAssistanceTyp/DirectOffsettingRevenueAmt 

    TtlFnnclAssstncTyp_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community benefit expense  xpath: /IRS990ScheduleH/TotalFinancialAssistanceTyp/NetCommunityBenefitExpnsAmt 

    TtlFnnclAssstncTyp_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/TotalFinancialAssistanceTyp/TotalExpensePct 

    CmmntyHlthSrvcs_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/CommunityHealthServicesGrp/ActivitiesOrProgramsCnt 

    CmmntyHlthSrvcs_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/CommunityHealthServicesGrp/PersonsServedCnt 

    CmmntyHlthSrvcs_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community benefit expense  xpath: /IRS990ScheduleH/CommunityHealthServicesGrp/TotalCommunityBenefitExpnsAmt 

    CmmntyHlthSrvcs_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/CommunityHealthServicesGrp/DirectOffsettingRevenueAmt 

    CmmntyHlthSrvcs_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community benefit expense  xpath: /IRS990ScheduleH/CommunityHealthServicesGrp/NetCommunityBenefitExpnsAmt 

    CmmntyHlthSrvcs_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/CommunityHealthServicesGrp/TotalExpensePct 

    HlthPrfssnsEdctn_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/HealthProfessionsEducationGrp/ActivitiesOrProgramsCnt 

    HlthPrfssnsEdctn_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/HealthProfessionsEducationGrp/PersonsServedCnt 

    HlthPrfssnsEdctn_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community benefit expense  xpath: /IRS990ScheduleH/HealthProfessionsEducationGrp/TotalCommunityBenefitExpnsAmt 

    HlthPrfssnsEdctn_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/HealthProfessionsEducationGrp/DirectOffsettingRevenueAmt 

    HlthPrfssnsEdctn_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community benefit expense  xpath: /IRS990ScheduleH/HealthProfessionsEducationGrp/NetCommunityBenefitExpnsAmt 

    HlthPrfssnsEdctn_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/HealthProfessionsEducationGrp/TotalExpensePct 

    SbsdzdHlthSrvcs_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/SubsidizedHealthServicesGrp/ActivitiesOrProgramsCnt 

    SbsdzdHlthSrvcs_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/SubsidizedHealthServicesGrp/PersonsServedCnt 

    SbsdzdHlthSrvcs_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community benefit expense  xpath: /IRS990ScheduleH/SubsidizedHealthServicesGrp/TotalCommunityBenefitExpnsAmt 

    SbsdzdHlthSrvcs_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/SubsidizedHealthServicesGrp/DirectOffsettingRevenueAmt 

    SbsdzdHlthSrvcs_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community benefit expense  xpath: /IRS990ScheduleH/SubsidizedHealthServicesGrp/NetCommunityBenefitExpnsAmt 

    SbsdzdHlthSrvcs_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/SubsidizedHealthServicesGrp/TotalExpensePct 

    Rsrch_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/ResearchGrp/ActivitiesOrProgramsCnt 

    Rsrch_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/ResearchGrp/PersonsServedCnt 

    Rsrch_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community benefit expense  xpath: /IRS990ScheduleH/ResearchGrp/TotalCommunityBenefitExpnsAmt 

    Rsrch_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/ResearchGrp/DirectOffsettingRevenueAmt 

    Rsrch_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community benefit expense  xpath: /IRS990ScheduleH/ResearchGrp/NetCommunityBenefitExpnsAmt 

    Rsrch_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/ResearchGrp/TotalExpensePct 

    CshAndInKndCntrbtns_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/CashAndInKindContributionsGrp/ActivitiesOrProgramsCnt 

    CshAndInKndCntrbtns_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/CashAndInKindContributionsGrp/PersonsServedCnt 

    CshAndInKndCntrbtns_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community benefit expense  xpath: /IRS990ScheduleH/CashAndInKindContributionsGrp/TotalCommunityBenefitExpnsAmt 

    CshAndInKndCntrbtns_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/CashAndInKindContributionsGrp/DirectOffsettingRevenueAmt 

    CshAndInKndCntrbtns_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community benefit expense  xpath: /IRS990ScheduleH/CashAndInKindContributionsGrp/NetCommunityBenefitExpnsAmt 

    CshAndInKndCntrbtns_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/CashAndInKindContributionsGrp/TotalExpensePct 

    TtlOthrBnfts_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/TotalOtherBenefitsGrp/ActivitiesOrProgramsCnt 

    TtlOthrBnfts_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/TotalOtherBenefitsGrp/PersonsServedCnt 

    TtlOthrBnfts_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community benefit expense  xpath: /IRS990ScheduleH/TotalOtherBenefitsGrp/TotalCommunityBenefitExpnsAmt 

    TtlOthrBnfts_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/TotalOtherBenefitsGrp/DirectOffsettingRevenueAmt 

    TtlOthrBnfts_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community benefit expense  xpath: /IRS990ScheduleH/TotalOtherBenefitsGrp/NetCommunityBenefitExpnsAmt 

    TtlOthrBnfts_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/TotalOtherBenefitsGrp/TotalExpensePct 

    TtlCmmntyBnfts_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/TotalCommunityBenefitsGrp/ActivitiesOrProgramsCnt 

    TtlCmmntyBnfts_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/TotalCommunityBenefitsGrp/PersonsServedCnt 

    TtlCmmntyBnfts_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community benefit expense  xpath: /IRS990ScheduleH/TotalCommunityBenefitsGrp/TotalCommunityBenefitExpnsAmt 

    TtlCmmntyBnfts_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/TotalCommunityBenefitsGrp/DirectOffsettingRevenueAmt 

    TtlCmmntyBnfts_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community benefit expense  xpath: /IRS990ScheduleH/TotalCommunityBenefitsGrp/NetCommunityBenefitExpnsAmt 

    TtlCmmntyBnfts_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/TotalCommunityBenefitsGrp/TotalExpensePct 

    SkdH_AllHsptlsPlcyInd = Column(String(length=1))
    # Line number:  Part I Line 2  Description:  Policy applied to all hospitals  xpath: /IRS990ScheduleH/AllHospitalsPolicyInd 

    SkdH_MstHsptlsPlcyInd = Column(String(length=1))
    # Line number:  Part I Line 2  Description:  Policy applied to most hospitals  xpath: /IRS990ScheduleH/MostHospitalsPolicyInd 

    SkdH_IndvHsptlTlrdPlcyInd = Column(String(length=1))
    # Line number:  Part I Line 2  Description:  Policy tailored to individual hospitals  xpath: /IRS990ScheduleH/IndivHospitalTailoredPolicyInd 

    SkdH_Prcnt100Ind = Column(String(length=1))
    # Line number:  Part I Line 3a  Description:  100%  xpath: /IRS990ScheduleH/Percent100Ind 

    SkdH_Prcnt150Ind = Column(String(length=1))
    # Line number:  Part I Line 3a  Description:  150%  xpath: /IRS990ScheduleH/Percent150Ind 

    SkdH_Prcnt200Ind = Column(String(length=1))
    # Line number:  Part I Line 3a  Description:  200%  xpath: /IRS990ScheduleH/Percent200Ind 

    SkdH_FrCrOthPrcntg = Column(Text)
    # xpath: /IRS990ScheduleH/FreeCareOthPercentageGrp 

    FrCrOthPrcntg_OthrInd = Column(String(length=1))
    # Line number:  Part I Line 3a  Description:  Other  xpath: /IRS990ScheduleH/FreeCareOthPercentageGrp/OtherInd 

    FrCrOthPrcntg_FrCrOthrPct = Column(Numeric(precision=22))
    # Line number:  Part I Line 3a  Description:  Free other percentage  xpath: /IRS990ScheduleH/FreeCareOthPercentageGrp/FreeCareOtherPct 

    SkdH_Prcnt200DInd = Column(String(length=1))
    # Line number:  Part I Line 3b  Description:  200%  xpath: /IRS990ScheduleH/Percent200DInd 

    SkdH_Prcnt250Ind = Column(String(length=1))
    # Line number:  Part I Line 3b  Description:  250%  xpath: /IRS990ScheduleH/Percent250Ind 

    SkdH_Prcnt300Ind = Column(String(length=1))
    # Line number:  Part I Line 3b  Description:  300%  xpath: /IRS990ScheduleH/Percent300Ind 

    SkdH_Prcnt350Ind = Column(String(length=1))
    # Line number:  Part I Line 3b  Description:  350%  xpath: /IRS990ScheduleH/Percent350Ind 

    SkdH_Prcnt400Ind = Column(String(length=1))
    # Line number:  Part I Line 3b  Description:  400%  xpath: /IRS990ScheduleH/Percent400Ind 

    SkdH_DscntdCrOthPrcntg = Column(Text)
    # xpath: /IRS990ScheduleH/DiscountedCareOthPercentageGrp 

    DscntdCrOthPrcntg_OthrInd = Column(String(length=1))
    # Line number:  Part I Line 3b  Description:  Other  xpath: /IRS990ScheduleH/DiscountedCareOthPercentageGrp/OtherInd 

    DscntdCrOthPrcntg_DscntdCrOthrPct = Column(Numeric(precision=22))
    # Line number:  Part I Line 3b  Description:  Discounted other percentage  xpath: /IRS990ScheduleH/DiscountedCareOthPercentageGrp/DiscountedCareOtherPct 

#######
#
# IRS990ScheduleH - ScheduleH Part II 
#
#######

class skedh_part_ii(Base):
    __tablename__='skedh_part_ii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    PhysclImprvAndHsng_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/PhysicalImprvAndHousingGrp/ActivitiesOrProgramsCnt 

    PhysclImprvAndHsng_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/PhysicalImprvAndHousingGrp/PersonsServedCnt 

    PhysclImprvAndHsng_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community building expense  xpath: /IRS990ScheduleH/PhysicalImprvAndHousingGrp/TotalCommunityBenefitExpnsAmt 

    PhysclImprvAndHsng_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/PhysicalImprvAndHousingGrp/DirectOffsettingRevenueAmt 

    PhysclImprvAndHsng_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community building expense  xpath: /IRS990ScheduleH/PhysicalImprvAndHousingGrp/NetCommunityBenefitExpnsAmt 

    PhysclImprvAndHsng_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/PhysicalImprvAndHousingGrp/TotalExpensePct 

    EcnmcDvlpmnt_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/EconomicDevelopmentGrp/ActivitiesOrProgramsCnt 

    EcnmcDvlpmnt_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/EconomicDevelopmentGrp/PersonsServedCnt 

    EcnmcDvlpmnt_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community building expense  xpath: /IRS990ScheduleH/EconomicDevelopmentGrp/TotalCommunityBenefitExpnsAmt 

    EcnmcDvlpmnt_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/EconomicDevelopmentGrp/DirectOffsettingRevenueAmt 

    EcnmcDvlpmnt_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community building expense  xpath: /IRS990ScheduleH/EconomicDevelopmentGrp/NetCommunityBenefitExpnsAmt 

    EcnmcDvlpmnt_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/EconomicDevelopmentGrp/TotalExpensePct 

    CmmntySpprt_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/CommunitySupportGrp/ActivitiesOrProgramsCnt 

    CmmntySpprt_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/CommunitySupportGrp/PersonsServedCnt 

    CmmntySpprt_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community building expense  xpath: /IRS990ScheduleH/CommunitySupportGrp/TotalCommunityBenefitExpnsAmt 

    CmmntySpprt_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/CommunitySupportGrp/DirectOffsettingRevenueAmt 

    CmmntySpprt_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community building expense  xpath: /IRS990ScheduleH/CommunitySupportGrp/NetCommunityBenefitExpnsAmt 

    CmmntySpprt_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/CommunitySupportGrp/TotalExpensePct 

    EnvrnmntlImprvmnts_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/EnvironmentalImprovementsGrp/ActivitiesOrProgramsCnt 

    EnvrnmntlImprvmnts_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/EnvironmentalImprovementsGrp/PersonsServedCnt 

    EnvrnmntlImprvmnts_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community building expense  xpath: /IRS990ScheduleH/EnvironmentalImprovementsGrp/TotalCommunityBenefitExpnsAmt 

    EnvrnmntlImprvmnts_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/EnvironmentalImprovementsGrp/DirectOffsettingRevenueAmt 

    EnvrnmntlImprvmnts_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community building expense  xpath: /IRS990ScheduleH/EnvironmentalImprovementsGrp/NetCommunityBenefitExpnsAmt 

    EnvrnmntlImprvmnts_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/EnvironmentalImprovementsGrp/TotalExpensePct 

    LdrshpDvlpmnt_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/LeadershipDevelopmentGrp/ActivitiesOrProgramsCnt 

    LdrshpDvlpmnt_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/LeadershipDevelopmentGrp/PersonsServedCnt 

    LdrshpDvlpmnt_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community building expense  xpath: /IRS990ScheduleH/LeadershipDevelopmentGrp/TotalCommunityBenefitExpnsAmt 

    LdrshpDvlpmnt_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/LeadershipDevelopmentGrp/DirectOffsettingRevenueAmt 

    LdrshpDvlpmnt_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community building expense  xpath: /IRS990ScheduleH/LeadershipDevelopmentGrp/NetCommunityBenefitExpnsAmt 

    LdrshpDvlpmnt_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/LeadershipDevelopmentGrp/TotalExpensePct 

    CltnBldng_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/CoalitionBuildingGrp/ActivitiesOrProgramsCnt 

    CltnBldng_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/CoalitionBuildingGrp/PersonsServedCnt 

    CltnBldng_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community building expense  xpath: /IRS990ScheduleH/CoalitionBuildingGrp/TotalCommunityBenefitExpnsAmt 

    CltnBldng_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/CoalitionBuildingGrp/DirectOffsettingRevenueAmt 

    CltnBldng_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community building expense  xpath: /IRS990ScheduleH/CoalitionBuildingGrp/NetCommunityBenefitExpnsAmt 

    CltnBldng_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/CoalitionBuildingGrp/TotalExpensePct 

    HlthImprvmntAdvccy_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/HealthImprovementAdvocacyGrp/ActivitiesOrProgramsCnt 

    HlthImprvmntAdvccy_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/HealthImprovementAdvocacyGrp/PersonsServedCnt 

    HlthImprvmntAdvccy_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community building expense  xpath: /IRS990ScheduleH/HealthImprovementAdvocacyGrp/TotalCommunityBenefitExpnsAmt 

    HlthImprvmntAdvccy_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/HealthImprovementAdvocacyGrp/DirectOffsettingRevenueAmt 

    HlthImprvmntAdvccy_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community building expense  xpath: /IRS990ScheduleH/HealthImprovementAdvocacyGrp/NetCommunityBenefitExpnsAmt 

    HlthImprvmntAdvccy_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/HealthImprovementAdvocacyGrp/TotalExpensePct 

    WrkfrcDvlpmnt_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/WorkforceDevelopmentGrp/ActivitiesOrProgramsCnt 

    WrkfrcDvlpmnt_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/WorkforceDevelopmentGrp/PersonsServedCnt 

    WrkfrcDvlpmnt_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community building expense  xpath: /IRS990ScheduleH/WorkforceDevelopmentGrp/TotalCommunityBenefitExpnsAmt 

    WrkfrcDvlpmnt_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/WorkforceDevelopmentGrp/DirectOffsettingRevenueAmt 

    WrkfrcDvlpmnt_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community building expense  xpath: /IRS990ScheduleH/WorkforceDevelopmentGrp/NetCommunityBenefitExpnsAmt 

    WrkfrcDvlpmnt_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/WorkforceDevelopmentGrp/TotalExpensePct 

    OthrCmmnttyBldngActy_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/OtherCommuntityBuildingActyGrp/ActivitiesOrProgramsCnt 

    OthrCmmnttyBldngActy_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/OtherCommuntityBuildingActyGrp/PersonsServedCnt 

    OthrCmmnttyBldngActy_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community building expense  xpath: /IRS990ScheduleH/OtherCommuntityBuildingActyGrp/TotalCommunityBenefitExpnsAmt 

    OthrCmmnttyBldngActy_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/OtherCommuntityBuildingActyGrp/DirectOffsettingRevenueAmt 

    OthrCmmnttyBldngActy_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community building expense  xpath: /IRS990ScheduleH/OtherCommuntityBuildingActyGrp/NetCommunityBenefitExpnsAmt 

    OthrCmmnttyBldngActy_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/OtherCommuntityBuildingActyGrp/TotalExpensePct 

    TtlCmmnttyBldngActy_ActvtsOrPrgrmsCnt = Column(BigInteger)
    # Line number:  Column (a)  Description:  Number of activities or programs  xpath: /IRS990ScheduleH/TotalCommuntityBuildingActyGrp/ActivitiesOrProgramsCnt 

    TtlCmmnttyBldngActy_PrsnsSrvdCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Persons served  xpath: /IRS990ScheduleH/TotalCommuntityBuildingActyGrp/PersonsServedCnt 

    TtlCmmnttyBldngActy_TtlCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Total community building expense  xpath: /IRS990ScheduleH/TotalCommuntityBuildingActyGrp/TotalCommunityBenefitExpnsAmt 

    TtlCmmnttyBldngActy_DrctOffsttngRvnAmt = Column(BigInteger)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  xpath: /IRS990ScheduleH/TotalCommuntityBuildingActyGrp/DirectOffsettingRevenueAmt 

    TtlCmmnttyBldngActy_NtCmmntyBnftExpnsAmt = Column(BigInteger)
    # Line number:  Column (e)  Description:  Net community building expense  xpath: /IRS990ScheduleH/TotalCommuntityBuildingActyGrp/NetCommunityBenefitExpnsAmt 

    TtlCmmnttyBldngActy_TtlExpnsPct = Column(Numeric(precision=6))
    # Line number:  Column (f)  Description:  Percent of total expense  xpath: /IRS990ScheduleH/TotalCommuntityBuildingActyGrp/TotalExpensePct 

#######
#
# IRS990ScheduleH - ScheduleH Part III - Bad Debt, Medicare, and Collection Practices 
#
#######

class skedh_part_iii(Base):
    __tablename__='skedh_part_iii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    BdDbtExpnsRprtdInd = Column(String(length=5))
    # Line number:  Part III Section A Line 1  Description:  Bad debt expense reported?  xpath: /IRS990ScheduleH/BadDebtExpenseReportedInd 

    BdDbtExpnsAmt = Column(BigInteger)
    # Line number:  Part III Section A Line 2  Description:  Bad debt expense amount  xpath: /IRS990ScheduleH/BadDebtExpenseAmt 

    BdDbtExpnsAttrbtblAmt = Column(BigInteger)
    # Line number:  Part III Section A Line 3  Description:  Amount attributable to  xpath: /IRS990ScheduleH/BadDebtExpenseAttributableAmt 

    RmbrsdByMdcrAmt = Column(BigInteger)
    # Line number:  Part III Section B Line 5  Description:  Amount reimbursed by Medicare  xpath: /IRS990ScheduleH/ReimbursedByMedicareAmt 

    CstOfCrRmbrsdByMdcrAmt = Column(BigInteger)
    # Line number:  Part III Section B Line 6  Description:  Cost of care reimbursed by Medicare  xpath: /IRS990ScheduleH/CostOfCareReimbursedByMedcrAmt 

    MdcrSrplsOrShrtfllAmt = Column(BigInteger)
    # Line number:  Part III Section B Line 7  Description:  Line 5 less line 6  xpath: /IRS990ScheduleH/MedicareSurplusOrShortfallAmt 

    CstngMthdlgyUsd = Column(Text)
    # Description:  Checkbox choice  xpath: /IRS990ScheduleH/CostingMethodologyUsedGrp 

    CstAccntngSystmInd = Column(String(length=1))
    # Line number:  Part III Section B Line 8  Description:  Cost accounting system  xpath: /IRS990ScheduleH/CostingMethodologyUsedGrp/CostAccountingSystemInd 

    CstTChrgRtInd = Column(String(length=1))
    # Line number:  Part III Section B Line 8  Description:  Cost to charge ratio  xpath: /IRS990ScheduleH/CostingMethodologyUsedGrp/CostToChargeRatioInd 

    OthrInd = Column(String(length=1))
    # Line number:  Part III Section B Line 8  Description:  Other  xpath: /IRS990ScheduleH/CostingMethodologyUsedGrp/OtherInd 

    WrttnDbtCllctnPlcyInd = Column(String(length=5))
    # Line number:  Part III Section C Line 9a  Description:  Written debt collection policy?  xpath: /IRS990ScheduleH/WrittenDebtCollectionPolicyInd 

    FnnclAssstncPrvsnInd = Column(String(length=5))
    # Line number:  Part III Section C Line 9b  Description:  Provision for financial assistance?  xpath: /IRS990ScheduleH/FinancialAssistancePrvsnInd 

#######
#
# IRS990ScheduleH - ScheduleH Part V-A - Facility Information 
#
#######

class skedh_part_va(Base):
    __tablename__='skedh_part_va'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    HsptlFcltsCnt = Column(Integer)
    # Line number:  Part V Section A  Description:  How many hospital facilities did the organization operate during the tax year?  xpath: /IRS990ScheduleH/HospitalFacilitiesCnt 

#######
#
# IRS990ScheduleH - ScheduleH Part V-D - Other Health Care Facilities 
#
#######

class skedh_part_vd(Base):
    __tablename__='skedh_part_vd'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    FcltyNm = Column(Integer)
    # Line number:  Part V Section D  Description:  Number of other facilities  xpath: /IRS990ScheduleH/FacilityNum 

    OthHlthCrFcltsNtHsptl = Column(Text)
    # Description:  Part V section D, other health care facilities  xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp 

#######
#
# IRS990ScheduleH - ManagementCoAndJntVenturesGrp
# A repeating structure from ScheduleH Part IV - Management Companies and Joint Ventures 
#
#######

class SkdHMngmntCAndJntVntrs(Base):
    __tablename__='SkdHMngmntCAndJntVntrs'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    MngmntCAndJntVntrs = Column(Text)
    # Description:  Part IV repeating group  xpath: /IRS990ScheduleH/ManagementCoAndJntVenturesGrp 

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part IV Column (a)  Description:  Business name line 1  xpath: /IRS990ScheduleH/ManagementCoAndJntVenturesGrp/EntityName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part IV Column (a)  Description:  Business name line 2  xpath: /IRS990ScheduleH/ManagementCoAndJntVenturesGrp/EntityName/BusinessNameLine2Txt 

    PrmryActvtsTxt = Column(String(length=100))
    # Line number:  Part IV Column (b)  Description:  Description of entity's primary activity  xpath: /IRS990ScheduleH/ManagementCoAndJntVenturesGrp/PrimaryActivitiesTxt 

    OrgPrftOrOwnrshpPct = Column(Numeric(precision=6))
    # Line number:  Part IV Column (c)  Description:  Organization's profit % or ownership %  xpath: /IRS990ScheduleH/ManagementCoAndJntVenturesGrp/OrgProfitOrOwnershipPct 

    OfcrEtcPrftOrOwnrshpPct = Column(Numeric(precision=6))
    # Line number:  Part IV Column (d)  Description:  Officers, etc. profit % or ownership %  xpath: /IRS990ScheduleH/ManagementCoAndJntVenturesGrp/OfcrEtcProfitOrOwnershipPct 

    PhyscnsPrftOrOwnrshpPct = Column(Numeric(precision=6))
    # Line number:  Part IV Column (e)  Description:  Physican's profit % or ownership %  xpath: /IRS990ScheduleH/ManagementCoAndJntVenturesGrp/PhysiciansProfitOrOwnershipPct 

#######
#
# IRS990ScheduleH - OthHlthCareFcltsGrp
# A repeating structure from ScheduleH Part V-D - Other Health Care Facilities 
#
#######

class SkdHOthHlthCrFclts(Base):
    __tablename__='SkdHOthHlthCrFclts'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    OthHlthCrFclts = Column(Text)
    # Description:  Part V Section D repeating group  xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp 

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part V Section D  Description:  Business name line 1  xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/BusinessName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part V Section D  Description:  Business name line 2  xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/BusinessName/BusinessNameLine2Txt 

    AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part V Section D  Description:  Address line 2  xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/USAddress/AddressLine2Txt 

    ZIPCd = Column(String(length=15))
    # Line number:  Part V Section D  Description:  ZIP code  xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/USAddress/ZIPCd 

    AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part V Section D  Description:  Address line 1  xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/USAddress/AddressLine1Txt 

    CtyNm = Column(String(length=22))
    # Line number:  Part V Section D  Description:  City  xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/USAddress/CityNm 

    SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part V Section D  Description:  State  xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/USAddress/StateAbbreviationCd 

    FcltyTxt = Column(String(length=100))
    # Line number:  Part V Section D  Description:  Facility type  xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/FacilityTxt 

#######
#
# IRS990ScheduleH - SupplementalInformationDetail
# A repeating structure from ScheduleH Part VI Supplemental Information 
#
#######

class SkdHSpplmntlInfrmtnDtl(Base):
    __tablename__='SkdHSpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtnDtl = Column(Text)
    # Description:  Part VI contents  xpath: /IRS990ScheduleH/SupplementalInformationDetail 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part VI  Description:  Form, part and line number reference  xpath: /IRS990ScheduleH/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part VI  Description:  Form, part and line number explanation  xpath: /IRS990ScheduleH/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleH - HospitalFacilitiesGrp
# A repeating structure from ScheduleH Part V-A - Facility Information 
#
#######

class SkdHHsptlFclts(Base):
    __tablename__='SkdHHsptlFclts'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SkdH_HsptlFclts = Column(Text)
    # Description:  Part V Section A repeating group  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp 

    HsptlFclts_FcltyNm = Column(Integer)
    # Line number:  Part V Section A  Description:  Hospital facility number  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/FacilityNum 

    BsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part V Section A  Description:  Business name line 1  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/BusinessName/BusinessNameLine1Txt 

    BsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part V Section A  Description:  Business name line 2  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/BusinessName/BusinessNameLine2Txt 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part V Section A  Description:  Address line 1  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part V Section A  Description:  Address line 2  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part V Section A  Description:  City  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part V Section A  Description:  State  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part V Section A  Description:  ZIP code  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/USAddress/ZIPCd 

    HsptlFclts_WbstAddrssTxt = Column(String(length=100))
    # Line number:  Part V Section A  Description:  Primary website address of the hospital facility  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/WebsiteAddressTxt 

    HsptlFclts_SttLcnsNm = Column(Text)
    # Line number:  Part V Section A  Description:  Hospital facilities state license number  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/StateLicenseNum 

    SbrdntHsptlNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part V Section A  Description:  Business name line 1  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/SubordinateHospitalName/BusinessNameLine1Txt 

    SbrdntHsptlNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part V Section A  Description:  Business name line 2  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/SubordinateHospitalName/BusinessNameLine2Txt 

    HsptlFclts_SbrdntHsptlEIN = Column(String(length=9))
    # Line number:  Part V Section A  Description:  EIN, subordinate hospital  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/SubordinateHospitalEIN 

    HsptlFclts_LcnsdHsptlInd = Column(String(length=1))
    # Line number:  Part V Section A  Description:  Licensed hospital  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/LicensedHospitalInd 

    HsptlFclts_GnrlMdclAndSrgclInd = Column(String(length=1))
    # Line number:  Part V Section A  Description:  General medical and surgical  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/GeneralMedicalAndSurgicalInd 

    HsptlFclts_ChldrnsHsptlInd = Column(String(length=1))
    # Line number:  Part V Section A  Description:  Children's hospital  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/ChildrensHospitalInd 

    HsptlFclts_TchngHsptlInd = Column(String(length=1))
    # Line number:  Part V Section A  Description:  Teaching hospital  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/TeachingHospitalInd 

    HsptlFclts_CrtclAccssHsptlInd = Column(String(length=1))
    # Line number:  Part V Section A  Description:  Critical Access hospital  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/CriticalAccessHospitalInd 

    HsptlFclts_RsrchFcltyInd = Column(String(length=1))
    # Line number:  Part V Section A  Description:  Research facility  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/ResearchFacilityInd 

    HsptlFclts_EmrgncyRm24HrsInd = Column(String(length=1))
    # Line number:  Part V Section A  Description:  ER - 24 hours  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/EmergencyRoom24HrsInd 

    HsptlFclts_EmrgncyRmOthrInd = Column(String(length=1))
    # Line number:  Part V Section A  Description:  ER - other  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/EmergencyRoomOtherInd 

    HsptlFclts_OthrDsc = Column(String(length=100))
    # Line number:  Part V Section A  Description:  Other  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/OtherDesc 

    HsptlFclts_FcltyRprtngGrpCd = Column(Text)
    # Line number:  Part V Section A  Description:  Facility reporting group  xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/FacilityReportingGroupCd 

#######
#
# IRS990ScheduleH - SupplementalInformationGrp
# A repeating structure from ScheduleH Part V-C - Supplemental Information for Part V, Section B 
#
#######

class SkdHSpplmntlInfrmtn(Base):
    __tablename__='SkdHSpplmntlInfrmtn'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtn = Column(Text)
    # Description:  Part V Section C, Supplemental Information for Part V Section B  xpath: /IRS990ScheduleH/SupplementalInformationGrp 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part V  Description:  Form, part and line number reference  xpath: /IRS990ScheduleH/SupplementalInformationGrp/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part V  Description:  Form, part and line number reference explanation  xpath: /IRS990ScheduleH/SupplementalInformationGrp/ExplanationTxt 

#######
#
# IRS990ScheduleH - HospitalFcltyPoliciesPrctcGrp
# A repeating structure from ScheduleH Part V-B - Facility Information 
#
#######

class SkdHHsptlFcltyPlcsPrctc(Base):
    __tablename__='SkdHHsptlFcltyPlcsPrctc'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    HsptlFcltyPlcsPrctc = Column(Text)
    # Description:  Part V Section B repeating group  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp 

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part V Section B  Description:  Business name line 1  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/HospitalFacilityName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part V Section B  Description:  Business name line 2  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/HospitalFacilityName/BusinessNameLine2Txt 

    FcltyNm = Column(Integer)
    # Line number:  Part V Section B  Description:  Line number of hospital facility  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FacilityNum 

    FrstLcnsdCYOrPYInd = Column(String(length=5))
    # Line number:  Part V Section B Line 1  Description:  First licensed, registered or recognized by a State in current year or preceding prior year?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FirstLicensedCYOrPYInd 

    TxExmptHsptlCYOrPYInd = Column(String(length=5))
    # Line number:  Part V Section B Line 2  Description:  Acquired or placed into service as tax-exempt hospital in current year or  preceding prior year?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/TaxExemptHospitalCYOrPYInd 

    CHNACndctdInd = Column(String(length=5))
    # Line number:  Part V Section B Line 3  Description:  Conduct community needs health assessments?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CHNAConductedInd 

    CmmntyDfntnInd = Column(String(length=1))
    # Line number:  Part V Section B Line 3a  Description:  Definition of community served  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CommunityDefinitionInd 

    CmmntyDmgrphcsInd = Column(String(length=1))
    # Line number:  Part V Section B Line 3b  Description:  Demographics of community  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CommunityDemographicsInd 

    ExstngRsrcsInd = Column(String(length=1))
    # Line number:  Part V Section B Line 3c  Description:  Existing health care facilities and resources  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ExistingResourcesInd 

    HwDtObtndInd = Column(String(length=1))
    # Line number:  Part V Section B Line 3d  Description:  How data obtained  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/HowDataObtainedInd 

    CmmntyHlthNdsInd = Column(String(length=1))
    # Line number:  Part V Section B Line 3e  Description:  Health needs of community  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CommunityHealthNeedsInd 

    OthrHlthIsssInd = Column(String(length=1))
    # Line number:  Part V Section B Line 3f  Description:  Other health issues  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherHealthIssuesInd 

    CmmntyHlthNdsIdPrcssInd = Column(String(length=1))
    # Line number:  Part V Section B Line 3g  Description:  Identifying process  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CommunityHlthNeedsIdProcessInd 

    CnsltngPrcssInd = Column(String(length=1))
    # Line number:  Part V Section B Line 3h  Description:  Consulting process  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ConsultingProcessInd 

    InfrmtnGpsInd = Column(String(length=1))
    # Line number:  Part V Section B Line 3i  Description:  Information gaps  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/InformationGapsInd 

    OthrInd = Column(String(length=1))
    # Line number:  Part V Section B Line 3j  Description:  CHNA describes other  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherInd 

    CHNACndctdYr = Column(Text)
    # Line number:  Part V Section B Line 4  Description:  Year last conducted CHNA  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CHNAConductedYr 

    TkIntAccntOthrsInptInd = Column(String(length=5))
    # Line number:  Part V Section B Line 5  Description:  Take community input into account  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/TakeIntoAccountOthersInputInd 

    CHNACndctdWthOthrFcltsInd = Column(String(length=5))
    # Line number:  Part V Section B Line 6a  Description:  Other hospital facilities?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CHNAConductedWithOtherFcltsInd 

    CHNACndctdWthNnFcltsInd = Column(String(length=5))
    # Line number:  Part V Section B Line 6b  Description:  Other than hospital facilities?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CHNAConductedWithNonFcltsInd 

    CHNARprtWdlyAvlblInd = Column(String(length=5))
    # Line number:  Part V Section B Line 7  Description:  CHNA widely available to public?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CHNAReportWidelyAvailableInd 

    RptAvlblOnOwnWbstInd = Column(String(length=1))
    # Line number:  Part V Section B Line 7a  Description:  Available on own website  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/RptAvailableOnOwnWebsiteInd 

    OwnWbstURLTxt = Column(String(length=100))
    # Line number:  Part V Section B Line 7a  Description:  Hospital facilities website URL  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OwnWebsiteURLTxt 

    OthrWbstInd = Column(String(length=1))
    # Line number:  Part V Section B Line 7b  Description:  Other website  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherWebsiteInd 

    OthrWbstURLTxt = Column(String(length=100))
    # Line number:  Part V Section B Line 7b  Description:  Other website URL  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherWebsiteURLTxt 

    PprCpyPblcInspctnInd = Column(String(length=1))
    # Line number:  Part V Section B Line 7c  Description:  Made paper copy  available for public inspection  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PaperCopyPublicInspectionInd 

    RptAvlblThrOthrMthdInd = Column(String(length=1))
    # Line number:  Part V Section B Line 7d  Description:  Available other method  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/RptAvailableThruOtherMethodInd 

    ImplmnttnStrtgyAdptInd = Column(String(length=5))
    # Line number:  Part V Section B Line 8  Description:  Adopt implementation strategy?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ImplementationStrategyAdoptInd 

    ImplmnttnStrtgyAdptYr = Column(Text)
    # Line number:  Part V Section B Line 9  Description:  Year last adopted implementation strategy  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ImplementationStrategyAdptYr 

    StrtgyPstdWbstInd = Column(String(length=5))
    # Line number:  Part V Section B Line 10  Description:  Implementation strategy posted on website?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/StrategyPostedWebsiteInd 

    StrtgyWbstURLTxt = Column(String(length=100))
    # Line number:  Part V Section B Line 10a  Description:  Implementation strategy website URL  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/StrategyWebsiteURLTxt 

    StrtgyAttchdInd = Column(Text)
    # Line number:  Part V Section B Line 10b  Description:  Implementation strategy attached to return?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/StrategyAttachedInd 

    OrgnztnIncrExcsTxInd = Column(String(length=5))
    # Line number:  Part V Section B Line 12a  Description:  Incur an excise tax under section 4959 for the hospital facility's failure to conduct a CHNA as required by section 501(r)(3)?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OrganizationIncurExciseTaxInd 

    Frm4720FldInd = Column(String(length=5))
    # Line number:  Part V Section B Line 12b  Description:  File Form 4720 to report the section 4959 excise tax?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/Form4720FiledInd 

    ExcsRprtFrm4720FrAllAmt = Column(BigInteger)
    # Line number:  Part V Section B Line 12c  Description:  Total amount of section 4959 excise tax reported on Form 4720 for all of its hospital facilities?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ExciseReportForm4720ForAllAmt 

    ElgCrtrExplndInd = Column(String(length=5))
    # Line number:  Part V Section B Line 13  Description:  Policy explains eligibility criteria for financial assistance?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/EligCriteriaExplainedInd 

    FPGFmlyIncmLmtFrDscntInd = Column(String(length=1))
    # Line number:  Part V Section B Line 13a  Description:  Explained free care percent and discounted care percent  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FPGFamilyIncmLmtFreeDscntInd 

    FPGFmlyIncmLmtFrCrPct = Column(Numeric(precision=22))
    # Line number:  Part V Section B Line 13a  Description:  Percentage of FPG used to determine free care  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FPGFamilyIncmLmtFreeCarePct 

    FPGFmlyIncmLmtDscntCrPct = Column(Numeric(precision=22))
    # Line number:  Part V Section B Line 13a  Description:  Percentage of FPG used to determine discount care  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FPGFamilyIncmLmtDscntCarePct 

    IncmLvlCrtrInd = Column(String(length=1))
    # Line number:  Part V Section B Line 13b  Description:  Income level criteria  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/IncomeLevelCriteriaInd 

    AsstLvlCrtrInd = Column(String(length=1))
    # Line number:  Part V Section B Line 13c  Description:  Asset level criteria  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/AssetLevelCriteriaInd 

    MdclIndgncyCrtrInd = Column(String(length=1))
    # Line number:  Part V Section B Line 13d  Description:  Medical indigency criteria  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/MedicalIndigencyCriteriaInd 

    InsrncSttsCrtrInd = Column(String(length=1))
    # Line number:  Part V Section B Line 13e  Description:  Insurance status criteria  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/InsuranceStatusCriteriaInd 

    UndrnsrncSttCrtrInd = Column(String(length=1))
    # Line number:  Part V Section B Line 13f  Description:  Underinsurance status criteria  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/UnderinsuranceStatCriteriaInd 

    RsdncyCrtrInd = Column(String(length=1))
    # Line number:  Part V Section B Line 13g  Description:  Residency criteria  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ResidencyCriteriaInd 

    OthrCrtrInd = Column(String(length=1))
    # Line number:  Part V Section B Line 13h  Description:  Other criteria  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherCriteriaInd 

    ExplndBssInd = Column(String(length=5))
    # Line number:  Part V Section B Line 14  Description:  Policy explains basis for calculating amounts?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ExplainedBasisInd 

    AppFnnclAsstExplnInd = Column(String(length=5))
    # Line number:  Part V Section B Line 15  Description:  Policy explains method for applying for assistance?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/AppFinancialAsstExplnInd 

    DscrbdInfInd = Column(String(length=1))
    # Line number:  Part V Section B Line 15a  Description:  Described information as part of application.  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/DescribedInfoInd 

    DscrbdSprtDcInd = Column(String(length=1))
    # Line number:  Part V Section B Line 15b  Description:  Described supporting documentation as part of application.  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/DescribedSuprtDocInd 

    PrvddHsptlCntctInd = Column(String(length=1))
    # Line number:  Part V Section B Line 15c  Description:  Provided  contact information of hospital staff.  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ProvidedHospitalContactInd 

    PrvddNnprftCntctInd = Column(String(length=1))
    # Line number:  Part V Section B Line 15d  Description:  Provided contact information of nonprofit organization.  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ProvidedNonprofitContactInd 

    OthrMthdInd = Column(String(length=1))
    # Line number:  Part V Section B Line 15e  Description:  Other method used to explain.  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherMethodInd 

    IncldsPblctyMsrsInd = Column(String(length=5))
    # Line number:  Part V Section B Line 16  Description:  Policy includes publicity measures?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/IncludesPublicityMeasuresInd 

    FAPAvlblOnWbstInd = Column(String(length=1))
    # Line number:  Part V Section B Line 16a  Description:  FAP widely available on a website  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPAvailableOnWebsiteInd 

    FAPAvlblOnWbstURLTxt = Column(String(length=100))
    # Line number:  Part V Section B Line 16a  Description:  FAP website URL  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPAvailableOnWebsiteURLTxt 

    FAPAppAvlblOnWbstInd = Column(String(length=1))
    # Line number:  Part V Section B Line 16b  Description:  FAP application form widely available on a website  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPAppAvailableOnWebsiteInd 

    FAPAppAvlblOnWbstURLTxt = Column(String(length=100))
    # Line number:  Part V Section B Line 16b  Description:  FAP application form website URL  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPAppAvailableOnWebsiteURLTxt 

    FAPSmmryOnWbstInd = Column(String(length=1))
    # Line number:  Part V Section B Line 16c  Description:  FAP plain language summary on a website  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPSummaryOnWebsiteInd 

    FAPSmmryOnWbstURLTxt = Column(String(length=100))
    # Line number:  Part V Section B Line 16c  Description:  FAP plain language summary website URL  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPSummaryOnWebsiteURLTxt 

    FAPAvlblOnRqstNChrgInd = Column(String(length=1))
    # Line number:  Part V Section B Line 16d  Description:  FAP available upon request and without charge  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPAvlblOnRequestNoChargeInd 

    FAPAppAvlblOnRqstNChrgInd = Column(String(length=1))
    # Line number:  Part V Section B Line 16e  Description:  FAP application form available upon request and without charge  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPAppAvlblOnRequestNoChrgInd 

    FAPSmAvlblOnRqstNChrgInd = Column(String(length=1))
    # Line number:  Part V Section B Line 16f  Description:  FAP plain language summary available upon request and without charge  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPSumAvlblOnRequestNoChrgInd 

    FAPNtcDsplydInd = Column(String(length=1))
    # Line number:  Part V Section B Line 16g  Description:  Notice of availability of FAP displayed throughout hospital facility  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPNoticeDisplayedInd 

    CmmnttyNtfdFAPInd = Column(String(length=1))
    # Line number:  Part V Section B Line 16h  Description:  Notified community about availability of FAP  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CommuntityNotifiedFAPInd 

    OthrPblctyInd = Column(String(length=1))
    # Line number:  Part V Section B Line 16i  Description:  Other publicity  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherPublicityInd 

    FAPActnsOnNnpymntInd = Column(String(length=5))
    # Line number:  Part V Section B Line 17  Description:  Policy explains actions taken upon non-payment?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPActionsOnNonpaymentInd 

    PrmtRprtTCrdtAgncyInd = Column(String(length=1))
    # Line number:  Part V Section B Line 18a  Description:  Report to credit agency permitted  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitReportToCreditAgencyInd 

    PrmtSllngDbtInd = Column(String(length=1))
    # Line number:  Part V Section B Line 18b  Description:  Selling debt permitted  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitSellingDebtInd 

    PrmtLglJdclPrcssInd = Column(String(length=1))
    # Line number:  Part V Section B Line 18c  Description:  Actions that required a legal or judicial process  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitLegalJudicialProcessInd 

    PrmtOthrActnsInd = Column(String(length=1))
    # Line number:  Part V Section B Line 18d  Description:  Other actions permitted  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitOtherActionsInd 

    PrmtNActnsInd = Column(String(length=1))
    # Line number:  Part V Section B Line 18e  Description:  None of these actions or similar actions permitted  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitNoActionsInd 

    CllctnActvtsInd = Column(String(length=5))
    # Line number:  Part V Section B Line 19  Description:  Authorize third-party to engage in collection activities?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CollectionActivitiesInd 

    RprtngTCrdtAgncyInd = Column(String(length=1))
    # Line number:  Part V Section B Line 19a  Description:  Credit agency engaged  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ReportingToCreditAgencyInd 

    EnggdSllngDbtInd = Column(String(length=1))
    # Line number:  Part V Section B Line 19b  Description:  Selling debt engaged  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/EngagedSellingDebtInd 

    EnggdLglJdclPrcssInd = Column(String(length=1))
    # Line number:  Part V Section B Line 19c  Description:  Engaged actions that required a legal or judicial process  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/EngagedLegalJudicialProcessInd 

    OthrActnsInd = Column(String(length=1))
    # Line number:  Part V Section B Line 19d  Description:  Other actions engaged  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherActionsInd 

    FAPNtfdUpnAdmssnInd = Column(String(length=1))
    # Line number:  Part V Section B Line 20a  Description:  Notified upon admission  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPNotifiedUponAdmissionInd 

    FAPNtfdBfrDschrgInd = Column(String(length=1))
    # Line number:  Part V Section B Line 20b  Description:  Notified prior to discharge  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPNotifiedBeforeDischargeInd 

    FAPNtfdAllPtntsInd = Column(String(length=1))
    # Line number:  Part V Section B Line 20c  Description:  Notified patients in communications  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPNotifiedAllPatientsInd 

    DcmntdElgDtrmntnInd = Column(String(length=1))
    # Line number:  Part V Section B Line 20d  Description:  Documented determination  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/DocumentedEligDeterminationInd 

    OthrActnsTknInd = Column(String(length=1))
    # Line number:  Part V Section B Line 20e  Description:  Other action taken  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherActionsTakenInd 

    NnMdInd = Column(String(length=1))
    # Line number:  Part V Section B Line 20f  Description:  None of these efforts were made  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/NoneMadeInd 

    NndsEmrgncyCrPlcyInd = Column(String(length=5))
    # Line number:  Part V Section B Line 21  Description:  Non-discriminatory emergency medical care policy?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/NondisEmergencyCarePolicyInd 

    NEmrgncyCrInd = Column(String(length=1))
    # Line number:  Part V Section B Line 21a  Description:  No emergency care  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/NoEmergencyCareInd 

    NEmrgncyCrPlcyInd = Column(String(length=1))
    # Line number:  Part V Section B Line 21b  Description:  No emergency policy  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/NoEmergencyCarePolicyInd 

    EmrgncyCrLmtdInd = Column(String(length=1))
    # Line number:  Part V Section B Line 21c  Description:  Limits emergency care  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/EmergencyCareLimitedInd 

    OthrRsnInd = Column(String(length=1))
    # Line number:  Part V Section B Line 21d  Description:  Other reason  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherReasonInd 

    LwstNgttdRtsInd = Column(String(length=1))
    # Line number:  Part V Section B Line 22a  Description:  Charged amount in excess of lowest negotiated rates?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/LowestNegotiatedRatesInd 

    AvrgNgttdRtsInd = Column(String(length=1))
    # Line number:  Part V Section B Line 22b  Description:  Charged amount in excess of average negotiated rates?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/AverageNegotiatedRatesInd 

    MdcrRtsInd = Column(String(length=1))
    # Line number:  Part V Section B Line 22c  Description:  Charged more than medicare rate?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/MedicareRatesInd 

    OthrMthdUsdInd = Column(String(length=1))
    # Line number:  Part V Section B Line 22d  Description:  Used other method  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherMethodUsedInd 

    AmntsGnrllyBlldInd = Column(String(length=5))
    # Line number:  Part V Section B Line 23  Description:  Charged more than amount generally billed?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/AmountsGenerallyBilledInd 

    GrssChrgsInd = Column(String(length=5))
    # Line number:  Part V Section B Line 24  Description:  Gross charges in billing?  xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/GrossChargesInd 

#######
#
# IRS990ScheduleI - ScheduleI Part I General Information on Grants and Assistance 
#
#######

class skedi_part_i(Base):
    __tablename__='skedi_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    GrntRcrdsMntndInd = Column(String(length=5))
    # Line number:  Part I Line 1  Description:  Does the organization maintain records to substantiate the amount of the grants or assistance, the grantees' eligibility for the grants or assistance, and the selection criteria used to award the grants or assistance?  xpath: /IRS990ScheduleI/GrantRecordsMaintainedInd 

#######
#
# IRS990ScheduleI - ScheduleI Part II Grants and Other Assistance to Governments and Organizations in the United States 
#
#######

class skedi_part_ii(Base):
    __tablename__='skedi_part_ii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Ttl501c3OrgCnt = Column(BigInteger)
    # Line number:  Part II Line 2  Description:  Enter total number of 501(c)(3) and government organizations  xpath: /IRS990ScheduleI/Total501c3OrgCnt 

    TtlOthrOrgCnt = Column(BigInteger)
    # Line number:  Part II Line 3  Description:  Enter total number of other organizations  xpath: /IRS990ScheduleI/TotalOtherOrgCnt 

#######
#
# IRS990ScheduleI - RecipientTable
# A repeating structure from ScheduleI Part II Grants and Other Assistance to Governments and Organizations in the United States 
#
#######

class SkdIRcpntTbl(Base):
    __tablename__='SkdIRcpntTbl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SkdI_RcpntTbl = Column(Text)
    # Line number:  Part II  Description:  Complete if the organization reported more than $5,000 on Form 990, Part IX, line 1 for any recipient that received more than $5,000  xpath: /IRS990ScheduleI/RecipientTable 

    RcpntBsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part II Line 1 Column (a)  Description:  Business name line 1  xpath: /IRS990ScheduleI/RecipientTable/RecipientBusinessName/BusinessNameLine1Txt 

    RcpntBsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part II Line 1 Column (a)  Description:  Business name line 2  xpath: /IRS990ScheduleI/RecipientTable/RecipientBusinessName/BusinessNameLine2Txt 

    RcpntTbl_RcpntEIN = Column(String(length=9))
    # Line number:  Part II Line  1 Column (b)  Description:  EIN of recipient  xpath: /IRS990ScheduleI/RecipientTable/RecipientEIN 

    RcpntTbl_IRCSctnDsc = Column(String(length=20))
    # Line number:  Part II Line  1 Column (c)  Description:  IRC code section if applicable  xpath: /IRS990ScheduleI/RecipientTable/IRCSectionDesc 

    RcpntTbl_CshGrntAmt = Column(BigInteger)
    # Line number:  Part II Line  1 Column (d)  Description:  Amount of cash grant  xpath: /IRS990ScheduleI/RecipientTable/CashGrantAmt 

    RcpntTbl_NnCshAssstncAmt = Column(BigInteger)
    # Line number:  Part II Line  1 Column (e)  Description:  Amount of non-cash assistance  xpath: /IRS990ScheduleI/RecipientTable/NonCashAssistanceAmt 

    RcpntTbl_VltnMthdUsdDsc = Column(String(length=100))
    # Line number:  Part II Line  1 Column (f)  Description:  Method of valuation (book. FMV, appraisal, other)  xpath: /IRS990ScheduleI/RecipientTable/ValuationMethodUsedDesc 

    RcpntTbl_NnCshAssstncDsc = Column(String(length=100))
    # Line number:  Part II Line  1 Column (g)  Description:  Description of non-cash assistance  xpath: /IRS990ScheduleI/RecipientTable/NonCashAssistanceDesc 

    RcpntTbl_PrpsOfGrntTxt = Column(Text)
    # Line number:  Part II Line  1 Column (h)  Description:  Purpose of grant  xpath: /IRS990ScheduleI/RecipientTable/PurposeOfGrantTxt 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part II Line  1 Column (a)  Description:  Address line 1  xpath: /IRS990ScheduleI/RecipientTable/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part II Line  1 Column (a)  Description:  Address line 2  xpath: /IRS990ScheduleI/RecipientTable/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part II Line  1 Column (a)  Description:  City  xpath: /IRS990ScheduleI/RecipientTable/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part II Line  1 Column (a)  Description:  State  xpath: /IRS990ScheduleI/RecipientTable/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part II Line  1 Column (a)  Description:  ZIP code  xpath: /IRS990ScheduleI/RecipientTable/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part II Line  1 Column (a)  Description:  Address line 1  xpath: /IRS990ScheduleI/RecipientTable/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part II Line  1 Column (a)  Description:  Address line 2  xpath: /IRS990ScheduleI/RecipientTable/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part II Line  1 Column (a)  Description:  City  xpath: /IRS990ScheduleI/RecipientTable/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part II Line  1 Column (a)  Description:  Province or state  xpath: /IRS990ScheduleI/RecipientTable/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part II Line  1 Column (a)  Description:  Country  xpath: /IRS990ScheduleI/RecipientTable/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part II Line  1 Column (a)  Description:  Postal code  xpath: /IRS990ScheduleI/RecipientTable/ForeignAddress/ForeignPostalCd 

#######
#
# IRS990ScheduleI - GrantsOtherAsstToIndivInUSGrp
# A repeating structure from ScheduleI Part III Grants and Other Assistance to Individuals in the United States 
#
#######

class SkdIGrntsOthrAsstTIndvInUS(Base):
    __tablename__='SkdIGrntsOthrAsstTIndvInUS'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    GrntsOthrAsstTIndvInUS = Column(Text)
    # Description:  Part III content  xpath: /IRS990ScheduleI/GrantsOtherAsstToIndivInUSGrp 

    GrntTxt = Column(Text)
    # Line number:  Part III Column (a)  Description:  Type of grant or assistance  xpath: /IRS990ScheduleI/GrantsOtherAsstToIndivInUSGrp/GrantTypeTxt 

    RcpntCnt = Column(BigInteger)
    # Line number:  Part III Column (b)  Description:  Number of recipients  xpath: /IRS990ScheduleI/GrantsOtherAsstToIndivInUSGrp/RecipientCnt 

    CshGrntAmt = Column(BigInteger)
    # Line number:  Part III Column (c)  Description:  Amount of cash grant  xpath: /IRS990ScheduleI/GrantsOtherAsstToIndivInUSGrp/CashGrantAmt 

    NnCshAssstncAmt = Column(BigInteger)
    # Line number:  Part III Column (d)  Description:  Amount of non-cash assistance  xpath: /IRS990ScheduleI/GrantsOtherAsstToIndivInUSGrp/NonCashAssistanceAmt 

    VltnMthdUsdDsc = Column(String(length=100))
    # Line number:  Part III Column (e)  Description:  Method of valuation (book, FMV, appraisal, other)  xpath: /IRS990ScheduleI/GrantsOtherAsstToIndivInUSGrp/ValuationMethodUsedDesc 

    NnCshAssstncDsc = Column(Text)
    # Line number:  Part III Column (f)  Description:  Description of non-cash assistance  xpath: /IRS990ScheduleI/GrantsOtherAsstToIndivInUSGrp/NonCashAssistanceDesc 

#######
#
# IRS990ScheduleI - SupplementalInformationDetail
# A repeating structure from ScheduleI Part IV Supplemental Information
#
#######

class SkdISpplmntlInfrmtnDtl(Base):
    __tablename__='SkdISpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtnDtl = Column(Text)
    # Description:  Part IV content  xpath: /IRS990ScheduleI/SupplementalInformationDetail 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part IV  Description:  Form, part and line number reference  xpath: /IRS990ScheduleI/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part IV  Description:  Form, part and line number reference explanation  xpath: /IRS990ScheduleI/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleJ - ScheduleJ Part I Questions Regarding Compensation
#
#######

class skedj_part_i(Base):
    __tablename__='skedj_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    FrstClssOrChrtrTrvlInd = Column(String(length=1))
    # Line number:  Part I Line 1a  Description:  First class or charter travel  xpath: /IRS990ScheduleJ/FirstClassOrCharterTravelInd 

    TrvlFrCmpnnsInd = Column(String(length=1))
    # Line number:  Part I Line 1a  Description:  Travel for companions  xpath: /IRS990ScheduleJ/TravelForCompanionsInd 

    IdmnfctnGrssUpPmtsInd = Column(String(length=1))
    # Line number:  Part I Line 1a  Description:  Idemnification and gross-up payments  xpath: /IRS990ScheduleJ/IdemnificationGrossUpPmtsInd 

    DscrtnrySpndngAcctInd = Column(String(length=1))
    # Line number:  Part I Line 1a  Description:  Discretionary spending account  xpath: /IRS990ScheduleJ/DiscretionarySpendingAcctInd 

    HsngAllwncOrRsdncInd = Column(String(length=1))
    # Line number:  Part I Line 1a  Description:  Housing allowance or residence  xpath: /IRS990ScheduleJ/HousingAllowanceOrResidenceInd 

    PymntsFrUsOfRsdncInd = Column(String(length=1))
    # Line number:  Part I Line 1a  Description:  Payments for use of residence  xpath: /IRS990ScheduleJ/PaymentsForUseOfResidenceInd 

    ClbDsOrFsInd = Column(String(length=1))
    # Line number:  Part I Line 1a  Description:  Club dues or fees  xpath: /IRS990ScheduleJ/ClubDuesOrFeesInd 

    PrsnlSrvcsInd = Column(String(length=1))
    # Line number:  Part I Line 1a  Description:  Personal services  xpath: /IRS990ScheduleJ/PersonalServicesInd 

    WrttnPlcyRfTAndEExpnssInd = Column(String(length=5))
    # Line number:  Part I Line 1b  Description:  Written policy reference T and E expenses?  xpath: /IRS990ScheduleJ/WrittenPolicyRefTAndEExpnssInd 

    SbstnttnRqrdInd = Column(String(length=5))
    # Line number:  Part I Line 2  Description:  Substantiation required?  xpath: /IRS990ScheduleJ/SubstantiationRequiredInd 

    CmpnstnCmmttInd = Column(String(length=1))
    # Line number:  Part I Line 3  Description:  Compensation committee  xpath: /IRS990ScheduleJ/CompensationCommitteeInd 

    IndpndntCnsltntInd = Column(String(length=1))
    # Line number:  Part I Line 3  Description:  Independent consultant  xpath: /IRS990ScheduleJ/IndependentConsultantInd 

    Frm990OfOthrOrgnztnsInd = Column(String(length=1))
    # Line number:  Part I Line 3  Description:  Form 990 of other organizations  xpath: /IRS990ScheduleJ/Form990OfOtherOrganizationsInd 

    WrttnEmplymntCntrctInd = Column(String(length=1))
    # Line number:  Part I Line 3  Description:  Written employment contract  xpath: /IRS990ScheduleJ/WrittenEmploymentContractInd 

    CmpnstnSrvyInd = Column(String(length=1))
    # Line number:  Part I Line 3  Description:  Compensation survey  xpath: /IRS990ScheduleJ/CompensationSurveyInd 

    BrdOrCmmttApprvlInd = Column(String(length=1))
    # Line number:  Part I Line 3  Description:  Board or committee approval  xpath: /IRS990ScheduleJ/BoardOrCommitteeApprovalInd 

    SvrncPymntInd = Column(String(length=5))
    # Line number:  Part I Line 4a  Description:  Severance payment?  xpath: /IRS990ScheduleJ/SeverancePaymentInd 

    SpplmntlNnqlRtrPlnInd = Column(String(length=5))
    # Line number:  Part I Line 4b  Description:  Supplemental nonqualified retirement plan?  xpath: /IRS990ScheduleJ/SupplementalNonqualRtrPlanInd 

    EqtyBsdCmpArrngmInd = Column(String(length=5))
    # Line number:  Part I Line 4c  Description:  Equity based compensation arrangement?  xpath: /IRS990ScheduleJ/EquityBasedCompArrngmInd 

    CmpBsdOnRvnOfFlngOrgInd = Column(String(length=5))
    # Line number:  Part I Line 5a  Description:  Compensation based on revenue of filing org?  xpath: /IRS990ScheduleJ/CompBasedOnRevenueOfFlngOrgInd 

    CmpBsdOnRvRltdOrgsInd = Column(String(length=5))
    # Line number:  Part I Line 5b  Description:  Compensation based on revenue of related orgs?  xpath: /IRS990ScheduleJ/CompBsdOnRevRelatedOrgsInd 

    CmpBsdNtErnsFlngOrgInd = Column(String(length=5))
    # Line number:  Part I Line 6a  Description:  Compensation based on net earnings of filing org?  xpath: /IRS990ScheduleJ/CompBsdNetEarnsFlngOrgInd 

    CmpBsdNtErnsRltdOrgsInd = Column(String(length=5))
    # Line number:  Part I Line 6b  Description:  Compensation based on net earnings of related orgs?  xpath: /IRS990ScheduleJ/CompBsdNetEarnsRltdOrgsInd 

    AnyNnFxdPymntsInd = Column(String(length=5))
    # Line number:  Part I Line 7  Description:  Any non-fixed payments?  xpath: /IRS990ScheduleJ/AnyNonFixedPaymentsInd 

    IntlCntrctExcptnInd = Column(String(length=5))
    # Line number:  Part I Line 8  Description:  Initial contract exception?  xpath: /IRS990ScheduleJ/InitialContractExceptionInd 

    RbttblPrsmptnPrcInd = Column(String(length=5))
    # Line number:  Part I Line 9  Description:  Rebuttable presumption procedure?  xpath: /IRS990ScheduleJ/RebuttablePresumptionProcInd 

#######
#
# IRS990ScheduleJ - SupplementalInformationDetail
# A repeating structure from ScheduleJ Part III Supplemental Information
#
#######

class SkdJSpplmntlInfrmtnDtl(Base):
    __tablename__='SkdJSpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtnDtl = Column(Text)
    # Description:  Part III contents  xpath: /IRS990ScheduleJ/SupplementalInformationDetail 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part III  Description:  Form, Part and line number reference  xpath: /IRS990ScheduleJ/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part III  Description:  Form, Part and line number reference explanation  xpath: /IRS990ScheduleJ/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleJ - RltdOrgOfficerTrstKeyEmplGrp
# A repeating structure from ScheduleJ Part II Officers, Directors, Trustees, Key Employees, and Highest Compensated Employees 
#
#######

class SkdJRltdOrgOffcrTrstKyEmpl(Base):
    __tablename__='SkdJRltdOrgOffcrTrstKyEmpl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    RltdOrgOffcrTrstKyEmpl = Column(Text)
    # Description:  Part II contents  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp 

    PrsnNm = Column(String(length=35))
    # Line number:  Part II Column (A)  Description:  Name of officer - person  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/PersonNm 

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part II Column (A)  Description:  Business name line 1  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/BusinessName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part II Column (A)  Description:  Business name line 2  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/BusinessName/BusinessNameLine2Txt 

    TtlTxt = Column(String(length=100))
    # Line number:  Part II Column (A)  Description:  Title of Officer  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/TitleTxt 

    BsCmpnstnFlngOrgAmt = Column(BigInteger)
    # Line number:  Part II Column (B)(i)  Description:  Base compensation ($) from filing organization  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/BaseCompensationFilingOrgAmt 

    CmpnstnBsdOnRltdOrgsAmt = Column(BigInteger)
    # Line number:  Part II Column (B)(i)  Description:  Compensation based on related organizations?  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/CompensationBasedOnRltdOrgsAmt 

    BnsFlngOrgnztnAmnt = Column(BigInteger)
    # Line number:  Part II Column (B)(ii)  Description:  Bonus and incentive compensation ($) from filing organization  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/BonusFilingOrganizationAmount 

    BnsRltdOrgnztnsAmt = Column(BigInteger)
    # Line number:  Part II Column (B)(ii)  Description:  Bonus and incentive compensation ($) from related organizations  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/BonusRelatedOrganizationsAmt 

    OthrCmpnstnFlngOrgAmt = Column(BigInteger)
    # Line number:  Part II Column (B)(iii)  Description:  Other compensation ($) from filing organization  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/OtherCompensationFilingOrgAmt 

    OthrCmpnstnRltdOrgsAmt = Column(BigInteger)
    # Line number:  Part II Column (B)(iii)  Description:  Other compensation ($) from related organizations  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/OtherCompensationRltdOrgsAmt 

    DfrrdCmpnstnFlngOrgAmt = Column(BigInteger)
    # Line number:  Part II Column (C)  Description:  Deferred compensation ($) from filing organization  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/DeferredCompensationFlngOrgAmt 

    DfrrdCmpRltdOrgsAmt = Column(BigInteger)
    # Line number:  Part II Column (C)  Description:  Deferred compensation ($) from related organizations  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/DeferredCompRltdOrgsAmt 

    NntxblBnftsFlngOrgAmt = Column(BigInteger)
    # Line number:  Part II Column (D)  Description:  Nontaxable benefits ($) from filing organization  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/NontaxableBenefitsFilingOrgAmt 

    NntxblBnftsRltdOrgsAmt = Column(BigInteger)
    # Line number:  Part II Column (D)  Description:  Nontaxable benefits ($) from related organizations  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/NontaxableBenefitsRltdOrgsAmt 

    TtlCmpnstnFlngOrgAmt = Column(BigInteger)
    # Line number:  Part II Column (E)  Description:  Total of (B)(i) - (D), from filing org  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/TotalCompensationFilingOrgAmt 

    TtlCmpnstnRltdOrgsAmt = Column(BigInteger)
    # Line number:  Part II Column (E)  Description:  Total of (B)(i) - (D), from related orgs  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/TotalCompensationRltdOrgsAmt 

    CmpRprtPrr990FlngOrgAmt = Column(BigInteger)
    # Line number:  Part II Column (F)  Description:  Comp reported prior 990 - from filing org  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/CompReportPrior990FilingOrgAmt 

    CmpRprtPrr990RltdOrgsAmt = Column(BigInteger)
    # Line number:  Part II Column (F)  Description:  Comp reported prior 990 - from related orgs  xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/CompReportPrior990RltdOrgsAmt 

#######
#
# IRS990ScheduleK - SupplementalInformationDetail
# A repeating structure from ScheduleK Part VI - Supplemental Information 
#
#######

class SkdKSpplmntlInfrmtnDtl(Base):
    __tablename__='SkdKSpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtnDtl = Column(Text)
    # Description:  Part VI contents  xpath: /IRS990ScheduleK/SupplementalInformationDetail 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part VI  Description:  Form, part and line number reference  xpath: /IRS990ScheduleK/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part VI  Description:  Form, part and line number reference explanation  xpath: /IRS990ScheduleK/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleK - ProceduresCorrectiveActionGrp
# A repeating structure from ScheduleK Part V - Violations Identified and Corrected 
#
#######

class SkdKPrcdrsCrrctvActn(Base):
    __tablename__='SkdKPrcdrsCrrctvActn'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    BndRfrncCd = Column(Text)
    # Line number:  Part V  Description:  Bond issue reference number (A-D)  xpath: /IRS990ScheduleK/ProceduresCorrectiveActionGrp/BondReferenceCd 

    PrcdrsCrrctvActnInd = Column(String(length=5))
    # Line number:  Part V  Description:  Procedures to ensure violations identified and corrected?  xpath: /IRS990ScheduleK/ProceduresCorrectiveActionGrp/ProceduresCorrectiveActionInd 

#######
#
# IRS990ScheduleK - TaxExemptBondsProceedsGrp
# A repeating structure from ScheduleK Part II - Proceeds Table 
#
#######

class SkdKTxExmptBndsPrcds(Base):
    __tablename__='SkdKTxExmptBndsPrcds'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    BndRfrncCd = Column(Text)
    # Line number:  Part II  Description:  Bond issue reference number (A-D)  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/BondReferenceCd 

    RtrdAmt = Column(BigInteger)
    # Line number:  Part II Line 1  Description:  Amount of bonds retired  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/RetiredAmt 

    BndDfsdAmt = Column(BigInteger)
    # Line number:  Part II Line 2  Description:  Amount of bonds defeased  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/BondDefeasedAmt 

    TtlPrcdsAmt = Column(BigInteger)
    # Line number:  Part II Line 3  Description:  Total proceeds of issue  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/TotalProceedsAmt 

    InRsrvFndAmt = Column(BigInteger)
    # Line number:  Part II Line 4  Description:  Gross proceeds in reserve funds  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/InReserveFundAmt 

    CptlzdIntrstAmt = Column(BigInteger)
    # Line number:  Part II Line 5  Description:  Capitalized interest from proceeds  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/CapitalizedInterestAmt 

    RfndngEscrwAmt = Column(BigInteger)
    # Line number:  Part II Line 6  Description:  Proceeds in refunding escrow  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/RefundingEscrowAmt 

    IssncCstsFrmPrcdsAmt = Column(BigInteger)
    # Line number:  Part II Line 7  Description:  Issuance costs from proceeds  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/IssuanceCostsFromProceedsAmt 

    CrdtEnhncmntAmt = Column(BigInteger)
    # Line number:  Part II Line 8  Description:  Credit enhancement from proceeds  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/CreditEnhancementAmt 

    WrkngCptlExpndtrsAmt = Column(BigInteger)
    # Line number:  Part II Line 9  Description:  Working capital expenditures from proceeds  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/WorkingCapitalExpendituresAmt 

    CptlExpndtrsAmt = Column(BigInteger)
    # Line number:  Part II Line 10  Description:  Capital expenditures from proceeds  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/CapitalExpendituresAmt 

    OthrSpntPrcdsAmt = Column(BigInteger)
    # Line number:  Part II Line 11  Description:  Other spent proceeds  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/OtherSpentProceedsAmt 

    UnspntAmt = Column(BigInteger)
    # Line number:  Part II Line 12  Description:  Amount unspent  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/UnspentAmt 

    SbstntlCmpltnYr = Column(Integer)
    # Line number:  Part II Line 13  Description:  Year of substantial completion  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/SubstantialCompletionYr 

    CrrntRfndngInd = Column(String(length=5))
    # Line number:  Part II Line 14  Description:  Current refunding?  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/CurrentRefundingInd 

    AdvncRfndngInd = Column(String(length=5))
    # Line number:  Part II Line 15  Description:  Advance refunding?  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/AdvanceRefundingInd 

    FnlAllctnMdInd = Column(String(length=5))
    # Line number:  Part II Line 16  Description:  Final allocation made?  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/FinalAllocationMadeInd 

    AdqtBksAndRcMntInd = Column(String(length=5))
    # Line number:  Part II Line 17  Description:  Adequate books and records maintained?  xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/AdequateBooksAndRecMaintInd 

#######
#
# IRS990ScheduleK - TaxExemptBondsIssuesGrp
# A repeating structure from ScheduleK Part I - Bond Issues Table 
#
#######

class SkdKTxExmptBndsIsss(Base):
    __tablename__='SkdKTxExmptBndsIsss'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    BndRfrncCd = Column(Text)
    # Line number:  Part I  Description:  Bond issue reference number (A-D)  xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/BondReferenceCd 

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part I Column (a)  Description:  Business name line 1  xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/IssuerName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part I Column (a)  Description:  Business name line 2  xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/IssuerName/BusinessNameLine2Txt 

    BndIssrEIN = Column(String(length=9))
    # Line number:  Part I Column (b)  Description:  Issuer EIN  xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/BondIssuerEIN 

    CUSIPNm = Column(String(length=9))
    # Line number:  Part I Column (c)  Description:  CUSIP number  xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/CUSIPNum 

    BndIssdDt = Column(String(length=31))
    # Line number:  Part I Column (d)  Description:  Date issued  xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/BondIssuedDt 

    IssPrcAmt = Column(BigInteger)
    # Line number:  Part I Column (e)  Description:  Issue price  xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/IssuePriceAmt 

    PrpsDsc = Column(String(length=100))
    # Line number:  Part I Column (f)  Description:  Description of purpose  xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/PurposeDesc 

    DfsdInd = Column(String(length=5))
    # Line number:  Part I Column (g)  Description:  Defeased?  xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/DefeasedInd 

    OnBhlfOfIssrInd = Column(String(length=5))
    # Line number:  Part I Column (h)  Description:  On behalf of issuer?  xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/OnBehalfOfIssuerInd 

    PlFnncngInd = Column(String(length=5))
    # Line number:  Part I Column (i)  Description:  Pool financing?  xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/PoolFinancingInd 

#######
#
# IRS990ScheduleK - TaxExemptBondsArbitrageGrp
# A repeating structure from ScheduleK Part IV - Arbitrage 
#
#######

class SkdKTxExmptBndsArbtrg(Base):
    __tablename__='SkdKTxExmptBndsArbtrg'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    TxExmptBndsArbtrg_BndRfrncCd = Column(Text)
    # Line number:  Part IV  Description:  Bond issue reference number (A-D)  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/BondReferenceCd 

    TxExmptBndsArbtrg_Frm8038TFldInd = Column(String(length=5))
    # Line number:  Part IV Line 1  Description:  Form 8038-T filed?  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/Form8038TFiledInd 

    TxExmptBndsArbtrg_RbtNtDYtInd = Column(String(length=5))
    # Line number:  Part IV Line 2a  Description:  Rebate not due yet?  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/RebateNotDueYetInd 

    TxExmptBndsArbtrg_ExcptnTRbtInd = Column(String(length=5))
    # Line number:  Part IV Line 2b  Description:  Exception to rebate?  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/ExceptionToRebateInd 

    TxExmptBndsArbtrg_NRbtDInd = Column(String(length=5))
    # Line number:  Part IV Line 2c  Description:  No rebate due?  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/NoRebateDueInd 

    TxExmptBndsArbtrg_VrblRtIssInd = Column(String(length=5))
    # Line number:  Part IV Line 3  Description:  Variable rate issue?  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/VariableRateIssueInd 

    TxExmptBndsArbtrg_HdgIdntfdInBksAndRcInd = Column(String(length=5))
    # Line number:  Part IV Line 4a  Description:  Hedge identified in books and records?  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/HedgeIdentifiedInBksAndRecInd 

    HdgPrvdrNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part IV Line 4b  Description:  Business name line 1  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/HedgeProviderName/BusinessNameLine1Txt 

    HdgPrvdrNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part IV Line 4b  Description:  Business name line 2  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/HedgeProviderName/BusinessNameLine2Txt 

    TxExmptBndsArbtrg_TrmOfHdgPct = Column(Numeric(precision=22))
    # Line number:  Part IV Line 4c  Description:  Term of hedge  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/TermOfHedgePct 

    TxExmptBndsArbtrg_SprntgrtdHdgInd = Column(String(length=5))
    # Line number:  Part IV Line 4d  Description:  Was the hedge superintegrated?  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/SuperintegratedHedgeInd 

    TxExmptBndsArbtrg_HdgTrmntdInd = Column(String(length=5))
    # Line number:  Part IV Line 4e  Description:  Was the hedge terminated?  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/HedgeTerminatedInd 

    TxExmptBndsArbtrg_GrssPrcdsInvstdInGICInd = Column(String(length=5))
    # Line number:  Part IV Line 5a  Description:  Gross proceeds invested in GIC?  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/GrossProceedsInvestedInGICInd 

    GICPrvdrNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part IV Line 5b  Description:  Business name line 1  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/GICProviderName/BusinessNameLine1Txt 

    GICPrvdrNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part IV Line 5b  Description:  Business name line 2  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/GICProviderName/BusinessNameLine2Txt 

    TxExmptBndsArbtrg_TrmOfGICPct = Column(Numeric(precision=22))
    # Line number:  Part IV Line 5c  Description:  Term of GIC  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/TermOfGICPct 

    TxExmptBndsArbtrg_RgltrySfHrbrStsfdInd = Column(String(length=5))
    # Line number:  Part IV Line 5d  Description:  Regulatory safe harbor satisfied?  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/RegulatorySafeHarborStsfdInd 

    TxExmptBndsArbtrg_GrssPrcdsInvstdInd = Column(String(length=5))
    # Line number:  Part IV Line 6  Description:  Gross proceeds invested?  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/GrossProceedsInvestedInd 

    TxExmptBndsArbtrg_WrttnPrcTMntrRqsInd = Column(String(length=5))
    # Line number:  Part IV Line 7  Description:  Written procedures to monitor requirements?  xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/WrittenProcToMonitorReqsInd 

#######
#
# IRS990ScheduleK - TaxExemptBondsPrivateBusUseGrp
# A repeating structure from ScheduleK Part III - Private Use 
#
#######

class SkdKTxExmptBndsPrvtBsUs(Base):
    __tablename__='SkdKTxExmptBndsPrvtBsUs'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    BndRfrncCd = Column(Text)
    # Line number:  Part III  Description:  Bond issue reference number (A-D)  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/BondReferenceCd 

    OwnngBndFnncdPrprtyInd = Column(String(length=5))
    # Line number:  Part III Line 1  Description:  Partnership or LLC owning bond financed property?  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/OwningBondFinancedPropertyInd 

    AnyLsArrngmntsInd = Column(String(length=5))
    # Line number:  Part III Line 2  Description:  Any lease arrangements?  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/AnyLeaseArrangementsInd 

    MgmtCntrctBndFncdPrpInd = Column(String(length=5))
    # Line number:  Part III Line 3a  Description:  Management contract for bond financed property?  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/MgmtContractBondFincdPropInd 

    EnggBndCnslCntrctsInd = Column(String(length=5))
    # Line number:  Part III Line 3b  Description:  Bond Counsel routinely engaged to review management or service contracts?  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/EngageBondCounselContractsInd 

    AnyRsrchAgrmntsInd = Column(String(length=5))
    # Line number:  Part III Line 3c  Description:  Any research agreements?  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/AnyResearchAgreementsInd 

    EnggBndCnslRsrchInd = Column(String(length=5))
    # Line number:  Part III Line 3d  Description:  Bond Counsel routinely engaged to review management or service contracts?  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/EngageBondCounselResearchInd 

    PrvtBsUsByOthrsPct = Column(Numeric(precision=6))
    # Line number:  Part III Line 4  Description:  Percentage of private business use by others  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/PrivateBusUseByOthersPct 

    PrvtBsCncrnngUBIPct = Column(Numeric(precision=6))
    # Line number:  Part III Line 5  Description:  Percentage of private business concerning UBI  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/PrivateBusConcerningUBIPct 

    TtlPrvtBsnssUsPct = Column(Numeric(precision=6))
    # Line number:  Part III Line 6  Description:  Total of lines 4 and 5  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/TotalPrivateBusinessUsePct 

    BndIssMtPrvtScPymtTstInd = Column(String(length=5))
    # Line number:  Part III Line 7  Description:  Bond issue meets private security or payment test?  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/BondIssMeetPrvtSecPymtTestInd 

    ChngInUsBndFnncdPrpInd = Column(String(length=5))
    # Line number:  Part III Line 8a  Description:  Change in use of bond financed property?  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/ChangeInUseBondFinancedPropInd 

    ChngInUsBndFnncdPrpPct = Column(Numeric(precision=6))
    # Line number:  Part III Line 8b  Description:  Percentage change in use of bond financed property  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/ChangeInUseBondFinancedPropPct 

    RmdlActnTknInd = Column(String(length=5))
    # Line number:  Part III Line 8c  Description:  Remedial action taken?  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/RemedialActionTakenInd 

    PrcsNnqlfdBndRmdtdInd = Column(String(length=5))
    # Line number:  Part III Line 9  Description:  Nonqualified bonds remediated procedures?  xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/ProcsNonqualifiedBondRemdtdInd 

#######
#
# IRS990ScheduleL - ScheduleL Part I Excess Benefit Transactions 
#
#######

class skedl_part_i(Base):
    __tablename__='skedl_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    TxImpsdAmt = Column(BigInteger)
    # Line number:  Part I Line 2  Description:  Amount of tax imposed  xpath: /IRS990ScheduleL/TaxImposedAmt 

    TxRmbrsdAmt = Column(BigInteger)
    # Line number:  Part I Line 3  Description:  Amount of tax reimbursed  xpath: /IRS990ScheduleL/TaxReimbursedAmt 

#######
#
# IRS990ScheduleL - ScheduleL Part II Loans to and/or From Interested Persons 
#
#######

class skedl_part_ii(Base):
    __tablename__='skedl_part_ii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    TtlBlncDAmt = Column(BigInteger)
    # Line number:  Part II Column d  Description:  Total balance due  xpath: /IRS990ScheduleL/TotalBalanceDueAmt 

#######
#
# IRS990ScheduleL - SupplementalInformationDetail
# A repeating structure from ScheduleL Part V Supplemental Information 
#
#######

class SkdLSpplmntlInfrmtnDtl(Base):
    __tablename__='SkdLSpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtnDtl = Column(Text)
    # Description:  Part V contents  xpath: /IRS990ScheduleL/SupplementalInformationDetail 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part V  Description:  Form, part and line number reference  xpath: /IRS990ScheduleL/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part V  Description:  Form, part and line number reference explanation  xpath: /IRS990ScheduleL/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleL - LoansBtwnOrgInterestedPrsnGrp
# A repeating structure from ScheduleL Part II Loans to and/or From Interested Persons 
#
#######

class SkdLLnsBtwnOrgIntrstdPrsn(Base):
    __tablename__='SkdLLnsBtwnOrgIntrstdPrsn'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    PrsnNm = Column(String(length=35))
    # Line number:  Part II Column (a)  Description:  Name - Person  xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/PersonNm 

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part II Column (a)  Description:  Business name line 1  xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/BusinessName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part II Column (a)  Description:  Business name line 2  xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/BusinessName/BusinessNameLine2Txt 

    LnTOrgnztnInd = Column(String(length=1))
    # Line number:  Part II Column (d)  Description:  Loan to organization?  xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/LoanToOrganizationInd 

    LnFrmOrgnztnInd = Column(String(length=1))
    # Line number:  Part II Column (d)  Description:  Loan from organization?  xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/LoanFromOrganizationInd 

    RltnshpWthOrgTxt = Column(String(length=100))
    # Line number:  Part II Column (b)  Description:  Relationship with organization  xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/RelationshipWithOrgTxt 

    LnPrpsTxt = Column(String(length=100))
    # Line number:  Part II Column (c)  Description:  Purpose of loan  xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/LoanPurposeTxt 

    OrgnlPrncplAmt = Column(BigInteger)
    # Line number:  Part II Column (e)  Description:  Original principal amount  xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/OriginalPrincipalAmt 

    BlncDAmt = Column(BigInteger)
    # Line number:  Part II Column (f)  Description:  Balance due  xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/BalanceDueAmt 

    DfltInd = Column(String(length=5))
    # Line number:  Part II Column (g)  Description:  Default?  xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/DefaultInd 

    BrdOrCmmttApprvlInd = Column(String(length=5))
    # Line number:  Part II Column (h)  Description:  Approved by board?  xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/BoardOrCommitteeApprovalInd 

    WrttnAgrmntInd = Column(String(length=5))
    # Line number:  Part II Column (i)  Description:  Written agreement?  xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/WrittenAgreementInd 

#######
#
# IRS990ScheduleL - GrntAsstBnftInterestedPrsnGrp
# A repeating structure from ScheduleL Part III Grants or Assistance Benefiting Interested Persons
#
#######

class SkdLGrntAsstBnftIntrstdPrsn(Base):
    __tablename__='SkdLGrntAsstBnftIntrstdPrsn'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    GrntAsstBnftIntrstdPrsn = Column(Text)
    # Description:  Part III content  xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp 

    PrsnNm = Column(String(length=35))
    # Line number:  Part III Column (a)  Description:  Name of interested person - Person  xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/PersonNm 

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part III Column (a)  Description:  Business name line 1  xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/BusinessName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part III Column (a)  Description:  Business name line 2  xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/BusinessName/BusinessNameLine2Txt 

    RltnshpWthOrgTxt = Column(String(length=100))
    # Line number:  Part III Column (b)  Description:  Relationship with organization  xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/RelationshipWithOrgTxt 

    CshGrntAmt = Column(BigInteger)
    # Line number:  Part III Column (c)  Description:  Amount of grant  xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/CashGrantAmt 

    OfAssstncTxt = Column(String(length=100))
    # Line number:  Part III Column (d)  Description:  Type of assistance  xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/TypeOfAssistanceTxt 

    AssstncPrpsTxt = Column(String(length=100))
    # Line number:  Part III Column (e)  Description:  Purpose of assistance  xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/AssistancePurposeTxt 

#######
#
# IRS990ScheduleL - BusTrInvolveInterestedPrsnGrp
# A repeating structure from ScheduleL Part IV Business Transactions Involving Interested Persons
#
#######

class SkdLBsTrInvlvIntrstdPrsn(Base):
    __tablename__='SkdLBsTrInvlvIntrstdPrsn'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    BsTrInvlvIntrstdPrsn = Column(Text)
    # Description:  Part IV content  xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp 

    NmOfIntrstd = Column(Text)
    # Description:  Name of interested person  xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/NameOfInterested 

    PrsnNm = Column(String(length=35))
    # Line number:  Part IV Column (a)  Description:  Name - Person  xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/NameOfInterested/PersonNm 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part IV Column (a)  Description:  Business name line 2  xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/NameOfInterested/BusinessName/BusinessNameLine2Txt 

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part IV Column (a)  Description:  Business name line 1  xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/NameOfInterested/BusinessName/BusinessNameLine1Txt 

    RltnshpDscrptnTxt = Column(String(length=100))
    # Line number:  Part IV Column (b)  Description:  Relationship with organization  xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/RelationshipDescriptionTxt 

    TrnsctnAmt = Column(BigInteger)
    # Line number:  Part IV Column (c)  Description:  Amount of transaction  xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/TransactionAmt 

    TrnsctnDsc = Column(Text)
    # Line number:  Part IV Column (d)  Description:  Description of transaction  xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/TransactionDesc 

    ShrngOfRvnsInd = Column(String(length=5))
    # Line number:  Part IV Column (e)  Description:  Sharing of revenues?  xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/SharingOfRevenuesInd 

#######
#
# IRS990ScheduleL - DisqualifiedPersonExBnftTrGrp
# A repeating structure from ScheduleL Part I Excess Benefit Transactions 
#
#######

class SkdLDsqlfdPrsnExBnftTr(Base):
    __tablename__='SkdLDsqlfdPrsnExBnftTr'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    PrsnNm = Column(String(length=35))
    # Line number:  Part I Column (1a)  Description:  Name - Person  xpath: /IRS990ScheduleL/DisqualifiedPersonExBnftTrGrp/PersonNm 

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part I Column (1a)  Description:  Business name line 1  xpath: /IRS990ScheduleL/DisqualifiedPersonExBnftTrGrp/BusinessName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part I Column (1a)  Description:  Business name line 2  xpath: /IRS990ScheduleL/DisqualifiedPersonExBnftTrGrp/BusinessName/BusinessNameLine2Txt 

    RlnDsqlfdPrsnOrgTxt = Column(String(length=100))
    # Line number:  Part I Column (1b)  Description:  Relationship between disqualified person and organization  xpath: /IRS990ScheduleL/DisqualifiedPersonExBnftTrGrp/RlnDisqualifiedPersonOrgTxt 

    TrnsctnDsc = Column(Text)
    # Line number:  Part I Column (1c)  Description:  Description of transaction  xpath: /IRS990ScheduleL/DisqualifiedPersonExBnftTrGrp/TransactionDesc 

    TrnsctnCrrctdInd = Column(String(length=5))
    # Line number:  Part I Column (1d)  Description:  Transaction corrected?  xpath: /IRS990ScheduleL/DisqualifiedPersonExBnftTrGrp/TransactionCorrectedInd 

#######
#
# IRS990ScheduleM - ScheduleM Part I Types of Property 
#
#######

class skedm_part_i(Base):
    __tablename__='skedm_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SkdM_Frm8283RcvdCnt = Column(BigInteger)
    # Line number:  Part I Line 29  Description:  Number of 8283s received  xpath: /IRS990ScheduleM/Form8283ReceivedCnt 

    SkdM_AnyPrprtyThtMstBHldInd = Column(String(length=5))
    # Line number:  Part I Line 30a  Description:  Any property that must be held?  xpath: /IRS990ScheduleM/AnyPropertyThatMustBeHeldInd 

    SkdM_RvwPrcssUnslNCGftsInd = Column(String(length=5))
    # Line number:  Part I Line 31  Description:  Review process reference unusual noncash gifts?  xpath: /IRS990ScheduleM/ReviewProcessUnusualNCGiftsInd 

    SkdM_ThrdPrtsUsdInd = Column(String(length=5))
    # Line number:  Part I Line 32a  Description:  Third parties used?  xpath: /IRS990ScheduleM/ThirdPartiesUsedInd 

    Txdrmy_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/TaxidermyGrp/NonCashCheckboxInd 

    ScrPrtnrshpTrstIntrsts_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/SecurPrtnrshpTrustIntrstsGrp/NonCashCheckboxInd 

    BtsAndPlns_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/BoatsAndPlanesGrp/NonCashCheckboxInd 

    ScrtsClslyHldStck_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/SecuritiesCloselyHeldStockGrp/NonCashCheckboxInd 

    QlfdCntrbOthr_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/QualifiedContribOtherGrp/NonCashCheckboxInd 

    ScrtsPblclyTrdd_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/SecuritiesPubliclyTradedGrp/NonCashCheckboxInd 

    RlEsttRsdntl_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/RealEstateResidentialGrp/NonCashCheckboxInd 

    FdInvntry_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/FoodInventoryGrp/NonCashCheckboxInd 

    BksAndPblctns_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/BooksAndPublicationsGrp/NonCashCheckboxInd 

    CrsAndOthrVhcls_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/CarsAndOtherVehiclesGrp/NonCashCheckboxInd 

    RlEsttCmmrcl_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/RealEstateCommercialGrp/NonCashCheckboxInd 

    ScrtsMsc_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/SecuritiesMiscellaneousGrp/NonCashCheckboxInd 

    Cllctbls_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/CollectiblesGrp/NonCashCheckboxInd 

    HstrclArtfcts_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/HistoricalArtifactsGrp/NonCashCheckboxInd 

    RlEsttOthr_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/RealEstateOtherGrp/NonCashCheckboxInd 

    DrgsAndMdclSppls_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/DrugsAndMedicalSuppliesGrp/NonCashCheckboxInd 

    IntllctlPrprty_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/IntellectualPropertyGrp/NonCashCheckboxInd 

    ClthngAndHshldGds_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/ClothingAndHouseholdGoodsGrp/NonCashCheckboxInd 

    WrksOfArt_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/WorksOfArtGrp/NonCashCheckboxInd 

    ScntfcSpcmns_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/ScientificSpecimensGrp/NonCashCheckboxInd 

    ArtFrctnlIntrst_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/ArtFractionalInterestGrp/NonCashCheckboxInd 

    ArchlgclArtfcts_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/ArchaeologicalArtifactsGrp/NonCashCheckboxInd 

    ArtHstrclTrsrs_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/ArtHistoricalTreasuresGrp/NonCashCheckboxInd 

    QlfdCntrbHstStrct_NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/QualifiedContribHistStructGrp/NonCashCheckboxInd 

    ScrtsPblclyTrdd_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/SecuritiesPubliclyTradedGrp/ContributionCnt 

    HstrclArtfcts_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/HistoricalArtifactsGrp/ContributionCnt 

    IntllctlPrprty_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/IntellectualPropertyGrp/ContributionCnt 

    Txdrmy_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/TaxidermyGrp/ContributionCnt 

    QlfdCntrbHstStrct_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/QualifiedContribHistStructGrp/ContributionCnt 

    QlfdCntrbOthr_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/QualifiedContribOtherGrp/ContributionCnt 

    ArchlgclArtfcts_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/ArchaeologicalArtifactsGrp/ContributionCnt 

    RlEsttCmmrcl_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/RealEstateCommercialGrp/ContributionCnt 

    ArtHstrclTrsrs_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/ArtHistoricalTreasuresGrp/ContributionCnt 

    RlEsttRsdntl_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/RealEstateResidentialGrp/ContributionCnt 

    ScrPrtnrshpTrstIntrsts_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/SecurPrtnrshpTrustIntrstsGrp/ContributionCnt 

    ArtFrctnlIntrst_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/ArtFractionalInterestGrp/ContributionCnt 

    RlEsttOthr_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/RealEstateOtherGrp/ContributionCnt 

    Cllctbls_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/CollectiblesGrp/ContributionCnt 

    BtsAndPlns_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/BoatsAndPlanesGrp/ContributionCnt 

    BksAndPblctns_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/BooksAndPublicationsGrp/ContributionCnt 

    ScntfcSpcmns_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/ScientificSpecimensGrp/ContributionCnt 

    CrsAndOthrVhcls_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/CarsAndOtherVehiclesGrp/ContributionCnt 

    WrksOfArt_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/WorksOfArtGrp/ContributionCnt 

    ScrtsMsc_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/SecuritiesMiscellaneousGrp/ContributionCnt 

    ClthngAndHshldGds_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/ClothingAndHouseholdGoodsGrp/ContributionCnt 

    DrgsAndMdclSppls_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/DrugsAndMedicalSuppliesGrp/ContributionCnt 

    ScrtsClslyHldStck_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/SecuritiesCloselyHeldStockGrp/ContributionCnt 

    FdInvntry_CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/FoodInventoryGrp/ContributionCnt 

    RlEsttOthr_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/RealEstateOtherGrp/NoncashContributionsRptF990Amt 

    RlEsttRsdntl_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/RealEstateResidentialGrp/NoncashContributionsRptF990Amt 

    ScntfcSpcmns_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/ScientificSpecimensGrp/NoncashContributionsRptF990Amt 

    ScrPrtnrshpTrstIntrsts_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/SecurPrtnrshpTrustIntrstsGrp/NoncashContributionsRptF990Amt 

    ScrtsClslyHldStck_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/SecuritiesCloselyHeldStockGrp/NoncashContributionsRptF990Amt 

    ScrtsMsc_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/SecuritiesMiscellaneousGrp/NoncashContributionsRptF990Amt 

    WrksOfArt_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/WorksOfArtGrp/NoncashContributionsRptF990Amt 

    Txdrmy_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/TaxidermyGrp/NoncashContributionsRptF990Amt 

    ArchlgclArtfcts_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/ArchaeologicalArtifactsGrp/NoncashContributionsRptF990Amt 

    ArtFrctnlIntrst_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/ArtFractionalInterestGrp/NoncashContributionsRptF990Amt 

    ArtHstrclTrsrs_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/ArtHistoricalTreasuresGrp/NoncashContributionsRptF990Amt 

    BtsAndPlns_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/BoatsAndPlanesGrp/NoncashContributionsRptF990Amt 

    BksAndPblctns_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/BooksAndPublicationsGrp/NoncashContributionsRptF990Amt 

    CrsAndOthrVhcls_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/CarsAndOtherVehiclesGrp/NoncashContributionsRptF990Amt 

    ClthngAndHshldGds_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/ClothingAndHouseholdGoodsGrp/NoncashContributionsRptF990Amt 

    Cllctbls_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/CollectiblesGrp/NoncashContributionsRptF990Amt 

    DrgsAndMdclSppls_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/DrugsAndMedicalSuppliesGrp/NoncashContributionsRptF990Amt 

    FdInvntry_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/FoodInventoryGrp/NoncashContributionsRptF990Amt 

    HstrclArtfcts_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/HistoricalArtifactsGrp/NoncashContributionsRptF990Amt 

    IntllctlPrprty_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/IntellectualPropertyGrp/NoncashContributionsRptF990Amt 

    ScrtsPblclyTrdd_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/SecuritiesPubliclyTradedGrp/NoncashContributionsRptF990Amt 

    QlfdCntrbHstStrct_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/QualifiedContribHistStructGrp/NoncashContributionsRptF990Amt 

    QlfdCntrbOthr_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/QualifiedContribOtherGrp/NoncashContributionsRptF990Amt 

    RlEsttCmmrcl_NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/RealEstateCommercialGrp/NoncashContributionsRptF990Amt 

    WrksOfArt_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/WorksOfArtGrp/MethodOfDeterminingRevenuesTxt 

    ClthngAndHshldGds_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/ClothingAndHouseholdGoodsGrp/MethodOfDeterminingRevenuesTxt 

    ArtFrctnlIntrst_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/ArtFractionalInterestGrp/MethodOfDeterminingRevenuesTxt 

    RlEsttCmmrcl_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/RealEstateCommercialGrp/MethodOfDeterminingRevenuesTxt 

    Cllctbls_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/CollectiblesGrp/MethodOfDeterminingRevenuesTxt 

    ArchlgclArtfcts_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/ArchaeologicalArtifactsGrp/MethodOfDeterminingRevenuesTxt 

    ArtHstrclTrsrs_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/ArtHistoricalTreasuresGrp/MethodOfDeterminingRevenuesTxt 

    BtsAndPlns_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/BoatsAndPlanesGrp/MethodOfDeterminingRevenuesTxt 

    BksAndPblctns_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/BooksAndPublicationsGrp/MethodOfDeterminingRevenuesTxt 

    CrsAndOthrVhcls_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/CarsAndOtherVehiclesGrp/MethodOfDeterminingRevenuesTxt 

    DrgsAndMdclSppls_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/DrugsAndMedicalSuppliesGrp/MethodOfDeterminingRevenuesTxt 

    FdInvntry_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/FoodInventoryGrp/MethodOfDeterminingRevenuesTxt 

    HstrclArtfcts_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/HistoricalArtifactsGrp/MethodOfDeterminingRevenuesTxt 

    IntllctlPrprty_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/IntellectualPropertyGrp/MethodOfDeterminingRevenuesTxt 

    QlfdCntrbHstStrct_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/QualifiedContribHistStructGrp/MethodOfDeterminingRevenuesTxt 

    QlfdCntrbOthr_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/QualifiedContribOtherGrp/MethodOfDeterminingRevenuesTxt 

    RlEsttOthr_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/RealEstateOtherGrp/MethodOfDeterminingRevenuesTxt 

    RlEsttRsdntl_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/RealEstateResidentialGrp/MethodOfDeterminingRevenuesTxt 

    ScntfcSpcmns_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/ScientificSpecimensGrp/MethodOfDeterminingRevenuesTxt 

    ScrPrtnrshpTrstIntrsts_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/SecurPrtnrshpTrustIntrstsGrp/MethodOfDeterminingRevenuesTxt 

    ScrtsClslyHldStck_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/SecuritiesCloselyHeldStockGrp/MethodOfDeterminingRevenuesTxt 

    ScrtsMsc_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/SecuritiesMiscellaneousGrp/MethodOfDeterminingRevenuesTxt 

    ScrtsPblclyTrdd_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/SecuritiesPubliclyTradedGrp/MethodOfDeterminingRevenuesTxt 

    Txdrmy_MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/TaxidermyGrp/MethodOfDeterminingRevenuesTxt 

#######
#
# IRS990ScheduleM - SupplementalInformationDetail
# A repeating structure from ScheduleM Part II Repeating Explanation Table 
#
#######

class SkdMSpplmntlInfrmtnDtl(Base):
    __tablename__='SkdMSpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtnDtl = Column(Text)
    # Line number:  Part II  Description:  Explanation repeating group  xpath: /IRS990ScheduleM/SupplementalInformationDetail 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part II  Description:  Form, part and line number reference  xpath: /IRS990ScheduleM/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part II  Description:  Form, part and line number reference explanation  xpath: /IRS990ScheduleM/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleM - OtherNonCashContriTableGrp
# A repeating structure from ScheduleM Part I Types of Property 
#
#######

class SkdMOthrNnCshCntrTbl(Base):
    __tablename__='SkdMOthrNnCshCntrTbl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    Dsc = Column(String(length=100))
    # Line number:  Lines 25 - 28  Description:  Description  xpath: /IRS990ScheduleM/OtherNonCashContriTableGrp/Desc 

    NnCshChckbxInd = Column(String(length=1))
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  xpath: /IRS990ScheduleM/OtherNonCashContriTableGrp/NonCashCheckboxInd 

    CntrbtnCnt = Column(BigInteger)
    # Line number:  Column (b)  Description:  Number of contributions  xpath: /IRS990ScheduleM/OtherNonCashContriTableGrp/ContributionCnt 

    NncshCntrbtnsRptF990Amt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  xpath: /IRS990ScheduleM/OtherNonCashContriTableGrp/NoncashContributionsRptF990Amt 

    MthdOfDtrmnngRvnsTxt = Column(String(length=100))
    # Line number:  Column (d)  Description:  Method of determining revenues  xpath: /IRS990ScheduleM/OtherNonCashContriTableGrp/MethodOfDeterminingRevenuesTxt 

#######
#
# IRS990ScheduleN - ScheduleN Part I Liquidation, Termination or Dissolution 
#
#######

class skedn_part_i(Base):
    __tablename__='skedn_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    LqdtnOfAsstsTbl = Column(Text)
    # Line number:  Part I Line 1  Description:  Complete Part I if the organization ceased its operations and any remaining activities are for the purpose of dissolving, paying debts, or distributing any remaining assets  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp 

    DrctrOfSccssrInd = Column(String(length=5))
    # Line number:  Part I Line 2a  Description:  Become a director or trustee of a successor or transferee organization?  xpath: /IRS990ScheduleN/DirectorOfSuccessorInd 

    EmplyOfSccssrInd = Column(String(length=5))
    # Line number:  Part I Line 2b  Description:  Become an employee of, or independent contractor for, a successor or transferee organization?  xpath: /IRS990ScheduleN/EmployeeOfSuccessorInd 

    OwnrOfSccssrInd = Column(String(length=5))
    # Line number:  Part I Line 2c  Description:  Become a direct or indirect owner of a successor or transferee organization?  xpath: /IRS990ScheduleN/OwnerOfSuccessorInd 

    RcvCmpnstnInd = Column(String(length=5))
    # Line number:  Part I Line 2d  Description:  Receive, or become entitled to, compensation or other similar payments as a result of the organization's liquidation, termination, or dissolution?  xpath: /IRS990ScheduleN/ReceiveCompensationInd 

    AsstsDstrbtdInd = Column(String(length=5))
    # Line number:  Part I Line 3  Description:  Did the organization distribute its assets in accordance with its governing instruments?  xpath: /IRS990ScheduleN/AssetsDistributedInd 

    RqrdTNtfyAGInd = Column(String(length=5))
    # Line number:  Part I Line 4a  Description:  Is the organization required to notify the attorney general or other appropriate state official of its intent to dissolve?  xpath: /IRS990ScheduleN/RequiredToNotifyAGInd 

    AttrnyGnrlNtfdInd = Column(String(length=5))
    # Line number:  Part I Line 4b  Description:  If "Yes," did the organization provide such notice?  xpath: /IRS990ScheduleN/AttorneyGeneralNotifiedInd 

    LbltsPdInd = Column(String(length=5))
    # Line number:  Part I Line 5  Description:  Did the organization discharge or pay all liabilities in accordance with state laws?  xpath: /IRS990ScheduleN/LiabilitiesPaidInd 

    BndsOtstndngInd = Column(String(length=5))
    # Line number:  Part I Line 6a  Description:  Did the organization have any tax-exempt bonds outstanding during the year?  xpath: /IRS990ScheduleN/BondsOutstandingInd 

    BndLbltsDschrgdInd = Column(String(length=5))
    # Line number:  Part I Line 6b  Description:  Did the organization discharge or defease tax-exempt bond liabilities in accordance with the Internal Revenue Code and state laws?  xpath: /IRS990ScheduleN/BondLiabilitiesDischargedInd 

#######
#
# IRS990ScheduleN - ScheduleN Part II Sale, Exchange, Disposition or Other Transfer of more than 25% of the Organization's Assets 
#
#######

class skedn_part_ii(Base):
    __tablename__='skedn_part_ii'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    DrctrOfSccssr2Ind = Column(String(length=5))
    # Line number:  Part II Line 2a  Description:  Become a director or trustee of a successor or transferee organization?  xpath: /IRS990ScheduleN/DirectorOfSuccessor2Ind 

    EmplyOfSccssr2Ind = Column(String(length=5))
    # Line number:  Part II Line 2b  Description:  Become an employee of, or independent contractor for, a successor or transferee organization?  xpath: /IRS990ScheduleN/EmployeeOfSuccessor2Ind 

    OwnrOfSccssr2Ind = Column(String(length=5))
    # Line number:  Part II Line 2c  Description:  Become a direct or indirect owner of a successor or transferee organization?  xpath: /IRS990ScheduleN/OwnerOfSuccessor2Ind 

    RcvCmpnstn2Ind = Column(String(length=5))
    # Line number:  Part II Line 2d  Description:  Receive, or become entitled to, compensation or other similar payments as a result of the organization's significant disposition of assets?  xpath: /IRS990ScheduleN/ReceiveCompensation2Ind 

#######
#
# IRS990ScheduleN - SupplementalInformationDetail
# A repeating structure from ScheduleN Part III Explanations 
#
#######

class SkdNSpplmntlInfrmtnDtl(Base):
    __tablename__='SkdNSpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtnDtl = Column(Text)
    # Description:  Part III contents  xpath: /IRS990ScheduleN/SupplementalInformationDetail 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part III  Description:  Form, part and line number reference  xpath: /IRS990ScheduleN/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part III  Description:  Form, part and line number reference explanation  xpath: /IRS990ScheduleN/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleN - DispositionOfAssetsDetail
# A repeating structure from ScheduleN Part II Sale, Exchange, Disposition or Other Transfer of more than 25% of the Organization's Assets 
#
#######

class SkdNDspstnOfAsstsDtl(Base):
    __tablename__='SkdNDspstnOfAsstsDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    DspstnOfAsstsDtl_AsstsDstrOrExpnssPdDsc = Column(Text)
    # Line number:  Column (a)  Description:  Description of asset(s) distributed or transactional expenses paid  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/AssetsDistriOrExpnssPaidDesc 

    DspstnOfAsstsDtl_DstrbtnDt = Column(String(length=31))
    # Line number:  Column (b)  Description:  Date of distribution  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/DistributionDt 

    DspstnOfAsstsDtl_FrMrktVlOfAsstAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Fair market value of asset(s) distributed or amount of transactional expenses  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/FairMarketValueOfAssetAmt 

    DspstnOfAsstsDtl_MthdOfFMVDtrmntnTxt = Column(Text)
    # Line number:  Column (d)  Description:  Method of determining FMV for asset(s) distributed or transactional expenses  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/MethodOfFMVDeterminationTxt 

    DspstnOfAsstsDtl_EIN = Column(String(length=9))
    # Line number:  Column (e)  Description:  EIN of recipient (if tax-exempt)  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/EIN 

    DspstnOfAsstsDtl_IRCSctnTxt = Column(String(length=100))
    # Line number:  Column (g)  Description:  IRC code section of recipient(s) (if tax-exempt) or type of entity  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/IRCSectionTxt 

    DspstnOfAsstsDtl_PrsnNm = Column(String(length=35))
    # Line number:  Column (f)  Description:  Name - Person  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/PersonNm 

    BsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Column (f)  Description:  Business name line 1  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/BusinessName/BusinessNameLine1Txt 

    BsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Column (f)  Description:  Business name line 2  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/BusinessName/BusinessNameLine2Txt 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Column (f)  Description:  Address line 1  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Column (f)  Description:  Address line 2  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Column (f)  Description:  City  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Column (f)  Description:  State  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Column (f)  Description:  ZIP code  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Column (f)  Description:  Address line 1  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Column (f)  Description:  Address line 2  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Column (f)  Description:  City  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Column (f)  Description:  Province or state  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Column (f)  Description:  Country  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Column (f)  Description:  Postal code  xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/ForeignAddress/ForeignPostalCd 

#######
#
# IRS990ScheduleN - LiquidationOfAssetsDetail
# A repeating structure from ScheduleN Part I Liquidation, Termination or Dissolution 
#
#######

class SkdNLqdtnOfAsstsDtl(Base):
    __tablename__='SkdNLqdtnOfAsstsDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    LqdtnOfAsstsDtl_AsstsDstrOrExpnssPdDsc = Column(Text)
    # Line number:  Column (a)  Description:  Description of asset(s) distributed or transactional expenses paid  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/AssetsDistriOrExpnssPaidDesc 

    LqdtnOfAsstsDtl_DstrbtnDt = Column(String(length=31))
    # Line number:  Column (b)  Description:  Date of distribution  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/DistributionDt 

    LqdtnOfAsstsDtl_FrMrktVlOfAsstAmt = Column(BigInteger)
    # Line number:  Column (c)  Description:  Fair market value of asset(s) distributed or amount of transactional expenses  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/FairMarketValueOfAssetAmt 

    LqdtnOfAsstsDtl_MthdOfFMVDtrmntnTxt = Column(Text)
    # Line number:  Column (d)  Description:  Method of determining FMV for asset(s) distributed or transactional expenses  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/MethodOfFMVDeterminationTxt 

    LqdtnOfAsstsDtl_EIN = Column(String(length=9))
    # Line number:  Column (e)  Description:  EIN of recipient (if tax-exempt)  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/EIN 

    LqdtnOfAsstsDtl_IRCSctnTxt = Column(String(length=100))
    # Line number:  Column (g)  Description:  IRC code section of recipient(s) (if tax-exempt) or type of entity  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/IRCSectionTxt 

    LqdtnOfAsstsDtl_PrsnNm = Column(String(length=35))
    # Line number:  Column (f)  Description:  Name - Person  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/PersonNm 

    BsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Column (f)  Description:  Business name line 1  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/BusinessName/BusinessNameLine1Txt 

    BsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Column (f)  Description:  Business name line 2  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/BusinessName/BusinessNameLine2Txt 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Column (f)  Description:  ZIP code  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/USAddress/ZIPCd 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Column (f)  Description:  Address line 2  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/USAddress/AddressLine2Txt 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Column (f)  Description:  State  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/USAddress/StateAbbreviationCd 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Column (f)  Description:  Address line 1  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/USAddress/AddressLine1Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Column (f)  Description:  City  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/USAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Column (f)  Description:  Province or state  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Column (f)  Description:  City  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/ForeignAddress/CityNm 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Column (f)  Description:  Address line 2  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Column (f)  Description:  Address line 1  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Column (f)  Description:  Country  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Column (f)  Description:  Postal code  xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/ForeignAddress/ForeignPostalCd 

#######
#
# IRS990ScheduleO - SupplementalInformationDetail
# A repeating structure from ScheduleO Part I 
#
#######

class SkdOSpplmntlInfrmtnDtl(Base):
    __tablename__='SkdOSpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Description:  Form, part and line number reference  xpath: /IRS990ScheduleO/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Description:  Form, part and line number reference explanation  xpath: /IRS990ScheduleO/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleR - ScheduleR Part V - Transactions with Related Organizations and Noncharitable Exempt Organizations 
#
#######

class skedr_part_v(Base):
    __tablename__='skedr_part_v'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    RcptOfIntAnntsRntsRyltsInd = Column(String(length=5))
    # Line number:  Part V Line 1a  Description:  Receipt of interest, annuities, rents, royalties?  xpath: /IRS990ScheduleR/ReceiptOfIntAnntsRntsRyltsInd 

    GftGrntOrCpCntrTOthOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1b  Description:  Gift, grant, or capital contribution to other organization?  xpath: /IRS990ScheduleR/GiftGrntOrCapContriToOthOrgInd 

    GftGrntCpCntrFrmOthOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1c  Description:  Gift, grant, or capital contribution from other organization?  xpath: /IRS990ScheduleR/GiftGrntCapContriFromOthOrgInd 

    LnsOrGrntsTOthrOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1d  Description:  Loans or loan guarantees to or for other organization?  xpath: /IRS990ScheduleR/LoansOrGuaranteesToOtherOrgInd 

    LnsOrGrntsFrmOthOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1e  Description:  Loans or loan guarantees by other organization?  xpath: /IRS990ScheduleR/LoansOrGuaranteesFromOthOrgInd 

    DvRltdOrgnztnInd = Column(String(length=5))
    # Line number:  Part V Line 1f  Description:  Dividends from related organization(s)? (Y-N)  xpath: /IRS990ScheduleR/DivRelatedOrganizationInd 

    AsstSlTOthrOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1g  Description:  Sale of assets to other organization?  xpath: /IRS990ScheduleR/AssetSaleToOtherOrgInd 

    AsstPrchsFrmOthrOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1h  Description:  Purchase of assets from other organization?  xpath: /IRS990ScheduleR/AssetPurchaseFromOtherOrgInd 

    AsstExchngInd = Column(String(length=5))
    # Line number:  Part V Line 1i  Description:  Exchange of assets?  xpath: /IRS990ScheduleR/AssetExchangeInd 

    RntlOfFcltsTOthOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1j  Description:  Lease of facilities, equipment, or other assets to other organizations?  xpath: /IRS990ScheduleR/RentalOfFacilitiesToOthOrgInd 

    RntlOfFcltsFrmOthOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1k  Description:  Lease of facilities, equipment, or other assets from other organizations?  xpath: /IRS990ScheduleR/RentalOfFcltsFromOthOrgInd 

    PrfrmOfSrvcsFrOthOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1l  Description:  Performance of services or membership or fundraising solicitations for other organizations?  xpath: /IRS990ScheduleR/PerformOfServicesForOthOrgInd 

    PrfrmOfSrvcsByOthrOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1m  Description:  Performance of services or membership or fundraising solicitations by other organizations?  xpath: /IRS990ScheduleR/PerformOfServicesByOtherOrgInd 

    ShrngOfFcltsInd = Column(String(length=5))
    # Line number:  Part V Line 1n  Description:  Sharing of facilities, equipment, mailing lists, other assets, or employees?  xpath: /IRS990ScheduleR/SharingOfFacilitiesInd 

    PdEmplysShrngInd = Column(String(length=5))
    # Line number:  Part V Line 1o  Description:  Sharing of paid employees?  xpath: /IRS990ScheduleR/PaidEmployeesSharingInd 

    RmbrsmntPdTOthrOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1p  Description:  Reimbursement paid to other organization for expenses?  xpath: /IRS990ScheduleR/ReimbursementPaidToOtherOrgInd 

    RmbrsmntPdByOthrOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1q  Description:  Reimbursement paid by other organization for expenses?  xpath: /IRS990ScheduleR/ReimbursementPaidByOtherOrgInd 

    TrnsfrTOthrOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1r  Description:  Other transfer of cash or property to other organization?  xpath: /IRS990ScheduleR/TransferToOtherOrgInd 

    TrnsfrFrmOthrOrgInd = Column(String(length=5))
    # Line number:  Part V Line 1s  Description:  Other transfer of cash or property from other organization?  xpath: /IRS990ScheduleR/TransferFromOtherOrgInd 

#######
#
# IRS990ScheduleR - IdDisregardedEntitiesGrp
# A repeating structure from ScheduleR Part I - Identification of Disregarded Entities 
#
#######

class SkdRIdDsrgrddEntts(Base):
    __tablename__='SkdRIdDsrgrddEntts'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SkdR_IdDsrgrddEntts = Column(Text)
    # Description:  Part I content - Identification of disregarded entities  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp 

    DsrgrddEnttyNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part I Column (a)  Description:  Business name line 1  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/DisregardedEntityName/BusinessNameLine1Txt 

    DsrgrddEnttyNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part I Column (a)  Description:  Business name line 2  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/DisregardedEntityName/BusinessNameLine2Txt 

    IdDsrgrddEntts_EIN = Column(String(length=9))
    # Line number:  Part I Column (a)  Description:  EIN  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/EIN 

    IdDsrgrddEntts_PrmryActvtsTxt = Column(String(length=100))
    # Line number:  Part I Column (b)  Description:  Nature of activities  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/PrimaryActivitiesTxt 

    IdDsrgrddEntts_TtlIncmAmt = Column(BigInteger)
    # Line number:  Part I Column (d)  Description:  Total income ($)  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/TotalIncomeAmt 

    IdDsrgrddEntts_EndOfYrAsstsAmt = Column(BigInteger)
    # Line number:  Part I Column (e)  Description:  End-of-year assets ($)  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/EndOfYearAssetsAmt 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part I Column (a)  Description:  Address line 1  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part I Column (a)  Description:  Address line 2  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part I Column (a)  Description:  City  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part I Column (a)  Description:  State  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part I Column (a)  Description:  ZIP code  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part I Column (a)  Description:  Address line 1  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part I Column (a)  Description:  Address line 2  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part I Column (a)  Description:  City  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part I Column (a)  Description:  Province or state  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part I Column (a)  Description:  Country  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part I Column (a)  Description:  Postal code  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/ForeignAddress/ForeignPostalCd 

    IdDsrgrddEntts_LglDmclSttCd = Column(String(length=2))
    # Line number:  Part I Column (c)  Description:  Legal domicile - State  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/LegalDomicileStateCd 

    IdDsrgrddEntts_LglDmclFrgnCntryCd = Column(String(length=2))
    # Line number:  Part I Column (c)  Description:  Legal domicile - Foreign Country  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/LegalDomicileForeignCountryCd 

    DrctCntrllngEnttyNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part I Column (f)  Description:  Business name line 1  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/DirectControllingEntityName/BusinessNameLine1Txt 

    DrctCntrllngEnttyNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part I Column (f)  Description:  Business name line 2  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/DirectControllingEntityName/BusinessNameLine2Txt 

    IdDsrgrddEntts_DrctCntrllngNACd = Column(Text)
    # Line number:  Part I Column (f)  Description:  Direct controlling entity - Literal for not applicable  xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/DirectControllingNACd 

#######
#
# IRS990ScheduleR - IdRelatedTaxExemptOrgGrp
# A repeating structure from ScheduleR Part II - Identification of Related Tax-Exempt Organizations 
#
#######

class SkdRIdRltdTxExmptOrg(Base):
    __tablename__='SkdRIdRltdTxExmptOrg'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SkdR_IdRltdTxExmptOrg = Column(Text)
    # Description:  Part II content - Identification of related tax-exempt organizations  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp 

    DsrgrddEnttyNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part II Column (a)  Description:  Business name line 1  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/DisregardedEntityName/BusinessNameLine1Txt 

    DsrgrddEnttyNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part II Column (a)  Description:  Business name line 2  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/DisregardedEntityName/BusinessNameLine2Txt 

    IdRltdTxExmptOrg_EIN = Column(String(length=9))
    # Line number:  Part II Column (a)  Description:  EIN  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/EIN 

    IdRltdTxExmptOrg_PrmryActvtsTxt = Column(String(length=100))
    # Line number:  Part II Column (b)  Description:  Primary activities  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/PrimaryActivitiesTxt 

    IdRltdTxExmptOrg_ExmptCdSctnTxt = Column(String(length=20))
    # Line number:  Part II Column (d)  Description:  Exempt code section  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ExemptCodeSectionTxt 

    IdRltdTxExmptOrg_PblcChrtySttsTxt = Column(String(length=20))
    # Line number:  Part II Column (e)  Description:  Public charity status (if 501(c)(3))  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/PublicCharityStatusTxt 

    IdRltdTxExmptOrg_CntrlldOrgnztnInd = Column(String(length=5))
    # Line number:  Part II Column (g)  Description:  512(b)(13) controlled organization? (Y-N)  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ControlledOrganizationInd 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part II Column (a)  Description:  Address line 1  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part II Column (a)  Description:  Address line 2  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part II Column (a)  Description:  City  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part II Column (a)  Description:  State  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part II Column (a)  Description:  ZIP code  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part II Column (a)  Description:  Address line 1  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part II Column (a)  Description:  Address line 2  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part II Column (a)  Description:  City  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part II Column (a)  Description:  Province or state  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part II Column (a)  Description:  Country  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part II Column (a)  Description:  Postal code  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ForeignAddress/ForeignPostalCd 

    IdRltdTxExmptOrg_LglDmclSttCd = Column(String(length=2))
    # Line number:  Part II Column (c)  Description:  Legal domicile - State  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/LegalDomicileStateCd 

    IdRltdTxExmptOrg_LglDmclFrgnCntryCd = Column(String(length=2))
    # Line number:  Part II Column (c)  Description:  Legal domicile - Foreign Country  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/LegalDomicileForeignCountryCd 

    DrctCntrllngEnttyNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part II Column (f)  Description:  Business name line 1  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/DirectControllingEntityName/BusinessNameLine1Txt 

    DrctCntrllngEnttyNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part II Column (f)  Description:  Business name line 2  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/DirectControllingEntityName/BusinessNameLine2Txt 

    IdRltdTxExmptOrg_DrctCntrllngNACd = Column(Text)
    # Line number:  Part II Column (f)  Description:  Direct controlling entity - Literal for not applicable  xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/DirectControllingNACd 

#######
#
# IRS990ScheduleR - IdRelatedOrgTxblPartnershipGrp
# A repeating structure from ScheduleR Part III - Identification of Related Organizations Taxable as a Partnership 
#
#######

class SkdRIdRltdOrgTxblPrtnrshp(Base):
    __tablename__='SkdRIdRltdOrgTxblPrtnrshp'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SkdR_IdRltdOrgTxblPrtnrshp = Column(Text)
    # Description:  Part III content - Identification of related organizations taxable as a partnership  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp 

    RltdOrgnztnNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part III Column (a)  Description:  Business name line 1  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/RelatedOrganizationName/BusinessNameLine1Txt 

    RltdOrgnztnNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part III Column (a)  Description:  Business name line 2  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/RelatedOrganizationName/BusinessNameLine2Txt 

    IdRltdOrgTxblPrtnrshp_EIN = Column(String(length=9))
    # Line number:  Part III Column (a)  Description:  EIN  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/EIN 

    IdRltdOrgTxblPrtnrshp_PrmryActvtsTxt = Column(String(length=100))
    # Line number:  Part III Column (b)  Description:  Primary business activity, product or service  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/PrimaryActivitiesTxt 

    IdRltdOrgTxblPrtnrshp_PrdmnntIncmTxt = Column(String(length=20))
    # Line number:  Part III Column (e)  Description:  Predominant income (related, investment, unrelated)  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/PredominantIncomeTypeTxt 

    IdRltdOrgTxblPrtnrshp_ShrOfTtlIncmAmt = Column(BigInteger)
    # Line number:  Part III Column (f)  Description:  Share of total income ($)  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ShareOfTotalIncomeAmt 

    IdRltdOrgTxblPrtnrshp_ShrOfEOYAsstsAmt = Column(BigInteger)
    # Line number:  Part III Column (g)  Description:  Share of end-of-year assets ($)  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ShareOfEOYAssetsAmt 

    IdRltdOrgTxblPrtnrshp_DsprprtntAllctnsInd = Column(String(length=5))
    # Line number:  Part III Column (h)  Description:  Disproportionate allocations? (Y-N)  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/DisproportionateAllocationsInd 

    IdRltdOrgTxblPrtnrshp_UBICdVAmt = Column(BigInteger)
    # Line number:  Part III Column (i)  Description:  Code V-UBI amount on Box 20 of K-1 ($)  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/UBICodeVAmt 

    IdRltdOrgTxblPrtnrshp_GnrlOrMngngPrtnrInd = Column(String(length=5))
    # Line number:  Part III Column (j)  Description:  General or managing partner? (Y-N)  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/GeneralOrManagingPartnerInd 

    IdRltdOrgTxblPrtnrshp_OwnrshpPct = Column(Numeric(precision=6))
    # Line number:  Part III Column (k)  Description:  Percentage ownership  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/OwnershipPct 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part III Column (a)  Description:  Address line 1  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part III Column (a)  Description:  Address line 2  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part III Column (a)  Description:  City  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part III Column (a)  Description:  State  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part III Column (a)  Description:  ZIP code  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part III Column (a)  Description:  Address line 1  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part III Column (a)  Description:  Address line 2  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part III Column (a)  Description:  City  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part III Column (a)  Description:  Province or state  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part III Column (a)  Description:  Country  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part III Column (a)  Description:  Postal code  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ForeignAddress/ForeignPostalCd 

    IdRltdOrgTxblPrtnrshp_LglDmclSttCd = Column(String(length=2))
    # Line number:  Part III Column (c)  Description:  Legal domicile - State  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/LegalDomicileStateCd 

    IdRltdOrgTxblPrtnrshp_LglDmclFrgnCntryCd = Column(String(length=2))
    # Line number:  Part III Column (c)  Description:  Legal domicile - Foreign Country  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/LegalDomicileForeignCountryCd 

    DrctCntrllngEnttyNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part III Column (d)  Description:  Business name line 1  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/DirectControllingEntityName/BusinessNameLine1Txt 

    DrctCntrllngEnttyNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part III Column (d)  Description:  Business name line 2  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/DirectControllingEntityName/BusinessNameLine2Txt 

    IdRltdOrgTxblPrtnrshp_DrctCntrllngNACd = Column(Text)
    # Line number:  Part III Column (d)  Description:  Direct controlling entity - Literal for not applicable  xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/DirectControllingNACd 

#######
#
# IRS990ScheduleR - TransactionsRelatedOrgGrp
# A repeating structure from ScheduleR Part V - Transactions with Related Organizations and Noncharitable Exempt Organizations 
#
#######

class SkdRTrnsctnsRltdOrg(Base):
    __tablename__='SkdRTrnsctnsRltdOrg'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part V Line 2 Column (a)  Description:  Business name line 1  xpath: /IRS990ScheduleR/TransactionsRelatedOrgGrp/OtherOrganizationName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part V Line 2 Column (a)  Description:  Business name line 2  xpath: /IRS990ScheduleR/TransactionsRelatedOrgGrp/OtherOrganizationName/BusinessNameLine2Txt 

    TrnsctnTxt = Column(Text)
    # Line number:  Part V Line 2 Column (b)  Description:  Transaction type, enter up to five characters  xpath: /IRS990ScheduleR/TransactionsRelatedOrgGrp/TransactionTypeTxt 

    InvlvdAmt = Column(BigInteger)
    # Line number:  Part V Line 2 Column (c)  Description:  Amount involved ($)  xpath: /IRS990ScheduleR/TransactionsRelatedOrgGrp/InvolvedAmt 

    MthdOfAmntDtrmntnTxt = Column(Text)
    # Line number:  Part V Line 2 Column (d)  Description:  Method of determining amount involved  xpath: /IRS990ScheduleR/TransactionsRelatedOrgGrp/MethodOfAmountDeterminationTxt 

#######
#
# IRS990ScheduleR - SupplementalInformationDetail
# A repeating structure from ScheduleR Part VII Supplemental Information 
#
#######

class SkdRSpplmntlInfrmtnDtl(Base):
    __tablename__='SkdRSpplmntlInfrmtnDtl'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SpplmntlInfrmtnDtl = Column(Text)
    # Description:  Part VII contents  xpath: /IRS990ScheduleR/SupplementalInformationDetail 

    FrmAndLnRfrncDsc = Column(String(length=100))
    # Line number:  Part VII  Description:  Form, part and line number reference  xpath: /IRS990ScheduleR/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = Column(Text)
    # Line number:  Part VII  Description:  Form, part and line number reference explanation  xpath: /IRS990ScheduleR/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleR - UnrelatedOrgTxblPartnershipGrp
# A repeating structure from ScheduleR Part VI 
#
#######

class SkdRUnrltdOrgTxblPrtnrshp(Base):
    __tablename__='SkdRUnrltdOrgTxblPrtnrshp'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SkdR_UnrltdOrgTxblPrtnrshp = Column(Text)
    # Description:  Part VI content  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp 

    BsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part VI Column (a)  Description:  Business name line 1  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/BusinessName/BusinessNameLine1Txt 

    BsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part VI Column (a)  Description:  Business name line 2  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/BusinessName/BusinessNameLine2Txt 

    UnrltdOrgTxblPrtnrshp_EIN = Column(String(length=9))
    # Line number:  Part VI Column (a)  Description:  EIN  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/EIN 

    UnrltdOrgTxblPrtnrshp_PrmryActvtsTxt = Column(String(length=100))
    # Line number:  Part VI Column (b)  Description:  Primary activity  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/PrimaryActivitiesTxt 

    UnrltdOrgTxblPrtnrshp_PrdmntIncmDsc = Column(Text)
    # Line number:  Part VI Column (d)  Description:  Predominate income (related, investment, unrelated)  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/PredominateIncomeDesc 

    UnrltdOrgTxblPrtnrshp_AllPrtnrsC3SInd = Column(String(length=5))
    # Line number:  Part VI Column (e)  Description:  All partners c3s?  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/AllPartnersC3SInd 

    UnrltdOrgTxblPrtnrshp_ShrOfTtlIncmAmt = Column(BigInteger)
    # Line number:  Part VI Column (f)  Description:  Share of total income ($)  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ShareOfTotalIncomeAmt 

    UnrltdOrgTxblPrtnrshp_ShrOfEOYAsstsAmt = Column(BigInteger)
    # Line number:  Part VI Column (g)  Description:  Share of end-of-year assets ($)  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ShareOfEOYAssetsAmt 

    UnrltdOrgTxblPrtnrshp_DsprprtntAllctnsInd = Column(String(length=5))
    # Line number:  Part VI Column (h)  Description:  Disproportionate allocations?  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/DisproportionateAllocationsInd 

    UnrltdOrgTxblPrtnrshp_UBICdVAmt = Column(BigInteger)
    # Line number:  Part VI Column (i)  Description:  Code V amount  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/UBICodeVAmt 

    UnrltdOrgTxblPrtnrshp_GnrlOrMngngPrtnrInd = Column(String(length=5))
    # Line number:  Part VI Column (j)  Description:  General or managing partner?  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/GeneralOrManagingPartnerInd 

    UnrltdOrgTxblPrtnrshp_OwnrshpPct = Column(Numeric(precision=6))
    # Line number:  Part VI Column (k)  Description:  Percentage ownership  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/OwnershipPct 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VI Column (a)  Description:  Address line 1  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VI Column (a)  Description:  Address line 2  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part VI Column (a)  Description:  City  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part VI Column (a)  Description:  State  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part VI Column (a)  Description:  ZIP code  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part VI Column (a)  Description:  Address line 1  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part VI Column (a)  Description:  Address line 2  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part VI Column (a)  Description:  City  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part VI Column (a)  Description:  Province or state  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part VI Column (a)  Description:  Country  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part VI Column (a)  Description:  Postal code  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ForeignAddress/ForeignPostalCd 

    UnrltdOrgTxblPrtnrshp_LglDmclSttCd = Column(String(length=2))
    # Line number:  Part VI Column (c)  Description:  Legal domicile - State  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/LegalDomicileStateCd 

    UnrltdOrgTxblPrtnrshp_LglDmclFrgnCntryCd = Column(String(length=2))
    # Line number:  Part VI Column (c)  Description:  Legal domicile - Foreign Country  xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/LegalDomicileForeignCountryCd 

#######
#
# IRS990ScheduleR - IdRelatedOrgTxblCorpTrGrp
# A repeating structure from ScheduleR Part IV - Identification of Related Organizations Taxable as a Corporation or Trust 
#
#######

class SkdRIdRltdOrgTxblCrpTr(Base):
    __tablename__='SkdRIdRltdOrgTxblCrpTr'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    SkdR_IdRltdOrgTxblCrpTr = Column(Text)
    # Description:  Part IV content - Identification of related organizations taxable as a corporation or trust  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp 

    RltdOrgnztnNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part IV Column (a)  Description:  Business name line 1  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/RelatedOrganizationName/BusinessNameLine1Txt 

    RltdOrgnztnNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part IV Column (a)  Description:  Business name line 2  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/RelatedOrganizationName/BusinessNameLine2Txt 

    IdRltdOrgTxblCrpTr_EIN = Column(String(length=9))
    # Line number:  Part IV Column (a)  Description:  EIN  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/EIN 

    IdRltdOrgTxblCrpTr_PrmryActvtsTxt = Column(String(length=100))
    # Line number:  Part IV Column (b)  Description:  Primary activity, product or service  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/PrimaryActivitiesTxt 

    IdRltdOrgTxblCrpTr_EnttyTxt = Column(String(length=20))
    # Line number:  Part IV Column (e)  Description:  Type of entity (C corp, S corp, or trust)  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/EntityTypeTxt 

    IdRltdOrgTxblCrpTr_ShrOfTtlIncmAmt = Column(BigInteger)
    # Line number:  Part IV Column (f)  Description:  Share of total income ($)  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ShareOfTotalIncomeAmt 

    IdRltdOrgTxblCrpTr_ShrOfEOYAsstsAmt = Column(BigInteger)
    # Line number:  Part IV Column (g)  Description:  Share of end-of-year assets ($)  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ShareOfEOYAssetsAmt 

    IdRltdOrgTxblCrpTr_OwnrshpPct = Column(Numeric(precision=6))
    # Line number:  Part IV Column (h)  Description:  Percentage ownership  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/OwnershipPct 

    IdRltdOrgTxblCrpTr_CntrlldOrgnztnInd = Column(String(length=5))
    # Line number:  Part IV Column (i)  Description:  512(b)(13) controlled organization? (Y-N)  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ControlledOrganizationInd 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part IV Column (a)  Description:  Address line 1  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part IV Column (a)  Description:  Address line 2  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Line number:  Part IV Column (a)  Description:  City  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Line number:  Part IV Column (a)  Description:  State  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Line number:  Part IV Column (a)  Description:  ZIP code  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Line number:  Part IV Column (a)  Description:  Address line 1  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Line number:  Part IV Column (a)  Description:  Address line 2  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Line number:  Part IV Column (a)  Description:  City  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Line number:  Part IV Column (a)  Description:  Province or state  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Line number:  Part IV Column (a)  Description:  Country  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Line number:  Part IV Column (a)  Description:  Postal code  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ForeignAddress/ForeignPostalCd 

    IdRltdOrgTxblCrpTr_LglDmclSttCd = Column(String(length=2))
    # Line number:  Part IV Column (c)  Description:  Legal domicile - State  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/LegalDomicileStateCd 

    IdRltdOrgTxblCrpTr_LglDmclFrgnCntryCd = Column(String(length=2))
    # Line number:  Part IV Column (c)  Description:  Legal domicile - Foreign Country  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/LegalDomicileForeignCountryCd 

    DrctCntrllngEnttyNm_BsnssNmLn1Txt = Column(String(length=75))
    # Line number:  Part IV Column (d)  Description:  Business name line 1  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/DirectControllingEntityName/BusinessNameLine1Txt 

    DrctCntrllngEnttyNm_BsnssNmLn2Txt = Column(String(length=75))
    # Line number:  Part IV Column (d)  Description:  Business name line 2  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/DirectControllingEntityName/BusinessNameLine2Txt 

    IdRltdOrgTxblCrpTr_DrctCntrllngNACd = Column(Text)
    # Line number:  Part IV Column (d)  Description:  Direct controlling entity - Literal for not applicable  xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/DirectControllingNACd 

#######
#
# ReturnHeader990x - ReturnHeader990x Part I Return Header Data 
#
#######

class returnheader990x_part_i(Base):
    __tablename__='returnheader990x_part_i'
    return_id = Column(String(31))
    ein = Column(String(15))
    id = Column(Integer, primary_key=True)

    RtrnHdr_RtrnTs = Column(String(length=63))
    # Description:  The date and time when the return was created  xpath: /ReturnHeader/ReturnTs 

    RtrnHdr_TxPrdEndDt = Column(String(length=31))
    # xpath: /ReturnHeader/TaxPeriodEndDt 

    RtrnHdr_DsstrRlfTxt = Column(String(length=100))
    # xpath: /ReturnHeader/DisasterReliefTxt 

    RtrnHdr_ISPNm = Column(String(length=6))
    # xpath: /ReturnHeader/ISPNum 

    RtrnHdr_PrprrFrm = Column(Text)
    # xpath: /ReturnHeader/PreparerFirmGrp 

    PrprrFrm_PrprrFrmEIN = Column(String(length=9))
    # xpath: /ReturnHeader/PreparerFirmGrp/PreparerFirmEIN 

    PrprrFrmNm_BsnssNmLn1Txt = Column(String(length=75))
    # Description:  Business name line 1  xpath: /ReturnHeader/PreparerFirmGrp/PreparerFirmName/BusinessNameLine1Txt 

    PrprrFrmNm_BsnssNmLn2Txt = Column(String(length=75))
    # Description:  Business name line 2  xpath: /ReturnHeader/PreparerFirmGrp/PreparerFirmName/BusinessNameLine2Txt 

    PrprrUSAddrss_AddrssLn1Txt = Column(String(length=35))
    # Description:  Address line 1  xpath: /ReturnHeader/PreparerFirmGrp/PreparerUSAddress/AddressLine1Txt 

    PrprrUSAddrss_AddrssLn2Txt = Column(String(length=35))
    # Description:  Address line 2  xpath: /ReturnHeader/PreparerFirmGrp/PreparerUSAddress/AddressLine2Txt 

    PrprrUSAddrss_CtyNm = Column(String(length=22))
    # Description:  City  xpath: /ReturnHeader/PreparerFirmGrp/PreparerUSAddress/CityNm 

    PrprrUSAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Description:  State  xpath: /ReturnHeader/PreparerFirmGrp/PreparerUSAddress/StateAbbreviationCd 

    PrprrUSAddrss_ZIPCd = Column(String(length=15))
    # Description:  ZIP code  xpath: /ReturnHeader/PreparerFirmGrp/PreparerUSAddress/ZIPCd 

    PrprrFrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Description:  Address line 1  xpath: /ReturnHeader/PreparerFirmGrp/PreparerForeignAddress/AddressLine1Txt 

    PrprrFrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Description:  Address line 2  xpath: /ReturnHeader/PreparerFirmGrp/PreparerForeignAddress/AddressLine2Txt 

    PrprrFrgnAddrss_CtyNm = Column(Text)
    # Description:  City  xpath: /ReturnHeader/PreparerFirmGrp/PreparerForeignAddress/CityNm 

    PrprrFrgnAddrss_PrvncOrSttNm = Column(Text)
    # Description:  Province or state  xpath: /ReturnHeader/PreparerFirmGrp/PreparerForeignAddress/ProvinceOrStateNm 

    PrprrFrgnAddrss_CntryCd = Column(String(length=2))
    # Description:  Country  xpath: /ReturnHeader/PreparerFirmGrp/PreparerForeignAddress/CountryCd 

    PrprrFrgnAddrss_FrgnPstlCd = Column(Text)
    # Description:  Postal code  xpath: /ReturnHeader/PreparerFirmGrp/PreparerForeignAddress/ForeignPostalCd 

    RtrnHdr_SftwrId = Column(String(length=8))
    # xpath: /ReturnHeader/SoftwareId 

    RtrnHdr_SftwrVrsnNm = Column(String(length=20))
    # xpath: /ReturnHeader/SoftwareVersionNum 

    RtrnHdr_MltSftwrPckgsUsdInd = Column(String(length=5))
    # xpath: /ReturnHeader/MultSoftwarePackagesUsedInd 

    RtrnHdr_Orgntr = Column(Text)
    # xpath: /ReturnHeader/OriginatorGrp 

    Orgntr_EFIN = Column(String(length=6))
    # xpath: /ReturnHeader/OriginatorGrp/EFIN 

    Orgntr_OrgntrCd = Column(String(length=15))
    # xpath: /ReturnHeader/OriginatorGrp/OriginatorTypeCd 

    Orgntr_PrcttnrPIN = Column(Text)
    # xpath: /ReturnHeader/OriginatorGrp/PractitionerPINGrp 

    PrcttnrPIN_EFIN = Column(String(length=6))
    # xpath: /ReturnHeader/OriginatorGrp/PractitionerPINGrp/EFIN 

    PrcttnrPIN_PIN = Column(String(length=5))
    # xpath: /ReturnHeader/OriginatorGrp/PractitionerPINGrp/PIN 

    RtrnHdr_PINEntrdByCd = Column(Text)
    # xpath: /ReturnHeader/PINEnteredByCd 

    RtrnHdr_SgntrOptnCd = Column(Text)
    # xpath: /ReturnHeader/SignatureOptionCd 

    RtrnHdr_RtrnCd = Column(Text)
    # xpath: /ReturnHeader/ReturnTypeCd 

    RtrnHdr_TxPrdBgnDt = Column(String(length=31))
    # xpath: /ReturnHeader/TaxPeriodBeginDt 

    RtrnHdr_Flr = Column(Text)
    # xpath: /ReturnHeader/Filer 

    Flr_EIN = Column(String(length=9))
    # xpath: /ReturnHeader/Filer/EIN 

    BsnssNm_BsnssNmLn1Txt = Column(String(length=75))
    # Description:  Business name line 1  xpath: /ReturnHeader/Filer/BusinessName/BusinessNameLine1Txt 

    BsnssNm_BsnssNmLn2Txt = Column(String(length=75))
    # Description:  Business name line 2  xpath: /ReturnHeader/Filer/BusinessName/BusinessNameLine2Txt 

    Flr_InCrOfNm = Column(String(length=35))
    # xpath: /ReturnHeader/Filer/InCareOfNm 

    Flr_BsnssNmCntrlTxt = Column(String(length=7))
    # xpath: /ReturnHeader/Filer/BusinessNameControlTxt 

    Flr_PhnNm = Column(String(length=10))
    # xpath: /ReturnHeader/Filer/PhoneNum 

    USAddrss_AddrssLn1Txt = Column(String(length=35))
    # Description:  Address line 1  xpath: /ReturnHeader/Filer/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = Column(String(length=35))
    # Description:  Address line 2  xpath: /ReturnHeader/Filer/USAddress/AddressLine2Txt 

    USAddrss_CtyNm = Column(String(length=22))
    # Description:  City  xpath: /ReturnHeader/Filer/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = Column(String(length=2))
    # Description:  State  xpath: /ReturnHeader/Filer/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = Column(String(length=15))
    # Description:  ZIP code  xpath: /ReturnHeader/Filer/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = Column(String(length=35))
    # Description:  Address line 1  xpath: /ReturnHeader/Filer/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = Column(String(length=35))
    # Description:  Address line 2  xpath: /ReturnHeader/Filer/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = Column(Text)
    # Description:  City  xpath: /ReturnHeader/Filer/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = Column(Text)
    # Description:  Province or state  xpath: /ReturnHeader/Filer/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CntryCd = Column(String(length=2))
    # Description:  Country  xpath: /ReturnHeader/Filer/ForeignAddress/CountryCd 

    FrgnAddrss_FrgnPstlCd = Column(Text)
    # Description:  Postal code  xpath: /ReturnHeader/Filer/ForeignAddress/ForeignPostalCd 

    RtrnHdr_BsnssOffcr = Column(Text)
    # xpath: /ReturnHeader/BusinessOfficerGrp 

    BsnssOffcr_PrsnNm = Column(String(length=35))
    # xpath: /ReturnHeader/BusinessOfficerGrp/PersonNm 

    BsnssOffcr_PrsnTtlTxt = Column(String(length=35))
    # xpath: /ReturnHeader/BusinessOfficerGrp/PersonTitleTxt 

    BsnssOffcr_PhnNm = Column(String(length=10))
    # xpath: /ReturnHeader/BusinessOfficerGrp/PhoneNum 

    BsnssOffcr_EmlAddrssTxt = Column(String(length=75))
    # xpath: /ReturnHeader/BusinessOfficerGrp/EmailAddressTxt 

    BsnssOffcr_SgntrDt = Column(String(length=31))
    # xpath: /ReturnHeader/BusinessOfficerGrp/SignatureDt 

    BsnssOffcr_TxpyrPIN = Column(String(length=5))
    # xpath: /ReturnHeader/BusinessOfficerGrp/TaxpayerPIN 

    BsnssOffcr_DscssWthPdPrprrInd = Column(String(length=5))
    # xpath: /ReturnHeader/BusinessOfficerGrp/DiscussWithPaidPreparerInd 

    RtrnHdr_PrprrPrsn = Column(Text)
    # xpath: /ReturnHeader/PreparerPersonGrp 

    PrprrPrsn_PrprrPrsnNm = Column(String(length=35))
    # xpath: /ReturnHeader/PreparerPersonGrp/PreparerPersonNm 

    PrprrPrsn_PhnNm = Column(String(length=10))
    # xpath: /ReturnHeader/PreparerPersonGrp/PhoneNum 

    PrprrPrsn_EmlAddrssTxt = Column(String(length=75))
    # xpath: /ReturnHeader/PreparerPersonGrp/EmailAddressTxt 

    PrprrPrsn_PrprtnDt = Column(String(length=31))
    # xpath: /ReturnHeader/PreparerPersonGrp/PreparationDt 

    PrprrPrsn_SlfEmplydInd = Column(String(length=1))
    # xpath: /ReturnHeader/PreparerPersonGrp/SelfEmployedInd 

    PrprrPrsn_SSN = Column(String(length=9))
    # xpath: /ReturnHeader/PreparerPersonGrp/SSN 

    PrprrPrsn_PTIN = Column(String(length=9))
    # xpath: /ReturnHeader/PreparerPersonGrp/PTIN 

    IPAddrss_IPv4AddrssTxt = Column(String(length=31))
    # xpath: /ReturnHeader/IPAddress/IPv4AddressTxt 

    IPAddrss_IPv6AddrssTxt = Column(String(length=31))
    # xpath: /ReturnHeader/IPAddress/IPv6AddressTxt 

    RtrnHdr_IPDt = Column(String(length=31))
    # xpath: /ReturnHeader/IPDt 

    RtrnHdr_IPTm = Column(String(length=15))
    # xpath: /ReturnHeader/IPTm 

    RtrnHdr_IPTmznCd = Column(String(length=31))
    # xpath: /ReturnHeader/IPTimezoneCd 

    RtrnHdr_DvcId = Column(String(length=40))
    # xpath: /ReturnHeader/DeviceId 

    RtrnHdr_TxYr = Column(Integer)
    # xpath: /ReturnHeader/TaxYr 
