from settings.base import *

SECRET_KEY = 'cambiar en producción'
DEBUG = True
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root_join('..', 'var', 'db_local.sqlite3'),
    }
}
