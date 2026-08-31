from leetcode_py import ListNode


def run_insertion_sort_list(solution_class: type, head_vals: list[int]):
    head = ListNode[int].from_list(head_vals)
    implementation = solution_class()
    return implementation.insertion_sort_list(head)


def assert_insertion_sort_list(result: ListNode[int] | None, expected_vals: list[int]) -> bool:
    expected = ListNode[int].from_list(expected_vals)
    assert result == expected
    return True
