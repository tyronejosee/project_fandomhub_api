"""Routers for Producers App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import ProducerViewSet


router_v1 = DefaultRouter()
router_v1.register(r"producers", ProducerViewSet, basename="producer")

urlpatterns = [path("api/v1/", include(router_v1.urls))]
