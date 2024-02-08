"""URLs for config project."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
      title="Project: Beehive API",
      default_version='v1',
      description="The Beehive API provides access to data about beehives, bees, and more. Search for information, get specific details, and stay updated on the latest developments in your beekeeping activities.",
      terms_of_service="https://github.com/tyronejosee/project_beehive_api/blob/main/LICENSE",
      contact=openapi.Contact(email="alt.tyronejose@gmail.com"),
      license=openapi.License(name="Apache License 2.0"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # Admin urls
    path('admin/', admin.site.urls),

    # Django-yasg urls
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Apps urls
    path('', include('apps.contents.routers')),
    path('', include('apps.categories.routers')),

    # Apps urls
    path('', include('apps.users.routers')),
]


# Debug Config
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Custom attributes for admin
admin.site.site_header = 'Project: Beehive'
admin.site.site_title = 'Beehive'
admin.site.index_title = 'Admin'
