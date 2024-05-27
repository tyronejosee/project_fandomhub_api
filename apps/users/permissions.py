"""Permissions for Users App."""

from rest_framework.permissions import BasePermission

from .choices import RoleChoices


class BaseRolePermission(BasePermission):
    """
    Base permission class that checks if a user has a specific role.
    """

    required_roles = []

    def has_permission(self, request, view):
        is_user_authenticated = request.user and request.user.is_authenticated
        is_user_valid = (
            request.user.is_active and request.user.role in self.required_roles
        )
        return bool(is_user_authenticated and is_user_valid)


class IsMember(BaseRolePermission):
    """
    Allows access only to users with the role "member".
    """

    required_roles = [
        RoleChoices.MEMBER,
        RoleChoices.ADMINISTRATOR,
    ]


class IsPremium(BaseRolePermission):
    """
    Allows access only to users with the role "premium".
    """

    required_roles = [
        RoleChoices.PREMIUM,
        RoleChoices.ADMINISTRATOR,
    ]


class IsContributor(BaseRolePermission):
    """
    Allows access only to users with the role "contributor".
    """

    required_roles = [
        RoleChoices.CONTRIBUTOR,
        RoleChoices.ADMINISTRATOR,
    ]


class IsModerator(BaseRolePermission):
    """
    Allows access only to users with the role "moderator".
    """

    required_roles = [
        RoleChoices.MODERATOR,
        RoleChoices.ADMINISTRATOR,
    ]


class IsAdministrator(BaseRolePermission):
    """
    Allows access only to users with the role "administrator".
    """

    required_roles = [
        RoleChoices.ADMINISTRATOR,
    ]
