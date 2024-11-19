"""Factories for Reviews App."""

import factory
from django.contrib.contenttypes.models import ContentType

from apps.animes.models import Anime
from apps.animes.tests.factories import AnimeFactory
from apps.users.tests.factories import MemberFactory
from ..models import Review


class ReviewFactory(factory.django.DjangoModelFactory):
    """Factory for Review model."""

    class Meta:
        model = Review

    user_id = factory.SubFactory(MemberFactory)
    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(Anime)
    )
    object_id = factory.LazyAttribute(lambda o: AnimeFactory().id)
    rating = factory.Faker("random_int", min=1, max=10)
    comment = factory.Faker("sentence", nb_words=10)
    is_spoiler = factory.Faker("boolean")
    helpful_count = factory.Faker("random_int", min=0, max=100)
    reported_count = factory.Faker("random_int", min=0, max=10)
