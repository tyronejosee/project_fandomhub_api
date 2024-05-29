"""Admin for Clubs App."""

from django.contrib import admin

from .models import Club, ClubMember, Event, Topic, Discussion


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    """Admin for Club model."""

    ordering = ["-created_at"]
    list_per_page = 25
    search_fields = [
        "name",
    ]
    list_display = [
        "name",
        "members",
        "is_public",
        "available",
    ]
    list_filter = [
        "available",
        "is_public",
        "category",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "created_at",
        "updated_at",
    ]


@admin.register(ClubMember)
class ClubMemberAdmin(admin.ModelAdmin):
    """Admin for ClubMember model."""

    ordering = ["-created_at"]
    list_per_page = 25
    search_fields = [
        "club",
        "user",
    ]
    list_display = [
        "club",
        "user",
        "available",
    ]
    list_filter = [
        "available",
        "club",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin for Event model."""

    ordering = ["-created_at"]
    list_per_page = 25
    search_fields = [
        "name",
    ]
    list_display = [
        "club",
        "name",
        "available",
    ]
    list_filter = [
        "available",
        "club",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """Admin for Topic model."""

    ordering = ["-created_at"]
    list_per_page = 25
    search_fields = [
        "name",
    ]
    list_display = [
        "club",
        "available",
    ]
    list_filter = [
        "available",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]


@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    """Admin for Discussion model."""

    ordering = ["-created_at"]
    list_per_page = 25
    search_fields = [
        "topic",
    ]
    list_display = [
        "topic",
        "content",
        "available",
    ]
    list_filter = [
        "available",
        "topic",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
