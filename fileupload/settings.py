"""
Django settings for fileupload project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t%sa%emmb966roefevildepm&xmdig9kyx0+y5%+_yr$(scs$%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'upload',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fileupload.urls'

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

WSGI_APPLICATION = 'fileupload.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwjxfHnRioo2QO1qfnulurwHFoKohPNXTLu81x32fX8ygKARs6i0UoKomfAJeJZC9DF4YXmCY6LaID6zmDwWnxvW80RUOCJBW5RakiqkaarfmCtcnHy0irUXdg18Muvy+R/2Jq1AJo6SGo5LUSGG6/gCr2XBACuaKJe9B5BHK/uL/7YF7sSoh+M7M5hehwU5UlOBw865GWXsQw5NJZnf8vAUa8+WhL+picp0T2/ZyqRFYyPmyA+bEeio6REHcC9+Xm/91wdbYhSPY6XrKJWtN60R3UNP0sbukNoLUdqkA2SVXJ1NuqSj3iw/I9ZJ4JAOwEqSHG9/LQM+IWF+F64LvywIDAQAB"
PUBLIC_KEY = """MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4v2Jg2Hk6tfgr4oKVoO9
grxCTHAXcBJeLR0QzDS0f7yseTg2YTtxVnxO9fFEf54/ZBvHD0Wjtbwx7S452oPm
xAHYcKOTfFrer72qGgdgCeSDFQTRXtRPsVH1UNukkV9rFMYtVfnYwLi0AE1llIEF
L5k2buKqrHCAAKwO989G0WBcUyJz8uqzclcPf+DQpxjez9Ua+jb7FVR9XQBCgOdu
O2fhhEoq/e4f5fwleRVfCL8qeyji0CLqqwlaLaS7JpGdk+YpGChHgX0acUzk6rGM
LsOzsaRmBEWadlg2MbYG1PYo8WYLHNTPSSf5GTAZkdN+8PG01EK8FcMJZZWgRj8n
VQIDAQAB"""

PRIVATE_KEY ="""
-----BEGIN RSA PRIVATE KEY-----
MIIBPQIBAAJBAKaZAcA5djMS1OqGLXFRbaegLny88cULWpVwoV0gSDObjNeckWp6
F42tSln7jp4H/2275n9Wwc1Naq8w+SUctQ0CAwEAAQJADHNvABDLVrHXm9d/WfK+
AUMldkkgwJtCn9yVEsKwz9mxauMv/1i+AT66CvP3gfFoa+2LmjLTJaVAzMZjAUra
AQIjAPyY3t4HVPamWWqhRbyR/x9r5ud2PzifkHy1VlUWFEPttE0CHwCo14z7FLDB
NcMLJMWKGN9wpAySvrkARmvrB5nmY8ECIwCaGu3FSXXVcNGWk0OHcw7R7bOWvPZ/
JiIxYzSDfo/ojWn1Ah4Bt+fkakp+POjWRTKJfEVR5SmHmM9TNGRGyRYE5UECIwCN
cxhCEYO9WcNEVy6GAthqXHVhd4mxYV8Vo0zJJKv7FQgq
-----END RSA PRIVATE KEY-----
"""