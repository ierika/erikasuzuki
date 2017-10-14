from .base import *


DEBUG = False
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'erika',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': 3306,
    'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
    'ATOMIC_REQUESTS': True,
}
