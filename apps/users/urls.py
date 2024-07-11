"""URLs for Users App."""

from django.urls import path, include

from .views import UserAboutView, UserReviewsView


urlpatterns = [
    path(
        "api/v1/users/<str:username>/about/",
        UserAboutView.as_view(),
    ),
    path(
        "api/v1/users/<str:username>/reviews/",
        UserReviewsView.as_view(),
    ),
    # Djoser urls
    path(
        "api/v1/",
        include("djoser.urls"),
    ),
    path(
        "api/v1/tokens/",
        include("djoser.urls.jwt"),
    ),
    path(
        "api/v1/socials/",
        include("djoser.social.urls"),
    ),
]
