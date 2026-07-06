from dataclasses import dataclass

@dataclass
class ExecutionResult:

    admissible: bool
    reason: str
    world_revision: int
