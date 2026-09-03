from collections import Counter


class Solution:
    # Time: O(n^2 + n * d) where d is the number of distinct pair AND values
    # Space: O(d)
    def count_triplets(self, nums: list[int]) -> int:
        pair_counts: Counter[int] = Counter()
        for a in nums:
            for b in nums:
                pair_counts[a & b] += 1

        total = 0
        for x in nums:
            for pair_and, count in pair_counts.items():
                if pair_and & x == 0:
                    total += count
        return total
