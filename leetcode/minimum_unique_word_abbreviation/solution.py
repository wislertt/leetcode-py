class Solution:
    # Time: O(2^m * n * m) — enumerate letter subsets, check against dictionary
    # Space: O(m) for the abbreviation buffer
    def min_abbreviation(self, target: str, dictionary: list[str]) -> str:
        m = len(target)
        words = [w for w in dictionary if len(w) == m]

        def abbr_from_mask(mask: int) -> str:
            parts: list[str] = []
            run = 0
            for i, ch in enumerate(target):
                if mask >> i & 1:
                    if run:
                        parts.append(str(run))
                        run = 0
                    parts.append(ch)
                else:
                    run += 1
            if run:
                parts.append(str(run))
            return "".join(parts)

        def matches(abbr: str, w: str) -> bool:
            i = j = 0
            while i < len(abbr) and j < len(w):
                if abbr[i].isdigit():
                    if abbr[i] == "0":
                        return False
                    k = 0
                    while i < len(abbr) and abbr[i].isdigit():
                        k = k * 10 + int(abbr[i])
                        i += 1
                    j += k
                else:
                    if w[j] != abbr[i]:
                        return False
                    i += 1
                    j += 1
            return i == len(abbr) and j == len(w)

        def conflicts(abbr: str) -> bool:
            return any(matches(abbr, w) for w in words)

        best_abbr = ""
        best_len = m + 1
        for mask in range(1 << m):
            candidate = abbr_from_mask(mask)
            candidate_len = sum(1 for c in candidate if c.isalpha()) + sum(
                1 for c in candidate if c.isdigit()
            )
            if candidate_len >= best_len:
                continue
            if not conflicts(candidate):
                best_abbr, best_len = candidate, candidate_len
        return best_abbr
