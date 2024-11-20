"""Factories for Profiles App."""

import factory

from apps.users.tests.factories import MemberFactory
from ..models import Profile


class ProfileFactory(factory.django.DjangoModelFactory):
    """Factory for Profile model."""

    class Meta:
        model = Profile

    user_id = factory.SubFactory(MemberFactory)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    birth_date = factory.Faker("date_of_birth", minimum_age=18, maximum_age=80)
    bio = factory.Faker("text")
    # image = factory.django.ImageField(
    #     color="blue", format="jpeg", width=600, height=600
    # )
    # cover = factory.django.ImageField(
    #     color="blue", format="jpeg", width=1200, height=600
    # )
