class Solution:
    # Time: O(len(ops))
    # Space: O(1)
    def max_count(self, m: int, n: int, ops: list[list[int]]) -> int:
        if not ops:
            return m * n
        min_a = min(op[0] for op in ops)
        min_b = min(op[1] for op in ops)
        return min_a * min_b
