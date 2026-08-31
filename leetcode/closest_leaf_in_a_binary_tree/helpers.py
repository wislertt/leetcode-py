from leetcode_py import TreeNode


def run_find_closest_leaf(solution_class: type, root_list: list[int | None], k: int):
    root = TreeNode[int].from_list(root_list) if root_list else None
    implementation = solution_class()
    return implementation.find_closest_leaf(root, k)


def assert_find_closest_leaf(result: int, expected: int) -> bool:
    assert result == expected
    return True
