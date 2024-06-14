"""Views for Tops App."""

# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from django.views.decorators.vary import vary_on_headers
from django.utils.translation import gettext as _
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from apps.animes.models import Anime
from apps.animes.serializers import AnimeMinimalSerializer


class TopAnimeView(APIView):
    """
    View lists the 100 most popular animes.

    Endpoints:
    - GET api/v1/top/animes/
    - PARAMS ?type=tv&filter=upcoming&limit=20
    """

    permission_classes = [AllowAny]
    serializer_class = AnimeMinimalSerializer

    # @method_decorator(cache_page(60 * 60 * 2))
    # @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get(self, request, *args, **kwargs):
        # Query params
        type_param = str(request.query_params.get("type"))
        filter_param = str(request.query_params.get("filter"))
        limit = int(request.query_params.get("limit", 50))

        if limit > 100:
            return Response(
                {"detail": _("Limit exceeds maximum allowed value of 100.")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        top_animes = Anime.objects.all()

        if type_param:
            top_animes = top_animes.filter(media_type=type_param)

        if filter_param:
            if filter_param == "airing":
                top_animes = top_animes.filter(status="airing")
            elif filter_param == "upcoming":
                top_animes = top_animes.filter(status="upcoming")
            elif filter_param == "popularity":
                top_animes = top_animes.order_by("-popularity")
            elif filter_param == "favorite":
                top_animes = top_animes.order_by("-favorites")

        top_animes = top_animes[: int(limit)]

        if top_animes.exists():
            serializer = self.serializer_class(top_animes, many=True)
            return Response(serializer.data)
        return Response({"detail": _("Empty list.")}, status=status.HTTP_404_NOT_FOUND)


class TopMangaView(APIView):
    pass


class TopCharacterView(APIView):
    pass


class TopArtistView(APIView):
    pass


class TopAuthorView(APIView):
    pass


class TopReviewView(APIView):
    pass
