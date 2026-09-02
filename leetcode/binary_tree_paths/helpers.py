from leetcode_py import TreeNode


def run_binary_tree_paths(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.binary_tree_paths(root)


def assert_binary_tree_paths(result: list[str], expected: list[str]) -> bool:
    # Sort both result and expected for comparison since order may vary
    assert sorted(result) == sorted(expected)
    return True
