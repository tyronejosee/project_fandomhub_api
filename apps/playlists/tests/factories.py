"""Factories for Playlists App."""

import factory

from apps.animes.tests.factories import AnimeFactory
from apps.mangas.tests.factories import MangaFactory
from apps.users.tests.factories import MemberFactory
from ..models import AnimeList, AnimeListItem, MangaList, MangaListItem
from ..choices import (
    AnimeStatusChoices,
    ScoreChoices,
    PriorityChoices,
    StorageChoices,
    MangaStatusChoices,
)


class AnimeListFactory(factory.django.DjangoModelFactory):
    """Factory for AnimeList model."""

    class Meta:
        model = AnimeList

    user = factory.SubFactory(MemberFactory)
    # banner = factory.django.ImageField(
    #     color="blue", format="jpg", width=500, height=1500
    # )
    is_public = True


class MangaListFactory(factory.django.DjangoModelFactory):
    """Factory for MangaList model."""

    class Meta:
        model = MangaList

    user = factory.SubFactory(MemberFactory)
    # banner = factory.django.ImageField(
    #     color="blue", format="jpg", width=500, height=1500
    # )
    is_public = True


class AnimeListItemFactory(factory.django.DjangoModelFactory):
    """Factory for AnimeListItem model."""

    class Meta:
        model = AnimeListItem

    animelist_id = factory.SubFactory(AnimeListFactory)
    anime_id = factory.SubFactory(AnimeFactory)
    status = factory.Iterator(AnimeStatusChoices.values)
    episodes_watched = factory.Faker("random_int", min=0, max=24)
    score = factory.Iterator(ScoreChoices.values)
    start_date = factory.Faker("date_between", start_date="-2y", end_date="today")
    finish_date = factory.Faker("date_between", start_date="today", end_date="+1y")
    tags = factory.Faker("words", nb=3)
    priority = factory.Iterator(PriorityChoices.values)
    storage = factory.Iterator(StorageChoices.values)
    times_rewatched = factory.Faker("random_int", min=0, max=5)
    notes = factory.Faker("paragraph")
    order = factory.Faker("random_int", min=0, max=10)
    is_watched = factory.Faker("boolean")
    is_favorite = factory.Faker("boolean")


class MangaListItemFactory(factory.django.DjangoModelFactory):
    """Factory for MangaListItem model."""

    class Meta:
        model = MangaListItem

    mangalist_id = factory.SubFactory(MangaListFactory)
    manga_id = factory.SubFactory(MangaFactory)
    status = factory.Iterator(MangaStatusChoices.values)
    volumes_read = factory.Faker("random_int", min=0, max=20)
    chapters_read = factory.Faker("random_int", min=0, max=100)
    score = factory.Iterator(ScoreChoices.values)
    start_date = factory.Faker("date_between", start_date="-2y", end_date="today")
    finish_date = factory.Faker("date_between", start_date="today", end_date="+1y")
    tags = factory.Faker("words", nb=3)
    priority = factory.Iterator(PriorityChoices.values)
    storage = factory.Iterator(StorageChoices.values)
    times_reread = factory.Faker("random_int", min=0, max=5)
    notes = factory.Faker("paragraph")
    order = factory.Faker("random_int", min=0, max=10)
    is_read = factory.Faker("boolean")
    is_favorite = factory.Faker("boolean")
