

def get_year_version_from_schema(schema_string):
    """ expects a schema string from xml like: 2015v2.1 """
    [year, version] = schema_string.split('v')
    return({'year':int(year), 'version':version})