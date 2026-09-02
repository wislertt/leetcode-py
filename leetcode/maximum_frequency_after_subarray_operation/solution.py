class Solution:
    # Time: O(50 * n) ~ O(n); Space: O(1)
    def max_frequency(self, nums: list[int], k: int) -> int:
        base = nums.count(k)
        best_gain = 0
        for target in sorted(set(nums) - {k}):
            # Kadane: +1 for target values (convertible to k), -1 for k values
            # (lost by the operation), 0 otherwise.
            cur = 0
            for num in nums:
                weight = 1 if num == target else (-1 if num == k else 0)
                cur = max(weight, cur + weight)
                best_gain = max(best_gain, cur)
        return base + best_gain
