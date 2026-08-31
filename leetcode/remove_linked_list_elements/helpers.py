from leetcode_py import ListNode


def run_remove_linked_list_elements(solution_class: type, head_vals: list[int], val: int):
    head = ListNode[int].from_list(head_vals)
    implementation = solution_class()
    return implementation.remove_linked_list_elements(head, val)


def assert_remove_linked_list_elements(
    result: ListNode[int] | None, expected_vals: list[int]
) -> bool:
    expected = ListNode[int].from_list(expected_vals)
    assert result == expected
    return True
