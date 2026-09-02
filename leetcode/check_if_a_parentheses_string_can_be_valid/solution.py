class Solution:
    # Time: O(n)
    # Space: O(1)
    def can_be_valid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        low = high = 0
        for char, lock in zip(s, locked, strict=True):
            if lock == "0":
                low -= 1
                high += 1
            elif char == "(":
                low += 1
                high += 1
            else:
                low -= 1
                high -= 1
            if high < 0:
                return False
            low = max(low, 0)
        return low == 0
