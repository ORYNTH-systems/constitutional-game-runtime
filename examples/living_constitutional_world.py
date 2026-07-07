import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from simulation.constitutional_world import ConstitutionalWorld


def main():
    world = ConstitutionalWorld()

    for _ in range(1000):
        world.tick()

    print(world)
    print(f"\nHistory Length: {len(world.history)}")


if __name__ == "__main__":
    main()