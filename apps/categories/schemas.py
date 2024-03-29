"""Schemas for Contents App."""

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


theme_schemas = {
    "list": extend_schema(
        summary="Get Several Themes",
        description="Retrieve a list of all theme entries.",
    ),
    "create": extend_schema(
        summary="Create Theme",
        description="Create a new theme entry.",
    ),
    "retrieve": extend_schema(
        summary="Get Theme",
        description="Get detailed information about a specific theme entry.",
    ),
    "update": extend_schema(
        summary="Change Theme",
        description="Change all fields of a specific theme entry.",
    ),
    "partial_update": extend_schema(
        summary="Update Theme",
        description="Update some fields of a specific theme entry.",
    ),
    "destroy": extend_schema(
        summary="Remove Theme",
        description="Remove a specific theme entry.",
    ),
}


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


demographic_schemas = {
    "list": extend_schema(
        summary="Get Several Demographics",
        description="Retrieve a list of all demographic entries.",
    ),
    "create": extend_schema(
        summary="Create Demographic",
        description="Create a new demographic entry.",
    ),
    "retrieve": extend_schema(
        summary="Get Demographic",
        description="Get detailed info about a specific demographic entry.",
    ),
    "update": extend_schema(
        summary="Change Demographic",
        description="Change all fields of a specific demographic entry.",
    ),
    "partial_update": extend_schema(
        summary="Update Demographic",
        description="Update some fields of a specific demographic entry.",
    ),
    "destroy": extend_schema(
        summary="Remove Demographic",
        description="Remove a specific demographic entry.",
    ),
}
