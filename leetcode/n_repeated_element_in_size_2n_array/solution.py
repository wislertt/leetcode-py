class Solution:
    # Time: O(n) worst case, returns after a handful of checks in practice
    # Space: O(1)
    def repeated_n_times(self, nums: list[int]) -> int:
        # Pigeonhole: the n copies of the answer cannot all sit 3+ slots apart,
        # so some pair at distance 1 or 2 must match. The only way no such pair
        # exists is n == 2 with the answer at both ends, hence the fallback.
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] or nums[i] == nums[i - 2]:
                return nums[i]
        return nums[0]
