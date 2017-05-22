# IRS 990 Admin

This is a helper to keep tabs on form 990 filings made electronically and released as described [here](https://aws.amazon.com/public-datasets/irs-990/).

# Installation

Clone this repository. It's recommended that you generate a [virtual env](https://virtualenv.pypa.io/en/stable/) for this code to live in. Install the dependencies with `$ pip install -r requirements.txt`.

The settings.py file automatically includes a local_settings.py file, which contains sensitive information and is not included in this repository. Start by copying the local_settings-example.py file to local_settings.py and set the needed values there. You will likely need to set the database configuration variables and template locations.

# Management commands

The simplest way to download the raw xml files is to sync a local directory to the master S3 bucket using AWS' command line tools. Doing so requires configuring the CLI tool--see more [here](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html). 



