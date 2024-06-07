"""Routers for Playlists App."""

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter

# from .viewsets import PlaylistViewSet


# router = DefaultRouter()
# router.register(r"playlists", PlaylistViewSet, basename="playlist")

# urlpatterns = [path("api/v1/", include(router.urls))]

# urlpatterns = [
#     path(
#         "api/v1/playlists/me/",
#         PlaylistView.as_view(),
#     ),
#     path(
#         "api/v1/playlists/animes/",
#         PlaylistAnimeListView.as_view(),
#     ),
#     path(
#         "api/v1/playlists/animes/<uuid:item_id>/",
#         PlaylistAnimeDetailView.as_view(),
#     ),
#     path(
#         "api/v1/playlists/mangas/",
#         PlaylistMangaListView.as_view(),
#     ),
#     path(
#         "api/v1/playlists/mangas/<uuid:item_id>/",
#         PlaylistMangaDetailView.as_view(),
#     ),
# ]
