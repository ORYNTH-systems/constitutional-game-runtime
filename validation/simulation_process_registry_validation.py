import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.world import World
from simulation.process_registry import ProcessRegistry
from simulation.resource_growth_process import ResourceGrowthProcess
from simulation.world_evolution_engine import WorldEvolutionEngine

world = World(
    world_id="GAME-WORLD-001",
    revision=1,
    state={}
)

registry = ProcessRegistry()
registry.register(ResourceGrowthProcess())

engine = WorldEvolutionEngine(registry=registry)

first = engine.evolve(world)
second = engine.evolve(world)

validation_passed = (
    first["processes_run"] == 1
    and second["processes_run"] == 1
    and world.state["resources"]["wild_food"] == 2
    and world.state["simulation_tick"] == 2
    and world.revision == 3
)

print(json.dumps({
    "validation": "simulation_process_registry_validation",
    "passed": validation_passed,
    "processes_run_first": first["processes_run"],
    "processes_run_second": second["processes_run"],
    "wild_food": world.state["resources"]["wild_food"],
    "simulation_tick": world.state["simulation_tick"],
    "world_revision": world.revision
}, indent=4))
