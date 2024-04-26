"""Admin for Profiles App."""

from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin config for Profile model."""
    search_fields = ["user",]
    list_display = ["user", "available"]
    list_editable = ["available"]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["created_at",]
