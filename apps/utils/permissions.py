"""Permissions for Utils App."""

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    """Allows access only to staff users."""

    def has_permission(self, request, view):
        is_safe_method = request.method in SAFE_METHODS
        is_staff = request.user and request.user.is_staff
        return bool(is_safe_method or is_staff)


class IsOwner(BasePermission):
    """Allows access only allow owners of an object to access it."""

    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user)
