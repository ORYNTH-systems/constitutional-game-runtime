class EnvironmentalProcess:
    process_id = "EP-000"
    name = "Base Environmental Process"

    def evaluate(self, world):
        return {
            "admissible": True,
            "reason": "ADMISSIBLE",
        }

    def execute(self, world):
        raise NotImplementedError


class SeasonalTransitionProcess(EnvironmentalProcess):
    process_id = "EP-001"
    name = "Seasonal Transition"

    SEASON_LENGTH_DAYS = 90

    def evaluate(self, world):
        should_transition = (
            world.environment.day_in_season
            >= self.SEASON_LENGTH_DAYS
        )

        return {
            "admissible": should_transition,
            "reason": (
                "ADMISSIBLE"
                if should_transition
                else "SEASON_NOT_READY"
            ),
            "season": world.environment.season,
            "day_in_season": world.environment.day_in_season,
            "season_length_days": self.SEASON_LENGTH_DAYS,
        }

    def execute(self, world):
        change = world.environment.next_season()

        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "changes": [change],
        }


class WeatherProcess(EnvironmentalProcess):
    process_id = "EP-002"
    name = "Weather Reconstruction"

    WEATHER_BY_SEASON = {
        "Spring": {
            "weather": "Rain",
            "temperature": 18,
            "rainfall": 6,
            "wind": "Light",
        },
        "Summer": {
            "weather": "Clear",
            "temperature": 30,
            "rainfall": 1,
            "wind": "Calm",
        },
        "Autumn": {
            "weather": "Cloudy",
            "temperature": 15,
            "rainfall": 3,
            "wind": "Moderate",
        },
        "Winter": {
            "weather": "Snow",
            "temperature": -2,
            "rainfall": 2,
            "wind": "Strong",
        },
    }

    def evaluate(self, world):
        return {
            "admissible": True,
            "reason": "ADMISSIBLE",
            "season": world.environment.season,
            "climate": world.environment.climate,
            "current_weather": world.environment.weather,
        }

    def execute(self, world):
        profile = self.WEATHER_BY_SEASON[
            world.environment.season
        ]

        previous_weather = world.environment.weather

        world.environment.weather = profile["weather"]
        world.environment.temperature = profile["temperature"]
        world.environment.rainfall = profile["rainfall"]
        world.environment.wind = profile["wind"]

        world.environment.environment_revision += 1

        world.environment.evidence = {
            "event": "weather_updated",
            "season": world.environment.season,
            "climate": world.environment.climate,
            "weather": world.environment.weather,
            "environment_revision": (
                world.environment.environment_revision
            ),
        }

        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "changes": [
                {
                    "environment_metric": "weather",
                    "previous": previous_weather,
                    "new_value": world.environment.weather,
                },
                {
                    "environment_metric": "temperature",
                    "new_value": world.environment.temperature,
                },
                {
                    "environment_metric": "rainfall",
                    "new_value": world.environment.rainfall,
                },
                {
                    "environment_metric": "wind",
                    "new_value": world.environment.wind,
                },
            ],
        }


class ClimateProcess(EnvironmentalProcess):
    process_id = "EP-003"
    name = "Climate Verification"

    def evaluate(self, world):
        admissible = (
            world.environment.climate
            in world.environment.CLIMATES
        )

        return {
            "admissible": admissible,
            "reason": (
                "CLIMATE_STABLE"
                if admissible
                else "INVALID_CLIMATE"
            ),
            "climate": world.environment.climate,
            "valid_climates": list(world.environment.CLIMATES),
        }

    def execute(self, world):
        change = world.environment.update_climate()

        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "changes": [change],
        }