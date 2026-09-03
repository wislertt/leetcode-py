class Solution:
    # Time: O(n * 30) - each OR set only holds distinct prefix-OR values, at most 30 bits
    # Space: O(30 * n) worst case across the rolling and global sets
    def subarray_bitwise_ors(self, arr: list[int]) -> int:
        seen: set[int] = set()
        current: set[int] = set()
        for num in arr:
            current = {num | prev for prev in current} | {num}
            seen |= current
        return len(seen)
