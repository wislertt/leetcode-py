from leetcode_py import TreeNode


def run_largest_values(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.largest_values(root)


def assert_largest_values(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
