class WorldEvolutionEngine:

    def __init__(self, registry=None):
        self.registry = registry

    def evolve(self, world):

        world.revision += 1

        state = world.state

        state.setdefault("simulation_tick", 0)
        state["simulation_tick"] += 1

        state.setdefault("world_events", [])

        process_results = []

        if self.registry is not None:
            process_results = self.registry.run_all(world)

        state["world_events"].append({
            "tick": state["simulation_tick"],
            "event": "world_evolved",
            "processes_run": len(process_results)
        })

        return {
            "revision": world.revision,
            "tick": state["simulation_tick"],
            "events": len(state["world_events"]),
            "processes_run": len(process_results),
            "process_results": process_results
        }
