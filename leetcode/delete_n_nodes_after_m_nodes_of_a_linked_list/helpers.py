from leetcode_py import ListNode


def run_delete_nodes(solution_class: type, head_vals: list[int], m: int, n: int):
    head = ListNode[int].from_list(head_vals)
    implementation = solution_class()
    return implementation.delete_nodes(head, m, n)


def assert_delete_nodes(result: ListNode[int] | None, expected_vals: list[int]) -> bool:
    expected = ListNode[int].from_list(expected_vals)
    assert result == expected
    return True
