from leetcode_py import TreeNode


def run_remove_leaf_nodes(solution_class: type, root_list: list[int | None], target: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.remove_leaf_nodes(root, target)


def assert_remove_leaf_nodes(result: TreeNode[int] | None, expected_list: list[int | None]) -> bool:
    expected = TreeNode[int].from_list(expected_list)
    assert result == expected
    return True
