from leetcode_py import ListNode


def run_plus_one(solution_class: type, head_vals: list[int]):
    head = ListNode[int].from_list(head_vals)
    implementation = solution_class()
    return implementation.plus_one(head)


def assert_plus_one(result: ListNode[int] | None, expected_vals: list[int]) -> bool:
    expected = ListNode.from_list(expected_vals)
    assert result == expected
    return True
