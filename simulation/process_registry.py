class ProcessRegistry:

    def __init__(self):
        self.processes = {}
        self.dependencies = {}

    def register(self, process, depends_on=None):
        self.processes[process.process_name] = process
        self.dependencies[process.process_name] = depends_on or []

    def execution_order(self):

        ordered = []
        visited = set()

        def visit(name):

            if name in visited:
                return

            visited.add(name)

            for dependency in self.dependencies[name]:
                visit(dependency)

            ordered.append(name)

        for process in self.processes:
            visit(process)

        return ordered

    def run_all(self, world):

        results = []

        for process_name in self.execution_order():

            process = self.processes[process_name]

            admissible = process.admissible(world)

            if not admissible:

                results.append({
                    "process": process_name,
                    "executed": False,
                    "reason": "NOT_ADMISSIBLE"
                })

                continue

            results.append({
                "process": process_name,
                "executed": True,
                "result": process.apply(world)
            })

        return results
