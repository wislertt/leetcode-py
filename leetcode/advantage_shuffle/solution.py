class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def advantage_count(self, nums1: list[int], nums2: list[int]) -> list[int]:
        sorted1 = sorted(nums1)
        order = sorted(range(len(nums2)), key=lambda i: nums2[i])
        result = [0] * len(nums1)
        low = 0
        high = len(nums1) - 1
        for idx in reversed(order):
            if sorted1[high] > nums2[idx]:
                result[idx] = sorted1[high]
                high -= 1
            else:
                result[idx] = sorted1[low]
                low += 1
        return result
