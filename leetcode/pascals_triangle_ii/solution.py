class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def get_row(self, row_index: int) -> list[int]:
        row = [1]
        for _ in range(row_index):
            row.append(1)
            for i in range(len(row) - 2, 0, -1):
                row[i] += row[i - 1]
        return row
