class Solution:
    # Time: O(n)
    # Space: O(1)
    def partition_disjoint(self, nums: list[int]) -> int:
        length = 1
        left_max = nums[0]
        cur_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(cur_max, nums[i])
            if nums[i] < left_max:
                left_max = cur_max
                length = i + 1
        return length
