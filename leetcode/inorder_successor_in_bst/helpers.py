from leetcode_py import TreeNode


def run_inorder_successor(solution_class: type, root_list: list[int | None], p_val: int):
    root = TreeNode[int].from_list(root_list)
    assert root is not None
    p = root.find_node(p_val)
    assert p is not None
    implementation = solution_class()
    return implementation.inorder_successor(root, p)


def assert_inorder_successor(result: TreeNode[int] | None, expected_val: int | None) -> bool:
    if expected_val is None:
        assert result is None
    else:
        assert result is not None
        assert result.val == expected_val
    return True
