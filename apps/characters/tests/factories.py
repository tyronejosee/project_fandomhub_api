"""Factories for Characters App."""

import factory

from apps.animes.tests.factories import AnimeFactory
from apps.mangas.tests.factories import MangaFactory
from apps.persons.tests.factories import PersonFactory
from ..models import Character, CharacterVoice, CharacterAnime, CharacterManga
from ..choices import RoleChoices


class CharacterFactory(factory.django.DjangoModelFactory):
    """Factory for Character model."""

    class Meta:
        model = Character
        skip_postgeneration_save = True

    name = factory.Faker("name")
    name_kanji = factory.Faker("name", locale="ja-JP")
    about = factory.Faker("text")
    role = factory.Iterator(RoleChoices.values)
    # image = factory.django.ImageField(
    #     color="blue", format="jpeg", width=600, height=600
    # )
    favorites = factory.Faker("random_int", min=0, max=10000)

    voices = factory.RelatedFactory(PersonFactory, "character")
    animes = factory.RelatedFactory(AnimeFactory, "character")
    mangas = factory.RelatedFactory(MangaFactory, "character")


class CharacterVoiceFactory(factory.django.DjangoModelFactory):
    """Factory for CharacterVoice model."""

    class Meta:
        model = CharacterVoice

    character_id = factory.SubFactory(CharacterFactory)
    voice_id = factory.SubFactory(PersonFactory)


class CharacterAnimeFactory(factory.django.DjangoModelFactory):
    """Factory for CharacterAnime model."""

    class Meta:
        model = CharacterAnime

    character_id = factory.SubFactory(CharacterFactory)
    anime_id = factory.SubFactory(AnimeFactory)


class CharacterMangaFactory(factory.django.DjangoModelFactory):
    """Factory for CharacterManga model."""

    class Meta:
        model = CharacterManga

    character_id = factory.SubFactory(CharacterFactory)
    manga_id = factory.SubFactory(MangaFactory)
