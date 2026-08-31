from leetcode_py import TreeNode


def _to_level_list(root: TreeNode[int] | None) -> list[int | None]:
    """Serialize a tree to compact LeetCode level-order form."""
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


def run_find_duplicate_subtrees(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    roots = implementation.find_duplicate_subtrees(root)
    return sorted(_to_level_list(node) for node in roots)


def assert_find_duplicate_subtrees(
    result: list[list[int | None]], expected: list[list[int | None]]
) -> bool:
    assert sorted(result) == sorted(expected)
    return True
