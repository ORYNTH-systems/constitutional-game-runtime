class PopulationModel:
    """
    Constitutional population state.
    """

    def __init__(self):
        self.total = 100
        self.health = 100
        self.hunger_pressure = 0

    def increase_hunger_pressure(self, amount):
        self.hunger_pressure += amount

        return {
            "population_metric": "hunger_pressure",
            "change": amount,
            "new_value": self.hunger_pressure,
        }

    def reduce_hunger_pressure(self, amount):
        self.hunger_pressure = max(
            0,
            self.hunger_pressure - amount,
        )

        return {
            "population_metric": "hunger_pressure",
            "change": -amount,
            "new_value": self.hunger_pressure,
        }

    def update_health(self):
        """
        Population health is reduced by accumulated
        constitutional hunger pressure.
        """

        previous = self.health

        if self.hunger_pressure > 0:
            self.health = max(
                0,
                self.health - self.hunger_pressure,
            )
        else:
            self.health = min(
                100,
                self.health + 1,
            )

        return {
            "population_metric": "health",
            "previous": previous,
            "new_value": self.health,
        }

    def __str__(self):
        return (
            f"Population: {self.total}\n"
            f"Health: {self.health}\n"
            f"Hunger Pressure: {self.hunger_pressure}"
        )