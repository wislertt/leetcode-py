from leetcode_py import TreeNode


class Codec:
    # Time: O(n) serialize, O(h) amortized per node for deserialize
    # Space: O(n)
    def __init__(self) -> None:
        pass

    def serialize(self, root: TreeNode[int] | None) -> str:
        values: list[str] = []
        stack: list[TreeNode[int]] = [root] if root is not None else []
        while stack:
            node = stack.pop()
            values.append(str(node.val))
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return ",".join(values)

    def deserialize(self, data: str) -> TreeNode[int] | None:
        values = [int(token) for token in data.split(",") if token]
        if not values:
            return None

        root = TreeNode(values[0])
        stack: list[TreeNode[int]] = [root]
        for value in values[1:]:
            node = TreeNode(value)
            if value < stack[-1].val:
                stack[-1].left = node
            else:
                parent = stack[-1]
                while stack and stack[-1].val < value:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)
        return root
