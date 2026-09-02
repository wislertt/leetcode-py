class Solution:
    # Time: O(n)
    # Space: O(n)
    def num_identical_pairs(self, nums: list[int]) -> int:
        counts: dict[int, int] = {}
        result = 0
        for num in nums:
            seen = counts.get(num, 0)
            result += seen
            counts[num] = seen + 1
        return result
