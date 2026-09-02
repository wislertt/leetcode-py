class Solution:
    # Time: O(n)
    # Space: O(n)
    def max_subarray_length(self, nums: list[int], k: int) -> int:
        freq: dict[int, int] = {}
        left = 0
        best = 0
        for right, val in enumerate(nums):
            freq[val] = freq.get(val, 0) + 1
            while freq[val] > k:
                freq[nums[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
