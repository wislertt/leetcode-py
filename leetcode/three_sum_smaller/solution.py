class Solution:
    # Time: O(n^2)
    # Space: O(1) excluding sort
    def three_sum_smaller(self, nums: list[int], target: int) -> int:
        nums = sorted(nums)
        count = 0
        n = len(nums)
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    count += k - j
                    j += 1
                else:
                    k -= 1
        return count
