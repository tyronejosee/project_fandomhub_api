"""Factories for Profiles App."""

import factory

from apps.utils.functions import generate_test_image
from apps.users.tests.factories import UserBaseFactory
from ..models import Profile


class ProfileFactory(factory.django.DjangoModelFactory):
    """Factory for Profile model."""

    class Meta:
        model = Profile

    user_id = factory.SubFactory(UserBaseFactory)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    birth_date = factory.Faker("date_of_birth", minimum_age=18, maximum_age=80)
    bio = factory.Faker("text")
    image = factory.LazyAttribute(lambda _: generate_test_image(size=(600, 600)))
    cover = factory.LazyAttribute(lambda _: generate_test_image(size=(1200, 600)))
