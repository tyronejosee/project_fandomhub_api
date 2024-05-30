"""Serializers for Persons App."""

from rest_framework.serializers import ModelSerializer

from .models import Person


class PersonSerializer(ModelSerializer):
    """Serializer for Person model."""

    class Meta:
        model = Person
        fields = [
            "id",
            "name",
        ]
