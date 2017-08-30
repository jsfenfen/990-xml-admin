# IRS 990 Admin

This is a helper application to make sense of the 990 xml filings
described [here](https://aws.amazon.com/public-datasets/irs-990/)--but it's *not* needed to simply read those filings [ See other library TK ]. This application generates the bindings that 990-xml-reader *uses* to standardize 990 returns by doing two things: counting xpath entries in actual 990 XML returns, and extracting documentation and other metadata from .XSD schema files.

# Installation

Clone this repository. It's recommended that you generate a [virtual env](https://virtualenv.pypa.io/en/stable/) for this code to live in. Install the dependencies with `$ pip install -r requirements.txt`.

The settings.py file automatically includes a local\_settings.py file, which contains sensitive information and is not included in this repository. Start by copying the local\_settings-example.py file to local_settings.py and set the needed values there. You will likely need to set the database configuration variables and template locations. You will need to make django's initial [migration](https://docs.djangoproject.com/en/1.11/topics/migrations/#workflow) and apply it, i.e., from the django application's main directory, run


	$ python manage.py makemigrations
And once the migrations are made, run:

	$ python manage.py migrate


# Getting the xml files

The simplest way to download all the raw xml files (~55GB uncompressed) to local disk is to sync a local directory to the master S3 bucket using AWS' command line tools. Doing so requires configuring the CLI tool--see more [here](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).  Note that you may want to first sync *your own* S3 bucket to the master bucket and then download from there.

Whatever the case, you want the files to go to the path defined in LOCAL\_DATA\_DIR in the local\_settings.py file. If you just copied the local settings from this file it should be BASE\_DIR/irs\_data/

It can take a while to do a complete sync, if you're logged in you probably want to use `nohup` to run it like this.

	$ nohup aws s3 sync s3://irs-form-990/ /full/path/to/LOCAL_DATA_DIR/ &


# Processing the files

## Filing model

### Commands:



## Schemas model

### Commands

#### 1. enter\_schema\_files

This enters the schemas files as XSDFile objects.


	$ python manage.py enter_schema_files

Enter the schema files by walking the SCHEMA\_DIR. 
Optionally pass a version\_string as an arg to run only on that version, e.g. 
	$ python manage.py enter\_schema\_files 2013v4.0 
	

Check db entry with: `select version_string, count(*) from schemas_xsdfile group by 1;`


Hard SQL undo: 
	delete from schemas\_xsdfile [ where version_string='2013v4.0'];


#### 2. read\_schema\_files

This enters the xsd elements, simpletypes, groups and complextypes from by reading the XSD files. 

$ python manage.py read\_schema\_files

Optionally pass a version\_string as an arg to run only on that version, e.g. 

	$ python manage.py read_schema_files 2013v4.0 
	
To undo with SQL:

    delete from schemas_simpletype;
    delete from schemas_fileinclude;
    delete from schemas_element;
    delete from schemas_group;
    delete from schemas_complextype;

Check existence with queries like:
`select version_string, count(*) from schemas_element group by 1;`
etc.


#### 3. Add the schedules we care about, from fixture

The fixture is in schemas/fixtures/schedules.json 

To add it use django's fixture thingy, i.e. type:

`$ python manage.py loaddata schedules.json`

It will note if it adds fixtures, if it's run for the first time output should be:

`Installed 20 object(s) from 1 fixture(s)`

undo with 
`delete from schemas_scheduleinstance;`


#### 4. attach\_schedule\_instances

This step just attaches actual XSDFile instances in the db to the schedule instan


#### 5. generate_mappings

Generate mappings from whitelisted forms/schedules.  

Optionally pass a version\_string as an arg
to run only on that version, e.g.  

$ python manage.py generate\_mappings 2013v4.0  

Hard undo: 

- elements: delete from schemas_versionedvariable
- groups: delete from schemas\_versionedgroup;







#### 6. parse_parts

Attach variables in canonical version to schedule_parts (and generate schedule parts) if needed.


#### 7. generate_canonical

Drop and regenerate canonical groups and variables based on whatever is set in settings.py (or local_settings.py ) for CANONICAL_VERSION. This should be a current version into which prior versions are transformed; the values in this transformation were used with 2015v2.1.

#### assign_canonical

Match the groups and variables to the canonical ones. Works for 2013 forwards as is. 
The details of how this works are in schemas.epoch_utils, which is described as: 
"Gnarly custom variable transformations to stitch variables across years. Current target: 2013 forwards. Double check the documentation; it's possible for the *meaning* of a var to change even if xpath doesn't. 

This assigns groups (schemas.models VersionedGroup to CanonicalGroup and VersionedVariable to CanonicalVariable)
Additional details that are sourced through the canonical vars (specifically, the group and form/part hierarchy)
are assigned in a later management command (propagate\_from\_canonical)."

#### propagate\_from\_canonical

####  generate_documentation

#### TK: generate_models