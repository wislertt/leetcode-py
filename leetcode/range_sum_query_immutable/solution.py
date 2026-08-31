from itertools import accumulate


class NumArray:
    # Time: O(n) init, O(1) per query
    # Space: O(n)
    def __init__(self, nums: list[int]) -> None:
        self.prefix = [0, *accumulate(nums)]

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
