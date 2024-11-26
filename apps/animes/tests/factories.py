"""Factories for Animes App."""

import factory
from datetime import timedelta
from django.utils import timezone

from apps.utils.functions import generate_test_image
from apps.producers.tests.factories import ProducerFactory
from apps.genres.tests.factories import GenreFactory, ThemeFactory
from ..models import Broadcast, Anime
from ..choices import (
    TimezoneChoices,
    SeasonChoices,
    MediaTypeChoices,
    SourceChoices,
    StatusChoices,
)


class BroadcastFactory(factory.django.DjangoModelFactory):
    """Factory for Broadcast model."""

    class Meta:
        model = Broadcast

    day = factory.Faker("day_of_week")
    time = timezone.now().time()
    timezone = factory.Iterator(TimezoneChoices.values)


class AnimeFactory(factory.django.DjangoModelFactory):
    """Factory for Anime model."""

    class Meta:
        model = Anime
        skip_postgeneration_save = True

    name = factory.Faker("sentence")
    name_jpn = factory.Faker("sentence", locale="ja-JP")
    image = factory.LazyAttribute(lambda _: generate_test_image(size=(600, 600)))
    trailer = factory.Faker("url")
    synopsis = factory.Faker("text")
    background = factory.Faker("text")
    season = factory.Iterator(SeasonChoices.values)
    year = factory.Faker("year")
    broadcast_id = factory.SubFactory(BroadcastFactory)
    media_type = factory.Iterator(MediaTypeChoices.values)
    source = factory.Iterator(SourceChoices.values)
    episodes = factory.Faker("random_int", min=1, max=1500)
    status = factory.Iterator(StatusChoices.values)
    aired_from = factory.Faker("date")
    aired_to = factory.Faker("date")
    licensors_id = factory.SubFactory(
        ProducerFactory,
        type="licensor",
    )
    studio_id = factory.SubFactory(
        ProducerFactory,
        type="studio",
    )
    duration = timedelta(hours=1, minutes=45, seconds=30)
    website = factory.Faker("url")
    members = factory.Faker("random_int", min=0, max=10000)
    favorites = factory.Faker("random_int", min=0, max=10000)

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.genres.set(extracted)
        else:
            default_genre = GenreFactory.create()
            self.genres.add(default_genre)

    @factory.post_generation
    def themes(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.themes.set(extracted)
        else:
            default_theme = ThemeFactory.create()
            self.themes.add(default_theme)

    @factory.post_generation
    def producers(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.producers.set(extracted)
        else:
            default_producer = ProducerFactory.create()
            self.producers.add(default_producer)
