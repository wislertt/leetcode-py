from __future__ import annotations


class Node:
    def __init__(self, val: int = 0, children: list[Node] | None = None) -> None:
        self.val = val
        self.children = children if children is not None else []


class Codec:
    # Time: O(n) for encode and decode
    # Space: O(n)
    def __init__(self) -> None:
        pass

    def encode(self, root: Node | None) -> str:
        vals: list[str] = []

        def dfs(node: Node | None) -> None:
            if node is None:
                return
            vals.append(str(node.val))
            vals.append(str(len(node.children)))
            for child in node.children:
                dfs(child)

        dfs(root)
        return ",".join(vals)

    def decode(self, data: str) -> Node | None:
        vals = [int(v) for v in data.split(",") if v != ""]
        pos = 0

        def dfs() -> Node | None:
            nonlocal pos
            if pos >= len(vals):
                return None
            node = Node(vals[pos])
            count = vals[pos + 1]
            pos += 2
            for _ in range(count):
                child = dfs()
                assert child is not None
                node.children.append(child)
            return node

        return dfs()
