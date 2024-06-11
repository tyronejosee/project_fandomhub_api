"""Resources for Producers App."""

from import_export.resources import ModelResource

from .models import Producer


class ProducerResource(ModelResource):
    """Resource definition for Producer model"""

    class Meta:
        model = Producer
