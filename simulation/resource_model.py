class ResourceModel:
    """
    Initial constitutional resource state.
    """

    def __init__(self):
        self.food = 1000
        self.water = float("inf")
        self.wood = 500
        self.stone = 200

    def __str__(self):
        return (
            f"Food: {self.food}\n"
            f"Water: Infinite\n"
            f"Wood: {self.wood}\n"
            f"Stone: {self.stone}"
        )