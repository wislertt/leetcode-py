class Solution:
    # Time: O(m^2 * n) where m is column count and n is row count
    # Space: O(m)
    def min_deletion_size(self, strs: list[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        # best[j] = max number of columns we can keep ending with column j
        best = [1] * cols
        for j in range(cols):
            for i in range(j):
                if all(strs[r][i] <= strs[r][j] for r in range(rows)):
                    best[j] = max(best[j], best[i] + 1)
        return cols - max(best)
