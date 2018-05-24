# Replace these settings with settings from your own Environment
# Rename file ldap.py

AUTHENTICATION_BACKENDS = (
    "django_python3_ldap.auth.LDAPBackend",
)

# The URL of the LDAP server.
LDAP_AUTH_URL = "ldap://127.0.0.1:389"

# Initiate TLS on connection.
LDAP_AUTH_USE_TLS = False

# The LDAP search base for looking up users.
LDAP_AUTH_SEARCH_BASE = "dc=example,dc=com"

# The LDAP class that represents a user.
LDAP_AUTH_OBJECT_CLASS = "user"

# User model fields mapped to the LDAP
# attributes that represent them.
LDAP_AUTH_USER_FIELDS = {
    # "username": "uid", # JRK - Had to change this to connect
    "username": "samAccountName",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

# A tuple of django model fields used to uniquely identify a user.
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)

# Path to a callable that takes a dict of {model_field_name: value},
# returning a dict of clean model data.
# Use this to customize how data loaded from LDAP is saved to the User model.
LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"

# Path to a callable that takes a user model
# and a dict of {ldap_field_name: [value]},
# and saves any additional user relationships based on the LDAP data.
# Use this to customize how data loaded from
# LDAP is saved to User model relations.
# For customizing non-related User model fields, use LDAP_AUTH_CLEAN_USER_DATA.
LDAP_AUTH_SYNC_USER_RELATIONS = "django_python3_ldap.utils.sync_user_relations"

# Path to a callable that takes a dict of {ldap_field_name: value},
# returning a list of [ldap_search_filter].
# The search filters will then be AND'd
# together when creating the final search filter.
LDAP_AUTH_FORMAT_SEARCH_FILTERS = \
        "django_python3_ldap.utils.format_search_filters"

# Path to callable that takes a dict of {model_field_name: value}, and returns
# a string of the username to bind to the LDAP server.
# Use this to support different types of LDAP server.

'''
LDAP_AUTH_FORMAT_USERNAME = \
        "django_python3_ldap.utils.format_username_openldap"
LDAP_AUTH_FORMAT_USERNAME = \
        "django_python3_ldap.utils.format_username_active_directory_principal"

'''
LDAP_AUTH_FORMAT_USERNAME = \
                "django_python3_ldap.utils.format_username_active_directory"

# Sets the login domain for Active Directory users.
LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = 'EXAMPLE_DOM'

# The LDAP username & pwd of a user for querying the LDAP database for user
# details. If None, then the authenticated user will be used for querying, and
# the `ldap_sync_users` command will perform an anonymous query.
LDAP_AUTH_CONNECTION_USERNAME = "administrator"
LDAP_AUTH_CONNECTION_PASSWORD = "password"

# Set connection/receive timeouts (in seconds) on the underlying `ldap3` lib.
LDAP_AUTH_CONNECT_TIMEOUT = None
LDAP_AUTH_RECEIVE_TIMEOUT = None

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django_python3_ldap": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}
