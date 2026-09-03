from leetcode_py import TreeNode


def run_is_unival_tree(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.is_unival_tree(root)


def assert_is_unival_tree(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
