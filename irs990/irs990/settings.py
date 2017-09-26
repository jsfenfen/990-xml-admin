import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'filing',
    'schemas',
    'returndata',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'irs990.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'irs990.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_URL = '/static/'

IRS_XML_BUCKET = 'irs-form-990'
IRS_XML_HTTP_BASE = "https://s3.amazonaws.com/%s/" % IRS_XML_BUCKET
IRS_INDEX_FILE = IRS_XML_HTTP_BASE + "index_%s.csv" 

# Most widely used at time of creation
CANONICAL_VERSION = '2015v2.1'

# Forms we can generate schemas for
SUPPORTED_SCHEMAS = [
     'IRS990.xsd', 'IRS990EZ.xsd', 'IRS990PF.xsd', 
    'IRS990ScheduleA.xsd', 'IRS990ScheduleB.xsd', 
    'IRS990ScheduleC.xsd', 'IRS990ScheduleD.xsd',
    'IRS990ScheduleE.xsd', 'IRS990ScheduleF.xsd',
    'IRS990ScheduleG.xsd', 'IRS990ScheduleH.xsd',
    'IRS990ScheduleI.xsd', 'IRS990ScheduleJ.xsd',
    'IRS990ScheduleK.xsd', 'IRS990ScheduleL.xsd',
    'IRS990ScheduleM.xsd', 'IRS990ScheduleN.xsd',
    'IRS990ScheduleO.xsd', 'IRS990ScheduleR.xsd',
    'ReturnHeader990x.xsd']


CSV_OUTPUT_SUPPORTED = [
    '2013v3.0', '2013v3.1', '2013v4.0', '2014v5.0', 
    '2014v6.0', '2015v2.0', '2015v2.1', '2015v3.0', '2016v3.0']

CSV_OUTPUT_DEVELOPMENT = ['2012v2.3']


try:
    from local_settings import *
except ImportError:
    print("Error importing local_settings.py")
