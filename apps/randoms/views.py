"""View for Randoms App."""

from random import choice
from django.utils.translation import gettext as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.animes.models import Anime
from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.models import Manga
from apps.mangas.serializers import MangaMinimalSerializer


class RandomContentView(APIView):
    """
    Get a random content (Base).
    """

    def get_queryset(self):
        raise NotImplementedError(_("Subclasses must implement get_queryset method."))

    def get_serializer_class(self):
        raise NotImplementedError(
            _("Subclasses must implement get_serializer_class method.")
        )

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset:
            content = choice(queryset)
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(content)
            return Response(serializer.data)
        return Response(
            {"detail": _("No available content found.")},
            status=status.HTTP_404_NOT_FOUND,
        )


class RandomAnimeView(RandomContentView):
    """
    Get a random anime.

    Endpoints:
    - GET api/v1/random/anime/
    """

    def get_queryset(self):
        return Anime.objects.get_available()

    def get_serializer_class(self):
        return AnimeMinimalSerializer


class RandomMangaView(RandomContentView):
    """
    Get a random manga.

    Endpoints:
    - GET api/v1/random/manga/
    """

    def get_queryset(self):
        return Manga.objects.get_available()

    def get_serializer_class(self):
        return MangaMinimalSerializer


# TODO: Pending implementation
# class RandomcharacterView(RandomContentView):
#     """
#     Get a random people.

#     Endpoints:
#     - GET api/v1/random/character/
#     """

#     def get_queryset(self):
#         return Character.objects.get_available()

#     def get_serializer_class(self):
#         return CharacterReadSerializer


# TODO: Pending implementation
# class RandomPeopleView(RandomContentView):
#     """
#     Get a random people.

#     Endpoints:
#     - GET api/v1/random/people/
#     """

#     def get_queryset(self):
#         return People.objects.get_available()

#     def get_serializer_class(self):
#         return PeopleReadSerializer
