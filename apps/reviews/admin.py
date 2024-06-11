"""Admin for Reviews App."""

from django.contrib import admin

from apps.utils.admin import BaseAdmin
from .models import Review


@admin.register(Review)
class ReviewAdmin(BaseAdmin):
    """Admin for Review model."""

    search_fields = ["user_id"]
    list_display = ["user_id", "comment", "is_available"]
    list_filter = ["rating", "is_spoiler"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
