"""Serializer Tests for News App."""

import pytest

from ...serializers import (
    NewsReadSerializer,
    NewsWriteSerializer,
    NewsMinimalSerializer,
)


@pytest.mark.django_db
class TestNewsSerializers:
    """Tests for News serializers."""

    def test_news_read_serializer(self, news):
        serializer = NewsReadSerializer(news)
        expected_data = {
            "id": str(news.id),
            "author_id": news.author_id.username,
            "name": news.name,
            "slug": news.slug,
            "description": news.description,
            "content": news.content,
            "image": news.image.url,
            "source": news.source,
            "tag": news.get_tag_display(),
            "anime_relations": serializer.data["anime_relations"],
            "manga_relations": serializer.data["manga_relations"],
            "created_at": news.created_at.isoformat(),
            "updated_at": news.updated_at.isoformat(),
        }
        assert serializer.data == expected_data

    def test_news_write_serializer_valid_data(self, news):
        data = {
            "name": "Lorem ipsum",
            "description": news.description,
            "content": news.content,
            "image": news.image,
            "source": news.source,
            "tag": news.tag,
            "author_id": str(news.author_id.id),
            "anime_relations": [str(anime.id) for anime in news.anime_relations.all()],
            "manga_relations": [str(manga.id) for manga in news.manga_relations.all()],
        }
        serializer = NewsWriteSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        assert serializer.validated_data["name"] == "Lorem ipsum"
        assert serializer.validated_data["image"]

    def test_news_write_serializer_invalid_data(self):
        data = {}
        serializer = NewsWriteSerializer(data=data)
        assert not serializer.is_valid()
        assert "name" in serializer.errors
        assert "description" in serializer.errors
        assert "content" in serializer.errors
        assert "image" in serializer.errors
        assert "source" in serializer.errors

    def test_news_minimal_serializer(self, news):
        serializer = NewsMinimalSerializer(news)
        expected_data = {
            "id": str(news.id),
            "name": news.name,
            "slug": news.slug,
            "description": news.description,
            "image": news.image.url,
            "tag": news.get_tag_display(),
            "author_id": news.author_id.username,
        }
        assert serializer.data == expected_data
