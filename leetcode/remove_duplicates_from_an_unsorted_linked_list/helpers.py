from leetcode_py import ListNode


def run_delete_duplicates_unsorted(solution_class: type, head_vals: list[int]):
    head = ListNode[int].from_list(head_vals)
    implementation = solution_class()
    return implementation.delete_duplicates_unsorted(head)


def assert_delete_duplicates_unsorted(
    result: ListNode[int] | None, expected_vals: list[int]
) -> bool:
    expected = ListNode[int].from_list(expected_vals)
    assert result == expected
    return True
