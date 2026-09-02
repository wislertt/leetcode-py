from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(n)
    def find_matrix(self, nums: list[int]) -> list[list[int]]:
        counts = Counter(nums)
        rows: list[list[int]] = [[] for _ in range(max(counts.values()))]
        for value, count in counts.items():
            for row in rows[:count]:
                row.append(value)
        return rows
