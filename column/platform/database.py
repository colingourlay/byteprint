DATABASES = {
    'default': {
        'NAME': '/Users/colin/db/db.sqlite',
        'ENGINE': 'django.db.backends.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {},
    }
}

# DATABASES = {           #
#     'default': {        # 
#         'NAME': '',     # The name of your database, or a path if using sqlite
#         'ENGINE': '',   # One of django.db.backends that connects to your DB
#         'USER': '',     # Database user username 
#         'PASSWORD': '', # Database user password
#         'HOST': '',     # Remote host of database (defaults to localhost)
#         'PORT': '',     # Port of remote host for database access
#         'OPTIONS': {},  # Special options to be interpreted by the database
#     }                   #
# }                       #
#                         # == HELP ==
#                         # If you are using sqlite, only NAME and ENGINE are
#                         # required. For other local databases, you also need
#                         # to complete the USER & PASSWORD fields. If the
#                         # database is on a separate host, enter the relevant
#                         # HOST and PORT details. OPTIONS is reserved for
#                         # special commands that may need to be run against the
#                         # database. This can be left blank.