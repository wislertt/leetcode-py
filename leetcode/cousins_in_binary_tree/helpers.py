from leetcode_py import TreeNode


def run_is_cousins(solution_class: type, root_list: list[int | None], x: int, y: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.is_cousins(root, x, y)


def assert_is_cousins(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
