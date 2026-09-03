from collections import Counter


class Solution:
    # Time: O(n * (m + k)) - n words, m word length, k <= 7 plate letters
    # Space: O(1) - at most 26 letters per counter
    def shortest_completing_word(self, license_plate: str, words: list[str]) -> str:
        need = Counter(c for c in license_plate.lower() if c.isalpha())
        best: str | None = None
        for word in words:
            count = Counter(word)
            if all(count[ch] >= k for ch, k in need.items()) and (
                best is None or len(word) < len(best)
            ):
                best = word
        return best or ""
