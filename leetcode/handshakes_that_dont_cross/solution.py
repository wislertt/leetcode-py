class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def number_of_ways(self, num_people: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (num_people + 1)
        dp[0] = 1
        for people in range(2, num_people + 1, 2):
            total = 0
            for left in range(0, people, 2):
                total += dp[left] * dp[people - left - 2]
            dp[people] = total % mod
        return dp[num_people]
