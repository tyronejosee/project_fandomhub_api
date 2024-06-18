"""Serializers for News App."""

from rest_framework import serializers

from apps.users.serializers import UserMinimumSerializer
from .models import News


class NewsReadSerializer(serializers.ModelSerializer):
    """Serializer for News model (List/retrieve)."""

    author_id = serializers.SerializerMethodField()
    tag = serializers.CharField(source="get_tag_display")

    class Meta:
        model = News
        fields = [
            "id",
            "author_id",
            "name",
            "description",
            "content",
            "image",
            "source",
            "tag",
            "anime_relations",
            "manga_relations",
            "created_at",
            "updated_at",
        ]

    def get_author(self, obj):
        return obj.author_id.username

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["image"] = representation.get("image", "") or ""
        return representation


class NewsWriteSerializer(serializers.ModelSerializer):
    """Serializer for News model (Create/update)."""

    class Meta:
        model = News
        fields = [
            "name",
            "description",
            "content",
            "image",
            "source",
            "tag",
            "anime_relations",
            "manga_relations",
        ]


class NewsMinimalSerializer(serializers.ModelSerializer):
    """Serializer for News model (Minimal)."""

    tag = serializers.CharField(source="get_tag_display")
    author_id = UserMinimumSerializer()

    class Meta:
        model = News
        fields = [
            "id",
            "name",
            "description",
            "image",
            "tag",
            "author_id",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["image"] = representation.get("image", "") or ""
        return representation
