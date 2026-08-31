def run_count_unival_subtrees(solution_class: type, root_list: list[int | None]):
    from leetcode_py import TreeNode

    root = TreeNode.from_list(root_list)
    implementation = solution_class()
    return implementation.count_unival_subtrees(root)


def assert_count_unival_subtrees(result: int, expected: int) -> bool:
    assert result == expected
    return True
