class Solution:
    # Time: O(n log n)
    # Space: O(1) (sort is in-place for this input list)
    def largest_perimeter(self, nums: list[int]) -> int:
        lengths = sorted(nums, reverse=True)
        for i in range(len(lengths) - 2):
            if lengths[i] < lengths[i + 1] + lengths[i + 2]:
                return lengths[i] + lengths[i + 1] + lengths[i + 2]
        return 0
