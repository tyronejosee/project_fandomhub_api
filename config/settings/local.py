"""Settings for config project (Local)."""

from .base import *


CORS_ORIGIN_ALLOW_ALL = True


MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "apps.utils.middlewares.RequestLoggingMiddleware",
    # "apps.utils.middlewares.CensorshipMiddleware"
]

# APPEND_SLASH = False

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
