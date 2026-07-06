import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

validation_files = sorted(
    ROOT.glob("*.py")
)

results = []

for validation in validation_files:

    if validation.name == Path(__file__).name:
        continue

    completed = subprocess.run(
        [sys.executable, str(validation)],
        capture_output=True,
        text=True
    )

    if completed.returncode != 0:

        results.append({
            "validation_file": str(validation),
            "passed": False,
            "error": completed.stderr
        })

        continue

    payload = json.loads(completed.stdout)

    results.append({
        "validation_file": str(validation),
        "passed": payload["passed"],
        "result": payload
    })

total = len(results)
passed = sum(r["passed"] for r in results)

summary = {
    "benchmark": "constitutional_game_runtime",
    "runtime_version": "0.1",
    "total_validations": total,
    "passed": passed,
    "failed": total - passed,
    "pass_rate": (
        passed / total
        if total
        else 0
    ),
    "results": results
}

print(json.dumps(summary, indent=4))
