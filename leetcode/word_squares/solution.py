class Solution:
    # Time: O(N * 26^L) where N = len(words), L = word length
    # Space: O(N * L) for the prefix map
    def word_squares(self, words: list[str]) -> list[list[str]]:
        n = len(words[0])
        prefixes: dict[str, list[str]] = {}
        for word in words:
            for i in range(n + 1):
                prefixes.setdefault(word[:i], []).append(word)

        results: list[list[str]] = []
        square: list[str] = []

        def backtrack() -> None:
            if len(square) == n:
                results.append(square[:])
                return
            prefix = "".join(word[len(square)] for word in square)
            for word in prefixes.get(prefix, []):
                square.append(word)
                backtrack()
                square.pop()

        backtrack()
        return results
