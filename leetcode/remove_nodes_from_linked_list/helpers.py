from leetcode_py import ListNode


def run_remove_nodes(solution_class: type, head_vals: list[int]):
    head = ListNode[int].from_list(head_vals)
    implementation = solution_class()
    return implementation.remove_nodes(head)


def assert_remove_nodes(result: ListNode[int] | None, expected_vals: list[int]) -> bool:
    expected = ListNode[int].from_list(expected_vals)
    assert result == expected
    return True
