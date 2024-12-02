"""Factories for Producers App."""

import factory

from apps.utils.functions import generate_test_image
from ..models import Producer
from ..choices import TypeChoices


class ProducerFactory(factory.django.DjangoModelFactory):
    """Factory for Producer model."""

    class Meta:
        model = Producer

    name = factory.Faker("name")
    name_jpn = factory.Faker("name")
    about = factory.Faker("text")
    established = factory.Faker("year")
    type = factory.Iterator(TypeChoices.values)
    image = factory.LazyAttribute(lambda _: generate_test_image(size=(600, 600)))
    favorites = factory.Faker("random_int", min=0, max=1000)
