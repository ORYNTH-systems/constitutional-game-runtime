class SettlementProcess:
    process_id = "SP-000"
    name = "Base Settlement Process"

    def evaluate(self, world):
        return {
            "admissible": True,
            "reason": "ADMISSIBLE",
        }

    def execute(self, world):
        raise NotImplementedError


class SettlementEvolutionProcess(SettlementProcess):
    """
    SP-001

    Constitutional settlement evolution.
    """

    process_id = "SP-001"
    name = "Settlement Evolution"

    def evaluate(self, world):
        admissible = (
            world.population.total >= world.settlement.capacity
            and world.population.health >= 90
            and world.population.hunger_pressure == 0
            and world.resources.food >= world.population.total
        )

        return {
            "admissible": admissible,
            "reason": (
                "ADMISSIBLE"
                if admissible
                else "SETTLEMENT_GROWTH_DENIED"
            ),
            "population": world.population.total,
            "capacity": world.settlement.capacity,
            "health": world.population.health,
            "hunger_pressure": world.population.hunger_pressure,
            "food": world.resources.food,
            "stage": world.settlement.stage,
        }

    def execute(self, world):
        change = world.settlement.advance_stage()

        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "changes": [change],
        }