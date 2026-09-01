from __future__ import annotations


class SparseVector:
    # Time: O(n)
    # Space: O(k)
    def __init__(self, nums: list[int]) -> None:
        self.nonzero = {i: v for i, v in enumerate(nums) if v}

    # Time: O(min(k1, k2))
    # Space: O(1)
    def dot_product(self, vec: SparseVector) -> int:
        a, b = self.nonzero, vec.nonzero
        if len(b) < len(a):
            a, b = b, a
        return sum(v * b.get(i, 0) for i, v in a.items())
