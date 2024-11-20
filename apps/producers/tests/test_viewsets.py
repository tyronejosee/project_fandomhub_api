"""ViewSet Tests for Producers App."""

import uuid
import pytest
from rest_framework import status

from apps.utils.functions import generate_test_image
from .factories import ProducerFactory
from ..models import Producer
from ..choices import TypeChoices


@pytest.mark.django_db
class TestProducerViewSet:

    def test_list_producers(self, anonymous_user, producer):
        response = anonymous_user.get("/api/v1/producers/")

        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_retrieve_producer(self, anonymous_user, producer):
        response = anonymous_user.get(f"/api/v1/producers/{producer.id}/")
        data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert uuid.UUID(data["id"]) == producer.id
        assert data["name"] == producer.name

    def test_retrieve_producer_not_found(self, anonymous_user):
        response = anonymous_user.get(
            "/api/v1/producers/989423d1-d6c0-431a-8f62-d805b8a5f321/"
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_create_producer(self, contributor_user):
        image = generate_test_image(size=(600, 600))
        data = {
            "name": "New Producer",
            "name_jpn": "新しいプロデューサー",
            "about": "This is a description about the new producer.",
            "established": "2020",
            "type": TypeChoices.LICENSOR,
            "image": image,
        }

        response = contributor_user.post(
            "/api/v1/producers/",
            data,
            format="multipart",
        )
        data = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert Producer.objects.filter(name="New Producer").exists()
        assert data["name"] == "New Producer"
        assert data["type"] == TypeChoices.LICENSOR

    def test_create_producer_unauthorized(self, member_user):
        image = generate_test_image(size=(600, 600))
        data = {
            "name": "Unauthorized Producer",
            "name_jpn": "新しいプロデューサー",
            "about": "This is a description about the new producer.",
            "established": "2020",
            "type": TypeChoices.LICENSOR,
            "image": image,
        }
        member_response = member_user.post(
            "/api/v1/producers/",
            data,
            format="multipart",
        )
        assert member_response.status_code == status.HTTP_403_FORBIDDEN

        member_user.logout()

        anonymus_response = member_user.post(
            "/api/v1/producers/",
            data,
            format="multipart",
        )
        assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED

        assert not Producer.objects.filter(name="Unauthorized Producer").exists()

    def test_update_producer(self, contributor_user, producer):
        image = generate_test_image(size=(600, 600))
        data = {
            "name": "Updated Producer",
            "name_jpn": producer.name_jpn,
            "about": producer.about,
            "established": producer.established,
            "type": producer.type,
            "image": image,
        }
        response = contributor_user.put(
            f"/api/v1/producers/{producer.id}/",
            data,
            format="multipart",
        )

        assert response.status_code == status.HTTP_200_OK
        producer.refresh_from_db()
        assert producer.name == "Updated Producer"

    def test_partial_update_producer(self, contributor_user, producer):
        data = {"name": "Partially Updated Producer"}
        response = contributor_user.patch(
            f"/api/v1/producers/{producer.id}/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        producer.refresh_from_db()
        assert producer.name == "Partially Updated Producer"

    def test_delete_producer(self, contributor_user, producer):
        assert producer.is_available

        response = contributor_user.delete(f"/api/v1/producers/{producer.id}/")
        producer.refresh_from_db()

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Producer.objects.filter(id=producer.id).exists()
        assert not producer.is_available

    def test_search_field_name(self, member_user):
        ProducerFactory(name="Kyoto Animation")
        ProducerFactory(name="MAPPA")
        ProducerFactory(name="Madhouse")

        response = member_user.get("/api/v1/producers/", {"q": "Kyoto Animation"})
        data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert len(data["results"]) == 1
        assert data["results"][0]["name"] == "Kyoto Animation"

        response_partial = member_user.get("/api/v1/producers/", {"q": "MAPPA"})
        data_partial = response_partial.json()
        assert response_partial.status_code == status.HTTP_200_OK
        assert len(data_partial["results"]) == 1
        assert data_partial["results"][0]["name"] == "MAPPA"

        response_no_results = member_user.get(
            "/api/v1/producers/", {"q": "Wit Studio"}  # Not Found
        )
        data_no_results = response_no_results.json()
        assert response_no_results.status_code == status.HTTP_200_OK
        assert len(data_no_results["results"]) == 0
