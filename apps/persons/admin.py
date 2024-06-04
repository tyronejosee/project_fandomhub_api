"""Admin for Persons App."""

from django.contrib import admin

from .models import Person, StaffAnime


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Admin for Person model."""

    ordering = ["-created_at"]
    list_per_page = 25
    search_fields = [
        "name",
    ]
    list_display = [
        "name",
        "category",
        "available",
    ]
    list_filter = [
        "available",
        "category",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "created_at",
        "updated_at",
    ]


@admin.register(StaffAnime)
class StaffAnimeAdmin(admin.ModelAdmin):
    """Admin for StaffAnime model."""

    list_per_page = 25
    search_fields = [
        "person_id",
        "anime_id",
    ]
    list_display = [
        "person_id",
        "anime_id",
        "available",
    ]
    list_filter = [
        "anime_id",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
