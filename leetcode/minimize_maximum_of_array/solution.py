class Solution:
    # Time: O(n)
    # Space: O(1)
    def minimize_array_value(self, nums: list[int]) -> int:
        # Operations never change a prefix sum, so every prefix must be levelable
        # under the answer: prefix sum <= answer * prefix length. The answer is the
        # largest such ceil(prefix_sum / length) over all prefixes.
        ans = 0
        prefix = 0
        for i, num in enumerate(nums):
            prefix += num
            ans = max(ans, -(-prefix // (i + 1)))
        return ans
