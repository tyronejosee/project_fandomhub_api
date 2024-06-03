"""Functions for Utils App."""

import random
import string


def generate_random_code(length=10):
    """Generates a random code."""
    letters_and_digits = string.ascii_letters + string.digits
    return "".join(random.choice(letters_and_digits) for i in range(min(length, 100)))
