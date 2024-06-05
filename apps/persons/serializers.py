"""Serializers for Persons App."""

from rest_framework import serializers

from .models import Person


class PersonReadSerializer(serializers.ModelSerializer):
    """Serializer for Person model (List/retrieve)."""

    language = serializers.CharField(source="get_language_display")
    category = serializers.CharField(source="get_category_display")

    class Meta:
        model = Person
        fields = [
            "id",
            "name",
            "slug",
            "given_name",
            "family_name",
            "image",
            "alternate_names",
            "birthday",
            "about",
            "website",
            "language",
            "category",
            "favorites",
            "created_at",
            "updated_at",
        ]


class PersonWriteSerializer(serializers.ModelSerializer):
    """Serializer for Person model (Create/update)."""

    class Meta:
        model = Person
        fields = [
            "name",
            "given_name",
            "family_name",
            "image",
            "alternate_names",
            "birthday",
            "about",
            "website",
            "language",
            "category",
        ]
        extra_kwargs = {
            "image": {"required": True},
        }


class PersonMinimalSerializer(serializers.ModelSerializer):
    """Serializer for Person model (Minimal)."""

    language = serializers.CharField(source="get_language_display")

    class Meta:
        model = Person
        fields = [
            "id",
            "name",
            "image",
            "language",
        ]


class StaffMinimalSerializer(serializers.ModelSerializer):
    """Serializer for Person model (Staff Minimal)."""

    category = serializers.CharField(source="get_category_display")

    class Meta:
        model = Person
        fields = [
            "id",
            "name",
            "image",
            "category",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["image"] = representation.get("image", "") or ""
        return representation
