"""View for Randoms App."""

from random import choice
from django.utils.translation import gettext as _
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.contents.models import Anime
from apps.contents.serializers import AnimeMinimalSerializer


class RandomAnimeView(APIView):
    """
    Get a random anime.

    Endpoints:
    - GET api/v1/random/anime/
    """

    def get(self, request, *args, **kwargs):
        anime = choice(Anime.objects.get_available())  # TODO: Add custom manager
        if anime:
            serializer = AnimeMinimalSerializer(anime)
            return Response(serializer.data)
        return Response(
            {"details": _("No available animes found.")},
            status=status.HTTP_404_NOT_FOUND,
        )
