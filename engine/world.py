from dataclasses import dataclass

@dataclass
class World:

    world_id: str
    revision: int
    state: dict
