"""ViewSet Tests for Mangas App."""

import pytest
from rest_framework import status

from apps.persons.tests.factories import PersonFactory
from apps.persons.choices import CategoryChoices
from ..models import Magazine, Manga


@pytest.mark.django_db
class TestMagazineViewSet:
    """Tests for MagazineViewSet API endpoints."""

    def test_list_magazines(self, anonymous_user, magazine):
        response = anonymous_user.get("/api/v1/magazines/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) > 0

    def test_retrieve_magazine(self, anonymous_user, magazine):
        response = anonymous_user.get(f"/api/v1/magazines/{magazine.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert str(response.data["id"]) == str(magazine.id)
        assert response.data["name"] == magazine.name

    def test_retrieve_magazine_not_found(self, anonymous_user):
        response = anonymous_user.get(
            "/api/v1/magazines/124f0ff1-5236-4cdb-9f0f-c0057e8d805f/"
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_create_magazine(self, contributor_user):
        data = {"name": "New Magazine"}
        response = contributor_user.post(
            "/api/v1/magazines/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert Magazine.objects.filter(name="New Magazine").exists()
        assert response.data["name"] == "New Magazine"

    def test_create_magazine_unauthorized(self, member_user):
        data = {"name": "Unauthorized Magazine"}
        member_response = member_user.post(
            "/api/v1/magazines/",
            data,
            format="json",
        )
        assert member_response.status_code == status.HTTP_403_FORBIDDEN

        member_user.logout()

        anonymus_response = member_user.post(
            "/api/v1/magazines/",
            data,
            format="json",
        )
        assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED

        assert not Magazine.objects.filter(name="Unauthorized Magazine").exists()

    def test_update_magazine(self, contributor_user, magazine):
        data = {"name": "Updated Magazine"}
        response = contributor_user.put(
            f"/api/v1/magazines/{magazine.id}/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        magazine.refresh_from_db()
        assert magazine.name == "Updated Magazine"

    def test_partial_update_magazine(self, contributor_user, magazine):
        data = {"name": "Partially Updated Magazine"}
        response = contributor_user.patch(
            f"/api/v1/magazines/{magazine.id}/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        magazine.refresh_from_db()
        assert magazine.name == "Partially Updated Magazine"

    def test_delete_magazine(self, contributor_user, magazine):
        assert magazine.is_available

        response = contributor_user.delete(f"/api/v1/magazines/{magazine.id}/")
        magazine.refresh_from_db()

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Magazine.objects.filter(id=magazine.id).exists()
        assert not magazine.is_available


@pytest.mark.django_db
class TestMangaViewSet:
    """Tests for MangaViewSet API endpoints."""

    def test_list_mangas(self, anonymous_user, manga):
        response = anonymous_user.get("/api/v1/mangas/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) > 0

    def test_retrieve_manga(self, anonymous_user, manga):
        response = anonymous_user.get(f"/api/v1/mangas/{manga.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert str(response.data["id"]) == str(manga.id)
        assert response.data["name"] == manga.name

    def test_retrieve_manga_not_found(self, anonymous_user):
        response = anonymous_user.get(
            "/api/v1/magazines/124f0ff1-5236-4cdb-9f0f-c0057e8d805f/"
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_create_manga(self, contributor_user, manga, demographic):
        author = PersonFactory.create(category=CategoryChoices.ARTIST)
        data = {
            "name": "Oyasumi Punpun",
            "name_jpn": "おやすみプンプン",
            "image": manga.image,
            "synopsis": manga.synopsis,
            "background": manga.background,
            "media_type": manga.media_type,
            "volumes": manga.volumes,
            "chapters": manga.chapters,
            "status": manga.status,
            "published_from": manga.published_from,
            "published_to": manga.published_to,
            "genres": [str(genre.id) for genre in manga.genres.all()],
            "themes": [str(theme.id) for theme in manga.themes.all()],
            "demographic_id": str(manga.demographic_id.id),
            "serialization_id": str(manga.serialization_id.id),
            "author_id": str(author.id),
            "website": manga.website,
        }
        response = contributor_user.post(
            "/api/v1/mangas/",
            data,
            format="multipart",
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert Manga.objects.filter(name="Oyasumi Punpun").exists()
        assert response.data["name"] == "Oyasumi Punpun"
        assert response.data["name_jpn"] == "おやすみプンプン"

    def test_create_manga_unauthorized(self, member_user):
        data = {}
        member_response = member_user.post(
            "/api/v1/mangas/",
            data,
            format="json",
        )
        assert member_response.status_code == status.HTTP_403_FORBIDDEN

        member_user.logout()

        anonymus_response = member_user.post(
            "/api/v1/mangas/",
            data,
            format="json",
        )
        assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED

        assert not Manga.objects.filter(name="Unauthorized manga").exists()

    def test_update_manga(self, contributor_user, manga):
        author = PersonFactory.create(category=CategoryChoices.ARTIST)
        data = {
            "name": "Frieren: Beyond Journey's End",
            "name_jpn": "葬送のフリーレン",
            "image": manga.image,
            "synopsis": manga.synopsis,
            "background": manga.background,
            "media_type": manga.media_type,
            "volumes": manga.volumes,
            "chapters": manga.chapters,
            "status": manga.status,
            "published_from": manga.published_from,
            "published_to": manga.published_to,
            "genres": [str(genre.id) for genre in manga.genres.all()],
            "themes": [str(theme.id) for theme in manga.themes.all()],
            "demographic_id": str(manga.demographic_id.id),
            "serialization_id": str(manga.serialization_id.id),
            "author_id": str(author.id),
            "website": manga.website,
        }
        response = contributor_user.put(
            f"/api/v1/mangas/{manga.id}/",
            data,
            format="multipart",
        )

        assert response.status_code == status.HTTP_200_OK
        manga.refresh_from_db()
        assert manga.name == "Frieren: Beyond Journey's End"
        assert manga.name_jpn == "葬送のフリーレン"

    def test_partial_update_manga(self, contributor_user, manga):
        data = {"name": "Houseki no Kuni"}
        response = contributor_user.patch(
            f"/api/v1/mangas/{manga.id}/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        manga.refresh_from_db()
        assert manga.name == "Houseki no Kuni"

    def test_delete_manga(self, contributor_user, manga):
        assert manga.is_available

        response = contributor_user.delete(f"/api/v1/mangas/{manga.id}/")
        manga.refresh_from_db()

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Manga.objects.filter(id=manga.id).exists()
        assert not manga.is_available

    # TODO: Add actions tests
