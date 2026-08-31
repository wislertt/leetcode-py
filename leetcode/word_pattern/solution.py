class Solution:
    # Time: O(n)  # n = number of words in s
    # Space: O(n)
    def word_pattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word: dict[str, str] = {}
        word_to_char: dict[str, str] = {}
        for char, word in zip(pattern, words, strict=True):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            elif word in word_to_char:
                return False
            else:
                char_to_word[char] = word
                word_to_char[word] = char
        return True
