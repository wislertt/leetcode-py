import heapq


class Solution:
    # Time: O(n log k) where k = ladders
    # Space: O(k)
    def furthest_building(self, heights: list[int], bricks: int, ladders: int) -> int:
        climbs: list[int] = []
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                continue
            heapq.heappush(climbs, climb)
            if len(climbs) > ladders:
                bricks -= heapq.heappop(climbs)
            if bricks < 0:
                return i
        return len(heights) - 1
