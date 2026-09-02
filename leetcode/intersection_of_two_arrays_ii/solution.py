from collections import Counter


class Solution:
    # Time: O(m + n)
    # Space: O(min(m, n))
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        counts = Counter(nums1)
        result: list[int] = []
        for num in nums2:
            if counts[num] > 0:
                counts[num] -= 1
                result.append(num)
        return result
