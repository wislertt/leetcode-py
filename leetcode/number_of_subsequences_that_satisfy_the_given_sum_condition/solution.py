class Solution:
    # Time: O(n log n)
    # Space: O(1) auxiliary (sorting aside)
    def num_subseq(self, nums: list[int], target: int) -> int:
        nums = sorted(nums)
        mod = 1_000_000_007
        n = len(nums)
        pows = [1] * n
        for i in range(1, n):
            pows[i] = pows[i - 1] * 2 % mod

        result = 0
        left, right = 0, n - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + pows[right - left]) % mod
                left += 1
            else:
                right -= 1
        return result
