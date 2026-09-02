import heapq


class Solution:
    # Time: O(n log k)
    # Space: O(k)
    def kth_largest_number(self, nums: list[str], k: int) -> str:
        heap: list[tuple[int, str]] = []
        for num in nums:
            key = (len(num), num)
            if len(heap) < k:
                heapq.heappush(heap, key)
            elif key > heap[0]:
                heapq.heapreplace(heap, key)
        return heap[0][1]
