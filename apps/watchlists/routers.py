"""Routers for Watchlists App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.watchlists.viewsets import AnimeWatchlistViewSet, MangaWatchlistViewSet


router_v1 = DefaultRouter()
router_v1.register(r'anime_watchlists', AnimeWatchlistViewSet, basename='anime_watchlist')
router_v1.register(r'manga_watchlists', MangaWatchlistViewSet, basename='manga_watchlist')


urlpatterns = [
    path('api/v1/', include(router_v1.urls))
]
