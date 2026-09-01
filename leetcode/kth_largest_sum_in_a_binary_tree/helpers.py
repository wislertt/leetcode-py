from leetcode_py import TreeNode


def run_kth_largest_level_sum(solution_class: type, root_list: list[int | None], k: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.kth_largest_level_sum(root, k)


def assert_kth_largest_level_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
