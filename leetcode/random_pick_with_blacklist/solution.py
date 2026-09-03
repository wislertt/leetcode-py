import random


class Solution:
    # Time: O(b) init, O(1) pick
    # Space: O(b)
    def __init__(self, n: int, blacklist: list[int]) -> None:
        self.size = n - len(blacklist)
        black = set(blacklist)
        tail = [x for x in range(self.size, n) if x not in black]
        self.remap: dict[int, int] = {}
        for i, b in enumerate(sorted(b for b in black if b < self.size)):
            self.remap[b] = tail[i]

    def pick(self) -> int:
        idx = random.randint(0, self.size - 1)
        return self.remap.get(idx, idx)
