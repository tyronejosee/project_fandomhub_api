"""Admin for Profiles App."""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.utils.admin import BaseAdmin
from .models import Profile
from .resources import ProfileResource


@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Profile model."""

    ordering = ["created_at"]
    search_fields = ["user_id"]
    list_display = ["user_id", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = ProfileResource
