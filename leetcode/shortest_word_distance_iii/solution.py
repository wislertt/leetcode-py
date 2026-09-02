class Solution:
    # Time: O(n)
    # Space: O(1)
    def shortest_word_distance(self, words_dict: list[str], word1: str, word2: str) -> int:
        n = len(words_dict)
        ans = n
        if word1 == word2:
            prev = -1
            for i, w in enumerate(words_dict):
                if w == word1:
                    if prev != -1:
                        ans = min(ans, i - prev)
                    prev = i
        else:
            i = j = -1
            for k, w in enumerate(words_dict):
                if w == word1:
                    i = k
                if w == word2:
                    j = k
                if i != -1 and j != -1:
                    ans = min(ans, abs(i - j))
        return ans
