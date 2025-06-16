from .base import *

DEBUG = False

ALLOWED_HOSTS = ['tu-dominio.com', 'www.tu-dominio.com']

# Configuracio de base de datos real aquí (para producción) si no se usa SQLite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#     }
# }

# Seguridad recomendada para producción
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Email real (opcional)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
