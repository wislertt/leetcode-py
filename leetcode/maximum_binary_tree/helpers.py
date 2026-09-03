from leetcode_py import TreeNode


def run_construct_maximum_binary_tree(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.construct_maximum_binary_tree(nums)


def assert_construct_maximum_binary_tree(
    result: TreeNode[int] | None, expected_list: list[int | None]
) -> bool:
    expected = TreeNode[int].from_list(expected_list)
    assert result == expected
    return True
