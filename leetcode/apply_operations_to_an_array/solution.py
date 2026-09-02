class Solution:
    # Time: O(n)
    # Space: O(1) extra, output written in place
    def apply_operations(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        insert = 0
        for read in range(n):
            if nums[read] != 0:
                nums[insert] = nums[read]
                insert += 1
        for idx in range(insert, n):
            nums[idx] = 0
        return nums
