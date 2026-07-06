from simulation.simulation_process import SimulationProcess


class ResourceGrowthProcess(SimulationProcess):

    process_name = "resource_growth"

    def apply(self, world):
        resources = world.state.setdefault("resources", {})
        resources.setdefault("wild_food", 0)
        resources["wild_food"] += 1

        return {
            "resource": "wild_food",
            "quantity": resources["wild_food"]
        }
