"""Views for Recommendations App."""

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.utils.mixins import ListCacheMixin
from apps.animes.models import Anime
from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.models import Manga
from apps.mangas.serializers import MangaMinimalSerializer


class AnimeRecommendationView(ListCacheMixin, ListAPIView):
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


class MangaRecommendationView(ListCacheMixin, ListAPIView):
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
