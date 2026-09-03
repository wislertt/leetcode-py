from leetcode_py import TreeNode


def run_vertical_traversal(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.vertical_traversal(root)


def assert_vertical_traversal(result: list[list[int]], expected_list: list[list[int]]) -> bool:
    assert result == expected_list
    return True
