from collections import defaultdict


class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def tuple_same_product(self, nums: list[int]) -> int:
        product_counts: dict[int, int] = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                product_counts[nums[i] * nums[j]] += 1
        return sum(8 * c * (c - 1) // 2 for c in product_counts.values())
