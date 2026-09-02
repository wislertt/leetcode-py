from leetcode_py import ListNode


def run_pair_sum(solution_class: type, head_list: list[int]):
    head = ListNode[int].from_list(head_list)
    implementation = solution_class()
    return implementation.pair_sum(head)


def assert_pair_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
