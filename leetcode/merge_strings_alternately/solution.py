class Solution:
    # Time: O(n + m)
    # Space: O(n + m)
    def merge_alternately(self, word1: str, word2: str) -> str:
        result: list[str] = []
        i = 0
        n, m = len(word1), len(word2)

        while i < n or i < m:
            if i < n:
                result.append(word1[i])
            if i < m:
                result.append(word2[i])
            i += 1

        return "".join(result)
