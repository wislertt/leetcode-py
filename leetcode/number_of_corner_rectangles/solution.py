from collections import Counter


class Solution:
    # Time: O(m * n^2)
    # Space: O(n^2)
    def count_corner_rectangles(self, grid: list[list[int]]) -> int:
        ans = 0
        cnt: Counter[tuple[int, int]] = Counter()
        for row in grid:
            ones = [i for i, v in enumerate(row) if v]
            for a in range(len(ones)):
                for b in range(a + 1, len(ones)):
                    pair = (ones[a], ones[b])
                    ans += cnt[pair]
                    cnt[pair] += 1
        return ans
