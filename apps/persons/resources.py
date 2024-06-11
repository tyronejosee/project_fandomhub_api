"""Resources for Persons App."""

from import_export.resources import ModelResource

from .models import Person, StaffAnime


class PersonResource(ModelResource):
    """Resource definition for Person model"""

    class Meta:
        model = Person


class StaffAnimeResource(ModelResource):
    """Resource definition for StaffAnime model"""

    class Meta:
        model = StaffAnime
