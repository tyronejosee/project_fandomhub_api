"""Serializer Tests for Clubs App."""

import pytest

from apps.users.tests.factories import MemberFactory
from ...serializers import (
    ClubReadSerializer,
    ClubWriteSerializer,
    ClubMemberReadSerializer,
    ClubMemberWriteSerializer,
)


@pytest.mark.django_db
class TestClubSerializers:
    """Tests for Club serializers."""

    def test_club_read_serializer(self, club):
        serializer = ClubReadSerializer(club)
        expected_data = {
            "id": str(club.id),
            "name": club.name,
            "description": club.description,
            "image": club.image.url,
            "category": club.category,
            "members": club.members,
            "created_by": club.created_by.username,
            "is_public": club.is_public,
            "created_at": club.created_at.isoformat(),
            "updated_at": club.updated_at.isoformat(),
        }
        assert serializer.data == expected_data

    def test_club_write_serializer_valid_data(self, club):
        user = MemberFactory()
        data = {
            "name": "Ikebana Club",
            "description": club.description,
            "image": club.image,
            "category": club.category,
            "created_by": user.id,
            "is_public": club.is_public,
        }
        serializer = ClubWriteSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        assert serializer.validated_data["name"] == "Ikebana Club"

    def test_club_write_serializer_invalid_data(self):
        data = {}
        serializer = ClubWriteSerializer(data=data)
        assert not serializer.is_valid()
        assert "name" in serializer.errors
        assert "description" in serializer.errors
        assert "category" in serializer.errors
        assert "created_by" in serializer.errors
        assert "is_public" in serializer.errors


@pytest.mark.django_db
class TestClubMemberSerializers:
    """Tests for ClubMember serializers."""

    def test_club_member_read_serializer(self, club_member):
        serializer = ClubMemberReadSerializer(club_member)
        expected_data = {
            "user_id": str(club_member.user_id),
            "joined_at": club_member.joined_at.isoformat().replace("+00:00", "Z"),
        }
        assert serializer.data == expected_data

    def test_club_member_write_serializer_valid_data(self):
        user = MemberFactory()
        data = {"user_id": user.id}
        serializer = ClubMemberWriteSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        assert serializer.validated_data["user_id"] == user
