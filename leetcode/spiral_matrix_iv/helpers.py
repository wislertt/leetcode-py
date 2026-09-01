from leetcode_py import ListNode


def run_spiral_matrix(solution_class: type, m: int, n: int, head_vals: list[int]):
    head = ListNode[int].from_list(head_vals)
    implementation = solution_class()
    return implementation.spiral_matrix(m, n, head)


def assert_spiral_matrix(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
