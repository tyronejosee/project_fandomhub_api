"""Settings for config project (Base)."""

import os
import sys
from datetime import timedelta
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
environ.Env.read_env(".env")

DEBUG = env("DEBUG")

SECRET_KEY = env("SECRET_KEY")

ADMINS = [
    (env("ADMIN_NAME"), env("ADMIN_EMAIL")),
]


ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST")

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")

INTERNAL_IPS = env.list("INTERNAL_IPS")


BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "apps.animes",
    "apps.characters",
    "apps.clubs",
    "apps.genres",
    "apps.home",
    "apps.mangas",
    "apps.news",
    "apps.persons",
    "apps.playlists",
    "apps.profiles",
    "apps.randoms",
    "apps.recommendations",
    "apps.reviews",
    "apps.producers",
    "apps.tops",
    "apps.users",
    "apps.utils",
]

THIRD_APPS = [
    "corsheaders",
    "rest_framework",
    "django_filters",
    "djoser",
    "django_prometheus",
    "import_export",
    "social_django",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "drf_spectacular",
    "drf_spectacular_sidecar",
]

INSTALLED_APPS = BASE_APPS + PROJECT_APPS + THIRD_APPS

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

LANGUAGE_CODE = "en"

LANGUAGES = [
    ("en", "English"),
    ("ja", "Japanese"),
    ("es", "Spanish"),
    ("it", "Italian"),
    ("pt", "Portuguese"),
    ("fr", "French"),
    ("de", "German"),
]

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


if "test" in sys.argv:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("DATABASE_NAME"),
            "USER": env("DATABASE_USER"),
            "PASSWORD": env("DATABASE_PASSWORD"),
            "HOST": "db",
            "PORT": "5432",
        }
    }


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("CACHE_LOCATION"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_CONTENT_LANGUAGE": "en",
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_PAGINATION_CLASS": "apps.utils.pagination.LimitSetPagination",
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "3/second",
        "user": "60/minute",
        "daily": "1000/day",
    },
    "NUM_PROXIES": None,
    "PAGE_SIZE": 25,
    "SEARCH_PARAM": "q",
    "ORDERING_PARAM": "order",
    # "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    # "DEFAULT_VERSION": "v2",
    # "ALLOWED_VERSIONS": ["v1", "v2"],
    # "VERSION_PARAM": "version",
}

AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10080),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESFH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SET_USERNAME_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SOCIAL_AUTH_TOKEN_STRATEGY": "djoser.social.token.jwt.TokenStrategy",
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [
        "http://localhost:8000/google",
        "http://localhost:8000/facebook",
    ],
    "SERIALIZERS": {
        "user_create": "apps.users.serializers.UserSerializer",
        "user": "apps.users.serializers.UserCreateSerializer",
        "current_user": "apps.users.serializers.UserSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
}

AUTH_USER_MODEL = "users.User"

SPECTACULAR_SETTINGS = {
    "TITLE": "FandomHub (API)",
    "VERSION": "v1",
    "DESCRIPTION": (
        "The FandomHub API provides access to data about animes and manga."
        "\nAccess the API documentation at `/docs` or `/redoc`."
    ),
    "LICENSE": {
        "name": env("LICENCE_NAME"),
        "url": env("LICENCE_URL"),
    },
    "CONTACT": {
        "name": env("CONTACT_NAME"),
        "url": env("CONTACT_URL"),
    },
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "TAGS": [
        {
            "name": "schedules",
            "description": "Operations related to schedules",
        },
        {
            "name": "animes",
            "description": "Operations related to animes",
        },
        {
            "name": "mangas",
            "description": "Operations related to mangas",
        },
        {
            "name": "genres",
            "description": "Operations related to genres",
        },
        {
            "name": "themes",
            "description": "Operations related to themes",
        },
        {
            "name": "demographics",
            "description": "Operations related to demographics",
        },
        {
            "name": "seasons",
            "description": "Operations related to seasons",
        },
        {
            "name": "characters",
            "description": "Operations related to characters",
        },
        {
            "name": "persons",
            "description": "Operations related to persons",
        },
        {
            "name": "producers",
            "description": "Operations related to producers",
        },
        {
            "name": "magazines",
            "description": "Operations related to magazines",
        },
        {
            "name": "news",
            "description": "Operations related to news",
        },
        {
            "name": "randoms",
            "description": "Operations related to randoms",
        },
        {
            "name": "recommendations",
            "description": "Operations related to recommendations",
        },
        {
            "name": "tops",
            "description": "Operations related to tops",
        },
        {
            "name": "clubs",
            "description": "Operations related to clubs",
        },
        {
            "name": "animelists",
            "description": "Operations related to animelists",
        },
        {
            "name": "mangalists",
            "description": "Operations related to mangalists",
        },
        {
            "name": "profiles",
            "description": "Operations related to profiles",
        },
        {
            "name": "users",
            "description": "Operations related to users",
        },
        {
            "name": "tokens",
            "description": "Operations related to tokens",
        },
        {
            "name": "socials",
            "description": "Operations related to socials",
        },
    ],
}

LOG_DIR = os.path.join(BASE_DIR, "logs")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_DIR, "general.log"),
            "level": "INFO",
            "formatter": "simple",  # verbose
        },
        # "console": {
        #     "class": "logging.StreamHandler",
        #     "level": "INFO",
        #     "formatter": "simple",
        # },
    },
    "loggers": {
        "": {
            "level": "INFO",
            "handlers": ["file"],  # "console"
            "propagate": True,
        },
    },
    "formatters": {
        "simple": {
            "format": "[{asctime}]    {levelname} - {message}",
            "style": "{",
        },
        "verbose": {
            "format": "[{asctime}]    {levelname} - {name} {module}.py (line {lineno:d}. {message})",
            "style": "{",
        },
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
