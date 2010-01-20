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
#         'NAME': '',     # - The name of your database, or a path to sqlite DB
#         'ENGINE': '',   # - django.db.backends.* that connects to your DB
#         'USER': '',     # - DB username 
#         'PASSWORD': '', # - DB password
#         'HOST': '',     # - DB remote host (defaults to localhost)
#         'PORT': '',     # - Remote host port for DB access
#         'OPTIONS': {},  # - Special options to be interpreted by the DB
#     }                   #
# }                       #
#                         # == HELP ============================================
#                         # If you are using sqlite, only NAME and ENGINE are
#                         # required. For other local databases, you also need
#                         # to complete the USER & PASSWORD fields. If the
#                         # database is on a separate host, enter the relevant
#                         # HOST and PORT details. OPTIONS is reserved for
#                         # special commands that may need to be run against the
#                         # database. This can be left blank.
#                         # ====================================================