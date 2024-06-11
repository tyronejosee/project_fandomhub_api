"""Resources for Clubs App."""

from import_export.resources import ModelResource

from .models import Club, ClubMember, Event, Topic, Discussion


class ClubResource(ModelResource):
    """Resource definition for Club model"""

    class Meta:
        model = Club


class ClubMemberResource(ModelResource):
    """Resource definition for ClubMember model"""

    class Meta:
        model = ClubMember


class EventResource(ModelResource):
    """Resource definition for Event model"""

    class Meta:
        model = Event


class TopicResource(ModelResource):
    """Resource definition for Topic model"""

    class Meta:
        model = Topic


class DiscussionResource(ModelResource):
    """Resource definition for Discussion model"""

    class Meta:
        model = Discussion
