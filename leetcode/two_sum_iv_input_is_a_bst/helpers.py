from leetcode_py import TreeNode


def run_find_target(solution_class: type, root_list: list[int | None], k: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.find_target(root, k)


def assert_find_target(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
