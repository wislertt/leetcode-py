from collections import Counter


class Solution:
    # Time: O(sum len(words))
    # Space: O(1) for the counter (26 letters)
    def common_chars(self, words: list[str]) -> list[str]:
        common = Counter(words[0])
        for word in words[1:]:
            common &= Counter(word)
        return list(common.elements())
