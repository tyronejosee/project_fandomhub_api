"""Views for Recommendations App."""

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema_view

from apps.utils.mixins import ListCacheMixin
from apps.animes.models import Anime
from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.models import Manga
from apps.mangas.serializers import MangaMinimalSerializer
from .schemas import anime_recommendation_schemas, manga_recommendation_schemas


@extend_schema_view(**anime_recommendation_schemas)
class AnimeRecommendationView(ListCacheMixin, ListAPIView):
    """
    View for retrieving recommended anime.

    Endpoints:
    - GET /api/v1/recommendations/anime/
    """

    permission_classes = [AllowAny]
    serializer_class = AnimeMinimalSerializer
    search_fields = ["name"]

    def get_queryset(self):
        return Anime.objects.get_recommendations()


@extend_schema_view(**manga_recommendation_schemas)
class MangaRecommendationView(ListCacheMixin, ListAPIView):
    """
    View for retrieving recommended manga.

    Endpoints:
    - GET /api/v1/recommendations/manga/
    """

    permission_classes = [AllowAny]
    serializer_class = MangaMinimalSerializer
    search_fields = ["name"]

    def get_queryset(self):
        return Manga.objects.get_recommendations()
