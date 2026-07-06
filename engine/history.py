class History:

    def __init__(self):
        self.events = []

    def record(self, event):
        self.events.append(event)

    def replay(self):
        return list(self.events)
