"""ViewSets for Animes App."""

from django.contrib.contenttypes.models import ContentType
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter

from apps.utils.mixins import LogicalDeleteMixin
from apps.users.permissions import IsMember, IsContributor
from apps.users.choices import RoleChoices
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer, ReviewWriteSerializer
from .models import Anime
from .serializers import (
    AnimeReadSerializer,
    AnimeWriteSerializer,
    AnimeMinimalSerializer,
)
from .schemas import anime_schemas


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

    serializer_class = AnimeWriteSerializer
    search_fields = ["name", "studio__name"]
    ordering_fields = ["name"]

    def get_queryset(self):
        return Anime.objects.get_available()

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsContributor()]
        else:
            return [AllowAny()]

    def get_serializer_class(self):
        if self.action == "list":
            return AnimeMinimalSerializer
        elif self.action == "retrieve":
            return AnimeReadSerializer
        return super().get_serializer_class()

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Get Popular Animes",
        description="Retrieve a list of the 50 most popular anime.",
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
        serializer = AnimeMinimalSerializer(popular_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=["GET", "POST"],
        permission_classes=[IsMember],
        url_path="reviews",
    )
    def review_list(self, request, *args, **kwargs):
        """
        Action retrieves and creates reviews for an anime.

        Endpoints:
        - GET /api/v1/animes/{id}/reviews/
        - POST /api/v1/animes/{id}/reviews/
        """

        if request.method == "GET":
            # Get all reviews for anime
            anime = self.get_object()
            content_type = ContentType.objects.get_for_model(Anime)

            reviews = Review.objects.filter(
                content_type=content_type, object_id=anime.pk
            )
            if reviews.exists():
                serializer = ReviewReadSerializer(reviews, many=True)
                return Response(serializer.data)

            return Response(
                {"detail": _("No reviews for this anime.")},
                status=status.HTTP_404_NOT_FOUND,
            )

        elif request.method == "POST":
            # Create a review for anime
            if not request.user.role == RoleChoices.MEMBER:
                return Response(
                    {"detail": _("You do not have permission to create reviews.")},
                    status=status.HTTP_403_FORBIDDEN,
                )
            serializer = ReviewWriteSerializer(data=request.data)
            if serializer.is_valid():
                anime = self.get_object()
                anime_model = ContentType.objects.get_for_model(Anime)
                serializer.save(
                    user=request.user,
                    content_type=anime_model,
                    object_id=anime.pk,
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
        Action retrieves, updates, or deletes a review for an anime.

        Endpoints:
        - GET /api/v1/animes/{id}/reviews/{id}/
        - PUT /api/v1/animes/{id}/reviews/{id}/
        - DELETE /api/v1/animes/{id}/reviews/{id}/
        """
        anime = self.get_object()
        anime_model = ContentType.objects.get_for_model(Anime)
        review = get_object_or_404(
            Review,
            id=review_id,
            content_type=anime_model,
            object_id=anime.pk,
        )
        message = _("You do not have permission to perform this action.")

        if request.method == "GET":
            # Retrieve the review associated with the anime
            serializer = ReviewReadSerializer(review)
            return Response(serializer.data)

        elif request.method == "PATCH":
            # Update the review associated with the anime
            if review.user != request.user:
                return Response({"detail": message}, status=status.HTTP_403_FORBIDDEN)
            serializer = ReviewWriteSerializer(review, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            # Delete the review associated with the anime
            if review.user != request.user:
                return Response({"detail": message}, status=status.HTTP_403_FORBIDDEN)
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
