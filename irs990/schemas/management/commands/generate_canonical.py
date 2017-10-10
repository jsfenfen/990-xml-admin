from django.core.management.base import BaseCommand
from django.conf import settings
from django.forms.models import model_to_dict


from schemas.models import VersionedGroup, VersionedVariable, \
    CanonicalVariable, CanonicalGroup

from schemas.naming_utils import fix_name


CANONICAL_VERSION = settings.CANONICAL_VERSION


class Command(BaseCommand):
    help = """  Drop and regenerate canonical groups and variables.
            """

    def drop_existing(self):
        print("Dropping existing canonical variables and groups...")
        CanonicalGroup.objects.all().delete()
        CanonicalVariable.objects.all().delete()

    def create_group(self, versioned_group):
        group_dict = model_to_dict(versioned_group)
        print("Handling group %s" % (group_dict))
        # set foreign key values, which come as pks. 
        group_dict['parent_sked'] = versioned_group.parent_sked
        group_dict['parent_sked_part'] = versioned_group.parent_sked_part
        group_dict['version'] = versioned_group.version
        group_dict['original_xpath'] = versioned_group.xpath
        group_dict['db_safe_name'] = fix_name(versioned_group.parent_sked_part.db_model_name + group_dict['name'])

        # todo: set ordering, empty_head

        # kill out nonmatching keys
        group_dict.pop('xpath')
        group_dict.pop('canonical_group')


        new_group = CanonicalGroup.objects.create(**group_dict)
        versioned_group.canonical_group = new_group
        versioned_group.save()

    def create_new_groups(self):
        all_groups = VersionedGroup.objects.filter(
            version__version_string=CANONICAL_VERSION
        )
        print("CNG len %s" % len(all_groups))
        for group in all_groups:
            print ("Group .. ")
            self.create_group(group)

    def create_variable(self, versioned_variable):
        print("Handling variable %s" % (versioned_variable))      
        variable_dict = model_to_dict(versioned_variable)
        variable_dict['parent_sked'] = versioned_variable.parent_sked
        variable_dict['parent_sked_part'] = versioned_variable.parent_sked_part
        variable_dict['version'] = versioned_variable.version
        variable_dict['original_xpath'] = versioned_variable.xpath
        variable_dict['db_safe_name'] = fix_name(versioned_variable.name)

        if variable_dict['in_a_group']:
            variable_dict['parent_group'] = versioned_variable.parent_group.canonical_group
        else:
            variable_dict['parent_group'] = None

        variable_dict.pop('xpath')
        variable_dict.pop('name')
        variable_dict.pop('canonical_variable')

        new_var = CanonicalVariable.objects.create(**variable_dict)
        versioned_variable.canonical_variable = new_var
        versioned_variable.save()  

    def create_new_variables(self):
        all_variables = VersionedVariable.objects.filter(
            version__version_string=CANONICAL_VERSION
        )
        for variable in all_variables:
            self.create_variable(variable)

    def handle(self, *args, **options):
        self.drop_existing()
        self.create_new_groups()
        self.create_new_variables()

