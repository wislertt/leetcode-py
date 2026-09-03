from leetcode_py import TreeNode


def run_longest_univalue_path(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.longest_univalue_path(root)


def assert_longest_univalue_path(result: int, expected: int) -> bool:
    assert result == expected
    return True
