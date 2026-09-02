class Solution:
    # Time: O(1)
    # Space: O(1)
    def total_money(self, n: int) -> int:
        full_weeks, rem = divmod(n, 7)
        weeks_total = full_weeks * 28 + 7 * full_weeks * (full_weeks - 1) // 2
        rem_total = rem * (full_weeks + 1) + rem * (rem - 1) // 2
        return weeks_total + rem_total
