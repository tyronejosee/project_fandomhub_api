"""Resources for Genres App."""

from import_export.resources import ModelResource

from .models import Genre, Theme, Demographic


class GenreResource(ModelResource):
    """Resource definition for Genre model"""

    class Meta:
        model = Genre


class ThemeResource(ModelResource):
    """Resource definition for Broadcast model"""

    class Meta:
        model = Theme


class DemographicResource(ModelResource):
    """Resource definition for Demographic model"""

    class Meta:
        model = Demographic
