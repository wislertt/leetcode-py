class Solution:
    # Time: O(n + m)
    # Space: O(n + m)
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return sorted(set(nums1) & set(nums2))
