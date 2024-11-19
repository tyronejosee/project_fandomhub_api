"""Factories for Animes Tests."""

import factory
from datetime import timedelta

from factory import Faker, SubFactory, RelatedFactoryList
from django.utils import timezone

from apps.producers.tests.factories import ProducerFactory
from apps.genres.tests.factories import GenreFactory, ThemeFactory
from ..models import Broadcast, Anime


class BroadcastFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Broadcast

    day = Faker("day_of_week")
    time = timezone.now().time()
    timezone = "JST"


class AnimeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Anime
        skip_postgeneration_save = True

    name = Faker("word")
    name_jpn = Faker("word")
    season = "Fall"
    year = Faker("year")
    broadcast_id = SubFactory(BroadcastFactory)
    media_type = "TV"
    source = "MANGA"
    episodes = 24
    status = "AIRING"
    aired_from = timezone.now().date()
    aired_to = timezone.now().date()
    producers = RelatedFactoryList(
        ProducerFactory,
        size=2,
    )
    genres = RelatedFactoryList(
        GenreFactory,
        size=2,
    )
    duration = timedelta(hours=1, minutes=45, seconds=30)
    themes = RelatedFactoryList(
        ThemeFactory,
        size=2,
    )
    studio_id = SubFactory(
        ProducerFactory,
        type="studio",
    )
    licensors_id = SubFactory(
        ProducerFactory,
        type="licensor",
    )
