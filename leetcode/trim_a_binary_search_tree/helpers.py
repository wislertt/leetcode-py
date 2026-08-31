from leetcode_py import TreeNode


def run_trim_bst(solution_class: type, root_list: list[int | None], low: int, high: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.trim_bst(root, low, high)


def assert_trim_bst(result: TreeNode[int] | None, expected_list: list[int | None]) -> bool:
    expected = TreeNode[int].from_list(expected_list)
    assert result == expected
    return True
