from leetcode_py import ListNode


def run_delete_duplicates(solution_class: type, head_list: list[int]):
    head = ListNode[int].from_list(head_list)
    implementation = solution_class()
    return implementation.delete_duplicates(head)


def assert_delete_duplicates(result: ListNode[int] | None, expected_list: list[int]) -> bool:
    expected = ListNode[int].from_list(expected_list)
    assert result == expected
    return True
