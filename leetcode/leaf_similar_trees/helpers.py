from leetcode_py import TreeNode


def run_leaf_similar(
    solution_class: type, root1_list: list[int | None], root2_list: list[int | None]
):
    root1 = TreeNode[int].from_list(root1_list)
    root2 = TreeNode[int].from_list(root2_list)
    implementation = solution_class()
    return implementation.leaf_similar(root1, root2)


def assert_leaf_similar(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
