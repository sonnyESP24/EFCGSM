# """
# Django settings for project project.
#
# Generated by 'django-admin startproject' using Django 1.9.2.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/1.9/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/1.9/ref/settings/
# """
#
# import os
#
# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '^h85uo#*&q+5r=a1_l8i_&t$^$(sgsz-3*ijq8%22ayrbapxyk'
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# #load frontend from webpack dev server rather than static
# WEBPACK_DEV_SERVER = True
#
# ALLOWED_HOSTS = []
#
#
# # Application definition
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#
#     'apps.home'
# ]
#
# MIDDLEWARE_CLASSES = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': ['/app/templates/'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#                 'context_processors.static_resources'
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'wsgi.application'
#
#
# # Database
# # https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'django',
#         'USER': 'django',
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }
#
#
#
# # Password validation
# # https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
#
# # Internationalization
# # https://docs.djangoproject.com/en/1.9/topics/i18n/
#
# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True
#
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.9/howto/static-files/
#
# STATIC_URL = '/static/'
# STATIC_ROOT = '/static/'
#
# STATIC_ASSETS_JSON  = os.path.join(STATIC_ROOT, 'assets.json')
#
# # user uploads
# MEDIA_URL = '/media/'
# MEDIA_ROOT = '/media/'


"""
Misago settings for testforum project.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from misago.conf.defaults import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

# Hosts allowed to POST to your site
# If you are unsure, just enter here your host name, eg. 'mysite.com'

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        # Only PostgreSQL is supported
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'denzzodb1',
        'USER': 'denzzodb1user',
        'PASSWORD': 'denzzodb1userpass',
        'HOST': '104.154.114.244',
        'PORT': 5432,
    }
}


# Cache
# https://docs.djangoproject.com/en/1.9/ref/settings/#caches

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


# Site language
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Fallback Timezone
# Used to format dates on server, that are then
# presented to clients with disabled JS
# Consult http://en.wikipedia.org/wiki/List_of_tz_database_time_zones TZ column
# for valid values

TIME_ZONE = 'UTC'


# Path used to access static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

# Path used to access uploaded media (Avatars and Profile Backgrounds, ect.)
# This is NOT path used to serve posts attachments.
# https://docs.djangoproject.com/en/1.9/howto/static-files/
MEDIA_URL = '/media/'


# Automatically setup default paths to media and attachments directories
MISAGO_ATTACHMENTS_ROOT = os.path.join(BASE_DIR, 'attachments')
MISAGO_AVATAR_STORE = os.path.join(BASE_DIR, 'avatar_store')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Automatically setup default paths for static and template directories
# You can use those directories to easily customize and add your own
# assets and templates to your site
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'theme', 'static'),
) + STATICFILES_DIRS

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'theme', 'templates'),
) + TEMPLATE_DIRS


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6HLJRsA^K^9g]5R6beF}\>+"wXa9`f![Xds$axCLGYK-PXyFJetY72??k8Dw'


# X-Sendfile support
# X-Sendfile is feature provided by Http servers that allows web apps to
# delegate serving files over to the better performing server instead of
# doing it within app.
# If your server supports X-Sendfile or its variation, enter header name here.
# For example if you are using Nginx with X-accel enabled, set this setting
# to "X-Accel-Redirect".
# Leave this setting empty to Django fallback instead
MISAGO_SENDFILE_HEADER = ''

# Allows you to use location feature of your Http server
# For example, if you have internal location /mymisago/avatar_cache/
# that points at /home/myweb/misagoforum/avatar_cache/, set this setting
# to "mymisago".
MISAGO_SENDFILE_LOCATIONS_PATH = ''


# Application definition
# Don't edit those settings unless you know what you are doing
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
