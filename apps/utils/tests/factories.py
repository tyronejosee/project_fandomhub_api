"""Factories for Utils App."""

import factory
from uuid import uuid4
from django.contrib.contenttypes.models import ContentType

from apps.animes.models import Anime
from apps.mangas.models import Manga
from apps.characters.models import Character
from apps.persons.models import Person
from ..models import Picture
from ..functions import generate_test_image, generate_random_code


class PictureFactory(factory.django.DjangoModelFactory):
    """Factory for Picture model."""

    class Meta:
        model = Picture
        skip_postgeneration_save = True

    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object.__class__)
    )
    object_id = factory.LazyAttribute(lambda o: uuid4())
    name = factory.LazyFunction(lambda: generate_random_code())
    image = factory.LazyAttribute(lambda _: generate_test_image(size=(600, 600)))

    @factory.lazy_attribute
    def content_object(self):
        model_mapping = {
            "anime": Anime.objects.first(),
            "manga": Manga.objects.first(),
            "character": Character.objects.first(),
            "person": Person.objects.first(),
        }
        content_type_model = model_mapping.get(self.content_type.model)
        return content_type_model
