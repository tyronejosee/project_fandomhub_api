"""Admin for Reviews App."""

from django.contrib import admin

from .models import ReviewAnime, ReviewManga


@admin.register(ReviewAnime)
class ReviewAnimeAdmin(admin.ModelAdmin):
    """Admin for ReviewAnime model."""
    search_fields = ["user"]
    list_display = ["comment", "available"]
    list_filter = ["rating",]
    list_editable = ["available",]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["user",]


@admin.register(ReviewManga)
class ReviewMangaAdmin(admin.ModelAdmin):
    """Admin for ReviewManga model."""
    search_fields = ["user"]
    list_display = ["comment", "available"]
    list_filter = ["rating",]
    list_editable = ["available",]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["user",]
