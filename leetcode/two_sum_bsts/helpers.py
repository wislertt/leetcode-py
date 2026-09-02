from leetcode_py import TreeNode


def run_two_sum_bsts(
    solution_class: type, root1_list: list[int | None], root2_list: list[int | None], target: int
):
    root1 = TreeNode[int].from_list(root1_list)
    root2 = TreeNode[int].from_list(root2_list)
    implementation = solution_class()
    return implementation.two_sum_bsts(root1, root2, target)


def assert_two_sum_bsts(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
