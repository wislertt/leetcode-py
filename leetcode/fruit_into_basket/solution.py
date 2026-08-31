from collections import defaultdict


class Solution:
    # Time: O(n)
    # Space: O(1)
    def total_fruit(self, fruits: list[int]) -> int:
        counts: defaultdict[int, int] = defaultdict(int)
        left = 0
        best = 0
        for right, fruit in enumerate(fruits):
            counts[fruit] += 1
            while len(counts) > 2:
                left_fruit = fruits[left]
                counts[left_fruit] -= 1
                if counts[left_fruit] == 0:
                    del counts[left_fruit]
                left += 1
            best = max(best, right - left + 1)
        return best
