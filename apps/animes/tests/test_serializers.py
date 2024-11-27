"""Serializer Tests for Animes App."""

import pytest

from apps.genres.tests.factories import GenreFactory, ThemeFactory
from ..serializers import (
    BroadcastMinimalSerializer,
    AnimeReadSerializer,
    AnimeWriteSerializer,
    AnimeMinimalSerializer,
)


@pytest.mark.django_db
class TestBroadcastSerializers:
    """Tests for Broadcast serializers."""

    def test_broadcast_minimal_serializer(self, broadcast):
        serializer = BroadcastMinimalSerializer(broadcast)
        expected_data = {
            "string": broadcast.string,
            "day": broadcast.day,
            "time": broadcast.time.isoformat(),
            "timezone": broadcast.timezone,
        }

        assert serializer.data == expected_data


@pytest.mark.django_db
class TestAnimeSerializers:
    """Tests for Anime serializers."""

    def test_anime_read_serializer(self, anime):
        serializer = AnimeReadSerializer(anime)
        expected_data = {
            "id": str(anime.id),
            "name": anime.name,
            "name_jpn": anime.name_jpn,
            "name_rom": anime.name_rom,
            "slug": anime.slug,
            "alternative_names": anime.alternative_names,
            "image": anime.image.url,
            "trailer": anime.trailer,
            "synopsis": anime.synopsis,
            "background": anime.background,
            "season": anime.season,
            "year": int(anime.year),
            # "broadcast_id": {
            #     "string": anime.broadcast_id.string,
            #     "day": anime.broadcast_id.day,
            #     "time": str(anime.broadcast_id.time),
            #     "timezone": anime.broadcast_id.timezone,
            # }, # TODO: Fix fk field
            "broadcast_id": serializer.data["broadcast_id"],
            "media_type": anime.media_type,
            "episodes": anime.episodes,
            "status": anime.get_status_display(),
            "aired_from": anime.aired_from,
            "aired_to": anime.aired_to,
            "studio_id": {
                "id": str(anime.studio_id.id),
                "name": anime.studio_id.name,
                "name_jpn": anime.studio_id.name_jpn,
                "slug": anime.studio_id.slug,
                "about": anime.studio_id.about,
                "established": anime.studio_id.established,
                "type": anime.studio_id.type,
                "image": anime.studio_id.image.url,
                "favorites": anime.studio_id.favorites,
                "created_at": anime.studio_id.created_at.isoformat(),
                "updated_at": anime.studio_id.updated_at.isoformat(),
            },
            "source": anime.source,
            "genres": [
                {
                    "id": str(genre.id),
                    "name": genre.name,
                }
                for genre in anime.genres.all()
            ],
            "themes": [
                {
                    "id": str(theme.id),
                    "name": theme.name,
                    "slug": theme.slug,
                    "created_at": theme.created_at.isoformat(),
                    "updated_at": theme.updated_at.isoformat(),
                }
                for theme in anime.themes.all()
            ],
            "duration": serializer.data["duration"],
            "rating": anime.rating.lower(),
            "website": anime.website,
            "is_recommended": anime.is_recommended,
            "score": anime.score,
            "ranked": anime.ranked,
            "popularity": anime.popularity,
            "members": anime.members,
            "favorites": anime.favorites,
        }

        assert serializer.data == expected_data

    def test_anime_write_serializer_valid_data(self, anime):
        genres = GenreFactory.create_batch(2)
        themes = ThemeFactory.create_batch(2)
        data = {
            "name": "Chainsaw Man",
            "name_jpn": "チェンソーマン",
            "name_rom": "Chainsaw Man",
            "alternative_names": anime.alternative_names,
            "image": anime.image,
            "trailer": anime.trailer,
            "synopsis": anime.synopsis,
            "background": anime.background,
            "season": anime.season,
            "year": anime.year,
            "broadcast_id": str(anime.broadcast_id.id),
            "media_type": anime.media_type,
            "episodes": anime.episodes,
            "status": anime.status,
            "aired_from": anime.aired_from,
            "aired_to": anime.aired_to,
            "studio_id": str(anime.studio_id.id),
            "source": anime.source,
            "genres": [genre.id for genre in genres],
            "themes": [genre.id for genre in themes],
            "duration": anime.duration,
            "rating": anime.rating,
            "website": anime.website,
        }
        serializer = AnimeWriteSerializer(data=data)

        assert serializer.is_valid(), serializer.errors
        assert serializer.validated_data["name"] == "Chainsaw Man"
        assert serializer.validated_data["name_jpn"] == "チェンソーマン"
        assert serializer.validated_data["name_rom"] == "Chainsaw Man"

    def test_anime_write_serializer_invalid_data(self):
        data = {}
        serializer = AnimeWriteSerializer(data=data)

        assert not serializer.is_valid()
        assert "name" in serializer.errors
        assert "name_jpn" in serializer.errors
        assert "image" in serializer.errors
        assert "season" in serializer.errors
        assert "aired_from" in serializer.errors
        assert "studio_id" in serializer.errors
        assert "genres" in serializer.errors
        assert "themes" in serializer.errors

    def test_anime_minimal_serializer(self, anime):
        serializer = AnimeMinimalSerializer(anime)
        expected_data = {
            "id": str(anime.id),
            "name": anime.name,
            "image": anime.image.url,
            "episodes": anime.episodes,
            "aired_from": anime.aired_from,
            "year": int(anime.year),
            "genres": [
                {"id": str(genre.id), "name": genre.name}
                for genre in anime.genres.all()
            ],
            "duration": serializer.data["duration"],
            "score": anime.score,
            "members": anime.members,
            "favorites": anime.favorites,
        }

        assert serializer.data == expected_data

    # TODO: Add AnimeStatsReadSerializer test
