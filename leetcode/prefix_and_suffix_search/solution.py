class WordFilter:
    # Time: __init__ O(n * L^2), f O(P + S)
    # Space: O(n * L^2) keys, each at most 2L + 1 characters
    def __init__(self, words: list[str]) -> None:
        # Encode every (prefix, suffix) pair of every word as "pref#suff". Because
        # words are visited in increasing index order, the last write for a key is the
        # largest matching index, which is exactly what f must return.
        self.best: dict[str, int] = {}
        for index, word in enumerate(words):
            for i in range(len(word) + 1):
                prefix = word[:i]
                for j in range(len(word) + 1):
                    self.best[f"{prefix}#{word[j:]}"] = index

    # Time: O(P + S)
    # Space: O(P + S)
    def f(self, pref: str, suff: str) -> int:
        return self.best.get(f"{pref}#{suff}", -1)
