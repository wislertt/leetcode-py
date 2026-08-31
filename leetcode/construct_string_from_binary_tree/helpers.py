from leetcode_py import TreeNode


def run_tree2str(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.tree2str(root)


def assert_tree2str(result: str, expected: str) -> bool:
    assert result == expected
    return True
