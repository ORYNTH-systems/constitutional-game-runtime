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
