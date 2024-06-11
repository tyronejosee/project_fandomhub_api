"""Resources for Mangas App."""

from import_export.resources import ModelResource

from .models import Magazine, Manga, MangaStats


class MagazineResource(ModelResource):
    """Resource definition for Magazine model"""

    class Meta:
        model = Magazine


class MangaResource(ModelResource):
    """Resource definition for Manga model"""

    class Meta:
        model = Manga


class MangaStatsResource(ModelResource):
    """Resource definition for MangaStats model"""

    class Meta:
        model = MangaStats
