import heapq


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def last_stone_weight(self, stones: list[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            heaviest = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            if heaviest != second:
                heapq.heappush(max_heap, -(heaviest - second))

        return -max_heap[0] if max_heap else 0
