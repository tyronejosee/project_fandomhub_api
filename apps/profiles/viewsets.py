"""ViewSets for Profiles App."""

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from apps.users.permissions import IsAdministrator, IsMember
from .models import Profile
from .serializers import (
    ProfileReadSerializer,
    ProfileWriteSerializer,
    ProfileMinimalSerializer,
)


class ProfileViewset(ModelViewSet):
    """
    ViewSet for managing Profiles instances.

    Endpoints:
    - GET /api/v1/profiles/
    - POST /api/v1/profiles/
    - GET /api/v1/profiles/{id}/
    - PUT /api/v1/profiles/{id}/
    - PATCH /api/v1/profiles/{id}/
    - DELETE /api/v1/profiles/{id}/
    """

    permission_classes = [IsAdministrator]
    serializer_class = ProfileWriteSerializer
    search_fields = ["user_id__username", "first_name", "last_name"]
    ordering_fields = ["first_name"]

    def get_queryset(self):
        return Profile.objects.get_available()

    def get_serializer_class(self):
        if self.action == "list":
            return ProfileMinimalSerializer
        elif self.action == "retrieve":
            return ProfileReadSerializer
        return super().get_serializer_class()

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[IsMember],
        url_path="my-profile",
    )
    def get_my_profile(self, request):
        """
        Action to retrieve the profile of the current user.

        Endpoints:
        - GET api/v1/profiles/my-profile/
        """
        profile = self.request.user.profile
        serializer = ProfileReadSerializer(profile)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["patch"],
        permission_classes=[IsMember],
        url_path="update-profile",
    )
    def update_user_profile(self, request, *args, **kwargs):
        """
        Action to update the profile of the current user.

        Endpoints:
        - PATCH api/v1/profiles/update-profile/
        """
        profile = self.request.user.profile
        serializer = ProfileWriteSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
