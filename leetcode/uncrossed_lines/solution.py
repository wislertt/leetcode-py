class Solution:
    # Time: O(m * n)
    # Space: O(min(m, n))
    def max_uncrossed_lines(self, nums1: list[int], nums2: list[int]) -> int:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        prev = [0] * (len(nums2) + 1)
        for a in nums1:
            curr = [0] * (len(nums2) + 1)
            for j, b in enumerate(nums2):
                if a == b:
                    curr[j + 1] = prev[j] + 1
                else:
                    curr[j + 1] = max(prev[j + 1], curr[j])
            prev = curr
        return prev[-1]
