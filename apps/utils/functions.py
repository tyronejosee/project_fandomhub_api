"""Functions for Utils App."""

import time
import random
import string
from functools import wraps


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
