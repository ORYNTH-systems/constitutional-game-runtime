class SimulationProcess:

    process_name = "base_process"

    def admissible(self, world):
        return True

    def apply(self, world):
        raise NotImplementedError()
