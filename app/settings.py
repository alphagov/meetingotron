TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
SITE_ID = 1
CAMPAIGN_ID = 1
USE_I18N = True
MEDIA_URL = '/site-media/'

ADMIN_MEDIA_PREFIX = '/admin-media/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'meeting',
)

try:
    from local_settings import *
except ImportError:
    print "Missing local_settings.py file or file not in PATH"

import os
import yaml

# Database settings
yaml_db = yaml.load(file(os.path.join(PROJECT_DIR, 'database.yml'), 'r'))[DB_ENV]
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.' + yaml_db['adapter'],
    'HOST': yaml_db['host'] if yaml_db.has_key('host') else '',
    'NAME': yaml_db['database'],
    'USER': yaml_db['username'],
    'PASSWORD': yaml_db['password'] if yaml_db.has_key('password') else '',
    'PORT': yaml_db['port'] if yaml_db.has_key('port') else '',
    'OPTIONS': {},
    'TEST_CHARSET': None,
    'TEST_COLLATION': None,
    'TEST_NAME': None,
  } 
}

