from collections import defaultdict
from heapq import nlargest


class Solution:
    # Time: O(n log n) for sorting scores
    # Space: O(n)
    def high_five(self, items: list[list[int]]) -> list[list[int]]:
        scores: dict[int, list[int]] = defaultdict(list)
        for student, score in items:
            scores[student].append(score)
        return [[student, sum(nlargest(5, vals)) // 5] for student, vals in sorted(scores.items())]
