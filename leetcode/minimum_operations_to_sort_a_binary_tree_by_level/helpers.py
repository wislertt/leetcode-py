from leetcode_py import TreeNode


def run_minimum_operations(solution_class: type, root_list: list[int | None]):
    implementation = solution_class()
    root = TreeNode.from_list(root_list) if root_list else None
    return implementation.minimum_operations(root)


def assert_minimum_operations(result: int, expected: int) -> bool:
    assert result == expected
    return True
