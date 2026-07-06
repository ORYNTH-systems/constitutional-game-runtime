import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.world import World
from simulation.constraint_graph import ConstraintGraph
from simulation.world_constraint import WorldConstraint

world = World(
    world_id="GAME-WORLD-001",
    revision=1,
    state={
        "resources": {
            "wild_food": 0
        }
    }
)

graph = ConstraintGraph()

graph.register(
    WorldConstraint(
        "minimum_food",
        lambda w: w.state["resources"]["wild_food"] >= 1
    )
)

result = graph.evaluate(world)

print(json.dumps({
    "validation": "constraint_graph_validation",
    "passed": (
        result["admissible"] is False
        and len(result["results"]) == 1
    ),
    **result
}, indent=4))
