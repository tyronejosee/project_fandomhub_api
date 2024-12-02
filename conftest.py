import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.core.cache import cache

from apps.animes.tests.factories import BroadcastFactory, AnimeFactory
from apps.characters.tests.factories import (
    CharacterFactory,
    CharacterVoiceFactory,
    CharacterAnimeFactory,
    CharacterMangaFactory,
)
from apps.clubs.tests.factories import ClubFactory, ClubMemberFactory
from apps.genres.tests.factories import GenreFactory, ThemeFactory, DemographicFactory
from apps.mangas.tests.factories import MagazineFactory, MangaFactory
from apps.producers.tests.factories import ProducerFactory
from apps.persons.tests.factories import PersonFactory, StaffAnimeFactory
from apps.playlists.tests.factories import (
    AnimeListFactory,
    MangaListFactory,
    AnimeListItemFactory,
    MangaListItemFactory,
)
from apps.news.tests.factories import NewsFactory
from apps.reviews.tests.factories import ReviewFactory
from apps.profiles.tests.factories import ProfileFactory
from apps.users.tests.factories import (
    UserBaseFactory,
    MemberFactory,
    PremiumFactory,
    ContributorFactory,
    ModeratorFactory,
    AdministratorFactory,
)
from apps.utils.tests.factories import PictureFactory

User = get_user_model()


@pytest.fixture(autouse=True)
def clear_cache():
    cache.clear()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def anonymous_user(api_client):
    return api_client


@pytest.fixture
def user():
    return UserBaseFactory.create()


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
def magazine():
    return MagazineFactory.create()


@pytest.fixture
def manga():
    return MangaFactory.create()


@pytest.fixture
def news():
    return NewsFactory.create()


@pytest.fixture
def broadcast():
    return BroadcastFactory.create()


@pytest.fixture
def anime():
    return AnimeFactory.create()


@pytest.fixture
def character():
    return CharacterFactory.create()


@pytest.fixture
def character_voice():
    return CharacterVoiceFactory.create()


@pytest.fixture
def character_anime():
    return CharacterAnimeFactory.create()


@pytest.fixture
def character_manga():
    return CharacterMangaFactory.create()


@pytest.fixture
def club():
    return ClubFactory.create()


@pytest.fixture
def club_member():
    return ClubMemberFactory.create()


@pytest.fixture()
def producer():
    return ProducerFactory.create()


@pytest.fixture()
def review():
    return ReviewFactory.create()


@pytest.fixture
def person():
    return PersonFactory.create()


@pytest.fixture
def staff_anime():
    return StaffAnimeFactory.create()


@pytest.fixture
def profile():
    return ProfileFactory.create()


@pytest.fixture
def anime_list():
    return AnimeListFactory.create()


@pytest.fixture
def manga_list():
    return MangaListFactory.create()


@pytest.fixture
def anime_list_item():
    return AnimeListItemFactory.create()


@pytest.fixture
def manga_list_item():
    return MangaListItemFactory.create()


@pytest.fixture
def picture():
    return PictureFactory.create()
