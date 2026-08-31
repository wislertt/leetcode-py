class Solution:
    # Time: O(n)
    # Space: O(n)
    def reverse_words(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(" "))
