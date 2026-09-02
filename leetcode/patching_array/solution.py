class Solution:
    # Time: O(len(nums) + log n)
    # Space: O(1)
    def min_patches(self, nums: list[int], n: int) -> int:
        patches = 0
        miss = 1  # smallest sum in [1, miss) that cannot be formed yet
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                patches += 1
                miss += miss
        return patches
