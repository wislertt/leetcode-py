import heapq


class Solution:
    # Time: O(n * log(max(nums)) * log n)
    # Space: O(n)
    def minimum_deviation(self, nums: list[int]) -> int:
        # Raise every element to its largest reachable form (an odd x can only
        # grow once, to 2x); then repeatedly shrink the current max while it is
        # even, tracking the tightest window seen.
        heap: list[int] = []
        low = 1 << 62
        for num in nums:
            value = num * 2 if num % 2 else num
            heapq.heappush(heap, -value)
            low = min(low, value)

        best = 1 << 62
        while True:
            high = -heapq.heappop(heap)
            best = min(best, high - low)
            if high % 2:
                break
            half = high // 2
            low = min(low, half)
            heapq.heappush(heap, -half)
        return best
