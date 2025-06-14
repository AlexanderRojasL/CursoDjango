from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']  # Puedes acceder desde cualquier IP/localhost

# Base de datos para desarrollo (usa SQLite por defecto)
# Si necesitas otra base de datos, aquí puedes sobrescribir DATABASES

# Email por consola para pruebas
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
