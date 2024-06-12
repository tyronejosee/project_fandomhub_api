"""ViewSets for Mangas App."""

from django.contrib.contenttypes.models import ContentType
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter

from apps.utils.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.utils.pagination import MediumSetPagination
from apps.users.permissions import IsContributor
from apps.users.choices import RoleChoices
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer, ReviewWriteSerializer
from .models import Magazine, Manga
from .serializers import (
    MagazineReadSerializer,
    MagazineWriteSerializer,
    MangaReadSerializer,
    MangaWriteSerializer,
    MangaMinimalSerializer,
)
from .schemas import manga_schemas


class MagazineViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Magazine instances.

    Endpoints:
    - GET /api/v1/magazines/
    - POST /api/v1/magazines/
    - GET /api/v1/magazines/{id}/
    - PUT /api/v1/magazines/{id}/
    - PATCH /api/v1/magazines/{id}/
    - DELETE /api/v1/magazines/{id}/
    """

    permission_classes = [IsContributor]
    serializer_class = MagazineWriteSerializer
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_queryset(self):
        return Magazine.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return MagazineReadSerializer
        return super().get_serializer_class()


@extend_schema_view(**manga_schemas)
class MangaViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
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

    permission_classes = [IsContributor]
    serializer_class = MangaWriteSerializer
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_queryset(self):
        return Manga.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return MangaMinimalSerializer
        elif self.action == "retrieve":
            return MangaReadSerializer
        return super().get_serializer_class()

    @extend_schema(
        summary="Get Popular Mangas",
        description="Retrieve a list of the 50 most popular mangas.",
    )
    @action(detail=False, methods=["get"], url_path="popular")
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
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
            serializer = MangaMinimalSerializer(result_page, many=True).data
            return paginator.get_paginated_response(serializer)

        return Response(
            {"detail": _("There are no popular mangas available.")},
            status=status.HTTP_204_NO_CONTENT,
        )

    # @extend_schema(
    #     summary="Get all review for a manga",
    #     description="Pending description.",
    #     responses={
    #         200: ReviewReadSerializer(many=True),
    #         404: None
    #     },
    #     methods=["GET"],
    # )
    # @extend_schema(
    #     summary="Create review for a manga",
    #     description="Pending description.",
    #     responses={
    #         201: ReviewReadSerializer(),
    #         404: None
    #     },
    #     methods=["POST"],
    # )
    @action(
        detail=True,
        methods=["GET", "POST"],
        permission_classes=[IsAuthenticatedOrReadOnly],
        url_path="reviews",
    )
    def review_list(self, request, *args, **kwargs):
        """
        Action retrieves and creates reviews for an manga.

        Endpoints:
        - GET /api/v1/mangas/{id}/reviews/
        - POST /api/v1/mangas/{id}/reviews/
        """

        if request.method == "GET":
            # Get all reviews for manga
            manga = self.get_object()
            content_type = ContentType.objects.get_for_model(Manga)

            reviews = Review.objects.filter(
                content_type=content_type, object_id=manga.pk
            )
            if reviews.exists():
                serializer = ReviewReadSerializer(reviews, many=True)
                return Response(serializer.data)

            return Response(
                {"detail": _("No reviews for this manga.")},
                status=status.HTTP_404_NOT_FOUND,
            )

        elif request.method == "POST":
            # Create a review for manga
            if not request.user.role == RoleChoices.MEMBER:
                return Response(
                    {"detail": _("You do not have permission to create reviews.")},
                    status=status.HTTP_403_FORBIDDEN,
                )
            serializer = ReviewWriteSerializer(data=request.data)
            if serializer.is_valid():
                manga = self.get_object()
                content_type = ContentType.objects.get_for_model(Manga)
                serializer.save(
                    user=request.user,
                    content_type=content_type,
                    object_id=manga.pk,
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[OpenApiParameter("review_id", str, OpenApiParameter.PATH)]
    )
    @action(
        detail=True,
        methods=["GET", "PATCH", "DELETE"],
        permission_classes=[IsAuthenticatedOrReadOnly],
        url_path="reviews/(?P<review_id>[^/.]+)",
    )
    def review_detail(self, request, pk=None, review_id=None, *args, **kwargs):
        """
        Action retrieves, updates, or deletes a review for an manga.

        Endpoints:
        - GET /api/v1/mangas/{id}/reviews/{id}/
        - PUT /api/v1/mangas/{id}/reviews/{id}/
        - DELETE /api/v1/mangas/{id}/reviews/{id}/
        """
        manga = self.get_object()
        content_type = ContentType.objects.get_for_model(Manga)
        review = get_object_or_404(
            Review, id=review_id, content_type=content_type, object_id=manga.pk
        )
        message = _("You do not have permission to perform this action.")

        if request.method == "GET":
            # Retrieve the review associated with the manga
            serializer = ReviewReadSerializer(review)
            return Response(serializer.data)

        elif request.method == "PATCH":
            # Update the review associated with the manga
            if review.user != request.user:
                return Response({"detail": message}, status=status.HTTP_403_FORBIDDEN)
            serializer = ReviewWriteSerializer(review, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            # Delete the review associated with the manga
            if review.user != request.user:
                return Response({"detail": message}, status=status.HTTP_403_FORBIDDEN)
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
