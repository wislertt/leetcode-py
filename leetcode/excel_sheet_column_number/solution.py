class Solution:
    # Time: O(n)
    # Space: O(1)
    def title_to_number(self, column_title: str) -> int:
        result = 0
        for char in column_title:
            result = result * 26 + (ord(char) - ord("A") + 1)
        return result
