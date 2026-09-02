class Solution:
    # Time: O(n + m) where n = len(s), m = len(shift)
    # Space: O(n) for the result string
    def string_shift(self, s: str, shift: list[list[int]]) -> str:
        offset = sum(amount if direction == 1 else -amount for direction, amount in shift)
        offset %= len(s)
        split = len(s) - offset
        return s[split:] + s[:split]
