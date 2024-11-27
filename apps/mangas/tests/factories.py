"""Factories for Mangas App."""

import factory

from apps.utils.functions import generate_test_image
from apps.genres.tests.factories import GenreFactory, ThemeFactory, DemographicFactory
from apps.persons.tests.factories import PersonFactory
from ..models import Magazine, Manga
from ..choices import MediaTypeChoices, StatusChoices


class MagazineFactory(factory.django.DjangoModelFactory):
    """Factory for Magazine model."""

    class Meta:
        model = Magazine

    name = factory.Faker("company")
    count = factory.Faker("random_int", min=1, max=5)


class MangaFactory(factory.django.DjangoModelFactory):
    """Factory for Manga model."""

    class Meta:
        model = Manga
        skip_postgeneration_save = True

    name = factory.Faker("sentence")
    name_jpn = factory.Faker("sentence", locale="ja-JP")
    name_rom = factory.Faker("sentence")
    alternative_names = factory.Faker("sentence")
    image = factory.LazyAttribute(lambda _: generate_test_image(size=(909, 1280)))
    synopsis = factory.Faker("text")
    background = factory.Faker("text")
    media_type = factory.Iterator(MediaTypeChoices.values)
    chapters = factory.Faker("random_int", min=1, max=50)
    volumes = factory.Faker("random_int", min=1, max=20)
    status = factory.Iterator(StatusChoices.values)
    published_from = factory.Faker("date_this_decade")
    published_to = factory.Faker("date_this_decade")
    website = factory.Faker("url")
    is_recommended = factory.Faker("boolean")
    score = factory.Faker("random_number", digits=2)
    ranked = factory.Faker("random_int", min=1, max=1000)
    popularity = factory.Faker("random_int", min=1, max=10000)
    members = factory.Faker("random_int", min=1, max=5000)
    favorites = factory.Faker("random_int", min=1, max=1000)

    # Relations
    author_id = factory.SubFactory(PersonFactory)
    demographic_id = factory.SubFactory(DemographicFactory)
    serialization_id = factory.SubFactory(MagazineFactory)

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
            default_genre = ThemeFactory.create()
            self.themes.add(default_genre)
