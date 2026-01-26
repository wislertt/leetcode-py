from leetcode_py import TreeNode


def run_inorder_traversal(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.inorder_traversal(root)


def assert_inorder_traversal(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
