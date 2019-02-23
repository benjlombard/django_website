from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ADMINS = [
    ('Lombard Benjamin','benjamin.lombard.fr@gmail.com')
]
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5n7dfv*i(7s$0!%_gb-=s@xgxys6r=28ir=)xh!+i(2b6myo-*'



ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'blog',
        'USER' : 'blog',
        'PASSWORD':'blog'
    }
}