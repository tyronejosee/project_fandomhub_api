"""Schemas for Seasons App."""

from drf_spectacular.utils import extend_schema


season_schemas = {
    "list": extend_schema(
        summary="Get Several Seasons",
        description="Retrieve a list of all season entries.",
    ),
    "create": extend_schema(
        summary="Create Season",
        description="Create a new season entry.",
    ),
    "retrieve": extend_schema(
        summary="Get Season",
        description="Get detailed information about a specific season entry.",
    ),
    "update": extend_schema(
        summary="Change Season",
        description="Change all fields of a specific season entry.",
    ),
    "partial_update": extend_schema(
        summary="Update Season",
        description="Update some fields of a specific season entry.",
    ),
    "destroy": extend_schema(
        summary="Remove Season",
        description="Remove a specific season entry.",
    ),
}
