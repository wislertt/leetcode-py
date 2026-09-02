from leetcode_py import TreeNode


def run_get_minimum_difference(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.get_minimum_difference(root)


def assert_get_minimum_difference(result: int, expected: int) -> bool:
    assert result == expected
    return True
