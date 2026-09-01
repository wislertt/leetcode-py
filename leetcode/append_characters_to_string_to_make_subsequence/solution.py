class Solution:
    # Time: O(len(s) + len(t))
    # Space: O(1)
    def append_characters(self, s: str, t: str) -> int:
        i = 0
        for ch in s:
            if i == len(t):
                break
            if ch == t[i]:
                i += 1
        return len(t) - i
