from collections import Counter


class Solution:
    # Reduces to house robber over consecutive value runs
    # Time: O(n + m log m) where m = number of distinct values
    # Space: O(m)
    def delete_and_earn(self, nums: list[int]) -> int:
        counts = Counter(nums)
        take = skip = 0
        previous = None
        for value in sorted(counts):
            gain = value * counts[value]
            if previous == value - 1:
                take, skip = skip + gain, max(take, skip)
            else:
                take, skip = max(take, skip) + gain, max(take, skip)
            previous = value
        return max(take, skip)
