"""Settings for config project (Testing)."""

import tempfile

from .base import *
from .base import BASE_DIR


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

TEMP_MEDIA = tempfile.TemporaryDirectory()

MEDIA_URL = "/media/"
MEDIA_ROOT = TEMP_MEDIA.name

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}
