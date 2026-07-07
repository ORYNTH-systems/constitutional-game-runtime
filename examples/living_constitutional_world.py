import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from simulation.constitutional_world import ConstitutionalWorld


def print_summary(world):
    evidence = world.revision.evidence

    print(world)
    print(f"\nHistory Length: {len(world.history)}")
    print("\nActive Constitutional Processes:")
    print(world.describe_process_registry())

    print("\nLatest Governance Summary:")
    governance = evidence.get("governance", {})
    print(f"Approved: {governance.get('approved', 0)}")
    print(f"Denied: {governance.get('denied', 0)}")

    print("\nLatest Executed Processes:")
    for process in evidence.get("processes_executed", []):
        print(f"- {process['process_id']} {process['name']}")

    print("\nLatest Denied Processes:")
    denied = evidence.get("processes_denied", [])
    if not denied:
        print("- None")
    else:
        for process in denied:
            print(f"- {process['process_id']} {process['name']}")


def main():
    world = ConstitutionalWorld()

    for _ in range(1000):
        world.tick()

    print_summary(world)


if __name__ == "__main__":
    main()