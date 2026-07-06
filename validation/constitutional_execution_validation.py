import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from engine.action import Action
from engine.entity import Entity
from engine.history import History
from engine.world import World
from engine.execution_engine import ExecutionEngine
from governance.governance_engine import GovernanceEngine

player = Entity.create(
    entity_type="player",
    state={"health": 100, "position": [0, 0]}
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
    action_type="move",
    target_id=None,
    payload={"to": [1, 0]}
)

governance = GovernanceEngine()
executor = ExecutionEngine()
history = History()

governance_result = governance.evaluate(world, action)
execution_result = executor.execute(world, action, governance_result)

history.record({
    "world_revision": execution_result.world_revision,
    "action_type": action.action_type,
    "admissible": execution_result.admissible
})

validation_passed = (
    governance_result["admissible"]
    and execution_result.admissible
    and world.revision == 2
    and len(history.replay()) == 1
)

result = {
    "validation": "constitutional_execution_validation",
    "passed": validation_passed,
    "requested_action": "move",
    "governance_admissible": governance_result["admissible"],
    "execution_admissible": execution_result.admissible,
    "world_revision": world.revision,
    "history_length": len(history.replay())
}

print(json.dumps(result, indent=4))
