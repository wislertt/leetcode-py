from leetcode_py import TreeNode


def run_min_diff_in_bst(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.min_diff_in_bst(root)


def assert_min_diff_in_bst(result: int, expected: int) -> bool:
    assert result == expected
    return True
