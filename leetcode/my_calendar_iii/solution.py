class MyCalendarThree:
    # Boundary delta map: a booking adds +1 at start and -1 at end, so a sweep
    # over the sorted boundaries gives the number of events alive at each point;
    # the answer is a running maximum and only ever grows.
    # Time: O(n log n) per book (n = bookings so far)
    # Space: O(n)
    def __init__(self) -> None:
        self._delta: dict[int, int] = {}
        self._max_k = 0

    def book(self, start_time: int, end_time: int) -> int:
        self._delta[start_time] = self._delta.get(start_time, 0) + 1
        self._delta[end_time] = self._delta.get(end_time, 0) - 1
        active = 0
        for time in sorted(self._delta):
            active += self._delta[time]
            if active > self._max_k:
                self._max_k = active
        return self._max_k
