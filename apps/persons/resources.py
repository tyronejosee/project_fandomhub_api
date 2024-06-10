"""Resources for Persons App."""

from import_export.resources import ModelResource

from .models import Person, StaffAnime


class PersonResource(ModelResource):
    class Meta:
        model = Person


class StaffAnimeResource(ModelResource):
    class Meta:
        model = StaffAnime
