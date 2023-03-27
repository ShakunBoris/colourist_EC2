"""
Django settings for colourist project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-gii4k+gh&1u%qilw%#+udjw15p-mspdon$f@pw(@&_qyup89xg')
# DEBUG = False if os.environ.get('DEBUG') == 'False' else True
DEBUG = False
print(f'\n{20*"-"}ATENCIÓN! DEBUG={DEBUG}{20*"-"}\n')
# print('environ', os.environ)
if DEBUG == False:
    print('ENVIRONMENT TEST ABC: ', os.environ.get('TEST'))
    print('type: ', type(DEBUG), DEBUG, os.environ.get('ALLOWED_HOSTS'))
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')
else:
    ALLOWED_HOSTS = ['*']

try:
    CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS').split()
    print('CSRF_TRUSTED_ORIGINS:', CSRF_TRUSTED_ORIGINS)
except AttributeError:
    print('No CSRF_TRUSTED_ORIGINS loaded')
    
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Application definition

INSTALLED_APPS = [
    'front',
    'phonenumber_field',
    'django_countries',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'colourist.urls'

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

WSGI_APPLICATION = 'colourist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# if DEBUG == False:
#     print('DEBUG IN DATABASE: ', DEBUG, 'PG')
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': os.environ.get('PGDATABASE'),
#             'USER': os.environ.get('PGUSER'),
#             'PASSWORD': os.environ.get('PGPASSWORD'),
#             'HOST': os.environ.get('PGHOST'),
#             'PORT': os.environ.get('PGPORT'),
#         }
#     }
# elif 
if DEBUG == False:    
    print('DEBUG IN DATABASE: ', DEBUG, 'SQLITE')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'front.User'

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
