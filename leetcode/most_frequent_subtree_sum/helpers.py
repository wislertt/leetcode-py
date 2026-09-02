from leetcode_py import TreeNode


def run_find_frequent_tree_sum(solution_class: type, root_list: list[int | None]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.find_frequent_tree_sum(root)


def assert_find_frequent_tree_sum(result: list[int], expected: list[int]) -> bool:
    # Order does not matter; sort both sides for comparison
    assert sorted(result) == sorted(expected)
    return True
