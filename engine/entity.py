from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Entity:

    entity_id: str
    entity_type: str
    state: dict

    @staticmethod
    def create(entity_type, state=None):
        return Entity(
            entity_id=str(uuid4()),
            entity_type=entity_type,
            state=state or {}
        )
