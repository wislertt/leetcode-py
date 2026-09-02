import random
from collections import defaultdict


class Solution:
    # Time: O(n) init, O(1) pick
    # Space: O(n)
    def __init__(self, nums: list[int]) -> None:
        self.indices: dict[int, list[int]] = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])
