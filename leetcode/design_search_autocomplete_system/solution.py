class AutocompleteSystem:
    # Time: input O(n * L + n log n) per call with n = sentence count
    # Space: O(total sentence length)
    def __init__(self, sentences: list[str], times: list[int]) -> None:
        self.counts: dict[str, int] = dict(zip(sentences, times, strict=True))
        self.buffer = ""

    def input(self, c: str) -> list[str]:
        if c == "#":
            if self.buffer:
                self.counts[self.buffer] = self.counts.get(self.buffer, 0) + 1
            self.buffer = ""
            return []
        self.buffer += c
        matches = [s for s in self.counts if s.startswith(self.buffer)]
        matches.sort(key=lambda s: (-self.counts[s], s))
        return matches[:3]
