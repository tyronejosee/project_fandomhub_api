"""Resources for Persons App."""

from import_export.resources import ModelResource

from .models import Broadcast, Anime, AnimeStats


class BroadcastResource(ModelResource):
    """Resource definition for Broadcast model"""

    class Meta:
        model = Broadcast


class AnimeResource(ModelResource):
    """Resource definition for Anime model"""

    class Meta:
        model = Anime


class AnimeStatsResource(ModelResource):
    """Resource definition for AnimeStats model"""

    class Meta:
        model = AnimeStats
