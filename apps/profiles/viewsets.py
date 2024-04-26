"""ViewSets for Profiles App."""

# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from django.views.decorators.vary import vary_on_cookie
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin)
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(RetrieveModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     GenericViewSet):
    """
    Viewset for managing Profile instances.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    ordering = ["id"]

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.get_available().filter(user=user)

    # @method_decorator(cache_page(60 * 60 * 2))
    # @method_decorator(vary_on_cookie)
    # def retrieve(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
