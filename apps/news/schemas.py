"""Schemas for News App."""

from drf_spectacular.utils import extend_schema


new_schemas = {
    "list": extend_schema(
        summary="Get Several News",
        description="Retrieve a list of all new entries.",
    ),
    "retrieve": extend_schema(
        summary="Get New",
        description="Get detailed information about a specific new entry.",
    ),
}
