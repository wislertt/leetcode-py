class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_profit(self, prices: list[int]) -> int:
        # State machine: held (own stock), sold (just sold -> cooldown), reset (no stock)
        held = float("-inf")
        sold = float("-inf")
        reset = 0
        for price in prices:
            prev_held, prev_sold, prev_reset = held, sold, reset
            held = max(prev_held, prev_reset - price)
            reset = max(prev_reset, prev_sold)
            sold = prev_held + price
        return int(max(sold, reset))
