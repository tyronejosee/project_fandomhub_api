"""Schemas for Playlists App."""

from drf_spectacular.utils import extend_schema


playlists_anime_schemas = {
    "get": extend_schema(
        summary="Get all Animes to the Playlist",
        description="Pending.",
    ),
    "post": extend_schema(
        summary="Create an Anime to the Playlist",
        description="Pending.",
    ),
    "patch": extend_schema(
        summary="Change an Anime to the Playlist",
        description="Pending.",
    ),
    "delete": extend_schema(
        summary="Remove an Anime to the Playlist",
        description="Pending.",
    ),
}

playlists_manga_schemas = {
    "get": extend_schema(
        summary="Get all Mangas to the Playlist",
        description="Pending.",
    ),
    "post": extend_schema(
        summary="Create an Manga to the Playlist",
        description="Pending.",
    ),
    "patch": extend_schema(
        summary="Change an Manga to the Playlist",
        description="Pending.",
    ),
    "delete": extend_schema(
        summary="Remove an Manga to the Playlist",
        description="Pending.",
    ),
}
