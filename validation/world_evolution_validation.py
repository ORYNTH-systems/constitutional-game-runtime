import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.world import World
from simulation.world_evolution_engine import WorldEvolutionEngine

world = World(
    world_id="GAME-WORLD-001",
    revision=1,
    state={}
)

engine = WorldEvolutionEngine()

first = engine.evolve(world)
second = engine.evolve(world)

validation_passed = (
    first["revision"] == 2
    and first["tick"] == 1
    and second["revision"] == 3
    and second["tick"] == 2
    and second["events"] == 2
)

print(json.dumps({
    "validation": "world_evolution_validation",
    "passed": validation_passed,
    "first_revision": first["revision"],
    "first_tick": first["tick"],
    "second_revision": second["revision"],
    "second_tick": second["tick"],
    "events": second["events"]
}, indent=4))
