class Solution:
    # Time: O(n)
    # Space: O(1)
    def valid_partition(self, nums: list[int]) -> bool:
        # dp over the last three prefix results, rolling to constant space
        dp2 = False  # can partition nums[:i-3]
        dp1 = True  # can partition nums[:i-2]
        dp0 = False  # can partition nums[:i-1]
        n = len(nums)
        for i in range(2, n + 1):
            nxt = False
            if dp1 and nums[i - 1] == nums[i - 2]:
                nxt = True
            elif i >= 3 and dp2:
                a, b, c = nums[i - 3], nums[i - 2], nums[i - 1]
                if (a == b == c) or (a + 1 == b and b + 1 == c):
                    nxt = True
            dp2, dp1, dp0 = dp1, dp0, nxt
        return dp0
