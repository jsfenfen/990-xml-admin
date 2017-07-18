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

### Commands:


	$ python manage.py enter_schema_files

Enter the schema files by walking the SCHEMA_DIR. 
Optionally pass a version_string as an arg to run only on that version, e.g. 
	$ python manage.py enter\_schema\_files 2013v4.0 

Hard SQL undo: delete from schemas\_xsdfile [ where version_string='2013v4.0'];


$ python manage.py read\_schema\_files

Optionally pass a version_string as an arg to run only on that version, e.g. 
	$ python manage.py read\_schema\_files 2013v4.0 




