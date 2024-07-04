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
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema_view

from apps.utils.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.utils.models import Picture
from apps.utils.serializers import PictureReadSerializer
from apps.users.permissions import IsMember, IsContributor
from apps.characters.models import Character, CharacterManga
from apps.characters.serializers import CharacterMinimalSerializer
from apps.news.models import News
from apps.news.serializers import NewsMinimalSerializer
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer, ReviewWriteSerializer
from apps.reviews.filters import ReviewMinimalFilter
from .models import Magazine, Manga
from .serializers import (
    MagazineReadSerializer,
    MagazineWriteSerializer,
    MangaReadSerializer,
    MangaWriteSerializer,
    MangaMinimalSerializer,
    MangaStatsReadSerializer,
)
from .filters import MagazineFilter, MangaFilter
from .schemas import magazine_schemas, manga_schemas


@extend_schema_view(**magazine_schemas)
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
    filterset_class = MagazineFilter

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
    filterset_class = MangaFilter

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

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="characters",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_characters(self, request, *args, **kwargs):
        """
        Action retrieve characters associated with a manga.

        Endpoints:
        - GET api/v1/mangas/{id}/characters/
        """
        manga = self.get_object()
        relations = CharacterManga.objects.filter(manga_id=manga)
        if not relations.exists():
            return Response(
                {"detail": "No characters found for this manga."},
                status=status.HTTP_404_NOT_FOUND,
            )
        character_ids = relations.values_list("character_id", flat=True)
        characters = Character.objects.filter(id__in=character_ids)
        if not characters.exists():
            return Response(
                {"detail": "No characters found."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = CharacterMinimalSerializer(characters, many=True)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="stats",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_stats(self, request, *args, **kwargs):
        """
        Action retrieve stats associated with a manga.

        Endpoints:
        - GET api/v1/mangas/{id}/stats/
        """
        manga = self.get_object()
        stats = manga.stats  # reverse relationship
        if stats:
            serializer = MangaStatsReadSerializer(stats)
            return Response(serializer.data)
        return Response(
            {"detail": _("No stats found for this manga.")},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="reviews",
    )
    def get_reviews(self, request, *args, **kwargs):
        """
        Action get all reviews for an manga.

        Endpoints:
        - GET /api/v1/mangas/{id}/reviews/
        """
        manga = self.get_object()
        content_type = ContentType.objects.get_for_model(Manga)

        reviews = Review.objects.filter(content_type=content_type, object_id=manga.pk)

        # Apply filter
        filterset = ReviewMinimalFilter(request.GET, queryset=reviews)
        if filterset.is_valid():
            reviews = filterset.qs
        else:
            return Response(filterset.errors, status=status.HTTP_400_BAD_REQUEST)

        if reviews.exists():
            serializer = ReviewReadSerializer(reviews, many=True)
            return Response(serializer.data)

        return Response(
            {"detail": _("No reviews for this manga.")},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsMember],
        url_path="reviews/create",
    )
    def create_review(self, request, *args, **kwargs):
        """
        Action creates a review for an manga.

        Endpoint:
        - POST /api/v1/mangas/{id}/reviews/create/
        """
        manga = self.get_object()
        manga_model = ContentType.objects.get_for_model(Manga)

        if Review.objects.filter(user_id=request.user, object_id=manga.pk).exists():
            return Response(
                {"detail": _("You have already reviewed this manga.")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = ReviewWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user_id=request.user,
                content_type=manga_model,
                object_id=manga.pk,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=True,
        methods=["patch", "delete"],
        permission_classes=[IsMember],
        url_path="reviews/(?P<review_id>[^/.]+)",
    )
    def update_or_delete_review(
        self, request, pk=None, review_id=None, *args, **kwargs
    ):
        """
        Update or delete a review for an manga.

        Endpoint:
        - PATCH /api/v1/mangas/{id}/reviews/{review_id}/
        - DELETE /api/v1/mangas/{id}/reviews/{review_id}/
        """
        manga = self.get_object()
        manga_model = ContentType.objects.get_for_model(Manga)

        review = get_object_or_404(
            Review,
            id=review_id,
            content_type=manga_model,
            object_id=manga.pk,
        )

        message = _("You do not have permission to perform this action.")
        if review.user_id != request.user:
            return Response({"detail": message}, status=status.HTTP_403_FORBIDDEN)

        if request.method == "PATCH":
            serializer = ReviewWriteSerializer(review, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="recommendations",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_recommendations(self, request, *args, **kwargs):
        """
        Action retrieve recommendations associated with a manga.

        Endpoints:
        - GET api/v1/mangas/{id}/recommendations/
        """
        manga = self.get_object()
        similar_manga = (
            Manga.objects.filter(
                genres__in=manga.genres.all(),
                themes__in=manga.themes.all(),
            )
            .exclude(id=manga.id)
            .distinct()[:25]
        )  # TODO: Add manager, add tests
        if similar_manga:
            serializer = MangaMinimalSerializer(similar_manga, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": _("No recommendations found for this manga.")},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="news",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_news(self, request, *args, **kwargs):
        """
        Action retrieve news associated with a manga.

        Endpoints:
        - GET api/v1/mangas/{id}/news/
        """
        manga = self.get_object()
        news = News.objects.get_manga_news(manga)  # TODO: Optimize query 43.5 ms
        if news.exists():
            serializer = NewsMinimalSerializer(news, many=True)
            return Response(serializer.data)
        return Response({"detail": _("No news found for this manga.")})

    # @action(
    #     detail=True,
    #     methods=["get"],
    #     permission_classes=[AllowAny],
    #     url_path="forum",
    # )
    # def get_forum(self, request, pk=None, *args, **kwargs):
    #     pass

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="pictures",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_pictures(self, request, *args, **kwargs):
        """
        Action retrieve pictures associated with a manga.

        Endpoints:
        - GET api/v1/mangas/{id}/pictures/
        """
        manga = self.get_object()
        pictures = Picture.objects.filter(
            content_type__model="manga", object_id=manga.id
        )  # TODO: Add manager
        if pictures.exists():
            serializer = PictureReadSerializer(pictures, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": _("No pictures found for this manga.")},
            status=status.HTTP_404_NOT_FOUND,
        )
