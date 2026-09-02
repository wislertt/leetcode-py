import heapq
from math import isqrt


class Solution:
    # Time: O(k log n + n)
    # Space: O(n)
    def pick_gifts(self, gifts: list[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            top = -heapq.heappop(heap)
            if top <= 1:
                heapq.heappush(heap, -top)
                break
            heapq.heappush(heap, -isqrt(top))
        return -sum(heap)
