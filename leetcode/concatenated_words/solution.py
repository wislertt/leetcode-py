class Solution:
    # Time: O(n * m^2) where n = len(words), m = max word length
    # Space: O(n * m)
    def find_all_concatenated_words_in_a_dict(self, words: list[str]) -> list[str]:
        word_set = set(words)

        def can_form(word: str) -> bool:
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(1, n + 1):
                for j in range(i):
                    if not dp[j]:
                        continue
                    if j == 0 and i == n:
                        continue
                    if word[j:i] in word_set:
                        dp[i] = True
                        break
            return dp[n]

        return [word for word in words if can_form(word)]
