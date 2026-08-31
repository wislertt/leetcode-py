class Solution:
    # Time: O(2^n * n) — one output string per bitmask, built in O(n)
    # Space: O(2^n * n) — output list dominates
    def generate_abbreviations(self, word: str) -> list[str]:
        n = len(word)
        result: list[str] = []
        for mask in range(1 << n):
            parts: list[str] = []
            run = 0
            for i, ch in enumerate(word):
                if mask >> i & 1:
                    run += 1
                else:
                    if run:
                        parts.append(str(run))
                        run = 0
                    parts.append(ch)
            if run:
                parts.append(str(run))
            result.append("".join(parts))
        return result
