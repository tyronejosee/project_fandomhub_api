"""ViewSet Tests for Clubs App."""

import uuid
import pytest
from rest_framework import status

from apps.users.tests.factories import MemberFactory
from ..models import Club
from .factories import ClubFactory


@pytest.mark.django_db
class TestClubViewSet:
    """Tests for ClubViewSet."""

    def test_list_clubs(self, anonymous_user, club):
        response = anonymous_user.get("/api/v1/clubs/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) > 0

    def test_retrieve_club(self, anonymous_user, club):
        response = anonymous_user.get(f"/api/v1/clubs/{club.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert uuid.UUID(response.data["id"]) == club.id
        assert response.data["name"] == club.name

    def test_retrieve_club_not_found(self, anonymous_user):
        response = anonymous_user.get(
            "/api/v1/clubs/989423d1-d6c0-431a-8f62-d805b8a5f321/"
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] == "Not found."

    def test_create_club(self, member_user, club):
        new_user = MemberFactory.create()
        data = {
            "name": "New Club",
            "description": club.description,
            "image": club.image,
            "category": club.category,
            "created_by": new_user.id,
            "is_public": club.is_public,
        }

        response = member_user.post(
            "/api/v1/clubs/",
            data,
            format="multipart",
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert Club.objects.filter(name="New Club").exists()
        assert response.data["name"] == "New Club"

    def test_create_club_unauthorized(self, contributor_user, club):
        new_user = MemberFactory.create()
        data = {
            "name": "Unauthorized Club",
            "description": club.description,
            "image": club.image,
            "category": club.category,
            "created_by": new_user.id,
            "is_public": club.is_public,
        }
        member_response = contributor_user.post(
            "/api/v1/clubs/",
            data,
            format="multipart",
        )
        assert member_response.status_code == status.HTTP_403_FORBIDDEN

        contributor_user.logout()

        anonymus_response = contributor_user.post(
            "/api/v1/clubs/",
            data,
            format="multipart",
        )
        assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED

        assert not Club.objects.filter(name="Unauthorized Club").exists()

    def test_update_club(self, member_user, club):
        data = {
            "name": "Updated Club",
            "description": club.description,
            "image": club.image,
            "category": club.category,
            "created_by": club.created_by.id,
            "is_public": club.is_public,
        }
        response = member_user.put(
            f"/api/v1/clubs/{club.id}/",
            data,
            format="multipart",
        )

        assert response.status_code == status.HTTP_200_OK
        club.refresh_from_db()
        assert club.name == "Updated Club"

    def test_partial_update_club(self, member_user, club):
        data = {"name": "Partially Updated Club"}
        response = member_user.patch(
            f"/api/v1/clubs/{club.id}/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        club.refresh_from_db()
        assert club.name == "Partially Updated Club"

    def test_delete_club(self, member_user, club):
        assert club.is_available

        response = member_user.delete(f"/api/v1/clubs/{club.id}/")
        club.refresh_from_db()

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Club.objects.filter(id=club.id).exists()
        assert not club.is_available

    def test_search_fields(self, anonymous_user):
        ClubFactory(name="First Club")
        ClubFactory(name="Second Club")

        response = anonymous_user.get("/api/v1/clubs/", {"q": "First Club"})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["name"] == "First Club"

    def test_action_get_members_success(self, anonymous_user, club_member):
        response = anonymous_user.get(
            f"/api/v1/clubs/{club_member.club_id.id}/members/"
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
