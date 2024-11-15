"""Routers for Users App."""

from django.urls import include
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from .viewsets import UserExtensionViewSet
from .views import (
    TokenObtainPairExtensionView,
    TokenRefreshExtensionView,
    TokenVerifyExtensionView,
    ProviderAuthExtensionView,
    UserAboutView,
    UserReviewsView,
)

router = DefaultRouter()
router.register(r"users", UserExtensionViewSet, basename="user")

urlpatterns = [
    # Routers urls
    path("api/v1/", include(router.urls)),
    # Djoser socials urls
    re_path(
        r"^api/v1/socials/o/(?P<provider>\S+)/$",
        ProviderAuthExtensionView.as_view(),
        name="provider-auth",
    ),
    # djangorestframework-simplejwt urls
    re_path(
        r"^api/v1/tokens/jwt/create/?",
        TokenObtainPairExtensionView.as_view(),
        name="jwt-create",
    ),
    re_path(
        r"^api/v1/tokens/jwt/refresh/?",
        TokenRefreshExtensionView.as_view(),
        name="jwt-refresh",
    ),
    re_path(
        r"^api/v1/tokens/jwt/verify/?",
        TokenVerifyExtensionView.as_view(),
        name="jwt-verify",
    ),
    # Views urls
    path(
        "api/v1/users/<str:username>/about/",
        UserAboutView.as_view(),
    ),
    path(
        "api/v1/users/<str:username>/reviews/",
        UserReviewsView.as_view(),
    ),
]
