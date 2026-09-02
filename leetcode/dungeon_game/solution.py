class Solution:
    # Time: O(m * n)
    # Space: O(n)
    def calculate_minimum_hp(self, dungeon: list[list[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        # need[j]: minimum health required upon entering cell (i, j); right
        # sentinel need[n] = INF means "no cell to the right" outside the grid.
        need = [10**9] * (n + 1)
        need[n - 1] = 1
        for i in range(m - 1, -1, -1):
            need[n] = 10**9
            for j in range(n - 1, -1, -1):
                need[j] = max(1, min(need[j], need[j + 1]) - dungeon[i][j])
        return need[0]
