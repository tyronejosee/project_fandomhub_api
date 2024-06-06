"""Serializers for Clubs App."""

from django.db import IntegrityError
from django.utils.translation import gettext as _
from rest_framework import serializers

from .models import Club, ClubMember


class ClubReadSerializer(serializers.ModelSerializer):
    """Serializer for Club model (List/retrieve)."""

    class Meta:
        model = Club
        fields = [
            "id",
            "name",
            "description",
            "image",
            "category",
            "members",
            "created_by",
            "is_public",
            "created_at",
            "updated_at",
        ]


class ClubWriteSerializer(serializers.ModelSerializer):
    """Serializer for Club model (Create/update)."""

    class Meta:
        model = Club
        fields = [
            "name",
            "description",
            "image",
            "category",
            "is_public",
        ]


class ClubMemberReadSerializer(serializers.ModelSerializer):
    """Serializer for ClubMember model (List/retrieve)."""

    user = serializers.StringRelatedField()
    joined_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = ClubMember
        fields = [
            "user_id",
            "joined_at",
        ]


class ClubMemberWriteSerializer(serializers.ModelSerializer):
    """Serializer for ClubMember model (Create/update)."""

    class Meta:
        model = ClubMember
        fields = [
            "user_id",
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                _("This user is already a member of the club.")
            )
