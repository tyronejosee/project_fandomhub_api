import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from apps.animes.tests.factories import BroadcastFactory, AnimeFactory
from apps.genres.tests.factories import GenreFactory, ThemeFactory, DemographicFactory
from apps.users.tests.factories import (
    MemberFactory,
    PremiumFactory,
    ContributorFactory,
    ModeratorFactory,
    AdministratorFactory,
)

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def anonymous_user(api_client):
    return api_client


@pytest.fixture
def member_user(api_client):
    user = MemberFactory()
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def premium_user(api_client):
    user = PremiumFactory()
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def contributor_user(api_client):
    user = ContributorFactory()
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def moderator_user(api_client):
    user = ModeratorFactory()
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def administrator_user(api_client):
    user = AdministratorFactory()
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def genre():
    return GenreFactory.create()


@pytest.fixture
def theme():
    return ThemeFactory.create()


@pytest.fixture
def demographic():
    return DemographicFactory.create()


@pytest.fixture
def broadcast():
    return BroadcastFactory.create()


@pytest.fixture
def anime():
    return AnimeFactory.create()
