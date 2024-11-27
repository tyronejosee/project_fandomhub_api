"""ViewSet Tests for Profiles App."""

import pytest
from rest_framework import status


@pytest.mark.django_db
class TestProfileViewset:
    """Tests for ProfileViewSet API endpoints."""

    def test_list_profiles(self, administrator_user, profile):
        response = administrator_user.get("/api/v1/profiles/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) > 1

    def test_list_profiles_unauthorized(self, member_user, profile):
        member_response = member_user.get("/api/v1/profiles/")
        assert member_response.status_code == status.HTTP_403_FORBIDDEN

        member_user.logout()

        anonymus_response = member_user.get("/api/v1/profiles/")
        assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED

    # def test_action_get_my_profile(self, member_user, profile):
    #     response = member_user.get("/api/v1/profiles/my-profile/")

    #     assert response.status_code == status.HTTP_200_OK
    #     print(response.data)
    # TODO: Add action tests
