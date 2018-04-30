from django.core.management.base import BaseCommand


from schemas.models import VersionedGroup, VersionedVariable,            \
    CanonicalVariable, CanonicalGroup, ProductionVersion, ScheduleName

from schemas.epoch_utils import apply_var_translation, test_for_missing, MODERN_EPOCH, GROUP_TRANSFORMATIONS, EPOCH_2017

class Command(BaseCommand):
    help = """ 
            Assign canonical groups, then variables to versions.
            """

    def init_version_errors(self):
        #self.all_versions = ProductionVersion.objects.filter(version_string__in=EPOCH_2014_FORWARDS).order_by('version_string').values('version_string')
        #self.all_versions = ProductionVersion.objects.filter(version_string__in=MODERN_EPOCH).order_by('version_string').values('version_string')
        self.all_versions = ProductionVersion.objects.filter(version_string__in=EPOCH_2017).order_by('version_string').values('version_string')

        self.version_group_errors = {}
        self.version_var_errors = {}
        for version in self.all_versions:
            self.version_group_errors[version['version_string']] = 0
            self.version_var_errors[version['version_string']] = 0

    def assign_groups(self):
        all_canonical_groups = CanonicalGroup.objects.all()
        for cgroup in all_canonical_groups:
            for version in self.all_versions:
                this_vs = version['version_string']
                versioned_group = None

                try:
                    versioned_group = VersionedGroup.objects.get(version_string=this_vs, xpath=cgroup.original_xpath)
                except VersionedGroup.DoesNotExist:
                    try:
                        xpath_transform = GROUP_TRANSFORMATIONS[cgroup.original_xpath]
                        if this_vs in xpath_transform['versions']:
                            try:
                                versioned_group = VersionedGroup.objects.get(version_string=this_vs, xpath=xpath_transform['corrected_value'])
                                print("Found match using transform %s in version %s" % (xpath_transform['corrected_value'], this_vs))

                            except VersionedGroup.DoesNotExist:
                                pass
                    except KeyError:
                        print("No match in transform for %s in version %s" % (cgroup.original_xpath, this_vs))

                if versioned_group:
                    versioned_group.canonical_group = cgroup
                    versioned_group.save()

                else:
                    #print ( "*** Missing %s in %s" % (cgroup.name, this_vs) )
                    self.version_group_errors[version['version_string']] += 1

    def show_group_key_errors(self):
        keys = sorted(self.version_group_errors.keys())
        print ("\n-----\nMissing Group Keys: ")
        for key in keys:
            print "%s %s" % (key, self.version_group_errors[key] )

    def assign_variables_by_sked(self, this_sked):
        all_canonical_vars = CanonicalVariable.objects.filter(parent_sked=this_sked)
        for cv in all_canonical_vars:
            #print ("\tProcessing %s" % (cv.original_xpath))

            for version in self.all_versions:
                this_vs = version['version_string']
                versioned_var = None

                try:
                    versioned_var = VersionedVariable.objects.get(version_string=this_vs, xpath=cv.original_xpath)
                    if versioned_var.canonical_variable != cv:
                        versioned_var.canonical_variable = cv
                        versioned_var.save()

                except VersionedVariable.DoesNotExist:

                    #print("No match for %s  in %s" % (cv.original_xpath, this_vs) )
                    new_var = apply_var_translation(cv.original_xpath, this_vs)

                    if new_var != cv.original_xpath:
                        #print ("Retrying with %s" % new_var)
                        try:
                            versioned_var = VersionedVariable.objects.get(version_string=this_vs, xpath=new_var)
                            if versioned_var.canonical_variable != cv:
                                versioned_var.canonical_variable = cv
                                versioned_var.save()

                        except VersionedVariable.DoesNotExist:
                            print("** No match with transformed var '%s' from '%s' " % (new_var, cv.original_xpath) )
                            self.version_var_errors[version['version_string']] += 1
                    else:

                        is_missing = test_for_missing(cv.original_xpath, this_vs)
                        if is_missing:
                            print("### Var %s marked as missing in %s, skipping" % (cv.original_xpath, this_vs) )
                        else:
                            print("-- No transformation to fix %s in %s" % (new_var, version['version_string']) )
                            self.version_var_errors[version['version_string']] += 1



                      
    def assign_variables(self):
        #all_skeds = ScheduleName.objects.all()
        #all_skeds = ScheduleName.objects.filter(schedule_name__in=['IRS990PF'])
        all_skeds = ScheduleName.objects.filter(schedule_name='IRS990ScheduleF')
        for sked in all_skeds:
            print ("Assigning canonical to %s" % sked)
            self.assign_variables_by_sked(sked)


    def show_var_key_errors(self):
        keys = sorted(self.version_var_errors.keys())
        print ("\n-----\nMissing Variable Keys: ")
        for key in keys:
            print "%s %s" % (key, self.version_var_errors[key] )



    def handle(self, *args, **options):
        self.init_version_errors()
        #print ("Assigning groups... ")
        #self.assign_groups()
        #self.show_group_key_errors()

        print ("Assigning variables...")
        self.assign_variables()
        self.show_var_key_errors()
