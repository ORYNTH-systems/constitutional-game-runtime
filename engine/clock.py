class SimulationClock:

    def __init__(self):
        self.tick = 0

    def advance(self):
        self.tick += 1
        return self.tick
