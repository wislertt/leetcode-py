from leetcode_py import TreeNode


def run_preorder_traversal(solution_class: type, root_list: list[int | None]):
    root = TreeNode.from_list(root_list)
    implementation = solution_class()
    return implementation.preorder_traversal(root)


def assert_preorder_traversal(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
