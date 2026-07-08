import math


class ConstitutionalProcess:
    process_id = "CP-000"
    name = "Base Constitutional Process"

    def evaluate(self, world):
        return {"admissible": True, "reason": "ADMISSIBLE"}

    def execute(self, world):
        raise NotImplementedError


class FoodGrowthProcess(ConstitutionalProcess):
    process_id = "CP-001"
    name = "Food Growth"

    def growth_amount(self, world):
        soil = world.environment.soil_fertility
        water = world.environment.water_availability

        if soil >= 90 and water == "Abundant":
            return 8
        if soil >= 75 and water == "Normal":
            return 5
        if soil >= 50 and water == "Normal":
            return 3
        if water == "Limited":
            return 1
        return 0

    def evaluate(self, world):
        admissible = (
            world.environment.water_availability in world.environment.WATER_STATES
            and 0 <= world.environment.soil_fertility <= 100
        )

        return {
            "admissible": admissible,
            "reason": "ADMISSIBLE" if admissible else "INVALID_ENVIRONMENTAL_STATE",
            "climate": world.environment.climate,
            "season": world.environment.season,
            "weather": world.environment.weather,
            "water_availability": world.environment.water_availability,
            "soil_fertility": world.environment.soil_fertility,
        }

    def execute(self, world):
        amount = self.growth_amount(world)
        change = world.resources.grow_food(amount)

        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "growth_amount": amount,
            "changes": [change],
        }


class FoodConsumptionProcess(ConstitutionalProcess):
    process_id = "CP-002"
    name = "Food Consumption"

    def evaluate(self, world):
        population = world.population.total
        available = world.resources.food
        required = max(population, 1)

        ratio = min(available / required, 1.0)
        consumed = math.floor(population * ratio)

        return {
            "admissible": True,
            "reason": "ADMISSIBLE",
            "population": population,
            "food_available": available,
            "food_required": required,
            "consumption_ratio": round(ratio, 3),
            "food_consumed": consumed,
        }

    def execute(self, world):
        governance = self.evaluate(world)

        world.population.last_consumption_ratio = governance["consumption_ratio"]
        world.population.last_food_consumed = governance["food_consumed"]

        change = world.resources.consume_food(governance["food_consumed"])

        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "consumption_ratio": governance["consumption_ratio"],
            "food_consumed": governance["food_consumed"],
            "changes": [change],
        }


class PopulationHungerPressureProcess(ConstitutionalProcess):
    process_id = "CP-003"
    name = "Population Hunger Pressure"

    def evaluate(self, world):
        ratio = getattr(world.population, "last_consumption_ratio", 1.0)

        return {
            "admissible": True,
            "reason": "ADMISSIBLE",
            "population": world.population.total,
            "food": world.resources.food,
            "consumption_ratio": ratio,
            "current_hunger_pressure": world.population.hunger_pressure,
        }

    def execute(self, world):
        ratio = getattr(world.population, "last_consumption_ratio", 1.0)

        if ratio >= 1.0:
            change = world.population.reduce_hunger_pressure(1)
        elif ratio >= 0.75:
            change = {
                "population_metric": "hunger_pressure",
                "change": 0,
                "new_value": world.population.hunger_pressure,
            }
        elif ratio >= 0.50:
            change = world.population.increase_hunger_pressure(1)
        elif ratio >= 0.25:
            change = world.population.increase_hunger_pressure(2)
        else:
            change = world.population.increase_hunger_pressure(3)

        return {
            "process_id": self.process_id,
            "name": self.name,
            "status": "EXECUTED",
            "consumption_ratio": ratio,
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