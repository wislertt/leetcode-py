import heapq


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def connect_sticks(self, sticks: list[int]) -> int:
        heap = list(sticks)
        heapq.heapify(heap)
        cost = 0
        while len(heap) > 1:
            merged = heapq.heappop(heap) + heapq.heappop(heap)
            cost += merged
            heapq.heappush(heap, merged)
        return cost
