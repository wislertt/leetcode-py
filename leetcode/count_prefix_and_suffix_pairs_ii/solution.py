from typing import Any


class Solution:
    # Time: O(total chars), each character pair inserted/visited once
    # Space: O(total chars) for the paired trie
    def count_prefix_and_suffix_pairs(self, words: list[str]) -> int:
        root: dict[Any, Any] = {}
        total = 0
        for word in words:
            node: dict[Any, Any] = root
            length = len(word)
            for i in range(length):
                key = (word[i], word[length - 1 - i])
                if key not in node:
                    node[key] = {}
                node = node[key]
                total += node.get("", 0)
            node[""] = node.get("", 0) + 1
        return total
