import heapq


class Solution:
    # Time: O(n + k * log n)
    # Space: O(n)
    def max_kelements(self, nums: list[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        score = 0
        for _ in range(k):
            num = -heapq.heappop(heap)
            score += num
            heapq.heappush(heap, -((num + 2) // 3))
        return score
