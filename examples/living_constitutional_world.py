import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from simulation.constitutional_world import ConstitutionalWorld


def main():
    world = ConstitutionalWorld()

    print("INITIAL WORLD")
    print(world)

    print("\nAFTER ONE CONSTITUTIONAL TICK")
    world.tick()
    print(world)


if __name__ == "__main__":
    main()