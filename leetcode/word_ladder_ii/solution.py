from string import ascii_lowercase


class Solution:
    # Time: O(N * L^2) BFS over N words of length L, plus backtracking over the
    # shortest-path DAG bounded by the total output size.
    # Space: O(N * L) for the parent graph and recursion stack.
    def find_ladders(self, begin_word: str, end_word: str, word_list: list[str]) -> list[list[str]]:
        words = set(word_list)
        if end_word not in words:
            return []
        words.discard(begin_word)

        parents: dict[str, list[str]] = {}
        level = [begin_word]
        reached = False
        while level and not reached:
            discovered: dict[str, list[str]] = {}
            for word in level:
                for i in range(len(word)):
                    prefix, suffix = word[:i], word[i + 1 :]
                    for ch in ascii_lowercase:
                        candidate = prefix + ch + suffix
                        if candidate in words and candidate not in parents:
                            discovered.setdefault(candidate, []).append(word)
            reached = end_word in discovered
            for candidate, defs in discovered.items():
                parents[candidate] = defs
                words.discard(candidate)
            level = list(discovered)

        paths: list[list[str]] = []
        if not reached:
            return paths
        self._backtrack(end_word, begin_word, parents, [end_word], paths)
        return paths

    def _backtrack(
        self,
        word: str,
        begin_word: str,
        parents: dict[str, list[str]],
        path: list[str],
        paths: list[list[str]],
    ) -> None:
        if word == begin_word:
            paths.append(path[::-1])
            return
        for parent in parents[word]:
            path.append(parent)
            self._backtrack(parent, begin_word, parents, path, paths)
            path.pop()
