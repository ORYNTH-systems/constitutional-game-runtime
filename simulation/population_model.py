class PopulationModel:
    """
    Initial constitutional population state.
    """

    def __init__(self):
        self.total = 100

    def __str__(self):
        return f"Population: {self.total}"