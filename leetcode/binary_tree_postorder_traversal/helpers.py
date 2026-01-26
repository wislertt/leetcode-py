from leetcode_py import TreeNode


def run_postorder_traversal(solution_class: type, root_list: list[int | None]):
    root = TreeNode.from_list(root_list)
    implementation = solution_class()
    return implementation.postorder_traversal(root)


def assert_postorder_traversal(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
