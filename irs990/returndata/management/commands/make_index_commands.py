from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = """ Print the create / drop index commands for returndata """

    def handle(self, *args, **options):
        returndata_app = apps.get_app_config('returndata')
        rdmodels = returndata_app.models
        create_cmds = []
        drop_cmds = []
        for key in rdmodels.keys():
            dbtablename = rdmodels[key]._meta.db_table
            index_name = "xzoid_" + dbtablename[:30]
            index_name = index_name.replace("returndata_", "")
            create_cmd = "CREATE INDEX %s on %s (object_id);" % (
                index_name, dbtablename
            )
            drop_cmd = "DROP INDEX %s;" % (index_name)
            create_cmds.append(create_cmd)
            drop_cmds.append(drop_cmd)
        

        """ 
        Indexes: for filing_xml_submission
]               | 
         sub_date       | character varying(511) | 
         taxpayer_name  | character varying(511) | 
         return_type    | character varying(7)   | 
        """

        create_cmds.append(
            "CREATE INDEX taxpayername_index ON filing_xml_submission (taxpayer_name varchar_pattern_ops);"
        )
        drop_cmds.append(
            "DROP INDEX taxpayername_index;"
        )


        print("Create commands:")
        for cc in create_cmds:
            print(cc)
        print("\nDrop commands:")
        for dc in drop_cmds:
            print(dc)



