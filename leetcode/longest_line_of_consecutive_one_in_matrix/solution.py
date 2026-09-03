class Solution:
    # Time: O(m * n)
    # Space: O(n)
    def longest_line(self, mat: list[list[int]]) -> int:
        n = len(mat[0])
        prev_vertical = [0] * n
        prev_diagonal = [0] * n
        prev_anti_diagonal = [0] * n
        best = 0
        for row in mat:
            cur_vertical = [0] * n
            cur_diagonal = [0] * n
            cur_anti_diagonal = [0] * n
            horizontal = 0
            for j, value in enumerate(row):
                if value == 1:
                    horizontal += 1
                    cur_vertical[j] = prev_vertical[j] + 1
                    cur_diagonal[j] = prev_diagonal[j - 1] + 1 if j > 0 else 1
                    cur_anti_diagonal[j] = prev_anti_diagonal[j + 1] + 1 if j + 1 < n else 1
                    best = max(
                        best, horizontal, cur_vertical[j], cur_diagonal[j], cur_anti_diagonal[j]
                    )
                else:
                    horizontal = 0
            prev_vertical = cur_vertical
            prev_diagonal = cur_diagonal
            prev_anti_diagonal = cur_anti_diagonal
        return best
