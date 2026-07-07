class PopulationModel:
    """
    Constitutional population state.
    """

    def __init__(self):
        self.total = 100
        self.hunger_pressure = 0

    def increase_hunger_pressure(self, amount):
        self.hunger_pressure += amount
        return {
            "population_metric": "hunger_pressure",
            "change": amount,
            "new_value": self.hunger_pressure,
        }

    def reduce_hunger_pressure(self, amount):
        self.hunger_pressure = max(0, self.hunger_pressure - amount)
        return {
            "population_metric": "hunger_pressure",
            "change": -amount,
            "new_value": self.hunger_pressure,
        }

    def __str__(self):
        return (
            f"Population: {self.total}\n"
            f"Hunger Pressure: {self.hunger_pressure}"
        )