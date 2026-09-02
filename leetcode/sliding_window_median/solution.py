import heapq


class Solution:
    # Time: O(n log n) - each element is pushed and popped a constant number of times
    # Space: O(n) - two heaps plus the delayed-deletion counter
    def median_sliding_window(self, nums: list[int], k: int) -> list[float]:
        small: list[int] = []  # max-heap (negated values), holds the lower half
        large: list[int] = []  # min-heap, holds the upper half
        delayed: dict[int, int] = {}
        small_size = 0
        large_size = 0
        medians: list[float] = []

        def prune(heap: list[int]) -> None:
            sign = -1 if heap is small else 1
            while heap:
                top = sign * heap[0]
                if top not in delayed:
                    break
                delayed[top] -= 1
                if delayed[top] == 0:
                    del delayed[top]
                heapq.heappop(heap)

        def rebalance() -> None:
            nonlocal small_size, large_size
            if small_size > large_size + 1:
                heapq.heappush(large, -small[0])
                heapq.heappop(small)
                small_size -= 1
                large_size += 1
                prune(small)
            elif small_size < large_size:
                heapq.heappush(small, -large[0])
                heapq.heappop(large)
                small_size += 1
                large_size -= 1
                prune(large)

        def insert(num: int) -> None:
            nonlocal small_size, large_size
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1
            rebalance()

        def erase(num: int) -> None:
            nonlocal small_size, large_size
            delayed[num] = delayed.get(num, 0) + 1
            if num <= -small[0]:
                small_size -= 1
                if num == -small[0]:
                    prune(small)
            else:
                large_size -= 1
                if num == large[0]:
                    prune(large)
            rebalance()

        def median() -> float:
            if k % 2 == 1:
                return float(-small[0])
            return (-small[0] + large[0]) / 2

        for num in nums[:k]:
            insert(num)
        medians.append(median())

        for i in range(k, len(nums)):
            insert(nums[i])
            erase(nums[i - k])
            medians.append(median())

        return medians
