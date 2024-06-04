"""ViewSets for Clubs App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from apps.utils.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.users.permissions import IsMember
from apps.utils.pagination import LargeSetPagination
from .models import Club, ClubMember
from .serializers import (
    ClubReadSerializer,
    ClubWriteSerializer,
    ClubMemberReadSerializer,
)


class ClubViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Club instances.

    Endpoints:
    - GET /api/v1/clubs/
    - POST /api/v1/clubs/
    - GET /api/v1/clubs/{id}/
    - PUT /api/v1/clubs/{id}/
    - PATCH /api/v1/clubs/{id}/
    - DELETE /api/v1/clubs/{id}/
    """

    permission_classes = [IsMember]
    serializer_class = ClubWriteSerializer
    pagination_class = LargeSetPagination
    search_fields = ["name", "category"]
    ordering_fields = ["name", "category", "members"]

    def get_queryset(self):
        return Club.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ClubReadSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=["get"], url_path="members")
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def member_list(self, request, pk=None):
        """
        Retrieve a list of members for club.

        Endpoints:
        - GET /api/v1/clubs/{id}/members/
        """
        club = self.get_object()
        members = ClubMember.objects.filter(club=club).only("user", "joined_at")
        if members.exists():
            serializer = ClubMemberReadSerializer(members, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No members found."}, status=status.HTTP_404_NOT_FOUND
        )

    # TODO: Add logic and list all the staff, GET clubs/{id}/staff
    # TODO: Add logic and list all relationships, GET clubs/{id}/relations
