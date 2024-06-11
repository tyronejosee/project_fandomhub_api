"""Resources for Reviews App."""

from import_export.resources import ModelResource

from .models import Review


class ReviewResource(ModelResource):
    """Resource definition for Review model"""

    class Meta:
        model = Review
