from leetcode_py import TreeNode


def run_average_of_levels(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list) if root_list else None
    implementation = solution_class()
    return implementation.average_of_levels(root)


def assert_average_of_levels(result: list[float], expected: list[float]) -> bool:
    assert len(result) == len(expected)
    assert all(abs(a - b) < 10**-5 for a, b in zip(result, expected, strict=True))
    return True
