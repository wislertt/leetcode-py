from leetcode_py import TreeNode


def run_smallest_from_leaf(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.smallest_from_leaf(root)


def assert_smallest_from_leaf(result: str, expected: str) -> bool:
    assert result == expected
    return True
