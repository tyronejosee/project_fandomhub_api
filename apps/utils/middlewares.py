"""Middlewares for Utils App."""

import time
import logging
from django.utils.translation import gettext as _
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """Middleware to capture logs from the request."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the response time between the request and the response
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time

        # Calculate the content length if available
        content_length = (
            len(response.content) if hasattr(response, "content") else "N/A"
        )

        logger.info(
            f"Request: {request.method} {request.path} {request.META.get('SERVER_PROTOCOL')} {response.status_code} {content_length} {duration:.3f}s"
        )

        return response


class CensorshipMiddleware:
    """Middleware for censoring words in requests."""

    CENSORED_WORDS = [
        "Hentai",
        "Lolis",
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST":
            try:
                text = request.data["name"]  # Fix request
            except AttributeError:
                text = request.POST.get("name", "")  # Fix request

            for word in self.CENSORED_WORDS:
                if word in text:
                    return Response(
                        {"detail": _(f"Censored text: {word}")},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

        response = self.get_response(request)
        return response
