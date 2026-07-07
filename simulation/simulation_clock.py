class SimulationClock:
    """
    Constitutional simulation clock.
    """

    def __init__(self):
        self.tick = 0
        self.day = 1
        self.season = "Spring"
        self.year = 1

    def advance(self):
        self.tick += 1
        self.day += 1

    def __str__(self):
        return (
            f"Year: {self.year}\n"
            f"Season: {self.season}\n"
            f"Day: {self.day}\n"
            f"Tick: {self.tick}"
        )