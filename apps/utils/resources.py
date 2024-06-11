"""Resources for Utils App."""

from import_export.resources import ModelResource

from .models import Picture, Video


class PictureResource(ModelResource):
    """Resource definition for Picture model"""

    class Meta:
        model = Picture


class VideoResource(ModelResource):
    """Resource definition for Video model"""

    class Meta:
        model = Video
