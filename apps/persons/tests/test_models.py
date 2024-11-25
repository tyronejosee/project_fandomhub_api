"""Model Tests for Persons App."""

from datetime import date
import pytest
from django.db import IntegrityError

from .factories import PersonFactory
from ..models import Person


@pytest.mark.django_db
class TestPersonModel:
    """Tests for Person model."""

    def test_person_creation(self, person):
        person = Person.objects.create(
            name="Hayao Miyazaki",
            given_name=person.given_name,
            family_name=person.family_name,
            image=person.image,
            alternate_names=person.alternate_names,
            birthday=person.birthday,
            about=person.about,
            website=person.website,
            language=person.language,
            category=person.category,
        )
        assert person.name == "Hayao Miyazaki"
        assert str(person) == "Hayao Miyazaki"

    def test_person_unique_fields(self, person):
        with pytest.raises(IntegrityError):
            Person.objects.create(
                name=person.name,
                given_name=person.given_name,
                family_name=person.family_name,
                image=person.image,
                alternate_names=person.alternate_names,
                birthday=person.birthday,
                about=person.about,
                website=person.website,
                language=person.language,
                category=person.category,
            )

    def test_person_slug_generation(self, person):
        person = Person.objects.create(
            name="Hayao Miyazaki",
            given_name=person.given_name,
            family_name=person.family_name,
            image=person.image,
            alternate_names=person.alternate_names,
            birthday=person.birthday,
            about=person.about,
            website=person.website,
            language=person.language,
            category=person.category,
        )
        assert person.slug == "hayao-miyazaki"

    def test_property_age(self):
        birth_date = date(1990, 5, 10)
        person = PersonFactory(birthday=birth_date)

        today = date.today()
        expected_age = (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )

        assert person.age == expected_age

    def test_manager_get_available(self, person):
        results = Person.objects.get_available()
        assert results.count() == 1
