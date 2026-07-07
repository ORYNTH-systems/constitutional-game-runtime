class ConstitutionalProcessEngine:
    """
    Registry of constitutional processes.
    """

    def __init__(self):
        self.processes = []

    def register(self, process):
        self.processes.append(process)

    def __str__(self):
        return (
            f"Registered Processes: "
            f"{len(self.processes)}"
        )