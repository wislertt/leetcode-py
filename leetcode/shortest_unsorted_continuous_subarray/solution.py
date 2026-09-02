class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_unsorted_subarray(self, nums: list[int]) -> int:
        n = len(nums)
        end = -2
        max_seen = nums[0]
        for i in range(1, n):
            if nums[i] < max_seen:
                end = i
            else:
                max_seen = nums[i]

        if end == -2:
            return 0

        start = 0
        min_seen = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if nums[i] > min_seen:
                start = i
            else:
                min_seen = nums[i]

        return end - start + 1
