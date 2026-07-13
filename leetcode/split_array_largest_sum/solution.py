class Solution:
    # Time: O(n * log(sum(nums))) binary search on the answer
    # Space: O(1)
    def split_array(self, nums: list[int], k: int) -> int:
        # Lower bound: a single element must fit. Upper bound: sum of all elements.
        low = max(nums)
        high = sum(nums)

        def count_subarrays(capacity: int) -> int:
            """Minimum subarrays needed so no subarray sum exceeds capacity."""
            subarrays = 1
            current = 0
            for value in nums:
                if current + value > capacity:
                    subarrays += 1
                    current = value
                else:
                    current += value
            return subarrays

        # Binary search for smallest capacity that fits within k subarrays.
        while low < high:
            mid = (low + high) // 2
            if count_subarrays(mid) <= k:
                high = mid
            else:
                low = mid + 1
        return low
