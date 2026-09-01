class Solution:
    # Time: O(n + m)
    # Space: O(1)
    def xor_all_nums(self, nums1: list[int], nums2: list[int]) -> int:
        # Each nums1[i] appears in len(nums2) pairings, each nums2[j] in len(nums1);
        # a value XORed an even number of times cancels out.
        result = 0
        if len(nums2) % 2:
            for num in nums1:
                result ^= num
        if len(nums1) % 2:
            for num in nums2:
                result ^= num
        return result
