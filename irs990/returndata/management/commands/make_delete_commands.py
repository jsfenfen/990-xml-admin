from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = """ Print the create / drop index commands for returndata """

    def handle(self, *args, **options):
        returndata_app = apps.get_app_config('returndata')
        rdmodels = returndata_app.models
        drop_cmds = []
        for key in rdmodels.keys():
            dbtablename = rdmodels[key]._meta.db_table
            drop_cmd = "drop table %s;" % dbtablename
            drop_cmds.append(drop_cmd)
        


        print("\nDrop commands:")
        for dc in drop_cmds:
            print(dc)



