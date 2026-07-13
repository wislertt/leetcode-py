class Solution:
    # Time: O(m) where m is total characters across all words
    # Space: O(1)
    def is_alien_sorted(self, words: list[str], order: str) -> bool:
        rank = {ch: i for i, ch in enumerate(order)}

        def less_or_equal(word1: str, word2: str) -> bool:
            for ch1, ch2 in zip(word1, word2, strict=False):
                if rank[ch1] < rank[ch2]:
                    return True
                if rank[ch1] > rank[ch2]:
                    return False
            return len(word1) <= len(word2)

        return all(less_or_equal(words[i], words[i + 1]) for i in range(len(words) - 1))
