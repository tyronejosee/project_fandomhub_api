"""Functions for Utils App."""

import time
import random
import string
from django.core.files.uploadedfile import SimpleUploadedFile
from functools import wraps
from io import BytesIO
from PIL import Image


def generate_random_code(length=10):
    """Generates a random code."""
    letters_and_digits = string.ascii_letters + string.digits
    return "".join(random.choice(letters_and_digits) for i in range(min(length, 100)))


def execution_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time:.2f}s")
        return result

    return wrapper


def generate_test_image(name="test_image.jpg", size=(1000, 1000), format="JPEG"):
    """
    Generates a valid image for tests.
    """
    storage = BytesIO()
    img = Image.new("RGB", size, color=(255, 0, 0))  # Red image
    img.save(storage, format)
    storage.seek(0)

    return SimpleUploadedFile(
        name=name, content=storage.getvalue(), content_type=f"image/{format.lower()}"
    )
