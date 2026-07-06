import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.action import Action
from engine.entity import Entity
from engine.world import World
from engine.execution_engine import ExecutionEngine
from governance.governance_engine import GovernanceEngine

player = Entity.create(
    entity_type="player"
)

world = World(
    world_id="GAME-WORLD-001",
    revision=1,
    state={
        "entities": {
            player.entity_id: player
        },
        "allowed_actions": [
            "move"
        ]
    }
)

action = Action(
    actor_id=player.entity_id,
    action_type="fly",
    target_id=None,
    payload={}
)

governance = GovernanceEngine()
executor = ExecutionEngine()

governance_result = governance.evaluate(world, action)
execution_result = executor.execute(
    world,
    action,
    governance_result
)

validation_passed = (
    not governance_result["admissible"]
    and not execution_result.admissible
    and world.revision == 1
)

result = {
    "validation": "constitutional_denial_validation",
    "passed": validation_passed,
    "requested_action": "fly",
    "governance_admissible": governance_result["admissible"],
    "execution_admissible": execution_result.admissible,
    "world_revision": world.revision,
    "constraints_failed": [
        c.constraint_name
        for c in governance_result["constraints"]
        if not c.satisfied
    ]
}

print(json.dumps(result, indent=4))
