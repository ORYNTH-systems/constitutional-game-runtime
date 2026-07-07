class WorldRevision:
    """
    Immutable constitutional world revision.
    """

    def __init__(
        self,
        revision,
        clock,
        resources,
        population,
        evidence,
    ):
        self.revision = revision
        self.clock = clock
        self.resources = resources
        self.population = population
        self.evidence = evidence

    def __str__(self):
        return (
            f"Revision: {self.revision}\n\n"
            f"{self.clock}\n\n"
            f"{self.population}\n\n"
            f"{self.resources}\n\n"
            f"Evidence: {self.evidence}"
        )