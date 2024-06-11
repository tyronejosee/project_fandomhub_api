"""Admin for Characters App."""

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from apps.utils.admin import BaseAdmin
from apps.utils.models import Picture
from .models import Character, CharacterVoice, CharacterAnime, CharacterManga


class PictureInline(GenericTabularInline):
    model = Picture


@admin.register(Character)
class CharacterAdmin(BaseAdmin):
    """Admin for Character model."""

    search_fields = ["name", "name_kanji", "name_rom"]
    list_display = ["name", "is_available"]
    list_filter = ["role"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "slug", "favorites", "created_at", "updated_at"]
    inlines = [PictureInline]


@admin.register(CharacterVoice)
class CharacterVoiceAdmin(BaseAdmin):
    """Admin for CharacterVoice model."""

    search_fields = ["character_id__name", "voice_id__name"]
    list_display = ["character_id", "voice_id", "is_available"]
    list_filter = ["character_id"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(CharacterManga)
class CharacterMangaAdmin(BaseAdmin):
    """Admin for CharacterManga model."""

    search_fields = ["character_id__name", "manga_id__name"]
    list_display = ["character_id", "manga_id", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]


@admin.register(CharacterAnime)
class CharacterAnimeAdmin(BaseAdmin):
    """Admin for CharacterAnime model."""

    search_fields = ["character_id__name", "anime_id__name"]
    list_display = ["character_id", "anime_id", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
