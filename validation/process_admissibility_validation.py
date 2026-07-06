import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.world import World
from simulation.process_registry import ProcessRegistry
from simulation.world_evolution_engine import WorldEvolutionEngine
from simulation.population_growth_process import PopulationGrowthProcess

world = World(
    world_id="GAME-WORLD-001",
    revision=1,
    state={
        "resources": {
            "wild_food": 1
        }
    }
)

registry = ProcessRegistry()
registry.register(PopulationGrowthProcess())

engine = WorldEvolutionEngine(registry)

result = engine.evolve(world)

process = result["process_results"][0]

validation_passed = (
    process["executed"] is False
    and world.state.get("population") is None
)

print(json.dumps({
    "validation": "process_admissibility_validation",
    "passed": validation_passed,
    "executed": process["executed"],
    "reason": process["reason"],
    "wild_food": world.state["resources"]["wild_food"]
}, indent=4))
