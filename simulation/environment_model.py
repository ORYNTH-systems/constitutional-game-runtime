class EnvironmentModel:
    """
    Constitutional environmental state.
    """

    SEASONS = (
        "Spring",
        "Summer",
        "Autumn",
        "Winter",
    )

    def __init__(self):
        self.season_index = 0
        self.season = self.SEASONS[self.season_index]

        self.day_in_season = 1

        self.weather = "Clear"
        self.climate = "Temperate"

        self.temperature = 20
        self.rainfall = 0

        self.water_availability = "Normal"
        self.soil_fertility = 100

        self.wind = "Calm"

        self.environment_revision = 0

        self.evidence = {
            "event": "environment_initialized"
        }

    def next_season(self):
        previous = self.season

        self.season_index = (
            self.season_index + 1
        ) % len(self.SEASONS)

        self.season = self.SEASONS[self.season_index]
        self.day_in_season = 1

        self.environment_revision += 1

        self.evidence = {
            "event": "season_changed",
            "previous": previous,
            "current": self.season,
            "environment_revision": self.environment_revision,
        }

        return {
            "environment_metric": "season",
            "previous": previous,
            "new_value": self.season,
        }

    def advance_day(self):
        self.day_in_season += 1

    def __str__(self):
        return (
            f"Season: {self.season}\n"
            f"Day In Season: {self.day_in_season}\n"
            f"Weather: {self.weather}\n"
            f"Climate: {self.climate}\n"
            f"Temperature: {self.temperature}\n"
            f"Rainfall: {self.rainfall}\n"
            f"Water Availability: {self.water_availability}\n"
            f"Soil Fertility: {self.soil_fertility}\n"
            f"Wind: {self.wind}"
        )