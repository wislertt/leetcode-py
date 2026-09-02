from leetcode_py import ListNode


class Solution:
    # Time: O(m * n)
    # Space: O(1) extra (output matrix excluded)
    def spiral_matrix(self, m: int, n: int, head: ListNode[int] | None) -> list[list[int]]:
        grid = [[-1] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row = col = d = 0

        node = head
        while node is not None:
            grid[row][col] = node.val
            node = node.next
            if node is None:
                break
            next_row, next_col = row + directions[d][0], col + directions[d][1]
            if not (0 <= next_row < m and 0 <= next_col < n and grid[next_row][next_col] == -1):
                d = (d + 1) % 4
                next_row, next_col = row + directions[d][0], col + directions[d][1]
            row, col = next_row, next_col

        return grid
