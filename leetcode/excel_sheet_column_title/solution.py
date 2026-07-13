class Solution:
    # Time: O(log_26 n)
    # Space: O(log_26 n)
    def convert_to_title(self, column_number: int) -> str:
        result: list[str] = []

        while column_number > 0:
            column_number -= 1  # shift 1-indexed alphabet to 0-indexed
            result.append(chr(ord("A") + column_number % 26))
            column_number //= 26

        return "".join(reversed(result))
