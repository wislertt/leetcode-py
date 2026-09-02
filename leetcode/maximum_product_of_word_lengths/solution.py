class Solution:
    # Time: O(n * (L + n)) where n = len(words) and L = max word length
    # Space: O(n)
    def max_product(self, words: list[str]) -> int:
        masks = [self._letter_mask(word) for word in words]
        best = 0
        for i, mask_i in enumerate(masks):
            for j in range(i + 1, len(masks)):
                if mask_i & masks[j] == 0:
                    best = max(best, len(words[i]) * len(words[j]))
        return best

    def _letter_mask(self, word: str) -> int:
        mask = 0
        for char in word:
            mask |= 1 << (ord(char) - ord("a"))
        return mask
