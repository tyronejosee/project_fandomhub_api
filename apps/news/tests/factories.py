"""Factories for News App."""

import factory

from apps.utils.functions import generate_test_image
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
    image = factory.LazyAttribute(lambda _: generate_test_image(size=(600, 600)))
    source = factory.Faker("url")
    tag = factory.Iterator(TagChoices.values)
    author_id = factory.SubFactory(MemberFactory)

    @factory.post_generation
    def anime_relations(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.anime_relations.set(extracted)
        else:
            default_anime = AnimeFactory.create()
            self.anime_relations.add(default_anime)

    @factory.post_generation
    def manga_relations(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.manga_relations.set(extracted)
        else:
            default_manga = MangaFactory.create()
            self.manga_relations.add(default_manga)
