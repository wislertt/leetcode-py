class Solution:
    # Time: O(sum of word lengths) (build set) + O(n * L) scan
    # Space: O(sum of word lengths)
    def longest_word(self, words: list[str]) -> str:
        seen: set[str] = set()
        best = ""
        for word in sorted(words):
            if len(word) == 1 or word[:-1] in seen:
                seen.add(word)
                if len(word) > len(best):
                    best = word
        return best
