from leetcode_py import ListNode


def run_swap_nodes(solution_class: type, head_list: list[int], k: int):
    head = ListNode[int].from_list(head_list)
    implementation = solution_class()
    result = implementation.swap_nodes(head, k)
    return result.to_list() if result else []


def assert_swap_nodes(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
