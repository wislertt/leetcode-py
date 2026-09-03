from leetcode_py import TreeNode


def run_increasing_bst(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.increasing_bst(root)


def assert_increasing_bst(result: TreeNode[int] | None, expected_list: list[int | None]) -> bool:
    expected = TreeNode[int].from_list(expected_list)
    assert result == expected
    return True
