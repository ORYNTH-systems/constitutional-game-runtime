from engine.execution import ExecutionResult


class ExecutionEngine:

    def execute(self, world, action, governance_result):
        if not governance_result["admissible"]:
            return ExecutionResult(
                admissible=False,
                reason="Action denied by governance constraints.",
                world_revision=world.revision
            )

        world.revision += 1

        world.state.setdefault("executed_actions", []).append({
            "revision": world.revision,
            "actor_id": action.actor_id,
            "action_type": action.action_type,
            "target_id": action.target_id,
            "payload": action.payload
        })

        return ExecutionResult(
            admissible=True,
            reason="Action executed.",
            world_revision=world.revision
        )
