from leetcode_py import TreeNode


def run_evaluate_tree(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.evaluate_tree(root)


def assert_evaluate_tree(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
