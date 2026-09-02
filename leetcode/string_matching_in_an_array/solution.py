class Solution:
    # Time: O(n^2 * m) where n = len(words), m = max word length
    # Space: O(1) excluding the output list
    def string_matching(self, words: list[str]) -> list[str]:
        result: list[str] = []
        for i, word in enumerate(words):
            for j, other in enumerate(words):
                if i != j and word in other:
                    result.append(word)
                    break
        return result
