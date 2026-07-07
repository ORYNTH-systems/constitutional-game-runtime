class ConstitutionalProcess:
    """
    Base class for deterministic constitutional processes.
    """

    process_id = "CP-000"
    name = "Base Constitutional Process"

    def evaluate(self, world):
        return {
            "admissible": True,
            "reason": "ADMISSIBLE",
        }

    def execute(self, world):
        raise NotImplementedError


class FoodGrowthProcess(ConstitutionalProcess):
    """
    CP-001: Food Growth

    Deterministically increases available food each tick.
    """

    process_id = "CP-001"
    name = "Food Growth"

    def execute(self, world):
        change = world.resources.grow_food(4)

        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "changes": [change],
        }


class FoodConsumptionProcess(ConstitutionalProcess):
    """
    CP-002: Food Consumption

    Deterministically consumes food based on population.
    """

    process_id = "CP-002"
    name = "Food Consumption"

    def evaluate(self, world):
        required_food = world.population.total * 1

        if world.resources.food < required_food:
            return {
                "admissible": False,
                "reason": "INSUFFICIENT_FOOD",
                "required_food": required_food,
                "available_food": world.resources.food,
            }

        return {
            "admissible": True,
            "reason": "ADMISSIBLE",
            "required_food": required_food,
            "available_food": world.resources.food,
        }

    def execute(self, world):
        required_food = world.population.total * 1
        change = world.resources.consume_food(required_food)

        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "changes": [change],
        }