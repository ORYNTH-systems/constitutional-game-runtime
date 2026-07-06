from engine.constraint import Constraint


class GovernanceEngine:

    def evaluate(self, world, action):
        constraints = []

        actor_exists = action.actor_id in world.state.get("entities", {})
        constraints.append(
            Constraint(
                constraint_name="actor_exists",
                satisfied=actor_exists,
                reason="" if actor_exists else "Actor does not exist in world state."
            )
        )

        action_type_allowed = action.action_type in world.state.get("allowed_actions", [])
        constraints.append(
            Constraint(
                constraint_name="action_type_allowed",
                satisfied=action_type_allowed,
                reason="" if action_type_allowed else "Action type is not allowed in current world state."
            )
        )

        admissible = all(constraint.satisfied for constraint in constraints)

        return {
            "admissible": admissible,
            "constraints": constraints
        }
