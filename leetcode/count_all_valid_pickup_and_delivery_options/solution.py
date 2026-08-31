class Solution:
    # Time: O(n)
    # Space: O(1)
    def count_orders(self, n: int) -> int:
        # Inserting the i-th order into a valid sequence of i-1 orders:
        # place pickup_i in one of 2i-1 gaps, then delivery_i in one of
        # the remaining 2i positions -> factor of (2i - 1) * i.
        mod = 1_000_000_007
        result = 1
        for i in range(2, n + 1):
            result = result * (2 * i - 1) % mod * i % mod
        return result
