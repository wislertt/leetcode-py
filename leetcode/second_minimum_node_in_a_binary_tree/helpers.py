from leetcode_py import TreeNode


def run_find_second_minimum_value(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.find_second_minimum_value(root)


def assert_find_second_minimum_value(result: int, expected: int) -> bool:
    assert result == expected
    return True
