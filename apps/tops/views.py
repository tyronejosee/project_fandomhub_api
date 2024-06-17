"""Views for Tops App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.utils.translation import gettext as _
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from apps.animes.models import Anime
from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.models import Manga
from apps.mangas.serializers import MangaMinimalSerializer
from apps.characters.models import Character
from apps.characters.filters import CharacterFilter
from apps.characters.serializers import CharacterMinimalSerializer
from apps.persons.models import Person
from apps.persons.choices import CategoryChoices
from apps.persons.serializers import PersonMinimalSerializer
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer


class TopAnimeView(APIView):
    """
    View lists the most popular animes.

    Endpoints:
    - GET api/v1/top/animes/
    - PARAMS ?type=tv&filter=upcoming&limit=20
    """

    permission_classes = [AllowAny]
    serializer_class = AnimeMinimalSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get(self, request, *args, **kwargs):
        # Query params
        type_param = request.query_params.get("type")
        filter_param = request.query_params.get("filter")
        limit_param = request.query_params.get("limit", 50)

        if limit_param > 100:
            return Response(
                {"detail": _("Limit exceeds maximum allowed value of 100.")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        top_animes = Anime.objects.filter_by_params(
            type_param, filter_param, limit_param
        )

        if top_animes.exists():
            serializer = self.serializer_class(top_animes, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TopMangaView(APIView):
    """
    View lists the most popular mangas.

    Endpoints:
    - GET api/v1/top/mangas/
    """

    def get(self, request, *args, **kwargs):
        top_mangas = Manga.objects.get_available().order_by("-favorites")
        if top_mangas.exists():
            serializer = MangaMinimalSerializer(top_mangas, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # TODO: Add query params and limit


class TopCharacterView(ListAPIView):
    """
    View lists the most popular characters.

    Endpoints:
    - GET api/v1/top/characters/
    """

    permission_classes = [AllowAny]
    serializer_class = CharacterMinimalSerializer
    search_fields = ["name", "name_kanji" "created_at"]
    search_fields = ["name", "name_kanji"]
    filterset_class = CharacterFilter

    def get_queryset(self):
        return Character.objects.get_available().order_by("-favorites")

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {"detail": "No character found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().list(request, *args, **kwargs)


class TopArtistView(APIView):
    """
    View lists the most popular artists.

    Endpoints:
    - GET api/v1/top/artists/
    """

    def get(self, request, *args, **kwargs):
        top_artists = (
            Person.objects.get_available()
            .filter(category=CategoryChoices.ARTIST)
            .order_by("-favorites")
        )
        if top_artists.exists():
            serializer = PersonMinimalSerializer(top_artists, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # TODO: Add query params and limit


class TopReviewView(APIView):
    """
    View lists the most popular reviews.

    Endpoints:
    - GET api/v1/top/reviews/
    """

    def get(self, request, *args, **kwargs):
        top_reviews = Review.objects.get_available().order_by("-helpful_count")
        if top_reviews.exists():
            serializer = ReviewReadSerializer(top_reviews, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # TODO: Add query params and limit
