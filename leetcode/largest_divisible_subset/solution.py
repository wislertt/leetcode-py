class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def largest_divisible_subset(self, nums: list[int]) -> list[int]:
        nums = sorted(nums)
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
        best = max(range(n), key=lambda i: dp[i])
        chain: list[int] = []
        while best != -1:
            chain.append(nums[best])
            best = parent[best]
        return chain[::-1]
