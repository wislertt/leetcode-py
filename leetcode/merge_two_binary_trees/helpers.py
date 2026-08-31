from leetcode_py import TreeNode


def _to_level_list(root: TreeNode[int] | None) -> list[int | None]:
    """Serialize a tree back to compact LeetCode level-order form."""
    out: list[int | None] = []
    queue: list[TreeNode[int] | None] = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def run_merge_trees(
    solution_class: type, root1_list: list[int | None], root2_list: list[int | None]
):
    root1 = TreeNode[int].from_list(root1_list)
    root2 = TreeNode[int].from_list(root2_list)
    implementation = solution_class()
    return _to_level_list(implementation.merge_trees(root1, root2))


def assert_merge_trees(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
