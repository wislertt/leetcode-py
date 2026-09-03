def run_print_tree(solution_class: type, root_list: list[int | None]):
    from leetcode_py import TreeNode

    root = TreeNode.from_list(root_list)
    implementation = solution_class()
    return implementation.print_tree(root)


def assert_print_tree(result: list[list[str]], expected: list[list[str]]) -> bool:
    assert result == expected
    return True
