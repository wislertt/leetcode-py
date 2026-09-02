import heapq


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def get_skyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events: list[tuple[int, int, int]] = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))
        events.sort()

        heap: list[tuple[int, int]] = [(0, 2**31)]
        result: list[list[int]] = []
        for x, neg_height, right in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            if neg_height < 0:
                heapq.heappush(heap, (neg_height, right))
            height = -heap[0][0]
            if not result or result[-1][1] != height:
                result.append([x, height])
        return result
