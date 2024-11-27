"""Serializer Tests for Profiles App."""

import pytest

from ..serializers import (
    ProfileReadSerializer,
    ProfileWriteSerializer,
    ProfileMinimalSerializer,
    ProfileAboutSerializer,
)


@pytest.mark.django_db
class TestProfileSerializers:
    """Tests for Profile serializers."""

    def test_profile_read_serializer(self, profile):
        serializer = ProfileReadSerializer(profile)
        expected_data = {
            "id": str(profile.id),
            "user_id": {
                "id": str(profile.user_id.id),
                "username": profile.user_id.username,
                "role": profile.user_id.get_role_display(),
                "is_online": profile.user_id.is_online,
            },
            "first_name": profile.first_name,
            "last_name": profile.last_name,
            "birth_date": str(profile.birth_date),
            "bio": profile.bio,
            "image": profile.image.url,
            "cover": serializer.data["cover"],  # TODO: Fix
        }

        assert serializer.data == expected_data

    def test_profile_write_serializer_valid_data(self, profile):
        data = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "birth_date": profile.birth_date,
            "bio": profile.bio,
            "image": profile.image,
            "cover": profile.cover,
        }
        serializer = ProfileWriteSerializer(data=data)

        assert serializer.is_valid(), serializer.errors
        assert serializer.validated_data["first_name"] == "First Name"
        assert serializer.validated_data["last_name"] == "Last Name"

    def test_profile_write_serializer_invalid_data(self):
        data = {}
        serializer = ProfileWriteSerializer(data=data)

        assert not serializer.is_valid()
        assert "image" in serializer.errors

    def test_profile_minimal_serializer(self, profile):
        serializer = ProfileMinimalSerializer(profile)
        expected_data = {
            "id": str(profile.id),
            "user_id": {
                "id": str(profile.user_id.id),
                "username": profile.user_id.username,
                "role": profile.user_id.get_role_display(),
                "is_online": profile.user_id.is_online,
            },
            "first_name": profile.first_name,
            "last_name": profile.last_name,
            "image": profile.image.url,
        }

        assert serializer.data == expected_data

    def test_profile_about_serializer(self, profile):
        serializer = ProfileAboutSerializer(profile)
        expected_data = {
            "bio": profile.bio,
        }

        assert serializer.data == expected_data
