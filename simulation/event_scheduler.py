class EventScheduler:

    def __init__(self):

        self.events = []

    def schedule(self, event):

        self.events.append(event)

    def due_events(self, current_tick):

        ready = []

        remaining = []

        for event in self.events:

            if event.tick <= current_tick:
                ready.append(event)
            else:
                remaining.append(event)

        self.events = remaining

        return ready
