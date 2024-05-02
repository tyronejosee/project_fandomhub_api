"""ViewSets for Contents App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema_view, extend_schema

from apps.utils.mixins import LogicalDeleteMixin
from apps.utils.permissions import IsStaffOrReadOnly
from apps.utils.pagination import MediumSetPagination
from apps.reviews.models import ReviewAnime, ReviewManga
from apps.reviews.serializers import (
    ReviewAnimeSerializer, ReviewMangaSerializer)
from .models import Anime, Manga
from .serializers import (
    AnimeSerializer, MangaSerializer, AnimeListSerializer, MangaListSerializer)
from .schemas import anime_schemas, manga_schemas


@extend_schema_view(**anime_schemas)
class AnimeViewSet(LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Anime instances.

    Endpoints:
    - GET /api/v1/animes/
    - POST /api/v1/animes/
    - GET /api/v1/animes/{id}/
    - PUT /api/v1/animes/{id}/
    - PATCH /api/v1/animes/{id}/
    - DELETE /api/v1/animes/{id}/
    """
    serializer_class = AnimeSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name", "studio__name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Anime.objects.get_available()

    def get_serializer_class(self):
        if self.action == "list":
            return AnimeListSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "review_list" or self.action == "review_detail":
            return [IsAuthenticatedOrReadOnly()]
        return super().get_permissions()

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Get Popular Animes",
        description="Retrieve a list of the 50 most popular anime."
    )
    @action(detail=False, methods=["get"], url_path="popular")
    @method_decorator(cache_page(60 * 60 * 2))
    def popular_list(self, request, pk=None):
        """
        Action return a list of the 50 most popular anime.

        Endpoints:
        - GET /api/v1/animes/popular/
        """
        popular_list = Anime.objects.get_popular()[:50]
        if not popular_list:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = AnimeListSerializer(popular_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["GET", "POST"], url_path="reviews")
    def review_list(self, request, pk=None, format=None):
        """
        Action retrieves and creates reviews for an anime

        Endpoints:
        - GET /api/v1/animes/{id}/reviews/
        - POST /api/v1/animes/{id}/reviews/
        """
        anime = self.get_object()

        if request.method == "GET":
            # Get all reviews for the anime
            reviews = ReviewAnime.objects.get_reviews_for_anime(anime)
            if reviews.exists():
                serializer = ReviewAnimeSerializer(reviews, many=True)
                return Response(serializer.data)
            return Response(
                {"detail": "No reviews for this anime."},
                status=status.HTTP_404_NOT_FOUND
            )

        elif request.method == "POST":
            # Create a new review for the anime
            serializer = ReviewAnimeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, anime=anime)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(
        detail=True,
        methods=["GET", "PUT", "DELETE"],
        url_path="reviews/(?P<review_id>[^/.]+)"
    )
    def review_detail(self, request, pk=None, review_id=None, format=None):
        """
        Action retrieves, updates, or deletes a review for an anime.

        Endpoints:
        - GET /api/v1/animes/{id}/reviews/{id}/
        - PUT /api/v1/animes/{id}/reviews/{id}/
        - DELETE /api/v1/animes/{id}/reviews/{id}/
        """
        anime = self.get_object()
        review = get_object_or_404(ReviewAnime, id=review_id, anime=anime)

        if request.method == "GET":
            # Retrieve the review associated with the anime
            serializer = ReviewAnimeSerializer(review)
            return Response(serializer.data)

        elif request.method == "PUT":
            # Update the review associated with the anime
            serializer = ReviewAnimeSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        elif request.method == "DELETE":
            # Delete the review associated with the anime
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema_view(**manga_schemas)
class MangaViewSet(LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Manga instances.

    Endpoints:
    - GET /api/v1/mangas/
    - POST /api/v1/mangas/
    - GET /api/v1/mangas/{id}/
    - PUT /api/v1/mangas/{id}/
    - PATCH /api/v1/mangas/{id}/
    - DELETE /api/v1/mangas/{id}/
    """
    serializer_class = MangaSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name",]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Manga.objects.get_available()

    def get_serializer_class(self):
        if self.action == "review_list" or self.action == "review_detail":
            return MangaListSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "reviews":
            return [IsAuthenticatedOrReadOnly()]
        return super().get_permissions()

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Get Popular Mangas",
        description="Retrieve a list of the 50 most popular mangas."
    )
    @action(detail=False, methods=["get"], url_path="popular")
    @method_decorator(cache_page(60 * 60 * 2))
    def popular_list(self, request, pk=None):
        """
        Action return a list of the 50 most popular mangas.

        Endpoints:
        - GET /api/v1/mangas/popular/
        """
        popular_list = Manga.objects.get_popular()[:50]
        paginator = MediumSetPagination()
        result_page = paginator.paginate_queryset(popular_list, request)
        if result_page is not None:
            serializer = MangaListSerializer(result_page, many=True).data
            return paginator.get_paginated_response(serializer)
        return Response(
            {"detail": _("There are no popular mangas available.")},
            status=status.HTTP_204_NO_CONTENT
        )

    @extend_schema(
        summary="Get all review for a manga",
        description="Pending description.",
        responses={
            200: ReviewMangaSerializer(many=True),
            404: None
        },
        methods=["GET"],
    )
    @extend_schema(
        summary="Create review for a manga",
        description="Pending description.",
        responses={
            201: ReviewMangaSerializer(),
            404: None
        },
        methods=["POST"],
    )
    @action(detail=True, methods=["GET", "POST"], url_path="reviews")
    def review_list(self, request, pk=None, format=None):
        """
        Action retrieves and creates reviews for an manga.

        Endpoints:
        - GET /api/v1/mangas/{id}/reviews/
        - POST /api/v1/mangas/{id}/reviews/
        """
        manga = self.get_object()

        if request.method == "GET":
            # Get all reviews for the manga
            reviews = ReviewManga.objects.get_reviews_for_manga(manga)
            if reviews.exists():
                serializer = ReviewMangaSerializer(reviews, many=True)
                return Response(serializer.data)
            return Response(
                {"detail": "No reviews for this anime."},
                status=status.HTTP_404_NOT_FOUND
            )

        elif request.method == "POST":
            # Create a new review for the manga
            serializer = ReviewMangaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, manga=manga)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(
        detail=True,
        methods=["GET", "PUT", "DELETE"],
        url_path="reviews/(?P<review_id>[^/.]+)"
    )
    def review_detail(self, request, pk=None, review_id=None, format=None):
        """
        Action retrieves, updates, or deletes a review for an manga.

        Endpoints:
        - GET /api/v1/mangas/{id}/reviews/{id}/
        - PUT /api/v1/mangas/{id}/reviews/{id}/
        - DELETE /api/v1/mangas/{id}/reviews/{id}/
        """
        manga = self.get_object()
        review = get_object_or_404(ReviewManga, id=review_id, manga=manga)

        if request.method == "GET":
            # Retrieve the review associated with the manga
            serializer = ReviewMangaSerializer(review)
            return Response(serializer.data)

        elif request.method == "PUT":
            # Update the review associated with the manga
            serializer = ReviewMangaSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        elif request.method == "DELETE":
            # Delete the review associated with the manga
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
