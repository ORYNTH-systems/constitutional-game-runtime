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

result = engine.evolve(world)

print(json.dumps({
    "example": "world_evolution",
    "passed": (
        result["revision"] == 2
        and result["tick"] == 1
        and result["events"] == 1
    ),
    **result
}, indent=4))
