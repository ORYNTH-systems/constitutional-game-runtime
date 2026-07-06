class ScheduledEvent:

    def __init__(self, tick, event_type, payload=None):

        self.tick = tick
        self.event_type = event_type
        self.payload = payload or {}
