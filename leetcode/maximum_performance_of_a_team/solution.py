import heapq


class Solution:
    # Time: O(n log n)
    # Space: O(k)
    def max_performance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        mod = 1_000_000_007
        engineers = sorted(zip(speed, efficiency, strict=True), key=lambda x: -x[1])
        heap: list[int] = []
        total = 0
        best = 0
        for spd, eff in engineers:
            heapq.heappush(heap, spd)
            total += spd
            if len(heap) > k:
                total -= heapq.heappop(heap)
            best = max(best, total * eff)
        return best % mod
