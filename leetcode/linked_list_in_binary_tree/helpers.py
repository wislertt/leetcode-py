from leetcode_py import ListNode, TreeNode


def run_is_sub_path(solution_class: type, head_list: list[int], root_list: list[int | None]):
    head = ListNode[int].from_list(head_list)
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.is_sub_path(head, root)


def assert_is_sub_path(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
