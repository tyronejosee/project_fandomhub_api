"""Serializer Tests for Users App."""

import pytest

from ..serializers import (
    UserReadSerializer,
    UserWriteSerializer,
    UserMinimalSerializer,
)


@pytest.mark.django_db
class TestReviewSerializers:
    """Tests for Review serializers."""

    def test_user_read_serializer(self, user):
        serializer = UserReadSerializer(user)
        expected_data = {
            "id": str(user.id),
            "email": user.email,
            "username": user.username,
            "role": user.get_role_display(),
            "is_online": user.is_online,
            "is_active": user.is_active,
            "is_staff": user.is_staff,
            "created_at": user.created_at.isoformat().replace("+00:00", "Z"),
            "updated_at": user.updated_at.isoformat().replace("+00:00", "Z"),
        }
        assert serializer.data == expected_data

    # def test_user_write_serializer_valid_data(self, user):
    #     # ! TODO: Fix password field
    #     data = {
    #         "email": "test_user@test.com",
    #         "username": "test_user",
    #         "password": "INSERT HERE",
    #         "role": user.role,
    #         "is_online": user.is_online,
    #         "is_active": user.is_active,
    #         "is_staff": user.is_staff,
    #     }
    #     serializer = UserWriteSerializer(data=data)

    #     assert serializer.is_valid(), serializer.errors
    #     assert serializer.validated_data["email"] == "test_user@test.com"

    def test_user_write_serializer_invalid_data(self):
        data = {}
        serializer = UserWriteSerializer(data=data)

        assert not serializer.is_valid()
        assert "email" in serializer.errors
        assert "username" in serializer.errors

    def test_user_minimal_serializer(self, user):
        serializer = UserMinimalSerializer(user)
        expected_data = {
            "id": str(user.id),
            "username": user.username,
            "role": user.get_role_display(),
            "is_online": user.is_online,
        }
        assert serializer.data == expected_data
