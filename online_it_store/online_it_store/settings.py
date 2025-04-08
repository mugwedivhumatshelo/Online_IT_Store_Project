"""
Django settings for online_it_store project.

Generated by 'django-admin startproject' using Django 4.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os 
from pathlib import Path 
import environ

env = environ.Env() 

# Build paths inside the project like this: BASE_DIR / 'subdir'. 
BASE_DIR = Path(__file__).resolve().parent.parent 

# Quick-start development settings - unsuitable for production 
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/ 

# SECURITY WARNING: keep the secret key used in production secret! 
SECRET_KEY = env('SECRET_KEY', default='django-insecure-#phjuvrf0y-e3lh@3x)%_k763@*q)j81#1m#7b5l8ivv*g-i0#i') 

if not SECRET_KEY: 
    raise ValueError("SECRET_KEY is not set") 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

# Application definition 
INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
    'rest_framework', 
    'environ', 
    'corsheaders', 
    'api', 
    'categories', 
    'orders', 
    'users', 
] 

AUTH_USER_MODEL = 'api.User' 
AUTHENTICATION_BACKENDS = ['api.backends.CustomUserBackend'] 

MIDDLEWARE = [ 
    'django.middleware.security.SecurityMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware', 
    'django.middleware.common.CommonMiddleware', 
    'django.middleware.csrf.CsrfViewMiddleware', 
    'django.contrib.auth.middleware.AuthenticationMiddleware', 
    'django.contrib.messages.middleware.MessageMiddleware', 
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
    'corsheaders.middleware.CorsMiddleware', 
] 

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=[ 
    'http://localhost:8000', 
    'http://127.0.0.1:8000', 
]) 

REST_FRAMEWORK = { 
    'DEFAULT_AUTHENTICATION_CLASSES': [ 
        'rest_framework.authentication.BasicAuthentication', 
        'rest_framework.authentication.SessionAuthentication', 
    ], 
    'DEFAULT_PERMISSION_CLASSES': [ 
        'rest_framework.permissions.IsAuthenticated', 
    ] 
} 

ROOT_URLCONF = 'online_it_store.urls'

TEMPLATES = [ 
    { 
        'BACKEND': 'django.template.backends.django.DjangoTemplates', 
        'DIRS': [os.path.join(BASE_DIR, 'templates')], 
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

WSGI_APPLICATION = 'online_it_store.wsgi.application'

# Database 
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'online_it_store',
        'USER': 'root',
        'PASSWORD': 'Futuree@2021',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

if not DATABASES['default']['NAME']: 
    raise ValueError("DB_NAME is not set") 

# Password validation 
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators 

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'categories/static/categories',
    BASE_DIR / 'api/static/api',
    BASE_DIR / 'orders/static/orders',
    BASE_DIR / 'users/static/users',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

