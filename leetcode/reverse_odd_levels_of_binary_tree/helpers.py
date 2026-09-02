from leetcode_py import TreeNode


def run_reverse_odd_levels(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.reverse_odd_levels(root)


def assert_reverse_odd_levels(
    result: TreeNode[int] | None, expected_list: list[int | None]
) -> bool:
    expected = TreeNode[int].from_list(expected_list)
    assert result == expected
    return True
