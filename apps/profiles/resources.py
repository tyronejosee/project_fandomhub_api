"""Resources for Profiles App."""

from import_export.resources import ModelResource

from .models import Profile


class ProfileResource(ModelResource):
    """Resource definition for Profile model"""

    class Meta:
        model = Profile
