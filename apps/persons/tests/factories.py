"""Factories for Persons App."""

import factory

from apps.utils.functions import generate_test_image
from apps.animes.tests.factories import AnimeFactory
from ..models import Person, StaffAnime
from ..choices import LanguageChoices, CategoryChoices


class PersonFactory(factory.django.DjangoModelFactory):
    """Factory for Person model."""

    class Meta:
        model = Person

    name = factory.Faker("name")
    given_name = factory.Faker("first_name")
    family_name = factory.Faker("last_name")
    image = factory.LazyAttribute(lambda _: generate_test_image(size=(600, 600)))
    alternate_names = factory.Faker("sentences", nb=3)
    birthday = factory.Faker("date_of_birth")
    about = factory.Faker("text")
    website = factory.Faker("url")
    language = factory.Iterator(LanguageChoices.values)
    category = factory.Iterator(CategoryChoices.values)
    favorites = factory.Faker("random_int", min=0, max=1000)


class StaffAnimeFactory(factory.django.DjangoModelFactory):
    """Factory for StaffAnime model."""

    class Meta:
        model = StaffAnime

    person_id = factory.SubFactory(PersonFactory)
    anime_id = factory.SubFactory(AnimeFactory)
