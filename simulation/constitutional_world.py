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

        self.revision = WorldRevision(
            revision=0,
            clock=self.clock,
            resources=self.resources,
            population=self.population,
        )

    def __str__(self):

        return (
            "Constitutional World\n"
            "--------------------\n"
            f"{self.revision}"
        )