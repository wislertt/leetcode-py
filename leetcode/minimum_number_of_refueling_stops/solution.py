import heapq


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def min_refuel_stops(self, target: int, start_fuel: int, stations: list[list[int]]) -> int:
        max_heap: list[int] = []
        reach = start_fuel
        stops = 0
        i = 0
        while reach < target:
            while i < len(stations) and stations[i][0] <= reach:
                heapq.heappush(max_heap, -stations[i][1])
                i += 1
            if not max_heap:
                return -1
            reach += -heapq.heappop(max_heap)
            stops += 1
        return stops
