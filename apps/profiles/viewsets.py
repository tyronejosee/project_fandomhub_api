"""ViewSets for Profiles App."""

from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.utils.permissions import IsOwner
from .models import Profile
from .serializers import ProfileReadSerializer, ProfileWriteSerializer


class ProfileViewSet(ViewSet):
    """
    ViewSet for retrieving and updating user profiles.
    """

    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, request):
        # Get a profile instance by user
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        if profile.user != user:
            return Response(
                {"detail": "You are not the owner of this profile."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return profile

    def retrieve(self, request, *args, **kwargs):
        # Retrieve profile of the user
        profile = self.get_object(request)
        serializer = ProfileReadSerializer(profile)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        #  Update profile of the user
        profile = self.get_object(request)
        serializer = ProfileWriteSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
