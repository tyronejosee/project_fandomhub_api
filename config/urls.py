"""URLs for config project."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    # Admin urls
    path('admin/', admin.site.urls),

    # Drf spectacular urls
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Apps urls
    # path('', include('apps.contents.routers')),
    path('', include('apps.categories.routers')),

    # # Apps urls
    # path('', include('apps.users.routers')),
]


# Debug Config
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Custom attributes for admin
admin.site.site_header = 'Project: Beehive'
admin.site.site_title = 'Beehive'
admin.site.index_title = 'Admin'
