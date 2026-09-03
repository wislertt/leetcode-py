from leetcode_py import TreeNode


def run_subtree_with_all_deepest(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    assert root is not None
    implementation = solution_class()
    return implementation.subtree_with_all_deepest(root)


def assert_subtree_with_all_deepest(
    result: TreeNode[int] | None, expected_list: list[int | None]
) -> bool:
    expected = TreeNode[int].from_list(expected_list)
    assert result == expected
    return True
