import heapq


class Solution:
    # Time: O(n + k * log n)
    # Space: O(n)
    def get_final_state(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        heap = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            value, index = heapq.heappop(heap)
            heapq.heappush(heap, (value * multiplier, index))
        result = [0] * len(nums)
        while heap:
            value, index = heapq.heappop(heap)
            result[index] = value
        return result
