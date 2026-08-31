class Solution:
    # Time: O(n)
    # Space: O(n)
    def shortest_palindrome(self, s: str) -> str:
        if not s:
            return s
        rev = s[::-1]
        combined = s + "#" + rev
        n = len(combined)
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = pi[j - 1]
            if combined[i] == combined[j]:
                j += 1
            pi[i] = j
        longest = pi[-1]
        return rev[: len(s) - longest] + s
