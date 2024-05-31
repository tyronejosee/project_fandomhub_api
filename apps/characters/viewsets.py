"""ViewSets for Characters App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from apps.utils.mixins import LogicalDeleteMixin
from apps.users.permissions import IsContributor
from .models import Character
from .serializers import CharacterReadSerializer, CharacterWriteSerializer


class CharacterViewSet(LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Characters instances.

    Endpoints:
    - GET /api/v1/characters/
    - POST /api/v1/characters/
    - GET /api/v1/characters/{id}/
    - PUT /api/v1/characters/{id}/
    - PATCH /api/v1/characters/{id}/
    - DELETE /api/v1/characters/{id}/
    """

    serializer_class = CharacterWriteSerializer
    search_fields = ["name", "name_kanji"]
    ordering_fields = ["name", "role"]

    def get_queryset(self):
        return Character.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsContributor()]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CharacterReadSerializer
        return super().get_serializer_class()

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # @action(detail=True, methods=["get"], url_path="voices")
    # def voices(self, request, pk=None):
    #     character = self.get_object()
    #     voices = CharacterVoice.objects.filter(character_id=character)
    #     serializer = CharacterVoiceSerializer(voices, many=True)
    #     return Response(serializer.data)
