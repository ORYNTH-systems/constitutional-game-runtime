class WorldEvolutionEngine:

    def evolve(self, world):

        world.revision += 1

        state = world.state

        state.setdefault("simulation_tick", 0)
        state["simulation_tick"] += 1

        state.setdefault("world_events", [])

        state["world_events"].append({
            "tick": state["simulation_tick"],
            "event": "world_evolved"
        })

        return {
            "revision": world.revision,
            "tick": state["simulation_tick"],
            "events": len(state["world_events"])
        }
