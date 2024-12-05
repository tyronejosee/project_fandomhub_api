"""Endpoints Tests for Profiles App."""

import pytest
from rest_framework import status


@pytest.mark.django_db
def test_list_profiles(administrator_user, profile):
    endpoint = "/api/v1/profiles/"
    response = administrator_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) == 1


@pytest.mark.django_db
def test_list_profiles_errors(member_user, profile):
    endpoint = "/api/v1/profiles/"
    member_response = member_user.get(endpoint)
    assert member_response.status_code == status.HTTP_403_FORBIDDEN
    assert member_response.reason_phrase == "Forbidden"
    member_user.logout()
    anonymus_response = member_user.get(endpoint)
    assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED
    assert anonymus_response.reason_phrase == "Unauthorized"


# TODO: Add action tests
