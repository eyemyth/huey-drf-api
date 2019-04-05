"""
Django settings for example project.

Generated by Cookiecutter Django Package

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "t!h=t_x-_#(@-xsur!q@#q_7e)*8widi=q)lhx%!$tt(#ks8%e"

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
    'huey.contrib.djhuey',
    'rest_framework',
    'hueydrfapi',
    'example_tasks',

    # if your app has other dependencies that need to be added to the site
    # they should be added here
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

ROOT_URLCONF = 'example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS':
            {
                'context_processors':
                    [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
            },
    },
]

WSGI_APPLICATION = 'example.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

CACHES = {
    'default':
        {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': '/tmp/django_cache',
        }
}

HUEY = {
    'huey_class': 'huey.SqliteHuey',  # Huey implementation to use.
    'name': DATABASES['default']['NAME'],  # Use db name for huey.
    'filename': os.path.join(BASE_DIR, 'huey.db'),
    'results': True,  # Store return values of tasks.
    'store_none': False,  # If a task returns None, do not save to results.
    'immediate': False,  # If DEBUG=True, run synchronously.
    'utc': True,  # Use UTC for all times internally.
    # 'connection': {
    #     'host': 'localhost',
    #     'port': 6379,
    #     'db': 0,
    #     'connection_pool': None,  # Definitely you should use pooling!
    #     # ... tons of other options, see redis-py for details.

    #     # huey-specific connection parameters.
    #     'read_timeout': 1,  # If not polling (blocking pop), use timeout.
    #     'url': None,  # Allow Redis config via a DSN.
    # },
    'consumer':
        {
            'workers': 1,
            'worker_type': 'thread',
            'initial_delay': 0.1,  # Smallest polling interval, same as -d.
            'backoff': 1.15,  # Exponential backoff using this rate, -b.
            'max_delay': 10.0,  # Max possible polling interval, -m.
            'scheduler_interval': 1,  # Check schedule every second, -s.
            'periodic': True,  # Enable crontab feature.
            'check_worker_health': True,  # Enable worker health checks.
            'health_check_interval': 1,  # Check worker health every second.
        },
}
