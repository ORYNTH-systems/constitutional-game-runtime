from simulation.simulation_clock import SimulationClock
from simulation.world_revision import WorldRevision
from simulation.resource_model import ResourceModel
from simulation.population_model import PopulationModel
from simulation.constitutional_process_engine import ConstitutionalProcessEngine


class ConstitutionalWorld:
    """
    Root object representing a governed constitutional world.
    """

    def __init__(self):
        self.clock = SimulationClock()
        self.resources = ResourceModel()
        self.population = PopulationModel()
        self.process_engine = ConstitutionalProcessEngine()
        self.history = []

        self.revision = self._create_revision(
            revision=0,
            evidence={
                "event": "world_initialized",
                "governance": "active",
            },
        )

    def _create_revision(self, revision, evidence):
        world_revision = WorldRevision(
            revision=revision,
            clock=self.clock,
            resources=self.resources,
            population=self.population,
            evidence=evidence,
        )
        self.history.append(world_revision)
        return world_revision

    def tick(self):
        self.clock.advance()

        food_growth = self.resources.grow_food(4)

        evidence = {
            "event": "simulation_tick",
            "tick": self.clock.tick,
            "processes_executed": ["food_growth"],
            "governance": {
                "approved": 1,
                "denied": 0,
            },
            "resource_changes": [food_growth],
        }

        self.revision = self._create_revision(
            revision=self.revision.revision + 1,
            evidence=evidence,
        )

        return self.revision

    def __str__(self):
        return (
            "Constitutional World\n"
            "--------------------\n"
            f"{self.revision}"
        )