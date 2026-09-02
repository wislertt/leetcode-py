import random


# LeetCode exposes rand7() as a black-box API. It is modelled here as a
# concrete seeded class so the generated tests are deterministic and can also
# count how many rand7() calls each rand10() draw consumed.
class Rand7:
    def __init__(self, seed: int) -> None:
        self._rng = random.Random(seed)
        self.calls = 0

    def rand7(self) -> int:
        self.calls += 1
        return self._rng.randint(1, 7)


class Solution:
    # Rejection sampling on a 7x7 grid: 49 equally likely outcomes, 40 of them
    # map onto [1, 10] and the remaining 9 are discarded and redrawn. Expected
    # rand7() calls per rand10() is 2 * 49 / 40 ~= 2.45.
    # Time: O(1) expected per rand10() call
    # Space: O(1)
    def __init__(self, rand7_api: Rand7) -> None:
        self._rand7_api = rand7_api

    def rand10(self) -> int:
        while True:
            row = self._rand7_api.rand7()
            col = self._rand7_api.rand7()
            idx = (row - 1) * 7 + col
            if idx <= 40:
                return (idx - 1) % 10 + 1
