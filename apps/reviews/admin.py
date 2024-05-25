"""Admin for Reviews App."""

from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin for Review model."""

    search_fields = ["user"]
    list_display = ["comment", "available"]
    list_filter = ["rating"]
    list_editable = ["available"]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["user"]
