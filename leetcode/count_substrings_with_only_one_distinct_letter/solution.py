class Solution:
    # Time: O(n)
    # Space: O(1)
    def count_letters(self, s: str) -> int:
        ans = 0
        i = 0
        n = len(s)
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                ans += j - i + 1
                j += 1
            i = j
        return ans
