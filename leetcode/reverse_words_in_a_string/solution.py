class Solution:
    # Time: O(n) where n is the length of the string
    # Space: O(n) for the split list
    def reverse_words(self, s: str) -> str:
        # Split by whitespace (handles multiple spaces)
        words = s.split()
        # Reverse the list and join with single space
        return " ".join(reversed(words))
