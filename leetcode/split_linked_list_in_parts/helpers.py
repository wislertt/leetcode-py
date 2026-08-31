from leetcode_py import ListNode


def run_split_list_to_parts(solution_class: type, head_vals: list[int], k: int):
    head = ListNode[int].from_list(head_vals)
    implementation = solution_class()
    parts = implementation.split_list_to_parts(head, k)
    return [part.to_list() if part is not None else [] for part in parts]


def assert_split_list_to_parts(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
