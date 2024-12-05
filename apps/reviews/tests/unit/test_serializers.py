"""Serializer Tests for Reviews App."""

import pytest

from ...serializers import ReviewReadSerializer, ReviewWriteSerializer


@pytest.mark.django_db
class TestReviewSerializers:
    """Tests for Review serializers."""

    def test_review_read_serializer(self, review):
        serializer = ReviewReadSerializer(review)
        expected_data = {
            "id": str(review.id),
            "user_id": str(review.user_id),
            "rating": review.rating,
            "comment": review.comment,
            "is_spoiler": review.is_spoiler,
            "helpful_count": review.helpful_count,
            "created_at": review.created_at.isoformat(),
            "updated_at": review.updated_at.isoformat(),
        }
        assert serializer.data == expected_data

    def test_review_write_serializer_valid_data(self, review):
        data = {
            "comment": "Lorem ipsum",
            "is_spoiler": review.is_spoiler,
            "rating": review.rating,
        }
        serializer = ReviewWriteSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        assert serializer.validated_data["comment"] == "Lorem ipsum"

    def test_review_write_serializer_invalid_data(self):
        data = {}
        serializer = ReviewWriteSerializer(data=data)
        assert not serializer.is_valid()
        assert "comment" in serializer.errors
        assert "rating" in serializer.errors
