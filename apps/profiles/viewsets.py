"""ViewSets for Profiles App."""

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.utils.permissions import IsOwner
from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """
    ViewSet for managing Profile instances.

    Endpoints:
    - GET /api/v1/profiles/{id}/
    - PUT /api/v1/profiles/{id}/
    - PATCH /api/v1/profiles/{id}/
    """

    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.get_by_user(user)

    @action(detail=False, methods=["get"], url_path="me")
    def me_detail(self, request, pk=None):
        """
        Action returns the detail of the authenticated profile.

        Endpoints:
        - GET /api/v1/profiles/me/
        """
        profile = self.get_queryset()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
