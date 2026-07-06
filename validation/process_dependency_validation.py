import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.world import World

from simulation.process_registry import ProcessRegistry
from simulation.world_evolution_engine import WorldEvolutionEngine

from simulation.resource_growth_process import ResourceGrowthProcess
from simulation.resource_consumption_process import ResourceConsumptionProcess

world = World(
    world_id="GAME-WORLD-001",
    revision=1,
    state={}
)

registry = ProcessRegistry()

registry.register(
    ResourceGrowthProcess()
)

registry.register(
    ResourceConsumptionProcess(),
    depends_on=["resource_growth"]
)

engine = WorldEvolutionEngine(registry)

engine.evolve(world)

validation_passed = (
    world.state["resources"]["wild_food"] == 0
    and registry.execution_order() == [
        "resource_growth",
        "resource_consumption"
    ]
)

print(json.dumps({
    "validation":"process_dependency_validation",
    "passed":validation_passed,
    "execution_order":registry.execution_order(),
    "remaining_food":world.state["resources"]["wild_food"]
}, indent=4))
