"""Admin for Characters App."""

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from import_export.admin import ImportExportModelAdmin

from apps.utils.admin import BaseAdmin
from apps.utils.models import Picture
from .models import Character, CharacterVoice, CharacterAnime, CharacterManga
from .resources import (
    CharacterResource,
    CharacterVoiceResource,
    CharacterAnimeResource,
    CharacterMangaResource,
)


class CharacterVoiceInline(admin.TabularInline):
    model = CharacterVoice
    extra = 1
    autocomplete_fields = ["voice_id"]


class CharacterAnimeInline(admin.TabularInline):
    model = CharacterAnime
    extra = 1
    autocomplete_fields = ["anime_id"]


class CharacterMangaInline(admin.TabularInline):
    model = CharacterManga
    extra = 1
    autocomplete_fields = ["manga_id"]


class PictureInline(GenericTabularInline):
    model = Picture


@admin.register(Character)
class CharacterAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Character model."""

    search_fields = ["name", "name_kanji", "name_rom"]
    list_display = ["name", "is_available"]
    list_filter = ["role"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "slug", "favorites", "created_at", "updated_at"]
    inlines = [
        PictureInline,
        CharacterVoiceInline,
        CharacterAnimeInline,
        CharacterMangaInline,
    ]
    resource_class = CharacterResource


@admin.register(CharacterVoice)
class CharacterVoiceAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for CharacterVoice model."""

    search_fields = [
        "character_id__name",
        "voice_id__name",
        "anime_id__name",
        "manga_id__name",
    ]
    list_display = ["character_id", "voice_id", "is_available"]
    list_filter = ["character_id"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = CharacterVoiceResource


@admin.register(CharacterAnime)
class CharacterAnimeAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for CharacterAnime model."""

    search_fields = ["character_id__name", "anime_id__name"]
    list_display = ["character_id", "anime_id", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = CharacterAnimeResource


@admin.register(CharacterManga)
class CharacterMangaAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for CharacterManga model."""

    search_fields = ["character_id__name", "manga_id__name"]
    list_display = ["character_id", "manga_id", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = CharacterMangaResource
