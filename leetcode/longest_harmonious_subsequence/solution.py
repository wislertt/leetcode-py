from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(n)
    def find_lhs(self, nums: list[int]) -> int:
        counts = Counter(nums)
        longest = 0
        for value, count in counts.items():
            if value + 1 in counts:
                longest = max(longest, count + counts[value + 1])
        return longest
