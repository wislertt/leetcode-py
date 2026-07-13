class Solution:
    # Time: O(m + n)
    # Space: O(1)
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Fill from the back to avoid overwriting nums1's real elements
        index = m + n - 1
        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1

        # Only nums2 leftovers can remain
        while j >= 0:
            nums1[index] = nums2[j]
            j -= 1
            index -= 1
