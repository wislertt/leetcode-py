from collections import Counter


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def can_reorder_doubled(self, arr: list[int]) -> bool:
        counts = Counter(arr)
        for value in sorted(counts, key=abs):
            need = counts[value]
            if need == 0:
                continue
            if need > counts[2 * value]:
                return False
            counts[value] = 0
            counts[2 * value] -= need
        return True
