from leetcode_py import TreeNode


def run_recover_from_preorder(solution_class: type, traversal: str):
    implementation = solution_class()
    return implementation.recover_from_preorder(traversal)


def assert_recover_from_preorder(
    result: TreeNode[int] | None, expected_list: list[int | None]
) -> bool:
    expected = TreeNode[int].from_list(expected_list)
    assert result == expected
    return True
