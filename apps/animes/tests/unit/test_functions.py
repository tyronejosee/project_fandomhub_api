"""Function tests for Animes App."""

import pytest
from freezegun import freeze_time

from ...functions import get_current_season, get_upcoming_season


@pytest.mark.parametrize(
    "frozen_date, expected_season, expected_year",
    [
        ("2024-01-15", "winter", 2024),
        ("2024-04-10", "spring", 2024),
        ("2024-07-25", "summer", 2024),
        ("2024-10-05", "fall", 2024),
    ],
)
def test_get_current_season(frozen_date, expected_season, expected_year):
    with freeze_time(frozen_date):
        season, year = get_current_season()
        assert season == expected_season
        assert year == expected_year


@pytest.mark.parametrize(
    "frozen_date, expected_season, expected_year",
    [
        ("2024-01-15", "spring", 2024),  # January -> Spring 2024
        ("2024-04-10", "summer", 2024),  # April -> Summer 2024
        ("2024-07-25", "fall", 2024),  # July -> Fall 2024
        ("2024-10-05", "winter", 2024),  # October -> Winter 2024
        ("2024-12-15", "winter", 2025),  # December -> Winter 2025
        ("2023-12-31", "winter", 2024),  # December 2023 -> Winter 2024
    ],
)
def test_get_upcoming_season(frozen_date, expected_season, expected_year):
    with freeze_time(frozen_date):
        season, year = get_upcoming_season()
        assert season == expected_season
        assert year == expected_year
