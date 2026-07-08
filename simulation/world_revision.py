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
        environment=None,
    ):
        self.revision = revision
        self.clock = clock
        self.resources = resources
        self.population = population
        self.environment = environment
        self.evidence = evidence

    def __str__(self):
        environment_text = (
            f"\n\n{self.environment}"
            if self.environment is not None
            else ""
        )

        return (
            f"Revision: {self.revision}\n\n"
            f"{self.clock}\n\n"
            f"{self.population}\n\n"
            f"{self.resources}"
            f"{environment_text}\n\n"
            f"Evidence: {self.evidence}"
        )