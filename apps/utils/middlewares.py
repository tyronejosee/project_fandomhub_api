"""Middlewares for Utils App."""

from rest_framework.response import Response
from rest_framework import status


CENSORED_WORDS = [
    "Hentai",
    "Lolis",
]


class CensorshipMiddleware:
    """Middleware for censoring words in requests."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST":
            try:
                text = request.data["name"]   # Fix request
            except AttributeError:
                text = request.POST.get("name", "")   # Fix request

            for word in CENSORED_WORDS:
                if word in text:
                    return Response(
                        {'detail': f'Censored text: {word}'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

        response = self.get_response(request)
        return response
