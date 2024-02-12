"""Routers for Contents App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.contents.viewsets import AnimeViewSet, MangaViewSet


router = DefaultRouter()
router.register(r'animes', AnimeViewSet, basename='anime')
router.register(r'mangas', MangaViewSet, basename='manga')


urlpatterns = [
    path('api/v1/', include(router.urls))
]
