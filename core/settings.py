# -*- encoding: utf-8 -*-

import os
from decouple import config
from unipath import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# load production server from .env
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.home',
    'apps.authentication',
]

CRYPTOCURRENCY_PAYMENT = {
    "BITCOIN": {
        "CODE": "btc",
        "BACKEND": "merchant_wallet.backends.btc.BitcoinBackend",
        "FEE": 0.00,
        "REFRESH_PRICE_AFTER_MINUTE": 15,
        "REUSE_ADDRESS": False,
        "ACTIVE": True,
        "MASTER_PUBLIC_KEY": 'PUT_YOUR_WALLET_MASTER_PUBLIC_KEY',
        "CANCEL_UNPAID_PAYMENT_HRS": 3,
        "CREATE_NEW_UNDERPAID_PAYMENT": True,
        "IGNORE_UNDERPAYMENT_AMOUNT": 10,
        "IGNORE_CONFIRMED_BALANCE_WITHOUT_SAVED_HASH_MINS": 20,
        "BALANCE_CONFIRMATION_NUM": 1,
        "ALLOW_ANONYMOUS_PAYMENT": True,
    }
 }
#RECAPTCHA_PUBLIC_KEY = '6LepxmYiAAAAAIxjWCwbRIhRo1BK52xuFFKFgVmw'
#RECAPTCHA_PRIVATE_KEY = '6LepxmYiAAAAALM4ucvJLoBFMyz9jHp7dPr1fgr5'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "pages/dashboard.html"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "login"  # Route defined in home/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
)

SITE_NAME = 'clarion-investments.com'

EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587  
EMAIL_HOST_USER = 'soluwatoogun@gmail.com'  
EMAIL_HOST_PASSWORD = 'ajcpmsglrjougawn'
ADMINS = (
('blackwolf', 'soluwatoogun@gmail.com'),
)
MANAGERS = ADMINS


EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(CORE_DIR, 'sent_emails')
#############################################################
#############################################################
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'