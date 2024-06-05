"""Schemas for News App."""

from drf_spectacular.utils import extend_schema


news_schemas = {
    "list": extend_schema(
        summary="Get Several News",
        description="Retrieve a list of all news entries.",
    ),
    "retrieve": extend_schema(
        summary="Get News",
        description="Get detailed information about a specific news entry.",
    ),
}
