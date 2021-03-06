"""
Django settings for djtwapp project.
Generated by 'django-admin startproject' using Django 2.1.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import json

import django_heroku
import tweepy
import firebase_admin
from firebase_admin import credentials

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if "DEPLOY" in os.environ.keys():
    DEPLOY = True
else:
    _credentials = json.load(open(BASE_DIR+"/credentials.json", "r"))
    DEPLOY = False

# Firebase setup
if DEPLOY:
    firebase_credentials = json.loads(os.environ["FIREBASE_CREDENTIALS"])
    twitter_credentials = json.loads(os.environ["TWITTER_CREDENTIALS"])
    django_credentials = json.loads(os.environ["DJANGO_CREDENTIALS"])
    
else:
    firebase_credentials = _credentials["firebase_credentials"]
    twitter_credentials = _credentials["twitter_credentials"]
    django_credentials = _credentials["django_credentials"]
    database_credentials = _credentials["database_credentials"]

# Firebase API

CRED = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(CRED, {'databaseURL': 'https://djtwapp.firebaseio.com'})

# Tweepy API

AUTH = tweepy.OAuthHandler(twitter_credentials["CONSUMER_KEY"], twitter_credentials["CONSUMER_SECRET"])
AUTH.set_access_token(twitter_credentials["ACCESS_TOKEN"], twitter_credentials["ACCESS_TOKEN_SECRET"])
TWEEPY_API = tweepy.API(AUTH)

# Tweepy exceptions
RATE_LIMIT_ERROR = tweepy.RateLimitError
TWEEP_ERROR = tweepy.TweepError

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = django_credentials["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not DEPLOY

ALLOWED_HOSTS = ["127.0.0.1", "https://djtwapp.herokuapp.com/"]


# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'profiles',
]


AUTH_USER_MODEL = "accounts.User"

# redirect urls
LOGIN_URL = "/accounts/login/"

REGISTER_REDIRECT_URL= "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djtwapp.urls'

TEMPLATES = [
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

WSGI_APPLICATION = 'djtwapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


DATABASES = {}
if not DEPLOY:
    DATABASES["default"] = database_credentials

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Activate Django-Heroku.
django_heroku.settings(locals())