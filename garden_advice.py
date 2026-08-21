"""
Garden Advice Program
Gives gardening tips based on the season and plant type entered by the user,
and suggests plants suited to that season.
"""

# Dictionary of advice, replacing the if/elif chains
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}

# Plants that thrive per season, for the suggestion feature
SEASON_PLANT_SUGGESTIONS = {
    "summer": ["Sunflowers", "Tomatoes", "Basil"],
    "winter": ["Pansies", "Kale", "Broccoli"],
}


def get_season_advice(season):
    """Look up season-based advice, with a fallback for unknown seasons."""
    return SEASON_ADVICE.get(season, "No advice for this season.\n")


def get_plant_advice(plant_type):
    """Look up plant-based advice, with a fallback for unknown plant types."""
    return PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")


def get_plant_suggestions(season):
    """Return a list of plants suited to the given season, or an empty list."""
    return SEASON_PLANT_SUGGESTIONS.get(season, [])


def build_advice(season, plant_type):
    """Combine season advice and plant advice into one message."""
    return get_season_advice(season) + get_plant_advice(plant_type)


def main():
    """Ask the user for their season and plant type, then show advice."""
    season = input("Enter the current season (summer/winter): ").strip().lower()
    plant_type = input("Enter the plant type (flower/vegetable): ").strip().lower()

    advice = build_advice(season, plant_type)
    print(advice)

    suggestions = get_plant_suggestions(season)
    if suggestions:
        print(f"Plants that thrive in {season}: {', '.join(suggestions)}")


if __name__ == "__main__":
    main()