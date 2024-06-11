"""Resources for News App."""

from import_export.resources import ModelResource

from .models import News


class NewsResource(ModelResource):
    """Resource definition for News model"""

    class Meta:
        model = News
