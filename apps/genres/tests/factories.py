"""Factories for Genres App."""

from factory import Faker, django

from ..models import Genre, Theme, Demographic


class GenreFactory(django.DjangoModelFactory):

    class Meta:
        model = Genre

    name = Faker("name")


class ThemeFactory(django.DjangoModelFactory):

    class Meta:
        model = Theme

    name = Faker("name")


class DemographicFactory(django.DjangoModelFactory):

    class Meta:
        model = Demographic

    name = Faker("name")
