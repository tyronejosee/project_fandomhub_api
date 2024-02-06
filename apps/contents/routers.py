"""Routers for Contents App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.contents.viewsets import (
    UrlViewSet, StudioViewSet, GenreViewSet, SeasonViewSet, RatingViewSet,
    DemographicViewSet, AuthorViewSet, AnimeViewSet, MangaViewSet
)

router = DefaultRouter()

# Entity
router.register(r'animes', AnimeViewSet, basename='anime')
router.register(r'mangas', MangaViewSet, basename='manga')

# Catalog
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'studios', StudioViewSet, basename='studio')
router.register(r'seasons', SeasonViewSet, basename='season')
router.register(r'ratings', RatingViewSet, basename='rating')
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'demographics', DemographicViewSet, basename='demographic')

# Association
router.register(r'urls', UrlViewSet, basename='url')

urlpatterns = [
    path('api/v1/', include(router.urls))
]
