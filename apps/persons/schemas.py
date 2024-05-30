"""Schemas for Persons App."""

from drf_spectacular.utils import extend_schema


person_schemas = {
    "list": extend_schema(
        summary="Get Several Persons",
        description="Retrieve a list of all person entries.",
    ),
    "create": extend_schema(
        summary="Create Person",
        description="Create a new person entry.",
    ),
    "retrieve": extend_schema(
        summary="Get Person",
        description="Get detailed information about a specific person entry.",
    ),
    "update": extend_schema(
        summary="Change Person",
        description="Change all fields of a specific person entry.",
    ),
    "partial_update": extend_schema(
        summary="Update Person",
        description="Update some fields of a specific person entry.",
    ),
    "destroy": extend_schema(
        summary="Remove Person",
        description="Remove a specific person entry.",
    ),
}
