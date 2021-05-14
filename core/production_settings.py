import os

import dj_database_url

DEBUG = False
ALLOW_HOSTS = ['django-coffee-shop-10656009.heroduapp.com']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500, ssl_require=True),
}

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', None)

EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', None)