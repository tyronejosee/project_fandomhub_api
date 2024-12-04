"""Model Tests for News App."""

import pytest
from django.core.exceptions import ValidationError

from ...models import News
from ..factories import NewsFactory


@pytest.mark.django_db
class TestNewsModel:
    """Tests for News model."""

    def test_news_creation(self, news):
        news = News.objects.create(
            name="New News",
            description=news.description,
            content=news.content,
            image=news.image,
            source=news.source,
            tag=news.tag,
            author_id=news.author_id,  # not null
        )
        news.anime_relations.set(news.anime_relations.all())
        news.anime_relations.set(news.manga_relations.all())
        assert news.name == "New News"
        assert str(news) == "New News"

    def test_field_slug_generation(self):
        news = NewsFactory.create(name="Lorem ipsum")
        assert news.slug == "lorem-ipsum"

    def test_field_name_max_length(self):
        news = NewsFactory.create(name="a" * 101)  # Max 100
        with pytest.raises(ValidationError):
            news.full_clean()

    def test_manager_get_available(self):
        NewsFactory.create_batch(2)
        NewsFactory.create(is_available=False)
        results = News.objects.get_available()
        assert results.count() == 2
