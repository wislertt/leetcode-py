from leetcode_py import TreeNode


def run_create_binary_tree(solution_class: type, descriptions_list: list[list[int]]):
    implementation = solution_class()
    return implementation.create_binary_tree(descriptions_list)


def assert_create_binary_tree(
    result: TreeNode[int] | None, expected_list: list[int | None]
) -> bool:
    expected = TreeNode[int].from_list(expected_list)
    assert result == expected
    return True
