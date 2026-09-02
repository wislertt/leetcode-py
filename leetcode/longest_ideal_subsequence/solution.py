class Solution:
    # Time: O(26 * n)
    # Space: O(26)
    def longest_ideal_string(self, s: str, k: int) -> int:
        best = [0] * 26
        for ch in s:
            c = ord(ch) - ord("a")
            window = best[max(0, c - k) : min(26, c + k + 1)]
            best[c] = max(best[c], 1 + max(window))
        return max(best)
