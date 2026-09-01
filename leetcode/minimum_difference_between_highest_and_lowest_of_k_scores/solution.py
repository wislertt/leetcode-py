class Solution:
    # Time: O(n log n)
    # Space: O(n) for the sort
    def minimum_difference(self, nums: list[int], k: int) -> int:
        scores = sorted(nums)
        return min(scores[i + k - 1] - scores[i] for i in range(len(scores) - k + 1))
