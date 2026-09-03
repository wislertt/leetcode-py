from leetcode_py import TreeNode


def run_check_equal_tree(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.check_equal_tree(root)


def assert_check_equal_tree(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
