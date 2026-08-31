import heapq


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def mincost_to_hire_workers(self, quality: list[int], wage: list[int], k: int) -> float:
        # Sort by wage/quality ratio; at ratio r the whole pool pays
        # r * total_quality, and lowest ratios keep the pool cheap
        workers = sorted(
            ((w / q, q) for q, w in zip(quality, wage, strict=True)),
            key=lambda x: x[0],
        )
        pool: list[int] = []  # negated qualities of the current k workers
        total_quality = 0
        best = float("inf")
        for ratio, q in workers:
            heapq.heappush(pool, -q)
            total_quality += q
            if len(pool) > k:
                total_quality += heapq.heappop(pool)
            if len(pool) == k:
                best = min(best, ratio * total_quality)
        return best
