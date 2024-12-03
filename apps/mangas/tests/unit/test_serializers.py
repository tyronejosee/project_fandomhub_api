"""Serializer Tests for Mangas App."""

import pytest

from ...serializers import (
    MagazineReadSerializer,
    MagazineWriteSerializer,
    MangaReadSerializer,
    # MangaWriteSerializer,
    # MangaMinimalSerializer,
    # MangaStatsReadSerializer,
)


@pytest.mark.django_db
class TestMagazineSerializers:
    """Tests for Magazine serializers."""

    def test_magazine_read_serializer(self, magazine):
        serializer = MagazineReadSerializer(magazine)
        expected_data = {
            "id": str(magazine.id),
            "name": magazine.name,
            "slug": magazine.slug,
            "count": magazine.count,
            "created_at": magazine.created_at.isoformat(),
            "updated_at": magazine.updated_at.isoformat(),
        }

        assert serializer.data == expected_data

    def test_magazine_write_serializer_valid_data(self, magazine):
        data = {"name": "Kadokawa"}
        serializer = MagazineWriteSerializer(data=data)

        assert serializer.is_valid(), serializer.errors
        assert serializer.validated_data["name"] == "Kadokawa"

    def test_magazine_write_serializer_invalid_data(self):
        data = {}
        serializer = MagazineWriteSerializer(data=data)

        assert not serializer.is_valid()
        assert "name" in serializer.errors


@pytest.mark.django_db
class TestMangaSerializers:
    """Tests for Manga serializers."""

    def test_manga_read_serializer(self, manga):
        serializer = MangaReadSerializer(manga)
        expected_data = {
            "id": str(manga.id),
            "name": manga.name,
            "name_jpn": manga.name_jpn,
            "name_rom": manga.name_rom,
            "alternative_names": manga.alternative_names,
            "slug": manga.slug,
            "image": manga.image.url,
            "synopsis": manga.synopsis,
            "background": manga.background,
            "media_type": manga.get_media_type_display(),
            "volumes": manga.volumes,
            "chapters": manga.chapters,
            "status": manga.get_status_display(),
            "published_from": str(manga.published_from),
            "published_to": str(manga.published_to),
            "genres": [
                {
                    "id": str(genre.id),
                    "name": genre.name,
                    "slug": genre.slug,
                    "created_at": genre.created_at.isoformat(),
                    "updated_at": genre.updated_at.isoformat(),
                }
                for genre in manga.genres.all()
            ],
            "themes": [
                {
                    "id": str(theme.id),
                    "name": theme.name,
                    "slug": theme.slug,
                    "created_at": theme.created_at.isoformat(),
                    "updated_at": theme.updated_at.isoformat(),
                }
                for theme in manga.themes.all()
            ],
            "demographic_id": {
                "id": str(manga.demographic_id.id),
                "name": manga.demographic_id.name,
                "slug": manga.demographic_id.slug,
                "created_at": manga.demographic_id.created_at.isoformat(),
                "updated_at": manga.demographic_id.updated_at.isoformat(),
            },
            "serialization_id": {
                "id": str(manga.serialization_id.id),
                "name": manga.serialization_id.name,
                "slug": manga.serialization_id.slug,
                "count": manga.serialization_id.count,
                "created_at": manga.serialization_id.created_at.isoformat(),
                "updated_at": manga.serialization_id.updated_at.isoformat(),
            },
            "author_id": manga.author_id.name,
            "website": manga.website,
            "is_recommended": manga.is_recommended,
            "score": manga.score,
            "ranked": manga.ranked,
            "popularity": manga.popularity,
            "members": manga.members,
            "favorites": manga.favorites,
            "created_at": manga.created_at.isoformat(),
            "updated_at": manga.updated_at.isoformat(),
        }

        assert serializer.data == expected_data
