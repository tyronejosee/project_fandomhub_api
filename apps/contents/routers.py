"""Routers for Contents App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.contents.viewsets import (
    UrlViewSet, StudioViewSet, GenreViewSet, PremieredViewSet, RatingViewSet, ContentViewSet
)

router = DefaultRouter()
router.register(r'urls', UrlViewSet, basename='url')
router.register(r'studios', StudioViewSet, basename='studio')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'premiereds', PremieredViewSet, basename='premiered')
router.register(r'ratings', RatingViewSet, basename='rating')
router.register(r'contents', ContentViewSet, basename='content')


urlpatterns = [
    path('', include(router.urls))
]
