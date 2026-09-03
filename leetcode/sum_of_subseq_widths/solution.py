class Solution:
    # Time: O(n log n)
    # Space: O(1)
    def sum_subseq_widths(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        ordered = sorted(nums)
        total = 0
        n = len(ordered)
        pow2 = 1
        for i, value in enumerate(ordered):
            total += value * (pow2 - 1) - value * (pow(2, n - 1 - i, mod) - 1)
            total %= mod
            pow2 = pow2 * 2 % mod
        return total
