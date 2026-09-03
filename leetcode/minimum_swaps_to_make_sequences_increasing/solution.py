class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_swap(self, nums1: list[int], nums2: list[int]) -> int:
        keep = 0
        swap = 1
        for i in range(1, len(nums1)):
            keep_next = swap_next = len(nums1)
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                keep_next = keep
                swap_next = swap + 1
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                keep_next = min(keep_next, swap)
                swap_next = min(swap_next, keep + 1)
            keep, swap = keep_next, swap_next
        return min(keep, swap)
