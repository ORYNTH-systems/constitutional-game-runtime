import sys
from pathlib import Path

# Make the repository root importable when running this file directly.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from simulation.constitutional_world import ConstitutionalWorld


def main():
    """Create and display the initial Constitutional World."""
    world = ConstitutionalWorld()
    print(world)


if __name__ == "__main__":
    main()