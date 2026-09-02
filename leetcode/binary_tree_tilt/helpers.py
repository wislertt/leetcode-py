def run_find_tilt(solution_class: type, root_list: list[int | None]):
    from leetcode_py import TreeNode

    root = TreeNode.from_list(root_list)
    implementation = solution_class()
    return implementation.find_tilt(root)


def assert_find_tilt(result: int, expected: int) -> bool:
    assert result == expected
    return True
