from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

print(type(DEBUG))
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-gii4k+gh&1u%qilw%#+udjw15p-mspdon$f@pw(@&_qyup89xg').strip("'")
# DEBUG = False if os.environ.get('DEBUG') == 'False' else True
print(str(os.getenv('DEBUG', 'True')).lower())
DEBUG = False if str(os.getenv('DEBUG', 'True')).lower() == 'false' else True
# os.getenv("ENV_VAR", 'False').lower() in ('true', '1', 't')
print(f'\n{20*"-"}ATENCIÓN! DEBUG={DEBUG}{20*"-"}\n')
# print('environ', os.environ)
if DEBUG == False:
    # print('ENVIRONMENT TEST ABC: ', os.environ.get('TEST'))
    # print('type: ', type(DEBUG), DEBUG, os.environ.get('ALLOWED_HOSTS'))
    ALLOWED_HOSTS = ['*']
    # ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]
else:
    ALLOWED_HOSTS = ['*']

print(ALLOWED_HOSTS, type(DEBUG))
try:
    CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS').split()
    print('CSRF_TRUSTED_ORIGINS:', CSRF_TRUSTED_ORIGINS)
except AttributeError:
    print('No CSRF_TRUSTED_ORIGINS loaded')
    


# Application definition
AUTH_USER_MODEL = 'front.User'
INSTALLED_APPS = [
    'front',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'requests',
    'corsheaders',
    'phonenumber_field',
    'django_countries',
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
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if DEBUG == True:
    print('DEBUG IN DATABASE: ', DEBUG, 'PG')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif DEBUG == False:    
    print('DEBUG IN DATABASE: ', DEBUG, 'SQLITE')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators


print('AUTH_USER_MODEL = front.User')
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

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
