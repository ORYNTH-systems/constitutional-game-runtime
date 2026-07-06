from dataclasses import dataclass

@dataclass
class Constraint:

    constraint_name: str
    satisfied: bool
    reason: str = ""
