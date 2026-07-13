from leetcode_py import ListNode


def run_is_palindrome(solution_class: type, head_list: list[int]):
    head = ListNode[int].from_list(head_list)
    implementation = solution_class()
    return implementation.is_palindrome(head)


def assert_is_palindrome(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
