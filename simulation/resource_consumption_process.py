from simulation.simulation_process import SimulationProcess

class ResourceConsumptionProcess(SimulationProcess):

    process_name = "resource_consumption"

    def apply(self, world):

        resources = world.state.setdefault("resources", {})

        resources["wild_food"] -= 1

        return {
            "remaining_food": resources["wild_food"]
        }
