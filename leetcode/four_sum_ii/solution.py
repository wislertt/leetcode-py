class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def four_sum_count(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        pair_sums: dict[int, int] = {}
        for a in nums1:
            for b in nums2:
                pair_sums[a + b] = pair_sums.get(a + b, 0) + 1

        count = 0
        for c in nums3:
            for d in nums4:
                count += pair_sums.get(-(c + d), 0)
        return count
