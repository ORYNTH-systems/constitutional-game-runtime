class ConstitutionalProcess:
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
    process_id = "CP-002"
    name = "Food Consumption"

    def evaluate(self, world):
        required_food = world.population.total

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
        required_food = world.population.total
        change = world.resources.consume_food(required_food)
        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "changes": [change],
        }


class PopulationHungerPressureProcess(ConstitutionalProcess):
    process_id = "CP-003"
    name = "Population Hunger Pressure"

    def evaluate(self, world):
        return {
            "admissible": True,
            "reason": "ADMISSIBLE",
            "food": world.resources.food,
            "population": world.population.total,
            "current_hunger_pressure": world.population.hunger_pressure,
        }

    def execute(self, world):
        if world.resources.food <= 0:
            change = world.population.increase_hunger_pressure(1)
        else:
            change = world.population.reduce_hunger_pressure(1)

        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "changes": [change],
        }


class PopulationHealthProcess(ConstitutionalProcess):
    process_id = "CP-004"
    name = "Population Health"

    def evaluate(self, world):
        return {
            "admissible": True,
            "reason": "ADMISSIBLE",
            "health": world.population.health,
            "hunger_pressure": world.population.hunger_pressure,
        }

    def execute(self, world):
        change = world.population.update_health()
        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "changes": [change],
        }


class PopulationGrowthProcess(ConstitutionalProcess):
    process_id = "CP-005"
    name = "Population Growth"

    def evaluate(self, world):
        admissible = (
            world.population.health >= 95
            and world.population.hunger_pressure == 0
            and world.resources.food >= world.population.total
        )

        return {
            "admissible": admissible,
            "reason": "ADMISSIBLE" if admissible else "GROWTH_DENIED",
            "health": world.population.health,
            "hunger_pressure": world.population.hunger_pressure,
            "food": world.resources.food,
            "population": world.population.total,
        }

    def execute(self, world):
        change = world.population.grow(1)
        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "changes": [change],
        }


class PopulationMortalityProcess(ConstitutionalProcess):
    process_id = "CP-006"
    name = "Population Mortality"

    def evaluate(self, world):
        admissible = (
            world.population.health <= 25
            or world.population.hunger_pressure >= 10
        )

        return {
            "admissible": admissible,
            "reason": "ADMISSIBLE" if admissible else "MORTALITY_DENIED",
            "health": world.population.health,
            "hunger_pressure": world.population.hunger_pressure,
            "food": world.resources.food,
            "population": world.population.total,
        }

    def execute(self, world):
        change = world.population.reduce_population(1)
        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "changes": [change],
        }