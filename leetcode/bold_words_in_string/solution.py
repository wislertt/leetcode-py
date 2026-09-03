class Trie:
    def __init__(self) -> None:
        self.children: dict[str, Trie] = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True


class Solution:
    # Time: O(total keyword chars + n * max keyword length + n)
    # Space: O(total keyword chars + n)
    def bold_words(self, words: list[str], s: str) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        n = len(s)
        intervals: list[list[int]] = []
        for i in range(n):
            node = trie
            for j in range(i, n):
                nxt = node.children.get(s[j])
                if nxt is None:
                    break
                node = nxt
                if node.is_end:
                    if intervals and intervals[-1][1] + 1 >= i:
                        intervals[-1][1] = max(intervals[-1][1], j)
                    else:
                        intervals.append([i, j])

        parts: list[str] = []
        prev = 0
        for start, end in intervals:
            parts.append(s[prev:start])
            parts.append("<b>")
            parts.append(s[start : end + 1])
            parts.append("</b>")
            prev = end + 1
        parts.append(s[prev:])
        return "".join(parts)
