import os
from django.core.management.base import BaseCommand
from schemas.models import XSDFile, ProductionVersion, XSDFile, ScheduleName, \
    SchedulePart, CanonicalVariable, CanonicalGroup
from django.conf import settings
from schemas.documentation_utils import most_recent, debracket

GENERATED_MODELS_DIR = settings.GENERATED_MODELS_DIR
soft_tab = '    '

class Command(BaseCommand):
    help = """  Generate django model file. 
                Hard overwrites the default file.

                SQLAlchemy in development as a CLI option ( -sqlalchemy )
                Pretty rough at this point

            """

    def add_arguments(self, parser):
            # Positional arguments
            parser.add_argument('-sqlalchemy', action='store_true')

    def write_model_top(self, sked_name, full_name, parent_sked_name, repeating_group_part=None):

        if self.run_django:

            result = "\n#######\n#\n# %s - %s\n" % (parent_sked_name, full_name)
            if repeating_group_part:
                result += "# A repeating structure from %s\n" % (repeating_group_part)            
            result += "#\n#######\n" 
            ## write the start of the first group:
            result += "\nclass %s(models.Model):\n" % sked_name
            result +=  soft_tab +  "return_id = models.CharField(max_length=31, blank=True, null=True, help_text=\"unique xml return id\")\n"
            result +=  soft_tab +  "ein = models.CharField(max_length=15, blank=True, null=True, help_text=\"filer EIN\")"
            
            return result

        elif self.run_sqlalchemy:
            
            result = "\n#######\n#\n# %s - %s\n" % (parent_sked_name, full_name)
            if repeating_group_part:
                result += "# A repeating structure from %s\n" % (repeating_group_part)            
            result += "#\n#######\n" 
            ## write the start of the first group:
            result += "\nclass %s(Base):\n%s__tablename__='%s'\n" % (sked_name,soft_tab, sked_name)
            result +=  soft_tab +  "return_id = Column(String(31))\n"
            result +=  soft_tab +  "ein = Column(String(15))\n"
            result +=  soft_tab +  "id = Column(Integer, primary_key=True)\n" # Add a primary key explicitly
            return result

    def write_top_matter(self):
        if self.run_django:
            self.outfile.write("from django.db import models\n")
        elif self.run_sqlalchemy:
            self.outfile.write("from sqlalchemy import Column, Integer, String, BigInteger, Text, Numeric\n")
            self.outfile.write("from sqlalchemy.ext.declarative import declarative_base\n\n")
            self.outfile.write("Base = declarative_base()\n\n")


    def write_variable(self, variable):
        """
        We fallback to a text field, but we expect the types to be filled in where missing
        """

        if self.run_django:
            variable_output = variable.django_type
            if not variable_output:
                variable_output = "TextField(null=True, blank=True)" 
            result =  "\n" + soft_tab + "%s = models.%s" % (variable.db_safe_name, variable_output)

        elif self.run_sqlalchemy:
            variable_output = variable.sql_alch_type
            if not variable_output:
                variable_output = "Text" 
            result =  "\n" + soft_tab + "%s = Column(%s)" % (variable.db_safe_name, variable_output)

        # add newline and documentation regardless of where it's going
        result += "\n" + soft_tab + "#"
        if variable.line_number:
            result += " Line number: %s " % most_recent(debracket(variable.line_number))
        if variable.description:
            result += " Description: %s " % most_recent(debracket(variable.description))
        result += " xpath: %s \n" % variable.original_xpath

        return result

    def write_sked(self, schedule):
        print("Handling schedule %s" % (schedule))

        form_parts = SchedulePart.objects.filter(parent_sked=schedule).order_by('ordering_ordinal')
        for form_part in form_parts:

            model_top = self.write_model_top(form_part.db_model_name, form_part.raw_part_name, schedule.schedule_name )

            variables_in_this_part = CanonicalVariable.objects.filter(parent_sked_part=form_part).exclude(in_a_group=True).order_by('ordering',)
            if variables_in_this_part:
                # only write it if it contains anything
                self.outfile.write(model_top)
                print(model_top)

                for variable in variables_in_this_part:
                    this_var = self.write_variable(variable)
                    print(this_var)
                    self.outfile.write(this_var)
            
        groups_in_this_sked = CanonicalGroup.objects.filter(parent_sked=schedule).order_by('ordering',)
        for group in groups_in_this_sked:
            
            model_top = self.write_model_top(group.db_safe_name, group.name, schedule.schedule_name, repeating_group_part=group.parent_sked_part.raw_part_name )
            
            variables_in_this_group = CanonicalVariable.objects.filter(parent_group=group).order_by('ordering',)
            if variables_in_this_group:
                # only write it if it contains anything
                self.outfile.write(model_top)
                print(model_top)

                for variable in variables_in_this_group:
                    this_var = self.write_variable(variable)
                    print(this_var)
                    self.outfile.write(this_var)
                

    def handle(self, *args, **options):
        print options
        self.run_sqlalchemy = options['sqlalchemy']

        self.run_django = not self.run_sqlalchemy    # Only run one or the other.

        file_output = os.path.join(GENERATED_MODELS_DIR, "django_models_auto.py")
        if self.run_sqlalchemy:
            file_output = os.path.join(GENERATED_MODELS_DIR, "sqlalchemy_models_auto.py")

        self.outfile = open(file_output, 'w')


        self.write_top_matter()
        skedlist = ScheduleName.objects.all().order_by('schedule_name')
        for schedule in skedlist:
            self.write_sked(schedule)
                




