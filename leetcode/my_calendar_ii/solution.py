class MyCalendarTwo:
    # Tracks single and double bookings; a new event is valid iff it
    # overlaps no double-booked region.
    # Time: O(n) per book
    # Space: O(n)
    def __init__(self) -> None:
        self._booked: list[tuple[int, int]] = []
        self._double_booked: list[tuple[int, int]] = []

    @staticmethod
    def _intersects(s1: int, e1: int, s2: int, e2: int) -> bool:
        return max(s1, s2) < min(e1, e2)

    def book(self, start_time: int, end_time: int) -> bool:
        if any(self._intersects(start_time, end_time, s, e) for s, e in self._double_booked):
            return False
        for s, e in self._booked:
            if self._intersects(start_time, end_time, s, e):
                self._double_booked.append((max(start_time, s), min(end_time, e)))
        self._booked.append((start_time, end_time))
        return True
