from leetcode_py import TreeNode


def run_sum_numbers(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.sum_numbers(root)


def assert_sum_numbers(result: int, expected: int) -> bool:
    assert result == expected
    return True
