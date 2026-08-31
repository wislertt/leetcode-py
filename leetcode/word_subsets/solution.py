from collections import Counter


class Solution:
    # Time: O(w1 * avg_len + w2 * avg_len)
    # Space: O(1)
    def word_subsets(self, words1: list[str], words2: list[str]) -> list[str]:
        need = Counter()
        for word in words2:
            counts = Counter(word)
            for letter, count in counts.items():
                need[letter] = max(need[letter], count)
        return [word for word in words1 if not (need - Counter(word))]
