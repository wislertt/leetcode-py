from collections import Counter


class Solution:
    # Time: O(m + n)
    # Space: O(m + n)
    def uncommon_from_sentences(self, s1: str, s2: str) -> list[str]:
        counts = Counter((s1 + " " + s2).split())
        return [word for word, count in counts.items() if count == 1]
