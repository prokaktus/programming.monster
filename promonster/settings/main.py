"""
Django settings for promonster project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

import sentry_sdk
from sentry_sdk.integrations.django import \
    DjangoIntegration

from ._utils import getenv


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY', 'Not Secure Default s3cRE+t')

# SECURITY WARNING: don't run with debug turned on in production!
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv('DEBUG', False)

ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', 'localhost').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',

    'apps.base',
    'apps.users',
    'apps.articles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'promonster.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'APP_DIRS': True,
        'OPTIONS': {
            'extensions': [
                'wagtail.core.jinja2tags.core',
                'wagtail.admin.jinja2tags.userbar',
                'wagtail.images.jinja2tags.images',
            ],
            'environment': 'promonster.environment.jinja.build',
            'context_processors': [
                'promonster.context_processors.third_parties'
            ]
        },
        'DIRS': [
            os.path.join(BASE_DIR, 'promonster', 'jinja2'),
        ],
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'promonster.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'promonster'),
        'USER': os.getenv('DB_USER', 'promonster'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'promonster'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# AUTH strategies
AUTH_USER_MODEL = 'users.User'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'apps.base.static_loader.FileStorage'

# Wagtail specific configuration
WAGTAIL_SITE_NAME = 'Programming.Monster'


# analytics / tracking section
GOOGLE_ANALYTICS = getenv('GOOGLE_ANALYTICS', '')
YANDEX_METRICA = getenv('YANDEX_METRICA', '')
TOP_MAILRU = getenv('TOP_MAILRU', '')


# Sentry settings
if not DEBUG:
    SENTRYJS_CONFIG = os.getenv('SENTRY_DSN_JS', '')
    sentry_sdk.init(
        getenv('SENTRY_DSN'),
        integrations=[DjangoIntegration()]
    )
else:
    SENTRYJS_CONFIG = ''


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'promonster.storage.FileStorage'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Deploy hidden configuration

ADMIN_PREFIX = getenv('ADMIN_PREFIX', 'hidden')

# Logging configuration

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'echo': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        } if getenv('LOGGING_ENABLE_ECHO', False) else {'class': 'logging.NullHandler'},
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/var/log/promonster/django.log',
            'formatter': 'verbose',
            'when': 'D'
        } if getenv('LOGGING_ENABLE_FILE') else {'class': 'logging.NullHandler'}
    },
    'loggers': {
        'django': {
            'handlers': ['echo', 'file'],
            'level': getenv('LOGGING_LEVEL_DJANGO', 'INFO'),
            'propagate': True,
        },
        'django.db': {
            'handlers': ['echo', 'file'],
            'level': getenv('LOGGING_LEVEL_DJANGO_DB', 'INFO'),
            'propagate': False
        },
        'apps': {
            'handlers': ['file', 'echo'],
            'level': getenv('LOGGING_LEVEL_MAIN', 'INFO'),
            'propagate': False
        },
        'promonster': {
            'handlers': ['file', 'echo'],
            'level': getenv('LOGGING_LEVEL_MAIN', 'INFO'),
            'propagate': False
        },
    },
}
