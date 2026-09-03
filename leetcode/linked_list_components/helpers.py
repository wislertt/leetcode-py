from leetcode_py import ListNode


def run_num_components(solution_class: type, head_vals: list[int], nums: list[int]):
    head = ListNode[int].from_list(head_vals)
    implementation = solution_class()
    return implementation.num_components(head, nums)


def assert_num_components(result: int, expected: int) -> bool:
    assert result == expected
    return True
