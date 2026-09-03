class _TrieNode:
    __slots__ = ("children", "word")

    def __init__(self) -> None:
        self.children: dict[str, _TrieNode] = {}
        self.word: str | None = None


class Solution:
    # Time: O(total chars in dictionary + total chars in sentence)
    # Space: O(total chars in dictionary)
    def replace_words(self, dictionary: list[str], sentence: str) -> str:
        root = _TrieNode()
        for entry in dictionary:
            node = root
            for char in entry:
                node = node.children.setdefault(char, _TrieNode())
            node.word = entry

        def shortest_root(word: str) -> str:
            node = root
            for char in word:
                if node.word is not None:
                    return node.word
                if char not in node.children:
                    return word
                node = node.children[char]
            return node.word if node.word is not None else word

        return " ".join(shortest_root(word) for word in sentence.split())
