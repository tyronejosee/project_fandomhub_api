"""URLs for Project."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.contents.routers')),
]

# Debug Config
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Custom attributes for admin
admin.site.site_header = 'Project: Beehive'
admin.site.site_title = 'Beehive'
admin.site.index_title = 'Admin'
