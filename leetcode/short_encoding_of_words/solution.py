class Solution:
    # Time: O(n * L^2) where n = len(words), L = max word length (suffix slices)
    # Space: O(n * L)
    def minimum_length_encoding(self, words: list[str]) -> int:
        unique = set(words)
        return sum(
            len(word) + 1
            for word in unique
            if not any(other.endswith(word) for other in unique if other != word)
        )
