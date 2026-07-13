from leetcode_py import TreeNode


def run_zigzag_level_order(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.zigzag_level_order(root)


def assert_zigzag_level_order(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
