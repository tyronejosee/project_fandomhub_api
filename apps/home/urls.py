"""URLs for Home App."""

from django.urls import path

from .views import HomePageView


urlpatterns = [
    path(
        "api/v1/home/",
        HomePageView.as_view(),
    )
]
