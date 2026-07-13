from collections import deque


class HitCounter:
    # Time: O(1) amortized per hit / get_hits
    # Space: O(n) where n is number of distinct timestamps in the 300s window
    def __init__(self) -> None:
        # Pairs of [timestamp, count] coalesce same-second hits so the counter
        # scales even when hits per second are huge (follow-up).
        self.deque: deque[list[int]] = deque()
        self.total = 0

    # Time: O(1)
    # Space: O(1)
    def hit(self, timestamp: int) -> None:
        if self.deque and self.deque[-1][0] == timestamp:
            self.deque[-1][1] += 1
        else:
            self.deque.append([timestamp, 1])
        self.total += 1

    # Time: O(1) amortized
    # Space: O(1)
    def get_hits(self, timestamp: int) -> int:
        # A hit at time t stays valid for 300 seconds, i.e. while
        # t > timestamp - 300. Evict entries that have expired.
        while self.deque and self.deque[0][0] <= timestamp - 300:
            _, count = self.deque.popleft()
            self.total -= count
        return self.total
