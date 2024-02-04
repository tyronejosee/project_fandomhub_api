"""Routers for Contents App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.contents.viewsets import (
    UrlViewSet, StudioViewSet, GenreViewSet, SeasonViewSet, RatingViewSet, ContentViewSet
)

router = DefaultRouter()
router.register(r'urls', UrlViewSet, basename='url')
router.register(r'studios', StudioViewSet, basename='studio')
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'seasons', SeasonViewSet, basename='season')
router.register(r'ratings', RatingViewSet, basename='rating')
router.register(r'contents', ContentViewSet, basename='content')


urlpatterns = [
    path('api/v1/', include(router.urls))
]
