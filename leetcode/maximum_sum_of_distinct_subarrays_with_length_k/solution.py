class Solution:
    # Time: O(n)
    # Space: O(k)
    def maximum_subarray_sum(self, nums: list[int], k: int) -> int:
        counts: dict[int, int] = {}
        window_sum = 0
        best = 0

        for i, val in enumerate(nums):
            counts[val] = counts.get(val, 0) + 1
            window_sum += val

            if i >= k:
                left = nums[i - k]
                window_sum -= left
                counts[left] -= 1
                if counts[left] == 0:
                    del counts[left]

            if i >= k - 1 and len(counts) == k:
                best = max(best, window_sum)

        return best
