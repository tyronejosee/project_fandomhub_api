"""Routers for Persons App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import PersonViewSet


router_v1 = DefaultRouter()
router_v1.register(r"persons", PersonViewSet, basename="person")

urlpatterns = [path("api/v1/", include(router_v1.urls))]
