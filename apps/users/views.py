"""Views for Users App."""

from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from djoser.social.views import ProviderAuthView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_spectacular.utils import extend_schema_view

from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer
from apps.profiles.models import Profile
from apps.profiles.serializers import ProfileAboutSerializer
from .models import User
from .permissions import IsMember
from .schemas import (
    token_obtain_pair_schemas,
    token_refresh_schemas,
    token_verify_schemas,
    provider_auth_schemas,
)


@extend_schema_view(**token_obtain_pair_schemas)
class TokenObtainPairExtensionView(TokenObtainPairView):
    """
    Extended view for obtaining JWT tokens.

    Extends the standard TokenObtainPairView in `rest_framework_simplejwt.views`
    to include custom schema documentation using drf-spectacular.
    """

    pass


@extend_schema_view(**token_refresh_schemas)
class TokenRefreshExtensionView(TokenRefreshView):
    """
    Extended view for refreshing JWT tokens.

    Extends the standard TokenRefreshView in `rest_framework_simplejwt.views`
    to include custom schema documentation using drf-spectacular.
    """

    pass


@extend_schema_view(**token_verify_schemas)
class TokenVerifyExtensionView(TokenVerifyView):
    """
    Extended view for verifying JWT tokens.

    Extends the standard TokenVerifyView in `rest_framework_simplejwt.views`
    to include custom schema documentation using drf-spectacular.
    """

    pass


@extend_schema_view(**provider_auth_schemas)
class ProviderAuthExtensionView(ProviderAuthView):
    """
    Extended view for handling social authentication provider requests.

    Extends the standard ProviderAuthView `djoser.social.urls`
    to include custom schema documentation using drf-spectacular.
    """

    pass


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
