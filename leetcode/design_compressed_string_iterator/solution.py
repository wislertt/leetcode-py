class StringIterator:
    # Time: next/has_next O(1) amortized
    # Space: O(k) for k letter-count pairs
    def __init__(self, compressed_string: str) -> None:
        self.pairs: list[tuple[str, int]] = []
        i = 0
        while i < len(compressed_string):
            ch = compressed_string[i]
            i += 1
            num = 0
            while i < len(compressed_string) and compressed_string[i].isdigit():
                num = num * 10 + int(compressed_string[i])
                i += 1
            self.pairs.append((ch, num))
        self.idx = 0

    def next(self) -> str:
        if self.idx >= len(self.pairs):
            return " "
        ch = self.pairs[self.idx][0]
        ch, count = self.pairs[self.idx]
        if count == 1:
            self.idx += 1
        else:
            self.pairs[self.idx] = (ch, count - 1)
        return ch

    def has_next(self) -> bool:
        return self.idx < len(self.pairs)
