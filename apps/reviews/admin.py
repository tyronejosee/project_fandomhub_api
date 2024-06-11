"""Admin for Reviews App."""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.utils.admin import BaseAdmin
from .models import Review
from .resources import ReviewResource


@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Review model."""

    search_fields = ["user_id"]
    list_display = ["user_id", "comment", "is_available"]
    list_filter = ["rating", "is_spoiler"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = ReviewResource
