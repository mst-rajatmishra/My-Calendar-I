class MyCalendar:
    def __init__(self):
        self.booked_events = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.booked_events:
            if start < e and end > s:  # Check for overlap
                return False
        self.booked_events.append((start, end))
        return True

