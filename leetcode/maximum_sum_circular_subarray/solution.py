class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_subarray_sum_circular(self, nums: list[int]) -> int:
        total = 0
        cur_max = 0
        cur_min = 0
        max_sum = nums[0]
        min_sum = nums[0]

        for num in nums:
            total += num
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)

        # If all numbers are negative, total - min_sum == 0 (empty subarray) is invalid.
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)
