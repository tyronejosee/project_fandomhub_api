"""Schemas for Studios App."""

from drf_spectacular.utils import extend_schema


studio_schemas = {
    "list": extend_schema(
        summary="Get Several Studios",
        description="Retrieve a list of all studio entries.",
    ),
    "create": extend_schema(
        summary="Create Studio",
        description="Create a new studio entry.",
    ),
    "retrieve": extend_schema(
        summary="Get Studio",
        description="Get detailed information about a specific studio entry.",
    ),
    "update": extend_schema(
        summary="Change Studio",
        description="Change all fields of a specific studio entry.",
    ),
    "partial_update": extend_schema(
        summary="Update Studio",
        description="Update some fields of a specific studio entry.",
    ),
    "destroy": extend_schema(
        summary="Remove Studio",
        description="Remove a specific studio entry.",
    ),
}
