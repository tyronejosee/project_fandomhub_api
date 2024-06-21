"""ViewSets for Animes App."""

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
from apps.utils.models import Picture, Video
from apps.utils.serializers import PictureReadSerializer, VideoReadSerializer
from apps.users.permissions import IsMember, IsContributor
from apps.users.choices import RoleChoices
from apps.characters.models import Character, CharacterAnime
from apps.characters.serializers import CharacterMinimalSerializer
from apps.persons.models import Person, StaffAnime
from apps.persons.serializers import StaffMinimalSerializer
from apps.news.models import News
from apps.news.serializers import NewsMinimalSerializer
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer, ReviewWriteSerializer
from apps.reviews.filters import ReviewMinimalFilter
from .models import Anime
from .serializers import (
    AnimeReadSerializer,
    AnimeWriteSerializer,
    AnimeMinimalSerializer,
    AnimeStatsReadSerializer,
)
from .filters import AnimeFilter
from .schemas import anime_schemas


@extend_schema_view(**anime_schemas)
class AnimeViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
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

    permission_classes = [IsContributor]
    serializer_class = AnimeWriteSerializer
    search_fields = ["name", "studio_id__name"]
    ordering_fields = ["name"]
    filterset_class = AnimeFilter
    # lookup_field = "slug"
    # lookup_url_kwarg = "anime_id"

    def get_queryset(self):
        return Anime.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return AnimeMinimalSerializer
        elif self.action == "retrieve":
            return AnimeReadSerializer
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
        Action retrieve characters associated with a anime.

        Endpoints:
        - GET api/v1/animes/{id}/characters/
        """
        anime = self.get_object()
        relations = CharacterAnime.objects.filter(anime_id=anime)
        if not relations.exists():
            return Response(
                {"detail": "No characters found for this anime."},
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

    # @action(
    #     detail=True,
    #     methods=["get"],
    #     permission_classes=[AllowAny],
    #     url_path="episodes",
    # )
    # def get_episodes(self, request, pk=None, *args, **kwargs):
    #     pass

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="staff",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_staff(self, request, *args, **kwargs):
        """
        Action retrieve staff associated with a anime.

        Endpoints:
        - GET api/v1/animes/{id}/characters/
        """
        anime = self.get_object()
        relations = StaffAnime.objects.filter(anime_id=anime)
        if not relations.exists():
            return Response(
                {"detail": "No staff found for this anime."},
                status=status.HTTP_404_NOT_FOUND,
            )
        staff_ids = relations.values_list("person_id", flat=True)
        staff = Person.objects.filter(id__in=staff_ids)
        if not staff.exists():
            return Response(
                {"detail": "No staff found."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = StaffMinimalSerializer(staff, many=True)
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
        Action retrieve stats associated with a anime.

        Endpoints:
        - GET api/v1/animes/{id}/stats/
        """
        anime = self.get_object()
        # stats = AnimeStats.objects.get(anime_id=anime.pk)
        stats = anime.stats  # reverse relationship
        if stats:
            serializer = AnimeStatsReadSerializer(stats)
            return Response(serializer.data)
        return Response(
            {"detail": _("No stats found for this anime.")},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=True,
        methods=["get", "post"],
        permission_classes=[IsMember],
        url_path="reviews",
    )
    def get_reviews(self, request, *args, **kwargs):
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
        methods=["get", "patch", "delete"],
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
        Action retrieve recommendations associated with a anime.

        Endpoints:
        - GET api/v1/animes/{id}/recommendations/
        """
        anime = self.get_object()
        similar_anime = (
            Anime.objects.filter(
                genres__in=anime.genres.all(),
                themes__in=anime.themes.all(),
            )
            .exclude(id=anime.id)
            .distinct()[:25]
        )  # TODO: Add manager, add tests
        if similar_anime:
            serializer = AnimeMinimalSerializer(similar_anime, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": _("No recommendations found for this anime.")},
            status=status.HTTP_404_NOT_FOUND,
        )

    # @action(
    #     detail=True,
    #     methods=["get"],
    #     permission_classes=[AllowAny],
    #     url_path="interest-stacks",
    # )
    # def get_interest_stacks(self, request, pk=None, *args, **kwargs):
    #     pass

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="news",
    )
    def get_news(self, request, *args, **kwargs):
        """
        Action retrieve news associated with a anime.

        Endpoints:
        - GET api/v1/animes/{id}/news/
        """
        anime = self.get_object()
        news = News.objects.get_anime_news(anime)  # TODO: Optimize query 43.5 ms
        if news.exists():
            serializer = NewsMinimalSerializer(news, many=True)
            return Response(serializer.data)
        return Response({"detail": _("No news found for this anime.")})

    # @action(
    #     detail=True,
    #     methods=["get"],
    #     permission_classes=[AllowAny],
    #     url_path="forum",
    # )
    # def get_forum(self, request, pk=None, *args, **kwargs):
    #     pass

    # @action(
    #     detail=True,
    #     methods=["get"],
    #     permission_classes=[AllowAny],
    #     url_path="clubs",
    # )
    # def get_clubs(self, request, pk=None, *args, **kwargs):
    #     pass

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="videos",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_videos(self, request, *args, **kwargs):
        """
        Action retrieve videos associated with a anime.

        Endpoints:
        - GET api/v1/animes/{id}/videos/
        """
        anime = self.get_object()
        videos = Video.objects.filter(
            content_type__model="anime", object_id=anime.id
        )  # TODO: Add manager
        if videos.exists():
            serializer = VideoReadSerializer(videos, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": _("No videos found for this anime.")},
            status=status.HTTP_404_NOT_FOUND,
        )

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
        Action retrieve pictures associated with a anime.

        Endpoints:
        - GET api/v1/animes/{id}/pictures/
        """
        anime = self.get_object()
        pictures = Picture.objects.filter(
            content_type__model="anime", object_id=anime.id
        )  # TODO: Add manager
        if pictures.exists():
            serializer = PictureReadSerializer(pictures, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": _("No pictures found for this anime.")},
            status=status.HTTP_404_NOT_FOUND,
        )
