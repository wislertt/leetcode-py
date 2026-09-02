class Solution:
    # Time: O(m + n)
    # Space: O(m + n) for the output
    def merge_arrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        result: list[list[int]] = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            if id1 == id2:
                result.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                result.append([id1, val1])
                i += 1
            else:
                result.append([id2, val2])
                j += 1
        result.extend(nums1[i:])
        result.extend(nums2[j:])
        return result
