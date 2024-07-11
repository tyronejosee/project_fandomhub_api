"""Views for Users App."""

from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer
from apps.profiles.models import Profile
from apps.profiles.serializers import ProfileAboutSerializer
from .models import User
from .permissions import IsMember


class UserDetailView(RetrieveAPIView):
    """
    View for retrieving detailed information about a user.

    Endpoints:
    - GET api/v1/users/{username}/
    """

    pass  # TODO: Pending for implementation


class UserAboutView(RetrieveAPIView):
    """
    View for retrieving the about section or bio of a user.

    Endpoints:
    - GET api/v1/users/{username}/about/
    """

    permission_classes = [AllowAny]
    serializer_class = ProfileAboutSerializer
    lookup_field = "username"
    lookup_url_kwarg = "username"

    def get_queryset(self):
        username = self.kwargs.get("username").lower()
        return Profile.objects.filter(user_id__username=username).select_related("user")

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset.values("bio"))


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
