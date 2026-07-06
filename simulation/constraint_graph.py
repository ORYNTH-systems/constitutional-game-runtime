class ConstraintGraph:

    def __init__(self):

        self.constraints = []

    def register(self, constraint):

        self.constraints.append(constraint)

    def evaluate(self, world):

        results = []

        admissible = True

        for constraint in self.constraints:

            passed = constraint.evaluate(world)

            results.append({
                "constraint": constraint.name,
                "passed": passed
            })

            admissible = admissible and passed

        return {
            "admissible": admissible,
            "results": results
        }
