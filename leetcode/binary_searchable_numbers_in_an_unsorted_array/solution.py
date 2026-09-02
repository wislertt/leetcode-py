class Solution:
    # Time: O(n)
    # Space: O(n)
    def binary_searchable_numbers(self, nums: list[int]) -> int:
        n = len(nums)
        searchable = [True] * n
        left_max = -(10**5 + 1)
        for i, value in enumerate(nums):
            if value < left_max:
                searchable[i] = False
            else:
                left_max = value
        right_min = 10**5 + 1
        total = 0
        for i in range(n - 1, -1, -1):
            if nums[i] > right_min:
                searchable[i] = False
            else:
                right_min = nums[i]
            if searchable[i]:
                total += 1
        return total
