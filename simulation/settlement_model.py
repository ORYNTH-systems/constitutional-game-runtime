class SettlementModel:
    """
    Constitutional settlement state.
    """

    STAGES = (
        "Nomadic",
        "Village",
        "Town",
        "City",
        "Metropolis",
    )

    def __init__(self):
        self.stage_index = 0
        self.stage = self.STAGES[self.stage_index]

        self.capacity = 100

        self.revision = 0

        self.evidence = {
            "event": "settlement_initialized",
            "stage": self.stage,
            "capacity": self.capacity,
        }

    def advance_stage(self):
        previous = self.stage

        if self.stage_index < len(self.STAGES) - 1:
            self.stage_index += 1

        self.stage = self.STAGES[self.stage_index]

        self.capacity += 100

        self.revision += 1

        self.evidence = {
            "event": "settlement_advanced",
            "previous": previous,
            "current": self.stage,
            "capacity": self.capacity,
            "revision": self.revision,
        }

        return {
            "settlement_metric": "stage",
            "previous": previous,
            "new_value": self.stage,
        }

    def __str__(self):
        return (
            f"Settlement: {self.stage}\n"
            f"Capacity: {self.capacity}"
        )