"""Views for Users App."""

from django.utils.translation import gettext as _
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.exceptions import NotFound

from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer
from .permissions import IsMember
from .models import User


class UserDetailView(RetrieveAPIView):
    """
    View for retrieving detailed information about a user.

    Endpoints:
    - GET api/v1/users/{username}/
    """

    pass  # TODO: Pending for implementation


class UserAboutView(RetrieveAPIView):
    """
    View for retrieving the about section of a user.

    Endpoints:
    - GET api/v1/users/{username}/about/
    """

    pass  # TODO: Pending for implementation


class UserHistoryView(RetrieveAPIView):
    """
    View for retrieving the history of a user.

    Endpoints:
    - GET api/v1/users/{username}/history/
    """

    pass  # TODO: Pending for implementation


class UserStatsView(RetrieveAPIView):
    """
    View for retrieving the statistics of a user.

    Endpoints:
    - GET api/v1/users/{username}/stats/
    """

    pass  # TODO: Pending for implementation


class UserFriendsView(ListAPIView):
    """
    View for retrieving the friends of a user.

    Endpoints:
    - GET api/v1/users/{username}/friends/
    """

    pass  # TODO: Pending for implementation


class UserReviewsView(ListAPIView):
    """
    View for retrieving the reviews written by a user.

    Endpoints:
    - GET api/v1/users/{username}/reviews/
    """

    serializer_class = ReviewReadSerializer
    permission_classes = [IsMember]

    def get_queryset(self):
        username = self.kwargs.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound(_("User not found."))
        return Review.objects.filter(user_id=user)


class UserFavoritesView(ListAPIView):
    """
    View for retrieving the favorite items of a user.

    Endpoints:
    - GET api/v1/users/{username}/favorites/
    """

    pass  # TODO: Pending for implementation


class UserRecommendationsView(ListAPIView):
    """
    View for retrieving the recommendations for a user.

    Endpoints:
    - GET api/v1/users/{username}/recommendations/
    """

    pass  # TODO: Pending for implementation


class UserClubsView(ListAPIView):
    """
    View for retrieving the clubs a user is a member of.

    Endpoints:
    - GET api/v1/users/{username}/clubs/
    """

    pass  # TODO: Pending for implementation
