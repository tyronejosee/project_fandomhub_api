"""Factories for Utils App."""

import factory
from django.contrib.contenttypes.models import ContentType

from apps.animes.models import Anime
from apps.mangas.models import Manga
from apps.characters.models import Character
from apps.persons.models import Person
from ..models import Picture, Video
from ..functions import generate_test_image, generate_random_code


class PictureFactory(factory.django.DjangoModelFactory):
    """Factory for Picture model."""

    class Meta:
        model = Picture
        skip_postgeneration_save = True

    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object.__class__)
    )
    object_id = factory.LazyAttribute(lambda o: o.content_object.id)
    name = factory.LazyFunction(lambda: generate_random_code())
    image = factory.LazyAttribute(lambda _: generate_test_image(size=(600, 600)))

    @factory.lazy_attribute
    def content_object(self):
        model_mapping = [
            Anime.objects.first(),
            Manga.objects.first(),
            Character.objects.first(),
            Person.objects.first(),
        ]
        return next((model for model in model_mapping if model is not None), None)


class VideoFactory(factory.django.DjangoModelFactory):
    """Factory for Video model."""

    class Meta:
        model = Video
        skip_postgeneration_save = True

    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object.__class__)
    )
    object_id = factory.LazyAttribute(lambda o: o.content_object.id)
    video = factory.Faker("url")

    @factory.lazy_attribute
    def content_object(self):
        model_mapping = [
            Anime.objects.first(),
            Manga.objects.first(),
        ]
        return next((model for model in model_mapping if model is not None), None)
