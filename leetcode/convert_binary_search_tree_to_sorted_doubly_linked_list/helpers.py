from leetcode_py import TreeNode


def run_tree_to_doubly_list(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list) if root_list else None
    implementation = solution_class()
    return implementation.tree_to_doubly_list(root)


def assert_tree_to_doubly_list(
    result: TreeNode[int] | None, expected_list: list[int] | None
) -> bool:
    if expected_list is None:
        assert result is None
        return True
    assert result is not None
    head = result
    vals: list[int] = []
    node: TreeNode[int] | None = head
    while True:
        assert node is not None
        vals.append(node.val)
        node = node.right
        if node is head:
            break
    assert vals == expected_list
    assert head.left is not None
    assert head.left.right is head
    return True
