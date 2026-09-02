from leetcode_py import TreeNode


def run_longest_consecutive(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list) if root_list else None
    implementation = solution_class()
    return implementation.longest_consecutive(root)


def assert_longest_consecutive(result: int, expected: int) -> bool:
    assert result == expected
    return True
