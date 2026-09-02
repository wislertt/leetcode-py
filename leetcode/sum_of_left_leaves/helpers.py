from leetcode_py import TreeNode


def run_sum_of_left_leaves(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.sum_of_left_leaves(root)


def assert_sum_of_left_leaves(result: int, expected: int) -> bool:
    assert result == expected
    return True
