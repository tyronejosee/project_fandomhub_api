"""Endpoint Tests for Clubs App."""

import pytest
from rest_framework import status

from apps.users.tests.factories import MemberFactory
from ...models import Club
from ..factories import ClubFactory


@pytest.mark.django_db
def test_list_clubs(anonymous_user, club):
    endpoint = "/api/v1/clubs/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.json()) > 0


@pytest.mark.django_db
def test_retrieve_club(anonymous_user, club):
    endpoint = f"/api/v1/clubs/{club.id}/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert str(response.data["id"]) == str(club.id)
    assert response.data["name"] == club.name


@pytest.mark.django_db
def test_retrieve_club_not_found(anonymous_user):
    endpoint = "/api/v1/clubs/989423d1-d6c0-431a-8f62-d805b8a5f321/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "Not found."


@pytest.mark.django_db
def test_create_club(member_user, club):
    new_user = MemberFactory.create()
    endpoint = "/api/v1/clubs/"
    data = {
        "name": "New Club",
        "description": club.description,
        "image": club.image,
        "category": club.category,
        "created_by": new_user.id,
        "is_public": club.is_public,
    }
    response = member_user.post(endpoint, data, format="multipart")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.reason_phrase == "Created"
    assert Club.objects.filter(name="New Club").exists()
    assert response.data["name"] == "New Club"


@pytest.mark.django_db
def test_create_club_errors(contributor_user, club):
    new_user = MemberFactory.create()
    endpoint = "/api/v1/clubs/"
    data = {
        "name": "Unauthorized Club",
        "description": club.description,
        "image": club.image,
        "category": club.category,
        "created_by": new_user.id,
        "is_public": club.is_public,
    }
    member_response = contributor_user.post(endpoint, data, format="multipart")
    assert member_response.status_code == status.HTTP_403_FORBIDDEN
    assert member_response.reason_phrase == "Forbidden"
    contributor_user.logout()
    anonymus_response = contributor_user.post(endpoint, data, format="multipart")
    assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED
    assert anonymus_response.reason_phrase == "Unauthorized"
    assert not Club.objects.filter(name="Unauthorized Club").exists()


@pytest.mark.django_db
def test_update_club(member_user, club):
    endpoint = f"/api/v1/clubs/{club.id}/"
    data = {
        "name": "Updated Club",
        "description": club.description,
        "image": club.image,
        "category": club.category,
        "created_by": club.created_by.id,
        "is_public": club.is_public,
    }
    response = member_user.put(endpoint, data, format="multipart")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    club.refresh_from_db()
    assert club.name == "Updated Club"


@pytest.mark.django_db
def test_partial_update_club(member_user, club):
    endpoint = f"/api/v1/clubs/{club.id}/"
    data = {"name": "Partially Updated Club"}
    response = member_user.patch(endpoint, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    club.refresh_from_db()
    assert club.name == "Partially Updated Club"


@pytest.mark.django_db
def test_delete_club(member_user, club):
    assert club.is_available
    endpoint = f"/api/v1/clubs/{club.id}/"
    response = member_user.delete(endpoint)
    club.refresh_from_db()
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.reason_phrase == "No Content"
    assert Club.objects.filter(id=club.id).exists()
    assert not club.is_available


@pytest.mark.django_db
def test_search_fields(anonymous_user):
    ClubFactory(name="First Club")
    ClubFactory(name="Second Club")
    endpoint = "/api/v1/clubs/"
    query_params = {"q": "First Club"}
    response = anonymous_user.get(endpoint, query_params)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["name"] == "First Club"


@pytest.mark.django_db
def test_list_members_by_club(anonymous_user, club_member):
    endpoint = f"/api/v1/clubs/{club_member.club_id.id}/members/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 1
