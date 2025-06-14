from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']  # Puedes acceder desde cualquier IP/localhost

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Products_Registry',
        'USER': 'postgres',
        'PASSWORD': 'ucuenca',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

