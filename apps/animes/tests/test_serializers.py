"""Serializer Tests for Genres App."""

import pytest

# from ..serializers import AnimeReadSerializer


@pytest.mark.django_db
class TestAnimeSerializers:
    pass

    # def test_anime_read_serializer(self, anime):
    #     serializer = AnimeReadSerializer(anime)
    #     expected_data = {
    #         "id": str(anime.id),
    #         "name": anime.name,
    #         "name_jpn": anime.name_jpn,
    #         "name_rom": anime.name_rom,
    #         "slug": anime.slug,
    #         "alternative_names": anime.alternative_names,
    #         "image": anime.image,
    #         "trailer": anime.trailer,
    #         "synopsis": anime.synopsis,
    #         "background": anime.background,
    #         "season": anime.season,
    #         "year": str(anime.year),
    #         "broadcast_id": str(anime.broadcast_id.id),
    #         "media_type": anime.media_type,
    #         "episodes": anime.episodes,
    #         "status": anime.status,
    #         "aired_from": anime.aired_from,
    #         "aired_to": anime.aired_to,
    #         "studio_id": anime.studio_id,
    #         "source": anime.source,
    #         "genres": list(anime.genres.values_list("id", flat=True)),
    #         "themes": list(anime.themes.values_list("id", flat=True)),
    #         "duration": anime.duration,
    #         "rating": anime.rating,
    #         "website": anime.website,
    #         "is_recommended": anime.is_recommended,
    #         "score": anime.score,
    #         "ranked": anime.ranked,
    #         "popularity": anime.popularity,
    #         "members": anime.members,
    #         "favorites": anime.favorites,
    #     }
    #     assert serializer.data == expected_data
