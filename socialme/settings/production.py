from socialme.settings.common import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# Should be reconfigured for PostgresQL or MySQL on production

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'db.sqlite3',
    },
}
