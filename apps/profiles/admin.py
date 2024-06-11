"""Admin for Profiles App."""

from django.contrib import admin

from apps.utils.admin import BaseAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(BaseAdmin):
    """Admin for Profile model."""

    ordering = ["created_at"]
    search_fields = ["user_id"]
    list_display = ["user_id", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
