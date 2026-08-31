from leetcode_py import TreeNode


def run_has_path_sum(solution_class: type, root_list: list[int | None], target_sum: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.has_path_sum(root, target_sum)


def assert_has_path_sum(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
