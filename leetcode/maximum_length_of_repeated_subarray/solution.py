class Solution:
    # Time: O(len(nums1) * len(nums2))
    # Space: O(len(nums2))
    def find_length(self, nums1: list[int], nums2: list[int]) -> int:
        best = 0
        prev = [0] * (len(nums2) + 1)
        for a in nums1:
            cur = [0] * (len(nums2) + 1)
            for j, b in enumerate(nums2, start=1):
                if a == b:
                    cur[j] = prev[j - 1] + 1
                    if cur[j] > best:
                        best = cur[j]
            prev = cur
        return best
