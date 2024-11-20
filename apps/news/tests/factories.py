"""Factories for News App."""

import factory

from apps.animes.tests.factories import AnimeFactory
from apps.mangas.tests.factories import MangaFactory
from apps.users.tests.factories import MemberFactory
from ..choices import TagChoices
from ..models import News


class NewsFactory(factory.django.DjangoModelFactory):
    """Factory for News model."""

    class Meta:
        model = News
        skip_postgeneration_save = True

    name = factory.Faker("sentence")
    description = factory.Faker("sentence", nb_words=10)
    content = factory.Faker("text")
    # image = factory.django.ImageField(
    #     color="blue", format="jpeg", width=909, height=1280
    # )
    source = factory.Faker("url")
    tag = factory.Iterator(TagChoices.values)
    anime_relations = factory.RelatedFactoryList(
        AnimeFactory,
        "news",
        size=2,
    )
    manga_relations = factory.RelatedFactoryList(
        MangaFactory,
        "news",
        size=2,
    )
    author_id = factory.SubFactory(MemberFactory)
