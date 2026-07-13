import bisect
import random


class Solution:
    # Build prefix sums of weights. pick_index draws r in [1, total],
    # binary search for first prefix >= r. Each index i chosen with prob w[i]/sum.
    # Time: O(n) init, O(log n) pick_index
    # Space: O(n)
    def __init__(self, w: list[int]) -> None:
        self.prefix: list[int] = []
        running = 0
        for weight in w:
            running += weight
            self.prefix.append(running)
        self.total = running

    def pick_index(self) -> int:
        r = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, r)
