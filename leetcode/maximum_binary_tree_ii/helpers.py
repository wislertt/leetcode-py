from leetcode_py import TreeNode


def run_insert_into_max_tree(solution_class: type, root_list: list[int | None], val: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.insert_into_max_tree(root, val)


def assert_insert_into_max_tree(
    result: TreeNode[int] | None, expected_list: list[int | None]
) -> bool:
    expected = TreeNode[int].from_list(expected_list)
    assert result == expected
    return True
