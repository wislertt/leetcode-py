class Solution:
    # Time: O(n)
    # Space: O(n)
    def count_bad_pairs(self, nums: list[int]) -> int:
        good = 0
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            key = num - i
            good += seen.get(key, 0)
            seen[key] = seen.get(key, 0) + 1
        n = len(nums)
        return n * (n - 1) // 2 - good
