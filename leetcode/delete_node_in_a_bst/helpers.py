from leetcode_py import TreeNode


def _inorder(node: TreeNode[int] | None) -> list[int]:
    """Inorder traversal; for a valid BST this yields strictly increasing values."""
    values: list[int] = []
    stack: list[TreeNode[int]] = []
    current: TreeNode[int] | None = node
    while stack or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        values.append(current.val)
        current = current.right
    return values


def run_delete_node(solution_class: type, root_list: list[int | None], key: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    result = implementation.delete_node(root, key)
    return _inorder(result)


def assert_delete_node(result: list[int], expected: list[int]) -> bool:
    # Inorder of a BST must equal the sorted remaining values.
    assert result == expected
    assert result == sorted(result)
    return True
