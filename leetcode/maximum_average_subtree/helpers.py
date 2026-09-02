from leetcode_py import TreeNode


def run_maximum_average_subtree(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list) if root_list else None
    implementation = solution_class()
    return implementation.maximum_average_subtree(root)


def assert_maximum_average_subtree(result: float, expected: float) -> bool:
    assert abs(result - expected) < 10**-4
    return True
