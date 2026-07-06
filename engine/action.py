from dataclasses import dataclass

@dataclass
class Action:

    actor_id: str
    action_type: str
    target_id: str | None
    payload: dict
