class Solution:
    # Time: O(n * total)
    # Space: O(total)
    def find_target_sum_ways(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        # P = sum of '+'. P - (total - P) = target -> P = (target + total) / 2.
        if (target + total) % 2 != 0 or total < abs(target):
            return 0
        subset_sum = (target + total) // 2

        # dp[s] = number of subsets summing to s
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[subset_sum]
