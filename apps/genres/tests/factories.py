"""Factories for Genres App."""

from factory import Faker, django

from ..models import Genre, Theme, Demographic


class GenreFactory(django.DjangoModelFactory):
    """Factory for Genre model."""

    class Meta:
        model = Genre

    name = Faker("name")


class ThemeFactory(django.DjangoModelFactory):
    """Factory for Theme model."""

    class Meta:
        model = Theme

    name = Faker("name")


class DemographicFactory(django.DjangoModelFactory):
    """Factory for Demographic model."""

    class Meta:
        model = Demographic

    name = Faker("name")
