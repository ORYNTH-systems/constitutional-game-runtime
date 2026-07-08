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
        settlement=None,
    ):
        self.revision = revision
        self.clock = clock
        self.resources = resources
        self.population = population
        self.environment = environment
        self.settlement = settlement
        self.evidence = evidence

    def __str__(self):
        environment_text = (
            f"\n\n{self.environment}"
            if self.environment is not None
            else ""
        )

        settlement_text = (
            f"\n\n{self.settlement}"
            if self.settlement is not None
            else ""
        )

        return (
            f"Revision: {self.revision}\n\n"
            f"{self.clock}\n\n"
            f"{self.population}\n\n"
            f"{self.resources}"
            f"{environment_text}"
            f"{settlement_text}\n\n"
            f"Evidence: {self.evidence}"
        )
