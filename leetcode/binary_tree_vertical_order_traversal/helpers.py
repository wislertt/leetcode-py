def run_vertical_order(solution_class: type, root_list: list[int | None]):
    from leetcode_py import TreeNode

    root = TreeNode.from_list(root_list)
    implementation = solution_class()
    return implementation.vertical_order(root)


def assert_vertical_order(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
