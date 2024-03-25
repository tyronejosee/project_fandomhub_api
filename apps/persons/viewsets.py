"""Viewsets for Persons App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.translation import gettext as _
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema

from apps.utils.mixins import LogicalDeleteMixin
from apps.utils.permissions import IsStaffOrReadOnly
from apps.utils.pagination import MediumSetPagination
from apps.contents.models import Manga
from apps.contents.serializers import MangaListSerializer
from .models import Author
from .serializers import AuthorSerializer
from .schemas import author_schemas


@extend_schema_view(**author_schemas)
class AuthorViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Author instances.
    """
    serializer_class = AuthorSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Author.objects.filter(available=True)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Get Mangas for Author",
        description="Retrieve a list of mangas for author."
    )
    @action(detail=True, methods=["get"], url_path="mangas")
    @method_decorator(cache_page(60 * 60 * 2))
    def manga_list(self, request, pk=None):
        """
        Retrieve a list of mangas for the specified author.
        """
        manga_list = Manga.objects.filter(author=pk)
        paginator = MediumSetPagination()
        result_page = paginator.paginate_queryset(manga_list, request)
        print(result_page)
        if result_page is not None:
            serializer = MangaListSerializer(result_page, many=True).data
            return paginator.get_paginated_response(serializer)
        return Response(
            {"detail": _("There are no mangas for this author.")},
            status=status.HTTP_404_NOT_FOUND
        )
