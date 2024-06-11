"""Resources for Playlists App."""

from import_export.resources import ModelResource

from .models import AnimeList, MangaList, AnimeListItem, MangaListItem


class AnimeListResource(ModelResource):
    """Resource definition for AnimeList model"""

    class Meta:
        model = AnimeList


class MangaListResource(ModelResource):
    """Resource definition for MangaList model"""

    class Meta:
        model = MangaList


class AnimeListItemResource(ModelResource):
    """Resource definition for AnimeListItem model"""

    class Meta:
        model = AnimeListItem


class MangaListItemResource(ModelResource):
    """Resource definition for MangaListItem model"""

    class Meta:
        model = MangaListItem
