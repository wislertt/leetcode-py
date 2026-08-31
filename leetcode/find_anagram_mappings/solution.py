class Solution:
    # Time: O(n)
    # Space: O(n)
    def anagram_mappings(self, nums1: list[int], nums2: list[int]) -> list[int]:
        index = {x: i for i, x in enumerate(nums2)}
        return [index[x] for x in nums1]
