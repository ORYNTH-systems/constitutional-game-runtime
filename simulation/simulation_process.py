class SimulationProcess:

    process_name = "base_process"

    def apply(self, world):
        raise NotImplementedError("Simulation processes must implement apply(world).")
