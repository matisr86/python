from __future__ import unicode_literals

SECRET_KEY = "b96530d1-f3d2-4dc2-85bc-4a290b9c4461f7b02149-7a81-4c7b-a2fc-19895f5f298189333765-f477-4855-b1d4-6fc1fe6ed610"
NEVERCACHE_KEY = "bc00a185-0d46-4367-9b4d-bd9cc8de71e14506fbd2-913f-485d-b381-e166f567eec7b1c8814f-25cc-4576-af8b-a59a5685f84d"
ALLOWED_HOSTS = ['contratempo.pl', 'www.contratempo.pl', '212.227.106.82', '*.contratempo.pl','212.227.106.82', '127.0.0.1', 'localhost', '127.0.0.1:8000', 'localhost:8000']

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "project.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

CACHE_MIDDLEWARE_SECONDS = 60

CACHE_MIDDLEWARE_KEY_PREFIX = "ct"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
