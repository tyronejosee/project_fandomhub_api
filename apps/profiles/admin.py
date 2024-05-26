"""Admin for Profiles App."""

from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin for Profile model."""

    list_per_page = 25
    ordering = ["created_at"]
    search_fields = [
        "user",
    ]
    list_display = [
        "user",
        "available",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
