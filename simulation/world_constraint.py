class WorldConstraint:

    def __init__(self, name, evaluator):

        self.name = name
        self.evaluator = evaluator

    def evaluate(self, world):

        return self.evaluator(world)
