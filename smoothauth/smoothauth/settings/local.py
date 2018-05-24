"""
Local Settings
"""
from .base import *
from .ldap import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'smoothauth',
        'USER': 'smoothauth',
        'PASSWORD': 'smoothauth',
        'HOST': 'localhost',
        'PORT': '',
    }
}
