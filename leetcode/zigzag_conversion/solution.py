class Solution:
    # Time: O(n)
    # Space: O(n)
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows >= len(s):
            return s

        rows: list[list[str]] = [[] for _ in range(num_rows)]
        current_row = 0
        step = 1
        for char in s:
            rows[current_row].append(char)
            if current_row == 0:
                step = 1
            elif current_row == num_rows - 1:
                step = -1
            current_row += step

        return "".join("".join(row) for row in rows)
