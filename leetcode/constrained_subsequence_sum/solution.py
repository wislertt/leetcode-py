from collections import deque


class Solution:
    # Time: O(n)
    # Space: O(k)
    def constrained_subset_sum(self, nums: list[int], k: int) -> int:
        dp = [0] * len(nums)
        window = deque()
        for i, num in enumerate(nums):
            dp[i] = num + (dp[window[0]] if window and dp[window[0]] > 0 else 0)
            while window and dp[window[-1]] <= dp[i]:
                window.pop()
            window.append(i)
            if window[0] <= i - k:
                window.popleft()
        return max(dp)
