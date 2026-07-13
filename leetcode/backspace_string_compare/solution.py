class Solution:
    # Walk both strings right-to-left, skipping chars consumed by backspace.
    # Compare next surviving char of each; mismatch or early exhaustion => false.
    # Time: O(n + m)
    # Space: O(1)
    def backspace_compare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = self._next_valid(s, i)
            j = self._next_valid(t, j)
            s_char = s[i] if i >= 0 else ""
            t_char = t[j] if j >= 0 else ""
            if s_char != t_char:
                return False
            i -= 1
            j -= 1
        return True

    def _next_valid(self, text: str, index: int) -> int:
        skip = 0
        while index >= 0:
            if text[index] == "#":
                skip += 1
                index -= 1
            elif skip > 0:
                skip -= 1
                index -= 1
            else:
                break
        return index
