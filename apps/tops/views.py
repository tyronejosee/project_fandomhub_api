"""Views for Tops App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.utils.translation import gettext as _
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from apps.animes.models import Anime
from apps.animes.filters import AnimeMinimalFilter
from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.models import Manga
from apps.mangas.filters import MangaMinimalFilter
from apps.mangas.serializers import MangaMinimalSerializer
from apps.characters.models import Character
from apps.characters.filters import CharacterFilter
from apps.characters.serializers import CharacterMinimalSerializer
from apps.persons.models import Person
from apps.persons.choices import CategoryChoices
from apps.persons.serializers import PersonMinimalSerializer
from apps.reviews.models import Review
from apps.reviews.filters import ReviewFilter
from apps.reviews.serializers import ReviewReadSerializer


class TopAnimeView(ListAPIView):
    """
    View lists the most popular animes.

    Endpoints:
    - GET api/v1/top/animes/
    """

    permission_classes = [AllowAny]
    serializer_class = AnimeMinimalSerializer
    search_fields = ["name", "name_jpn", "name_rom"]
    filterset_class = AnimeMinimalFilter

    def get_queryset(self):
        return Anime.objects.get_available().order_by("-favorites")

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {"detail": _("No anime found.")},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().list(request, *args, **kwargs)


class TopMangaView(ListAPIView):
    """
    View lists the most popular mangas.

    Endpoints:
    - GET api/v1/top/mangas/
    """

    permission_classes = [AllowAny]
    serializer_class = MangaMinimalSerializer
    search_fields = ["name", "name_jpn", "name_rom"]
    filterset_class = MangaMinimalFilter

    def get_queryset(self):
        return Manga.objects.get_available().order_by("-favorites")

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {"detail": _("No manga found.")},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().list(request, *args, **kwargs)


class TopCharacterView(ListAPIView):
    """
    View lists the most popular characters.

    Endpoints:
    - GET api/v1/top/characters/
    """

    permission_classes = [AllowAny]
    serializer_class = CharacterMinimalSerializer
    search_fields = ["name", "name_kanji"]
    filterset_class = CharacterFilter

    def get_queryset(self):
        return Character.objects.get_available().order_by("-favorites")

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {"detail": _("No character found.")},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().list(request, *args, **kwargs)


class TopArtistView(ListAPIView):
    """
    View lists the most popular artists.

    Endpoints:
    - GET api/v1/top/artists/
    """

    permission_classes = [AllowAny]
    serializer_class = PersonMinimalSerializer
    search_fields = ["name", "given_name", "family_name"]

    def get_queryset(self):
        return (
            Person.objects.get_available()
            .filter(category=CategoryChoices.ARTIST)
            .order_by("-favorites")
        )

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {"detail": _("No artists found.")},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().list(request, *args, **kwargs)


class TopReviewView(ListAPIView):
    """
    View lists the most popular reviews.

    Endpoints:
    - GET api/v1/top/reviews/
    """

    permission_classes = [AllowAny]
    serializer_class = ReviewReadSerializer
    search_fields = ["user__username", "name_kanji"]
    filterset_class = ReviewFilter

    def get_queryset(self):
        return Review.objects.get_available().order_by("-helpful_count")

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {"detail": _("No reviews found.")},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().list(request, *args, **kwargs)
