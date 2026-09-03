class Solution:
    # Time: O(n)
    # Space: O(1) (26 alphabet slots)
    def unique_letter_string(self, s: str) -> int:
        # Each character contributes to the substrings in which it is the only
        # occurrence of its letter. For index i with previous occurrence at
        # prev[i] and next occurrence at next[i], the number of such substrings
        # is (i - prev[i]) * (next[i] - i).
        n = len(s)
        prev = [-1] * n
        last: dict[str, int] = {}
        for i, ch in enumerate(s):
            prev[i] = last.get(ch, -1)
            last[ch] = i

        next_pos = [n] * n
        last = {}
        for i in range(n - 1, -1, -1):
            next_pos[i] = last.get(s[i], n)
            last[s[i]] = i

        return sum((i - prev[i]) * (next_pos[i] - i) for i in range(n))
