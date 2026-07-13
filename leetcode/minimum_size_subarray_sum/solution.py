class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_sub_array_len(self, target: int, nums: list[int]) -> int:
        left = 0
        window_sum = 0
        min_len = len(nums) + 1

        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if min_len > len(nums) else min_len
