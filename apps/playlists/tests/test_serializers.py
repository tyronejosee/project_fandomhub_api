"""Serializer Tests for Mangas App."""

import pytest

from ..serializers import (
    AnimeListReadSerializer,
    AnimeListWriteSerializer,
    AnimeListItemReadSerializer,
    # AnimeListItemWriteSerializer,
    MangaListReadSerializer,
    MangaListWriteSerializer,
    MangaListItemReadSerializer,
    # MangaListItemWriteSerializer,
)


@pytest.mark.django_db
class TestAnimeListSerializers:
    """Tests for AnimeList serializers."""

    def test_anime_list_read_serializer(self, anime_list):
        serializer = AnimeListReadSerializer(anime_list)
        expected_data = {
            "id": str(anime_list.id),
            "banner": anime_list.banner.url,
            "is_public": anime_list.is_public,
            "created_at": anime_list.created_at.isoformat(),
            "updated_at": anime_list.updated_at.isoformat(),
        }

        assert serializer.data == expected_data

    def test_anime_list_write_serializer_valid_data(self, anime_list):
        data = {
            "banner": anime_list.banner,
            "is_public": anime_list.is_public,
        }
        serializer = AnimeListWriteSerializer(data=data)

        assert serializer.is_valid(), serializer.errors
        assert serializer.validated_data["banner"]

    def test_anime_list_write_serializer_invalid_data(self):
        data = {}
        serializer = AnimeListWriteSerializer(data=data)

        assert not serializer.is_valid()
        assert "banner" in serializer.errors


@pytest.mark.django_db
class TestAnimeListItemSerializers:
    """Tests for AnimeListItem serializers."""

    def test_anime_list_item_read_serializer(self, anime_list_item):
        serializer = AnimeListItemReadSerializer(anime_list_item)
        expected_data = {
            "id": str(anime_list_item.id),
            "anime_id": serializer.data["anime_id"],
            # "anime_id": {
            #     "id": str(anime_list_item.anime_id.id),
            #     "name": anime_list_item.anime_id.name,
            #     "image": anime_list_item.anime_id.image.url,
            #     "episodes": anime_list_item.anime_id.episodes,
            #     "aired_from": str(anime_list_item.anime_id.aired_from),
            #     "year": int(anime_list_item.anime_id.year),
            #     # "genres": [
            #     #     {
            #     #         "id": str(genre.id),
            #     #         "name": genre.name,
            #     #     }
            #     #     for genre in anime_list_item.anime_id.genres.all()
            #     # ],
            #     "duration": str(anime_list_item.anime_id.duration),
            #     "score": anime_list_item.anime_id.score,
            #     "members": anime_list_item.anime_id.members,
            #     "favorites": anime_list_item.anime_id.favorites,
            # },
            # ! TODO: Fix anime_id field
            "status": anime_list_item.get_status_display(),
            "episodes_watched": anime_list_item.episodes_watched,
            "score": anime_list_item.get_score_display(),
            "start_date": str(anime_list_item.start_date),
            "finish_date": str(anime_list_item.finish_date),
            "tags": anime_list_item.tags,
            "priority": anime_list_item.get_priority_display(),
            "storage": anime_list_item.get_storage_display(),
            "times_rewatched": anime_list_item.times_rewatched,
            "notes": anime_list_item.notes,
            "order": anime_list_item.order,
            "is_watched": anime_list_item.is_watched,
            "is_favorite": anime_list_item.is_favorite,
            "created_at": anime_list_item.created_at.isoformat(),
            "updated_at": anime_list_item.updated_at.isoformat(),
        }

        assert serializer.data == expected_data

        # TODO: Add AnimeListItemWriteSerializer test


@pytest.mark.django_db
class TestMangaListSerializers:
    """Tests for MangaList serializers."""

    def test_manga_list_read_serializer(self, manga_list):
        serializer = MangaListReadSerializer(manga_list)
        expected_data = {
            "id": str(manga_list.id),
            "banner": manga_list.banner.url,
            "is_public": manga_list.is_public,
            "created_at": manga_list.created_at.isoformat(),
            "updated_at": manga_list.updated_at.isoformat(),
        }

        assert serializer.data == expected_data

    def test_manga_list_write_serializer_valid_data(self, manga_list):
        data = {
            "banner": manga_list.banner,
            "is_public": manga_list.is_public,
        }
        serializer = MangaListWriteSerializer(data=data)

        assert serializer.is_valid(), serializer.errors
        assert serializer.validated_data["banner"]

    def test_manga_list_write_serializer_invalid_data(self):
        data = {}
        serializer = MangaListWriteSerializer(data=data)

        assert not serializer.is_valid()
        assert "banner" in serializer.errors


@pytest.mark.django_db
class TestMangaListItemSerializers:
    """Tests for MangaListItem serializers."""

    def test_manga_list_item_read_serializer(self, manga_list_item):
        serializer = MangaListItemReadSerializer(manga_list_item)
        expected_data = {
            "id": str(manga_list_item.id),
            "manga_id": serializer.data["manga_id"],
            # "manga_id": {},
            # ! TODO: Fix manga_id field
            "status": manga_list_item.get_status_display(),
            "volumes_read": manga_list_item.volumes_read,
            "chapters_read": manga_list_item.chapters_read,
            "score": manga_list_item.get_score_display(),
            "start_date": str(manga_list_item.start_date),
            "finish_date": str(manga_list_item.finish_date),
            "tags": manga_list_item.tags,
            "priority": manga_list_item.get_priority_display(),
            "storage": manga_list_item.get_storage_display(),
            "times_reread": manga_list_item.times_reread,
            "notes": manga_list_item.notes,
            "order": manga_list_item.order,
            "is_read": manga_list_item.is_read,
            "is_favorite": manga_list_item.is_favorite,
            "created_at": manga_list_item.created_at.isoformat(),
            "updated_at": manga_list_item.updated_at.isoformat(),
        }

        assert serializer.data == expected_data

        # TODO: Add MangaListItemWriteSerializer test
