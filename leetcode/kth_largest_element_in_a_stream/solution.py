import heapq


class KthLargest:
    # Time: O(n log k) init, O(log k) per add
    # Space: O(k)
    def __init__(self, k: int, nums: list[int]) -> None:
        self.k = k
        self.min_heap: list[int] = []
        for num in nums:
            self.add(num)

    # Time: O(log k)
    # Space: O(k)
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        # kth largest is the smallest among the k largest elements
        return self.min_heap[0]
