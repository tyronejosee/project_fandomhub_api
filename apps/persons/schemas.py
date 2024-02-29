"""Schemas for Persons App."""

from drf_spectacular.utils import extend_schema


author_schemas = {
    "list": extend_schema(
        summary="Get Several Authors",
        description="Retrieve a list of all author entries.",
    ),
    "create": extend_schema(
        summary="Create Author",
        description="Create a new author entry.",
    ),
    "retrieve": extend_schema(
        summary="Get Author",
        description="Get detailed information about a specific author entry.",
    ),
    "update": extend_schema(
        summary="Change Author",
        description="Change all fields of a specific author entry.",
    ),
    "partial_update": extend_schema(
        summary="Update Author",
        description="Update some fields of a specific author entry.",
    ),
    "destroy": extend_schema(
        summary="Remove Author",
        description="Remove a specific author entry.",
    ),
}
