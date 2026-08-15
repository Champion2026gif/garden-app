"""garden_advice.py

Gives gardening enthusiasts a short tip based on the current month and
season. Season and tip lookups are data-driven (dictionaries) so new
months or tips can be added without changing any logic.
"""

import datetime

# Maps each calendar month (1-12) to a season name.
SEASON_BY_MONTH = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Spring", 4: "Spring", 5: "Spring",
    6: "Summer", 7: "Summer", 8: "Summer",
    9: "Autumn", 10: "Autumn", 11: "Autumn",
}

# Maps each season to a single gardening tip.
TIPS_BY_SEASON = {
    "Winter": "Protect young plants from frost with mulch.",
    "Spring": "Start planting seeds indoors for later transplant.",
    "Summer": "Water plants early in the morning to reduce evaporation.",
    "Autumn": "Rake fallen leaves and add them to your compost.",
}


def get_season(month):
    """Return the season name for a given calendar month (1-12).

    Args:
        month: An integer from 1 to 12.

    Returns:
        The season name as a string, or "Unknown" if the month is
        not recognised.
    """
    return SEASON_BY_MONTH.get(month, "Unknown")


def get_tip(season):
    """Return the gardening tip for a given season.

    Args:
        season: A season name, e.g. "Winter".

    Returns:
        The tip as a string, or a fallback message if the season is
        not recognised.
    """
    return TIPS_BY_SEASON.get(season, "No tip available.")


def main():
    """Look up today's season and print the matching gardening tip."""
    current_month = datetime.date.today().month
    season = get_season(current_month)
    tip = get_tip(season)
    print(f"{season} gardening tip: {tip}")
    print("Current season: " + season)


if __name__ == "__main__":
    main()
