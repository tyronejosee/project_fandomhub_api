"""Admin for Persons App."""

from django.contrib import admin

from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Admin for Author model."""

    list_per_page = 25
    search_fields = [
        "name",
    ]
    list_display = [
        "name",
        "available",
    ]
    list_filter = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "-created_at",
    ]
