"""Throttles for Utils App."""

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class AnonUserThrottle(AnonRateThrottle):
    """Throttle class for anon users (100 requests/day)."""
    scope = "anon"
    THROTTLE_RATES = {"anon": "100/day"}


class AuthUserThrottle(UserRateThrottle):
    """Throttle class for auth users (1000 requests/day)."""
    scope = "user"
    THROTTLE_RATES = {"user": "1000/day"}


class StaffUserThrottle(UserRateThrottle):
    """Throttle class for staff (no limits)."""
    scope = "staff"
    THROTTLE_RATES = {"staff": None}

    def allow_request(self, request, view):
        user_is_staff = request.user and request.user.is_staff
        return user_is_staff or super().allow_request(request, view)
