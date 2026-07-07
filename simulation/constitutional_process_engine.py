class ConstitutionalProcessEngine:
    """
    Registry and executor of constitutional processes.
    """

    def __init__(self):
        self.processes = []

    def register(self, process):
        self.processes.append(process)

    def execute_all(self, world):
        executed = []
        denied = []

        for process in self.processes:
            evaluation = process.evaluate(world)

            if evaluation["admissible"]:
                result = process.execute(world)
                result["governance"] = evaluation
                executed.append(result)
            else:
                denied.append({
                    "process_id": process.process_id,
                    "name": process.name,
                    "status": "DENIED",
                    "governance": evaluation,
                })

        return {
            "executed": executed,
            "denied": denied,
        }

    def __str__(self):
        return f"Registered Processes: {len(self.processes)}"