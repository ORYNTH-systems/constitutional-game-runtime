class ConstitutionalProcessRegistry:
    """
    Canonical registry for Constitutional Processes.

    The registry is responsible for discovering, organizing,
    and exposing every process available to the Constitutional Runtime.

    It does not execute processes.

    Execution remains the responsibility of the
    Constitutional Process Engine.
    """

    def __init__(self):
        self._processes = {}

    def register(self, process):
        """
        Register a constitutional process.
        """

        self._processes[process.process_id] = process

    def unregister(self, process_id):
        """
        Remove a registered process.
        """

        if process_id in self._processes:
            del self._processes[process_id]

    def get(self, process_id):
        """
        Retrieve a process by identifier.
        """

        return self._processes.get(process_id)

    def exists(self, process_id):
        """
        Determine whether a process exists.
        """

        return process_id in self._processes

    def all(self):
        """
        Return all registered processes ordered by identifier.
        """

        return [
            self._processes[key]
            for key in sorted(self._processes.keys())
        ]

    def count(self):
        """
        Number of registered processes.
        """

        return len(self._processes)

    def identifiers(self):
        """
        Return registered process identifiers.
        """

        return sorted(self._processes.keys())

    def describe(self):
        """
        Produce a human-readable registry description.
        """

        lines = [
            "Constitutional Process Registry",
            "-------------------------------",
        ]

        for process in self.all():
            lines.append(
                f"{process.process_id}  {process.name}"
            )

        return "\n".join(lines)

    def __str__(self):
        return self.describe()