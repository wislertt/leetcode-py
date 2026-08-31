from leetcode_py import ListNode


def run_partition(solution_class: type, head_list: list[int], x: int):
    head = ListNode[int].from_list(head_list)
    implementation = solution_class()
    return implementation.partition(head, x)


def assert_partition(result: ListNode[int] | None, expected_list: list[int]) -> bool:
    expected = ListNode[int].from_list(expected_list)
    assert result == expected
    return True
