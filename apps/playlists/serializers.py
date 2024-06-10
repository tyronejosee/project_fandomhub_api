"""Serializers for Playlists App."""

from rest_framework import serializers

from apps.animes.serializers import AnimeMinimalSerializer
from .models import AnimeList, AnimeListItem


class AnimeListReadSerializer(serializers.ModelSerializer):
    """Serializer for AnimeList model (List/retrieve)."""

    class Meta:
        model = AnimeList
        fields = [
            "id",
            "banner",
            "is_public",
            "created_at",
            "updated_at",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["banner"] = representation.get("banner", "") or ""
        return representation


class AnimeListWriteSerializer(serializers.ModelSerializer):
    """Serializer for AnimeList model (Create/update)."""

    class Meta:
        model = AnimeList
        fields = [
            "banner",
            "is_public",
        ]
        extra_kwargs = {
            "banner": {"required": True},
        }


class AnimeListItemReadSerializer(serializers.ModelSerializer):
    """Serializer for AnimeList model (List/retrieve)."""

    anime_id = AnimeMinimalSerializer()
    status = serializers.CharField(source="get_status_display")
    score = serializers.CharField(source="get_score_display")
    priority = serializers.CharField(source="get_priority_display")
    storage = serializers.CharField(source="get_storage_display")

    class Meta:
        model = AnimeListItem
        fields = [
            "id",
            "anime_id",
            "status",
            "episodes_watched",
            "score",
            "start_date",
            "finish_date",
            "tags",
            "priority",
            "storage",
            "times_rewatched",
            "notes",
            "order",
            "is_watched",
            "is_favorite",
            "created_at",
            "updated_at",
        ]


class AnimeListItemWriteSerializer(serializers.ModelSerializer):
    """Serializer for AnimeList model (Create/update)."""

    class Meta:
        model = AnimeListItem
        fields = [
            "anime_id",
            "status",
            "episodes_watched",
            "score",
            "start_date",
            "finish_date",
            "tags",
            "priority",
            "storage",
            "times_rewatched",
            "notes",
            "order",
            "is_watched",
            "is_favorite",
        ]
