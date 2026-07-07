class ConstitutionalProcessEngine:
    """
    Executor for registered Constitutional Processes.

    The process registry owns the catalog.
    The process engine executes the registered processes.
    """

    def __init__(self, registry):
        self.registry = registry

    def execute_all(self, world):
        executed = []
        denied = []

        for process in self.registry.all():
            evaluation = process.evaluate(world)

            if evaluation["admissible"]:
                result = process.execute(world)
                result["governance"] = evaluation
                executed.append(result)
            else:
                denied.append(
                    {
                        "process_id": process.process_id,
                        "name": process.name,
                        "status": "DENIED",
                        "governance": evaluation,
                    }
                )

        return {
            "executed": executed,
            "denied": denied,
        }

    def __str__(self):
        return f"Registered Processes: {self.registry.count()}"