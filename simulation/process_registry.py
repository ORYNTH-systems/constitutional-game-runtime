class ProcessRegistry:

    def __init__(self):
        self.processes = []

    def register(self, process):
        self.processes.append(process)

    def run_all(self, world):
        results = []

        for process in self.processes:
            result = process.apply(world)
            results.append({
                "process": process.process_name,
                "result": result
            })

        return results
