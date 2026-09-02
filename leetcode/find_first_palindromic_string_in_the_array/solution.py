class Solution:
    # Time: O(total characters)
    # Space: O(1)
    def first_palindrome(self, words: list[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
