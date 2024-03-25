"""Routers for Persons App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import AuthorViewSet


router_v1 = DefaultRouter()
router_v1.register(r"authors", AuthorViewSet, basename="author")

urlpatterns = [
    path("api/v1/", include(router_v1.urls))
]
