"""Factories for Producers App."""

import factory

from ..models import Producer
from ..choices import TypeChoices


class ProducerFactory(factory.django.DjangoModelFactory):
    """Factory for Producer model."""

    class Meta:
        model = Producer

    name = factory.Faker("company")
    name_jpn = factory.Faker("company")
    about = factory.Faker("text")
    established = factory.Faker("year")
    type = factory.Iterator(TypeChoices.values)
    # image = factory.django.ImageField(
    #     color="blue", format="jpeg", width=600, height=600
    # )
    favorites = factory.Faker("random_int", min=0, max=1000)
