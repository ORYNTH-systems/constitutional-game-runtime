from simulation.simulation_process import SimulationProcess

class PopulationGrowthProcess(SimulationProcess):

    process_name = "population_growth"

    def admissible(self, world):

        resources = world.state.setdefault("resources", {})

        return resources.get("wild_food", 0) >= 2

    def apply(self, world):

        world.state.setdefault("population", 0)

        world.state["population"] += 1

        return {
            "population": world.state["population"]
        }
