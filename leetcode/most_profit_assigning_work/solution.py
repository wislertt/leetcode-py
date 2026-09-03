import bisect


class Solution:
    # Time: O(n log n + m log n)
    # Space: O(n)
    def max_profit_assignment(
        self, difficulty: list[int], profit: list[int], worker: list[int]
    ) -> int:
        pairs = sorted(zip(difficulty, profit, strict=True))
        diffs = [d for d, _ in pairs]
        best: list[int] = []
        top = 0
        for _d, p in pairs:
            top = max(top, p)
            best.append(top)
        total = 0
        for ability in worker:
            i = bisect.bisect_right(diffs, ability)
            if i > 0:
                total += best[i - 1]
        return total
