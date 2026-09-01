class Solution:
    # Time: O(n + m)
    # Space: O(n + m)
    def find_difference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [sorted(set1 - set2), sorted(set2 - set1)]
