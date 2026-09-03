class Solution:
    # Time: O(n)
    # Space: O(1)
    def count_binary_substrings(self, s: str) -> int:
        prev = 0
        cur = 1
        total = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                total += min(prev, cur)
                prev = cur
                cur = 1
        total += min(prev, cur)
        return total
