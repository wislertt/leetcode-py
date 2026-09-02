class Solution:
    # Time: O(n)
    # Space: O(n)
    def min_operations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        n = len(nums)
        if target == 0:
            return n
        if target < 0:
            return -1
        best = -1
        first_at = {0: -1}
        prefix = 0
        for i, val in enumerate(nums):
            prefix += val
            j = first_at.get(prefix - target)
            if j is not None and i - j > best:
                best = i - j
            if prefix not in first_at:
                first_at[prefix] = i
        return n - best if best != -1 else -1
