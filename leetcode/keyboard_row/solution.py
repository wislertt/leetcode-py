class Solution:
    # Time: O(n * m) where n = len(words), m = max word length
    # Space: O(1) (row sets are constant size)
    def find_words(self, words: list[str]) -> list[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        return [word for word in words if any(set(word.lower()) <= row for row in rows)]
