"""Factories for Genres Tests."""

import factory

from ..models import Genre


class GenreFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Genre

    name = "Anime Genre"
