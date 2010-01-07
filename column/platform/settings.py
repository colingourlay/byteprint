from django.conf.global_settings import *

import os

PLATFORM_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

USE_I18N = False

MEDIA_URL = '/content/'

CONTENT_DIR = os.path.join(PLATFORM_DIR, '../content')
THEMES_DIR = (os.path.join(PLATFORM_DIR, '../themes'),)

TEMPLATE_DIRS = ()
for root, dirs, files in os.walk(PLATFORM_DIR):
    if 'templates' in dirs:
        TEMPLATE_DIRS += (os.path.join(root, 'templates'),)
TEMPLATE_DIRS += THEMES_DIR

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    #'django.template.loaders.app_directories.load_template_source',
    #'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'platform.core.context_processors.request',
)

if DEBUG:
    TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'platform.installation.middleware.InstallationMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'platform.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
	'django.contrib.sessions',
    'platform.admin',
    'platform.core',
    'platform.widgets',
)

try:
    from database import *
except ImportError:
    pass

DATABASE_OPTIONS = {}
TIME_ZONE = 'Australia/Brisbane'
LANGUAGE_CODE = 'en'
ADMINS = ()
SECRET_KEY = 'vk%spllo^0y$iskqrr%6mpo_*7826_(!&x+gt#&^kjfw*1m2d_'

LOGIN_URL = '/admin/login/'
LOGIN_REDIRECT_URL ='/admin/'

VERSION = '0.1'