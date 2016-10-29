from .settings import *


ALLOWED_HOSTS = ['*']

DEBUG = False
TEMPLATE_DEBUG = False
#WEBPACK_DEV_SERVER = False

STATIC_ASSETS_JSON = os.path.join(BASE_DIR, 'assets.json')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'applogfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/logs/app/app.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['applogfile'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

DEFAULT_FILE_STORAGE = 'storages.backends.gs.GSBotoStorage'
GS_ACCESS_KEY_ID = 'GOOGULHRN6XBTRCQ6ZYB'
GS_SECRET_ACCESS_KEY = 'fPcHWztGSx4J2bfWg3UUb0qYid+5eqnMUBBH5Ltp'
GS_BUCKET_NAME = '365partydotnet'
STATICFILES_STORAGE = 'storages.backends.gs.GSBotoStorage'