from .base import *


DEBUG = True
DATABASES['default'] = {
    'ENGINE': get_key('DB_ENGINE'),
    'NAME': get_key('DB_NAME'),
    'USER': get_key('DB_USER'),
    'PASSWORD': get_key('DB_PASSWORD'),
    'HOST': get_key('DB_HOST'),
    'PORT': get_key('DB_PORT'),
    'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
    'ATOMIC_REQUESTS': True,
}
