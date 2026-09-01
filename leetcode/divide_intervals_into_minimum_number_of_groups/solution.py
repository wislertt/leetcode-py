class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def min_groups(self, intervals: list[list[int]]) -> int:
        starts = sorted(left for left, _ in intervals)
        ends = sorted(r for _, r in intervals)
        groups = 0
        j = 0
        for start in starts:
            if start > ends[j]:
                j += 1
            else:
                groups += 1
        return groups
