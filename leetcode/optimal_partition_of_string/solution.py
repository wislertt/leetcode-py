class Solution:
    # Time: O(n)
    # Space: O(1)
    def partition_string(self, s: str) -> int:
        seen = 0
        count = 1
        for ch in s:
            bit = 1 << (ord(ch) - 97)
            if seen & bit:
                count += 1
                seen = bit
            else:
                seen |= bit
        return count
