from .base import *

ALLOWED_HOSTS = ['3.34.111.69']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'F.fTsZFAZR:!!<B0GY5t]=AcovD!n*)=',
        'HOST': 'ls-195bae6e626085979ab732df1a00121384aadf4a.cfwmsv8nqg9b.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}