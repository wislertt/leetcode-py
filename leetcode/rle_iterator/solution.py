from bisect import bisect_left


class RLEIterator:
    # Time: O(1) init, O(log k) next where k is the number of runs
    # Space: O(k) for the prefix counts

    def __init__(self, encoding: list[int]) -> None:
        self.prefix: list[int] = []
        self.values = encoding[1::2]
        self.pos: int = 0
        total = 0
        for count in encoding[::2]:
            total += count
            self.prefix.append(total)

    def next(self, n: int) -> int:
        self.pos += n
        idx = bisect_left(self.prefix, self.pos)
        if idx == len(self.prefix):
            return -1
        return self.values[idx]
