# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
import os

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "f1(ve#1%vq%!)6bunhje(y_jpa_m^!1m0sea=20pwc%=r@xwyl"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "rest_framework",
    "huey.contrib.djhuey",
    "hueydrfapi",
]

SITE_ID = 1

MIDDLEWARE = ()

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:{}'.format(
            os.environ['MEMCACHED_11211_TCP_PORT']
        ),
    }
}

HUEY = {
    'huey_class': 'huey.RedisHuey',    # Huey implementation to use.
    'name': DATABASES['default']['NAME'],    # Use db name for huey.
    'results': True,    # Store return values of tasks.
    'store_none': False,    # If a task returns None, do not save to results.
    'immediate': DEBUG,    # If DEBUG=True, run synchronously.
    'utc': True,    # Use UTC for all times internally.
    'blocking': True,    # Perform blocking pop rather than poll Redis.
    'connection': {
        'host': 'localhost',
        'port': os.environ['REDIS_6379_TCP_PORT'],
        'db': 0,
        'connection_pool': None,    # Definitely you should use pooling!
        'read_timeout': 1,    # If not polling (blocking pop), use timeout.
        'url': None,    # Allow Redis config via a DSN.
    },
    'consumer': {
        'workers': 1,
        'worker_type': 'thread',
        'initial_delay': 0.1,    # Smallest polling interval, same as -d.
        'backoff': 1.15,    # Exponential backoff using this rate, -b.
        'max_delay': 10.0,    # Max possible polling interval, -m.
        'scheduler_interval': 1,    # Check schedule every second, -s.
        'periodic': True,    # Enable crontab feature.
        'check_worker_health': True,    # Enable worker health checks.
        'health_check_interval': 1,    # Check worker health every second.
    },
}
