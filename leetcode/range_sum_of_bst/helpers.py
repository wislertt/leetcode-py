from leetcode_py import TreeNode


def run_range_sum_bst(solution_class: type, root_list: list[int | None], low: int, high: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.range_sum_bst(root, low, high)


def assert_range_sum_bst(result: int, expected: int) -> bool:
    assert result == expected
    return True
