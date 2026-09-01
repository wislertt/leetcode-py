import heapq


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def max_score(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = sorted(zip(nums1, nums2, strict=True), key=lambda p: p[1], reverse=True)
        heap: list[int] = []
        total = 0
        best = 0
        for n1, n2 in pairs:
            heapq.heappush(heap, n1)
            total += n1
            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                best = max(best, total * n2)
        return best
