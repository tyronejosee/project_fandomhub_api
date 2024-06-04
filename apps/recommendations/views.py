"""Views for Recommendations App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.animes.models import Anime
from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.models import Manga
from apps.mangas.serializers import MangaMinimalSerializer


class AnimeRecommendationView(ListAPIView):
    """
    View for retrieving recommended anime.

    Endpoints:
    - GET /api/v1/recomendations/anime/
    """

    permission_classes = [AllowAny]
    serializer_class = AnimeMinimalSerializer
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_queryset(self):
        return Anime.objects.get_recommendations()

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class MangaRecommendationView(ListAPIView):
    """
    View for retrieving recommended manga.

    Endpoints:
    - GET /api/v1/recomendations/manga/
    """

    permission_classes = [AllowAny]
    serializer_class = MangaMinimalSerializer
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_queryset(self):
        return Manga.objects.get_recommendations()

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
