import random


class Solution:
    # Time: __init__ O(1), flip O(1), reset O(1)
    # Space: O(k) where k is the number of flips since the last reset
    def __init__(self, m: int, n: int) -> None:
        self.m = m
        self.n = n
        self.total = m * n
        self.available = self.total
        self.swapped: dict[int, int] = {}

    def flip(self) -> list[int]:
        idx = random.randrange(self.available)
        self.available -= 1
        picked = self.swapped.get(idx, idx)
        self.swapped[idx] = self.swapped.get(self.available, self.available)
        return [picked // self.n, picked % self.n]

    def reset(self) -> None:
        self.available = self.total
        self.swapped = {}
