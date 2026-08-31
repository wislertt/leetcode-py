from leetcode_py import TreeNode


def run_find_bottom_left_value(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.find_bottom_left_value(root)


def assert_find_bottom_left_value(result: int, expected: int) -> bool:
    assert result == expected
    return True
