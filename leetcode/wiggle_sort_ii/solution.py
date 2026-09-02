class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def wiggle_sort(self, nums: list[int]) -> None:
        sorted_nums = sorted(nums)
        n = len(nums)
        nums[::2] = sorted_nums[: (n + 1) // 2][::-1]
        nums[1::2] = sorted_nums[(n + 1) // 2 :][::-1]
