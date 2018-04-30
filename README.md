# IRS 990 Admin

This is a helper application to make sense of the 990 xml filings
described [here](https://aws.amazon.com/public-datasets/irs-990/)--but it's *not* needed to simply read those filings--for reading filings see [IRSx](https://github.com/jsfenfen/990-xml-reader/) . This application generates the bindings that 990-xml-reader *uses* to stardardize 990 returns by doing two things: counting xpath entries in actual 990 XML returns, and extracting documentation and other metadata from .XSD schema files.

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

#### retrieve\_annual\_file

Refresh the yearly csv file.
 Takes the four-digit year as a positional argument  
 
    $ manage.py retrieve_annual_file 2017
            

#### enter\_yearly\_submissions

Read the yearly csv file line by line and add new lines to the xml_submission model if they don't exist. Lines are added in bulk at the end.
	
	
	$ python manage.py enter_yearly_submissions 2017
	
#### run\_new\_filings

This command will automatically add new filings. In it's current implementation it retrieves the filings if they are not present--it might be a good strategy to use s3's sync command upstream if this is a significant update.

	$ python manage.py run\_new\_filings

It works by processing all the XML_Submissions where json_set is false. There are really two steps as it now runs: converting the file into a standardized json and then entering that into "flattened" relational tables. When each filing is entered, it's given a ProcessedFiling object. 



erase data from *all* return tables with:

	python manage.py dbshell < returndata/sql/remove_returns.sql


Shows number of entries (in all tables) credit [StackOverflow](https://stackoverflow.com/a/2611745):

	SELECT schemaname,relname,n_live_tup 
  	FROM pg_stat_user_tables 
  	ORDER BY n_live_tup DESC;
  

#### Quirks 
 - The 2014 csv is "broken" in that it has a comma in a field. Look for "AMAGEMENT" and it can be fixed by hand. 



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

This step isn't required for an update. 

The fixture is in schemas/fixtures/schedules.json 

To add it use django's fixture thingy, i.e. type:

`$ python manage.py loaddata schedules.json`

It will note if it adds fixtures, if it's run for the first time output should be:

`Installed 20 object(s) from 1 fixture(s)`

undo with 
`delete from schemas_scheduleinstance;`


#### 4. attach\_schedule\_instances

This should be run during an update.

This step just attaches actual XSDFile instances in the db to the schedule instances.


#### 5. generate_mappings

Create the versioned_variable and versioned_group elements from whitelisted forms/schedules.  This is generating the xpaths from the xsd files.

Optionally pass a version\_string as an arg
to run only on that version, e.g.  

$ python manage.py generate\_mappings 2013v4.0  

Hard undo: 

- elements: delete from schemas_versionedvariable
- groups: delete from schemas\_versionedgroup;







#### 6. parse_parts

not needed for an update.

Attach variables in canonical version to schedule_parts (and generate schedule parts) if needed.


#### 7. generate_canonical

not needed for an update

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

Writes documentation

#### generate_models

Generates the django models for returndata, by default in schemas/generated_models/. In development: -sqlalchemy option, which will export a sqlalchemy models file. 
 
#### generate_csvs

Generates schedule_parts.csv, groups.csv and variables.csv, which are used to feed xml-reader.



## Adding new schemas

### When the .xsd files are available

This is very much like creating the db from scratch, though some steps are omitted.

For this example we're adding 2016v3.

Notes: 
-- filing\_known\_version\_string <- that's from the xml xpath "census" in the filing app. We're trying to add a new version that we don't necessarily have filings for yet. For the moment, we don't care about this--it's really a way of summarizing data about filings we have, so ignore it here. 

1. Add a new production version. (This should probably be part of a fixture?). Hack: just run at the db prompt:

		insert into schemas_productionversion (version_string) values ('2016v3.0');


2. Try to add the schema files. If you're not sure if they are there check with something like this:  

		select version_string, count(*) from schemas_xsdfile group by 1 order by 1;
		
	
	To add run: 
	
		$ python manage.py enter_schema_files 2016v3.0

	If you get "schemas.models.DoesNotExist: ProductionVersion matching query does not exist." it wasn't properly added. 
	
	It should say it entered 448 new XSDFiles. Verify with the same sql in the prior step. 

3. Read the schema files with: 

		python manage.py read_schema_files 2016v3.0 
		

	Check existence with queries like:
	
	`select version_string, count(*) from schemas_element group by 1 order by 1;`
	`select version_string, count(*) from schemas_simpletype group by 1 order by 1;`
	`select version_string, count(*) from schemas_fileinclude group by 1 order by 1;`
	`select version_string, count(*) from schemas_element group by 1 order by 1;`
	`select version_string, count(*) from schemas_group group by 1 order by 1;`
	`select version_string, count(*) from schemas_complextype group by 1 order by 1;`

	and if you need to delete them use: 


	    delete from schemas_simpletype where version_string = '2016v3.0';
	    delete from schemas_fileinclude where version_string = '2016v3.0';
	    delete from schemas_element where version_string = '2016v3.0';
	    delete from schemas_group where version_string = '2016v3.0';
	    delete from schemas_complextype where version_string = '2016v3.0';
 
4. Attach schedule instances to the new xsd file we created with:
	 
 		$ python manage.py attach_schedule_instances 2016v3.0

5. Generate the mappings with:

		$ python manage.py generate\_mappings 2016v3.0

	This should be creating the versioned\_group and versioned\_variable objects for 2016v3.0. Check in the db with:

		select version_string, count(*) from schemas_versionedvariable group by 1 order by 1;

6. assign_canonical

	This is the hard part. We need to assign the canonical variables--which were created for version 2015v2.1--to 2016v3.0 variables. Moreover, we need to do this for several thousand variables as well as about 91 repeating groups. Also note that version 2016v3.0 introduces a new repeating group "/IRS990ScheduleA/AgriculturalNameAndAddressGrp" which didn't exist in prior versions. 
	
	To do this, read and modify the assign\_canonical management command. The really ugly version-specific transformation stuff is handled in schemas.epoch\_utils. Add the new version string to the definition of MODERN_EPOCH in epoch\_utils to make sure it gets processed.

	It makes sense to handle the groups first. Note that assign\_canonical, when run on groups only, doesn't complain because there are no *missing* groups. You can figure out what the new group is with this (once the others have been assigned a canonical group by running assign\_canonical )

		select xpath from schemas_versionedgroup where version_string = '2016v3.0' and canonical\_group\_id is null; 
	
	You may also want to consult the diff files availables in the IRS' schemas distributions. This version change, it should be noted, also includes a  new "FilingSecurityInformation" section of the returnheader and lots of new variables in a "HospitalFcltyPoliciesPrctcGrp" in Schedule H.
		
	The output of assign canonical looks like this, near the end:
	
			Missing Variable Keys: 
		2013v3.0 155
		2013v3.1 155
		2013v4.0 155
		2014v5.0 0
		2014v6.0 0
		2015v2.0 0
		2015v2.1 0
		2015v3.0 0
		2016v3.0 16
	
	To figure out which ones are missing, run a db query like: 
	
	 select xpath from schemas\_versionedvariable where canonical\_variable\_id is null and version\_string = '2016v3.0' order by 1;
	 
	That includes both new variables in 2016 (which shouldn't be assigned) and variables that are missing (which should be assigned). 
	
7. Regenerate the csv files that are used downstream by 990-xml-reader. 
Add the new version in the settings to: 
CSV\_OUTPUT\_SUPPORTED


### When the .xsd files are not available

This is a harder process! Best approach is to get the schemas. But you can generally just run a version in the reader library by allowing earlier versions to run on later years. This will fail to pick up any new or changed variables, but misses will can be retrieved with Filing.get_keyerrors(), where Filing is the returned parsed result.

### Recanonicalize

You probably *don't* wan't to recanonicalize, since it has the power to rename the database bindings for every variable in the system, but here's how you might do it from 2015 to 2016.

Also note you'll probably want to entirely drop and recreate the returndata tables, especially if they've changed. 

1. Kill out the canonical groups variables

		>>> from schemas.models import *
		>>> a = CanonicalVariable.objects.all()
		>>> a.delete()
		(3188, {u'schemas.CanonicalVariable': 3188})
		
		>>> b = CanonicalGroup.objects.all()
		>>> b.delete()
		(91, {u'schemas.CanonicalGroup': 91})


2. Set CANONICAL_VERSION = '2016v3.0' in the settings file. 

3. Run parse_parts. This tries to put canonical variables into "parts" as divvied up by the tax forms, but this will likely miss any new variables that have appeared. Lets see which ones:

		select count(*) from schemas_versionedvariable where version_string  = '2016v3.0' and parent_sked_part_id is null;
		
	Sometimes returnheader is not set, but it's easier to set manually. Likely what's left are the new sections		
		
		    select xpath from schemas_versionedvariable where version_string  = '2016v3.0' and parent_sked_part_id is null order by 1;
		                                           xpath                                           
-------------------------------------------------------------------------------------------
 /IRS990ScheduleA/AgriculturalNameAndAddressGrp/CityNm
 /IRS990ScheduleA/AgriculturalNameAndAddressGrp/CollegeUniversityName/BusinessNameLine1Txt
 /IRS990ScheduleA/AgriculturalNameAndAddressGrp/CollegeUniversityName/BusinessNameLine2Txt
 /IRS990ScheduleA/AgriculturalNameAndAddressGrp/CountryCd
 /IRS990ScheduleA/AgriculturalNameAndAddressGrp/StateAbbreviationCd
 /IRS990ScheduleA/AgriculturalResearchOrgInd
(6 rows)

This has happened because the parse parts script was looking at an outdated version. Edit the schema to reflect the new variables. 



4. run generate_canonical to generate the canonical names for the canonical version only.

5. run assign_canonical to assign variables in each other version to it. This requires some special casing.

6. Run propagate_from_canonical to reassign the schedule parts that were given to the variables in the canonical version to their related variables in each other version. This is necessary because we determine the 'part' of a tax form that a variable occurs in by hand editing the schema files [schema_parts_fixed](in (https://github.com/jsfenfen/irs990_admin/tree/master/irs990/schemas/schema_parts_fixed). Unfortunately the form parts are listed in the .xsd comments--which are excluded by xmltodict and many xml parsers--but worse they are sometimes missing (hence the hand editing).


