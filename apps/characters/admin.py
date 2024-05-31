"""Admin for Characters App."""

from django.contrib import admin

from .models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    """Admin for Character model."""

    list_per_page = 25
    search_fields = [
        "name",
        "name_kanji",
        "name_rom",
    ]
    list_display = [
        "name",
        "available",
    ]
    list_filter = [
        "role",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "favorites",
        "created_at",
        "updated_at",
    ]
