class Solution:
    # Time: O(n^2) amortized over recursion (sorting dominates at each level)
    # Space: O(n^2) recursion depth O(n) plus per-level substring copies
    def make_largest_special(self, s: str) -> str:
        bal = 0
        start = 0
        parts: list[str] = []
        for i, ch in enumerate(s):
            bal += 1 if ch == "1" else -1
            if bal == 0:
                parts.append("1" + self.make_largest_special(s[start + 1 : i]) + "0")
                start = i + 1
        parts.sort(reverse=True)
        return "".join(parts)
