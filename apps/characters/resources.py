"""Resources for Characters App."""

from import_export.resources import ModelResource

from .models import Character, CharacterVoice, CharacterAnime, CharacterManga


class CharacterResource(ModelResource):
    """Resource definition for Character model"""

    class Meta:
        model = Character


class CharacterVoiceResource(ModelResource):
    """Resource definition for CharacterVoice model"""

    class Meta:
        model = CharacterVoice


class CharacterAnimeResource(ModelResource):
    """Resource definition for CharacterAnime model"""

    class Meta:
        model = CharacterAnime


class CharacterMangaResource(ModelResource):
    """Resource definition for CharacterManga model"""

    class Meta:
        model = CharacterManga
