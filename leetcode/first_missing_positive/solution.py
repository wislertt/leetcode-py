class Solution:
    # Time: O(n)
    # Space: O(1)
    def first_missing_positive(self, nums: list[int]) -> int:
        n = len(nums)

        # Place each number in its correct position
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        # Find the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
