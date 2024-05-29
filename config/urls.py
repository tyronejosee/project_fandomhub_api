"""URLs for config project."""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    # Temp urls
    path(
        "",
        RedirectView.as_view(pattern_name="swagger"),
    ),
    # Admin urls
    path(
        "admin/",
        admin.site.urls,
    ),
    # Schemas urls
    path(
        "api/schema/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Apps urls (Routers)
    path("", include("apps.contents.routers")),
    path("", include("apps.categories.routers")),
    path("", include("apps.persons.routers")),
    path("", include("apps.users.routers")),
    path("", include("apps.profiles.routers")),
    path("", include("apps.clubs.routers")),
    path("", include("apps.playlists.routers")),
    path("", include("apps.news.routers")),
    # Apps urls (URLs)
    path("", include("apps.randoms.urls")),
]


# Debug config
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# AdminSite props.
admin.site.site_header = "FandomHub"
admin.site.site_title = "FandomHub"
admin.site.index_title = "Admin"
