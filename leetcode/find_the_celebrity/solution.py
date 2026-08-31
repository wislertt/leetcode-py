from typing import ClassVar


class Solution:
    # Backing store for the knows API, injected by the test helper
    graph: ClassVar[list[list[int]]] = []

    # Time: O(n) knows calls
    # Space: O(1)
    def knows(self, a: int, b: int) -> bool:
        return bool(self.graph[a][b])

    # Time: O(n) knows calls
    # Space: O(1)
    def find_celebrity(self, n: int) -> int:
        candidate = 0
        for other in range(1, n):
            if self.knows(candidate, other):
                candidate = other
        for other in range(n):
            if other == candidate:
                continue
            if self.knows(candidate, other) or not self.knows(other, candidate):
                return -1
        return candidate
