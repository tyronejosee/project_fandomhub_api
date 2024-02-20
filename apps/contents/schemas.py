"""Schemas for Contents App."""

from drf_spectacular.utils import extend_schema


anime_schemas = {
    "list": extend_schema(
        summary="Get Several Animes",
        description="Retrieve a list of all anime entries.",
    ),
    "create": extend_schema(
        summary="Create Anime",
        description="Create a new anime entry.",
    ),
    "retrieve": extend_schema(
        summary="Get Anime",
        description="Get detailed information about a specific anime entry.",
    ),
    "update": extend_schema(
        summary="Change Anime",
        description="Change all fields of a specific anime entry.",
    ),
    "partial_update": extend_schema(
        summary="Update Anime",
        description="Update some fields of a specific anime entry.",
    ),
    "destroy": extend_schema(
        summary="Remove Anime",
        description="Remove a specific anime entry.",
    ),
}


manga_schemas = {
    "list": extend_schema(
        summary="Get Several Mangas",
        description="Retrieve a list of all manga entries.",
    ),
    "create": extend_schema(
        summary="Create Manga",
        description="Create a new manga entry.",
    ),
    "retrieve": extend_schema(
        summary="Get Manga",
        description="Get detailed information about a specific manga entry.",
    ),
    "update": extend_schema(
        summary="Change Manga",
        description="Change all fields of a specific manga entry.",
    ),
    "partial_update": extend_schema(
        summary="Update Manga",
        description="Update some fields of a specific manga entry.",
    ),
    "destroy": extend_schema(
        summary="Remove Manga",
        description="Remove a specific manga entry.",
    ),
}
