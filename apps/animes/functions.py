"""Functions for Animes App."""

from django.utils import timezone


# Winter Season (January-March)
# Spring Season (April-June)
# Summer Season (July-September)
# Fall Season (October-December)


def get_current_season():
    now = timezone.now()  # Format: 2024-06-12 20:32:16.759526+00:00
    year = now.year  # Example: 2024
    month = now.month  # Example: 6

    if month in [1, 2, 3]:
        season = "winter"
    elif month in [4, 5, 6]:
        season = "spring"
    elif month in [7, 8, 9]:
        season = "summer"
    else:  # [10, 11, 12]
        season = "fall"

    return season, year


def get_upcoming_season():
    now = timezone.now()  # Format: 2024-06-12 20:32:16.759526+00:00
    year = now.year  # Example: 2024
    month = now.month  # Example: 6

    if month in [1, 2, 3]:
        season = "spring"
    elif month in [4, 5, 6]:
        season = "summer"
    elif month in [7, 8, 9]:
        season = "fall"
    else:  # [10, 11, 12]
        season = "winter"
        if month == 12:
            year += 1  # Move to the next year if December

    return season, year
