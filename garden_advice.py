"""
Garden Advice Program
Gives simple gardening tips based on the season and plant type.
"""

# Hardcoded values for the season and plant type
season = "summer"       # TODO (Issue 2): replace with input() for user interaction
plant_type = "flower"   # TODO (Issue 2): replace with input() for user interaction


def get_season_advice(season):
    """
    Return watering/protection advice for the given season.

    Parameters:
        season (str): the current season, e.g. "summer" or "winter"

    Returns:
        str: one line of advice about caring for plants in that season
    """
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """
    Return care advice for the given plant type.

    Parameters:
        plant_type (str): the type of plant, e.g. "flower" or "vegetable"

    Returns:
        str: one line of advice for caring for that plant type
    """
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def build_advice(season, plant_type):
    """Combine season advice and plant advice into one message."""
    return get_season_advice(season) + get_plant_advice(plant_type)


# Generate and print the advice
advice = build_advice(season, plant_type)
print(advice)