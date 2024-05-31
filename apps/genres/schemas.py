"""Schemas for Genres App."""

from drf_spectacular.utils import extend_schema


genre_schemas = {
    "list": extend_schema(
        summary="Get Several Genres",
        description="Retrieve a list of all genre entries.",
    ),
    "create": extend_schema(
        summary="Create Genre",
        description="Create a new genre entry.",
    ),
    "retrieve": extend_schema(
        summary="Get Genre",
        description="Get detailed information about a specific genre entry.",
    ),
    "update": extend_schema(
        summary="Change Genre",
        description="Change all fields of a specific genre entry.",
    ),
    "partial_update": extend_schema(
        summary="Update Genre",
        description="Update some fields of a specific genre entry.",
    ),
    "destroy": extend_schema(
        summary="Remove Genre",
        description="Remove a specific genre entry.",
    ),
}
