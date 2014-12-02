from .base import *

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eventosdb',
        'USER': 'eventosuser',
        'PASSWORD': 'JacaEventos',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.child('media')

TEMPLATE_DIRS = [BASE_DIR.child('templates')]

STATICFILES_DIRS = [BASE_DIR.child('static')]
