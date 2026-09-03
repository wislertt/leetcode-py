from __future__ import annotations


class MapSum:
    # Each node holds the sum of the values of every key passing through it.
    # Re-inserting a key applies only the value delta to the affected path.

    def __init__(self) -> None:
        self.children: dict[str, MapSum] = {}
        self.total = 0
        self.key_values: dict[str, int] = {}

    # Time: O(k) where k is the key length
    # Space: O(k)
    def insert(self, key: str, val: int) -> None:
        delta = val - self.key_values.get(key, 0)
        self.key_values[key] = val
        node: MapSum = self
        for char in key:
            node = node.children.setdefault(char, MapSum())
            node.total += delta

    # Time: O(p) where p is the prefix length
    # Space: O(1)
    def sum(self, prefix: str) -> int:
        node: MapSum | None = self
        for char in prefix:
            node = node.children.get(char)
            if node is None:
                return 0
        assert node is not None
        return node.total
