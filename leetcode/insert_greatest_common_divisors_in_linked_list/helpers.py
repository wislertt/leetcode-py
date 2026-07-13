from leetcode_py import ListNode


def run_insert_greatest_common_divisors(solution_class: type, head_list: list[int]):
    head = ListNode[int].from_list(head_list)
    implementation = solution_class()
    return implementation.insert_greatest_common_divisors(head)


def assert_insert_greatest_common_divisors(
    result: ListNode[int] | None, expected_list: list[int]
) -> bool:
    expected = ListNode[int].from_list(expected_list)
    assert result == expected
    return True
