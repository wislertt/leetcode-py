class Solution:
    # Time: O(m * n) for m rows of length n
    # Space: O(1)
    def valid_word_square(self, words: list[str]) -> bool:
        for i, word in enumerate(words):
            for j, ch in enumerate(word):
                if j >= len(words) or i >= len(words[j]) or words[j][i] != ch:
                    return False
        return True
