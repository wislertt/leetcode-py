from leetcode_py import TreeNode


def run_find_leaves(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.find_leaves(root)


def assert_find_leaves(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Node order within each level does not matter.
    assert sorted(sorted(level) for level in result) == sorted(sorted(level) for level in expected)
    return True
