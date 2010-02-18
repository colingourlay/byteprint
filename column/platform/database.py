# == DATABASE SETTINGS ======================================================= #
#                                                                              #
# If you are using sqlite, only NAME and ENGINE are required. For other local  #
# databases, you also need to complete the USER & PASSWORD fields. If the      #
# database is on a separate host, enter the relevant HOST and PORT details.    #
# OPTIONS is reserved for special commands that may need to be run against the #
# database. This can be left blank.                                            #
#                                                                              #
# 'NAME'     - Database name / path to a local sqlite database                 #
# 'ENGINE'   - django.db.backends.* that connects to your database             #
# 'USER'     - Database username                                               #
# 'PASSWORD' - Database password                                               #
# 'HOST'     - Database host (defaults to localhost if left blank)             #
# 'PORT'     - Database port (used with the database host)                     #
# 'OPTIONS'  - Special options to be interpreted by the database engine        #
#                                                                              #
# To get you up and running quickly, settings have already been provided for a #
# local sqlite database, which will allow you to complete the installation     #
# process, and have a look at the system. You should change these settings to  #
# those of your real database before performing a permanent installation.      #
#                                                                              #
# ============================================================================ #

DATABASES = {
    'default': {
        'NAME': 'platform/testdb.sqlite',
        'ENGINE': 'django.db.backends.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {},
    }
}