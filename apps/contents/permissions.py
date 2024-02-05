"""Permissions for Contents App."""

from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in ['GET', 'HEAD', 'OPTIONS'] or (request.user and request.user.is_staff)
        )
