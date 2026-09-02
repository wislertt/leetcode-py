from leetcode_py import TreeNode


def run_find_mode(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list) if root_list else None
    implementation = solution_class()
    return implementation.find_mode(root)


def assert_find_mode(result: list[int], expected: list[int]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
