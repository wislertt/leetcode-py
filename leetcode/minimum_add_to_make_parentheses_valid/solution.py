class Solution:
    # Time: O(?)
    # Space: O(?)
    def min_add_to_make_valid(self, s: str) -> int:
        open_needed = 0
        insertions = 0
        for char in s:
            if char == "(":
                open_needed += 1
            elif open_needed > 0:
                open_needed -= 1
            else:
                insertions += 1
        return insertions + open_needed
