import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from simulation.event_scheduler import EventScheduler
from simulation.scheduled_event import ScheduledEvent

scheduler = EventScheduler()

scheduler.schedule(
    ScheduledEvent(
        tick=3,
        event_type="resource_growth"
    )
)

tick2 = scheduler.due_events(2)

tick3 = scheduler.due_events(3)

validation_passed = (
    len(tick2) == 0
    and len(tick3) == 1
    and tick3[0].event_type == "resource_growth"
)

print(json.dumps({
    "validation":"event_scheduler_validation",
    "passed":validation_passed,
    "events_tick2":len(tick2),
    "events_tick3":len(tick3),
    "event_type":tick3[0].event_type
}, indent=4))
