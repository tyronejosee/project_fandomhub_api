"""Factories for Clubs App."""

import factory
from django.utils import timezone

from apps.users.tests.factories import MemberFactory
from ..models import Club, ClubMember, Event, Topic, Discussion
from ..choices import CategoryChoices


class ClubFactory(factory.django.DjangoModelFactory):
    """Factory for Club model."""

    class Meta:
        model = Club

    name = factory.Faker("company")
    description = factory.Faker("text")
    # image = factory.django.ImageField(
    #     color="blue", format="jpg", width=600, height=600
    # )
    category = factory.Iterator(CategoryChoices.values)
    members = factory.Faker("random_number", digits=2)
    created_by = factory.SubFactory(MemberFactory)
    is_public = factory.Faker("boolean")


class ClubMemberFactory(factory.django.DjangoModelFactory):
    """Factory for ClubMember model."""

    class Meta:
        model = ClubMember

    club_id = factory.SubFactory(ClubFactory)
    user_id = factory.SubFactory(MemberFactory)
    joined_at = timezone.now()


class EventFactory(factory.django.DjangoModelFactory):
    """Factory for Event model."""

    class Meta:
        model = Event

    club_id = factory.SubFactory(ClubFactory)
    name = factory.Faker("word")
    description = factory.Faker("paragraph")
    date = factory.Faker("date_this_year")


class TopicFactory(factory.django.DjangoModelFactory):
    """Factory for Topic model."""

    class Meta:
        model = Topic

    name = factory.Faker("paragraph")
    club_id = factory.SubFactory(ClubFactory)
    created_by = factory.SubFactory(MemberFactory)


class DiscussionFactory(factory.django.DjangoModelFactory):
    """Factory for Discussion model."""

    class Meta:
        model = Discussion

    topic_id = factory.SubFactory(TopicFactory)
    content = factory.Faker("text")
    created_by = factory.SubFactory(MemberFactory)
