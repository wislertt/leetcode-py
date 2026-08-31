class Solution:
    # Time: O(n)
    # Space: O(1)
    def length_of_last_word(self, s: str) -> int:
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # Count characters of the last word
        length = 0
        while i >= 0 and s[i] != " ":
            i -= 1
            length += 1
        return length
