from simulation.simulation_clock import SimulationClock
from simulation.world_revision import WorldRevision
from simulation.resource_model import ResourceModel
from simulation.population_model import PopulationModel
from simulation.constitutional_process_registry import ConstitutionalProcessRegistry
from simulation.constitutional_process_engine import ConstitutionalProcessEngine
from simulation.constitutional_processes import (
    FoodGrowthProcess,
    FoodConsumptionProcess,
    PopulationHungerPressureProcess,
    PopulationHealthProcess,
    PopulationGrowthProcess,
)


class ConstitutionalWorld:
    def __init__(self):
        self.clock = SimulationClock()
        self.resources = ResourceModel()
        self.population = PopulationModel()
        self.history = []

        self.process_registry = ConstitutionalProcessRegistry()
        self.process_registry.register(FoodGrowthProcess())
        self.process_registry.register(FoodConsumptionProcess())
        self.process_registry.register(PopulationHungerPressureProcess())
        self.process_registry.register(PopulationHealthProcess())
        self.process_registry.register(PopulationGrowthProcess())

        self.process_engine = ConstitutionalProcessEngine(self.process_registry)

        self.revision = self._create_revision(
            revision=0,
            evidence={
                "event": "world_initialized",
                "governance": "active",
                "registered_processes": self.process_registry.identifiers(),
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
        process_results = self.process_engine.execute_all(self)

        evidence = {
            "event": "simulation_tick",
            "tick": self.clock.tick,
            "processes_executed": process_results["executed"],
            "processes_denied": process_results["denied"],
            "governance": {
                "approved": len(process_results["executed"]),
                "denied": len(process_results["denied"]),
            },
            "registered_processes": self.process_registry.identifiers(),
        }

        self.revision = self._create_revision(
            revision=self.revision.revision + 1,
            evidence=evidence,
        )
        return self.revision

    def describe_process_registry(self):
        return self.process_registry.describe()

    def __str__(self):
        return (
            "Constitutional World\n"
            "--------------------\n"
            f"{self.revision}"
        )
