class Solution:
    # Time: O(n * m) where n = len(words), m = max word length
    # Space: O(1) since allowed is at most 26 characters
    def count_consistent_strings(self, allowed: str, words: list[str]) -> int:
        allowed_mask = 0
        for ch in allowed:
            allowed_mask |= 1 << (ord(ch) - ord("a"))

        count = 0
        for word in words:
            word_mask = 0
            for ch in word:
                word_mask |= 1 << (ord(ch) - ord("a"))
            if word_mask | allowed_mask == allowed_mask:
                count += 1
        return count
