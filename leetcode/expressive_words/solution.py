class Solution:
    # Time: O(len(s) + sum(len(w) for w in words))
    # Space: O(len(s)) for the reference group encoding of s
    def expressive_words(self, s: str, words: list[str]) -> int:
        s_groups = self._group(s)

        def stretchy(word: str) -> bool:
            w_groups = self._group(word)
            if len(w_groups) != len(s_groups):
                return False
            return all(
                s_char == w_char and (s_len == w_len or (s_len >= 3 and s_len > w_len))
                for (s_char, s_len), (w_char, w_len) in zip(s_groups, w_groups, strict=True)
            )

        return sum(1 for word in words if stretchy(word))

    def _group(self, text: str) -> list[tuple[str, int]]:
        groups: list[tuple[str, int]] = []
        for char in text:
            if groups and groups[-1][0] == char:
                prev_char, prev_len = groups[-1]
                groups[-1] = (prev_char, prev_len + 1)
            else:
                groups.append((char, 1))
        return groups
