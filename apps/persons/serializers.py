"""Serializers for Persons App."""

from rest_framework.serializers import ModelSerializer

from .models import Author


class AuthorSerializer(ModelSerializer):
    """Serializer for Author model."""

    class Meta:
        model = Author
        fields = [
            "id",
            "name"
        ]
