def run_largest_bst_subtree(solution_class: type, root_list: list[int | None]):
    from leetcode_py import TreeNode

    root = TreeNode.from_list(root_list)
    implementation = solution_class()
    return implementation.largest_bst_subtree(root)


def assert_largest_bst_subtree(result: int, expected: int) -> bool:
    assert result == expected
    return True
