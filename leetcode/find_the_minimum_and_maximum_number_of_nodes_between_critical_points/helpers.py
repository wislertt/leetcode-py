from leetcode_py import ListNode


def run_nodes_between_critical_points(solution_class: type, head_list: list[int]):
    head = ListNode[int].from_list(head_list)
    implementation = solution_class()
    return implementation.nodes_between_critical_points(head)


def assert_nodes_between_critical_points(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
