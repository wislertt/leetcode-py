from collections import deque


class ZigzagIterator:
    # Time: O(1) per call
    # Space: O(v1.length + v2.length)
    def __init__(self, v1: list[int], v2: list[int]) -> None:
        self._queues: list[deque[int]] = [deque(v) for v in (v1, v2) if v]
        self._turn = 0

    def _prune_empty(self) -> None:
        self._queues = [queue for queue in self._queues if queue]
        if self._turn >= len(self._queues):
            self._turn = 0

    # Time: O(1) amortized
    # Space: O(1)
    def next(self) -> int:
        self._prune_empty()
        queue = self._queues[self._turn]
        value = queue.popleft()
        if self._queues:
            self._turn = (self._turn + 1) % len(self._queues)
        return value

    # Time: O(1)
    # Space: O(1)
    def has_next(self) -> bool:
        self._prune_empty()
        return bool(self._queues)
