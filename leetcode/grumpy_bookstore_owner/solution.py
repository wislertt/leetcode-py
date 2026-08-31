class Solution:
    # Time: O(n) sliding window
    # Space: O(1)
    def max_satisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        base = sum(c for c, g in zip(customers, grumpy, strict=True) if g == 0)
        gain = sum(customers[i] * grumpy[i] for i in range(minutes))
        best = gain
        for i in range(minutes, len(customers)):
            gain += customers[i] * grumpy[i] - customers[i - minutes] * grumpy[i - minutes]
            best = max(best, gain)
        return base + best
