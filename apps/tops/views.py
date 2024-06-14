"""Views for Tops App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.utils.translation import gettext as _
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from apps.utils.pagination import LargeSetPagination
from apps.animes.models import Anime
from apps.animes.serializers import AnimeMinimalSerializer


class TopAnimeView(APIView):
    """
    View lists the 100 most popular animes.

    Endpoints:
    - GET api/v1/top/animes/
    """

    permission_classes = [AllowAny]
    serializer_class = AnimeMinimalSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get(self, request, *args, **kwargs):
        top_animes = Anime.objects.order_by("favorites")[:100]
        # TODO: Replace with the popularity field after implementation

        if not top_animes.exists():
            return Response(
                {"detail": _("Empty list.")}, status=status.HTTP_404_NOT_FOUND
            )

        paginator = LargeSetPagination()
        page = paginator.paginate_queryset(top_animes, request)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = self.serializer_class(top_animes, many=True)
        return Response(serializer.data)
