"""Serializers for Playlists App."""

from rest_framework import serializers

from .models import Playlist, PlaylistItem


class PlaylistReadSerializer(serializers.ModelSerializer):
    """Serializer for Playlist model (List/retrieve)."""

    # tags

    class Meta:
        model = Playlist
        fields = [
            "id",
            "name",
            "description",
            "tags",
            "number_items",
            "cover",
            "is_public",
            "created_at",
            "updated_at",
        ]


class PlaylistWriteSerializer(serializers.ModelSerializer):
    """Serializer for Playlist model (Create/update)."""

    class Meta:
        model = Playlist
        fields = [
            "name",
            "description",
            "is_public",
            "tags",
            "cover",
        ]


class PlaylistItemReadSerializer(serializers.ModelSerializer):
    """Pending."""

    class Meta:
        model = PlaylistItem
        fields = "__all__"


class PlaylistItemWriteSerializer(serializers.ModelSerializer):
    """Pending."""

    class Meta:
        model = PlaylistItem
        fields = "__all__"


# class PlaylistAnimeSerializer(serializers.ModelSerializer):
#     """Serializer for PlaylistAnime model."""

#     anime_id = serializers.UUIDField(write_only=True)
#     anime = AnimeMinimumSerializer(read_only=True)

#     class Meta:
#         model = PlaylistAnime
#         fields = [
#             "id",
#             "anime",
#             "anime_id",
#             "status",
#             "is_watched",
#             "is_favorite",
#         ]  # Add order field

#         def create(self, validated_data):
#             anime_id = validated_data.pop("anime_id")
#             anime = get_object_or_404(Anime, id=anime_id)
#             playlist_anime = PlaylistAnime.objects.create(
#                 anime=anime,
#                 **validated_data,
#             )
#             return playlist_anime


# class PlaylistMangaSerializer(serializers.ModelSerializer):
#     """Serializer for PlaylistManga model."""

#     manga_id = serializers.UUIDField(write_only=True)
#     manga = MangaMinimumSerializer(read_only=True)

#     class Meta:
#         model = PlaylistManga
#         fields = [
#             "id",
#             "manga",
#             "manga_id",
#             "status",
#             "is_watched",
#             "is_favorite",
#         ]  # Add order field

#         def create(self, validated_data):
#             manga_id = validated_data.pop("manga_id")
#             manga = get_object_or_404(Manga, id=manga_id)
#             playlist_manga = PlaylistManga.objects.create(
#                 manga=manga,
#                 **validated_data,
#             )
#             return playlist_manga
