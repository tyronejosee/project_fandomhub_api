"""Serializers for News App."""

from rest_framework import serializers

from .models import New


class NewListSerializer(serializers.ModelSerializer):
    """Serializer for New model (List only).."""
    tag = serializers.CharField(source="get_tag_display")
    author = serializers.SerializerMethodField()

    class Meta:
        """Meta definition for NewListSerializer."""
        model = New
        fields = [
            "id", "title", "description", "image", "tag", "author"
        ]
        read_only_fields = ["author"]

    def get_author(self, obj) -> str:
        return obj.author.username


class NewSerializer(serializers.ModelSerializer):
    """Serializer for New model."""
    tag = serializers.CharField(source="get_tag_display")

    class Meta:
        """Meta definition for NewSerializer."""
        model = New
        fields = [
            "id", "title", "description", "content", "image",
            "source", "tag", "author", "created_at", "updated_at"
        ]
