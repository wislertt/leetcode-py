from leetcode_py import TreeNode


def run_add_one_row(solution_class: type, root_list: list[int | None], val: int, depth: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.add_one_row(root, val, depth)


def assert_add_one_row(result: TreeNode[int] | None, expected_list: list[int | None]) -> bool:
    expected = TreeNode[int].from_list(expected_list)
    assert result == expected
    return True
