"""Admin for Profiles App."""

from django.contrib import admin
from apps.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin config for Profile model."""
