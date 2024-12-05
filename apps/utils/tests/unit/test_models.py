"""Model tests for Utils App."""

import pytest
from django.core.exceptions import ValidationError

from ..factories import PictureFactory, VideoFactory


@pytest.mark.django_db
class TestPictureModel:
    """Tests for Picture model."""

    def test_picture_creation(self, anime):
        picture = PictureFactory.create(content_object=anime)
        assert picture.pk is not None
        assert picture.content_type.model == "anime"
        assert picture.object_id == anime.id
        assert picture.image.name.endswith(".jpg")

    def test_picture_creation_errors(self, producer):
        with pytest.raises(ValidationError, match="Invalid model relationship"):
            PictureFactory.create(content_object=producer)


@pytest.mark.django_db
class TestVideoModel:
    """Tests for Video model."""

    def test_video_creation(self, anime):
        video = VideoFactory.create(content_object=anime)
        assert video.pk is not None
        assert video.content_type.model == "anime"
        assert video.object_id == anime.id

    def test_video_creation_errors(self, producer):
        with pytest.raises(ValidationError, match="Invalid model relationship"):
            VideoFactory.create(content_object=producer)
