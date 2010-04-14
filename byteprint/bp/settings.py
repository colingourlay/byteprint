import os

from django.conf.global_settings import *

BP_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(BP_DIR, 'core')
THEMES_DIR = (os.path.join(BP_DIR, 'themes'),)
PLUGINS_DIR = os.path.join(BP_DIR, 'plugins')
STATIC_DIR = os.path.join(BP_DIR, '../static')
STATIC_CORE_DIR = os.path.join(STATIC_DIR, 'core')
STATIC_THEMES_DIR = os.path.join(STATIC_DIR, 'themes')
STATIC_PLUGINS_DIR = os.path.join(STATIC_DIR, 'plugins')
UPLOADS_DIR = os.path.join(STATIC_DIR, 'uploads')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

USE_I18N = False

MEDIA_URL = '/static/'

TEMPLATE_DIRS = ()
for root, dirs, files in os.walk(BP_DIR):
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
    'bp.core.public.context_processors.request',
)

if DEBUG:
    TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'bp.core.installation.middleware.InstallationMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'bp.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
	'django.contrib.sessions',
    'bp.core.admin',
    'bp.core.articles',
    'bp.core.config',
    'bp.core.public',
    'bp.core.scraps',
)

try:
    from database import *
except ImportError:
    pass

TIME_ZONE = 'Australia/Brisbane'
LANGUAGE_CODE = 'en'
ADMINS = ()
SECRET_KEY = 'vk%spllo^0y$iskqrr%6mpo_*7826_(!&x+gt#&^kjfw*1m2d_'

LOGIN_URL = '/admin/login/'
LOGIN_REDIRECT_URL ='/admin/'

VERSION = '0.1'