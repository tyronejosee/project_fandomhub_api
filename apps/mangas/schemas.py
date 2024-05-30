"""Schemas for Mangas App."""

from drf_spectacular.utils import extend_schema


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
