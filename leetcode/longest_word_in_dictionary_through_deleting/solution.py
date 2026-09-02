class Solution:
    # Time: O(n * (len(s) + len(word)))
    # Space: O(1) extra beyond the answer
    def find_longest_word(self, s: str, dictionary: list[str]) -> str:
        def is_subsequence(word: str) -> bool:
            it = iter(s)
            return all(char in it for char in word)

        best = ""
        for word in dictionary:
            if not is_subsequence(word):
                continue
            if len(word) > len(best) or (len(word) == len(best) and word < best):
                best = word
        return best
