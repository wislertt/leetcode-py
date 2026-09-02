class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_substring_in_wrapround_string(self, s: str) -> int:
        best: dict[str, int] = {}
        run = 0
        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1])) % 26 == 1:
                run += 1
            else:
                run = 1
            best[ch] = max(best.get(ch, 0), run)
        return sum(best.values())
