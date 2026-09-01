class Solution:
    # Time: O(n)
    # Space: O(min(n, p))
    def min_subarray(self, nums: list[int], p: int) -> int:
        total = sum(nums) % p
        if total == 0:
            return 0
        n = len(nums)
        last = {0: -1}
        cur = 0
        best = n
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            need = (cur - total) % p
            if need in last:
                best = min(best, i - last[need])
            last[cur] = i
        return -1 if best == n else best
