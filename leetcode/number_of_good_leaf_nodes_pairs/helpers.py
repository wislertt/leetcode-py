from leetcode_py import TreeNode


def run_count_pairs(solution_class: type, root_list: list[int | None], distance: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.count_pairs(root, distance)


def assert_count_pairs(result: int, expected: int) -> bool:
    assert result == expected
    return True
