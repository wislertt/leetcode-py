from leetcode_py import TreeNode


def run_closest_value(solution_class: type, root_list: list[int | None], target: float):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.closest_value(root, target)


def assert_closest_value(result: int, expected: int) -> bool:
    assert result == expected
    return True
