from leetcode_py import TreeNode


def run_boundary_of_binary_tree(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list) if root_list else None
    implementation = solution_class()
    return implementation.boundary_of_binary_tree(root)


def assert_boundary_of_binary_tree(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
