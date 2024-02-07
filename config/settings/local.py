"""Settings for config project (Local)."""

from .base import *


DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
#     'http://localhost:8000',
#     'http://127.0.0.1:8000',
#     'http://127.0.0.1:3000',
# ]

# CSRF_TRUSTED_ORIGINS = [
#     'http://localhost:3000',
#     'http://localhost:8000',
#     'http://127.0.0.1:8000',
#     'http://127.0.0.1:3000',
# ]

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
