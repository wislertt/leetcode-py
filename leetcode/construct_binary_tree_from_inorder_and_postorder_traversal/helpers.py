from leetcode_py import TreeNode


def run_build_tree(solution_class: type, inorder: list[int], postorder: list[int]):
    implementation = solution_class()
    return implementation.build_tree(inorder, postorder)


def assert_build_tree(result: TreeNode[int] | None, expected_list: list[int | None]) -> bool:
    expected = TreeNode[int].from_list(expected_list)
    assert result == expected
    return True
