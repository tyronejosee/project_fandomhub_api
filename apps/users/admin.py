"""Admin for Users App."""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.utils.admin import BaseAdmin
from .models import User
from .resources import UserResource


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for User model."""

    ordering = ["username"]
    list_display = ["username", "email", "is_staff", "is_superuser"]
    list_display_links = ["username"]
    search_fields = ["username", "email", "first_name", "last_name"]
    list_filter = ["is_staff", "is_superuser", "is_active"]
    readonly_fields = ["pk"]
    resource_class = UserResource
