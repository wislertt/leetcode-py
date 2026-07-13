from leetcode_py import TreeNode


def run_rob(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.rob(root)


def assert_rob(result: int, expected: int) -> bool:
    assert result == expected
    return True
