class Solution:
    # Time: O(n)
    # Space: O(1)
    def is_ideal_permutation(self, nums: list[int]) -> bool:
        # A global inversion that is not local needs indices i, j with j > i + 1
        # and nums[i] > nums[j]. In a permutation that can only happen when some
        # value sits more than one slot away from its own index, so every value
        # must be within distance 1 of its position.
        return all(abs(value - index) <= 1 for index, value in enumerate(nums))
