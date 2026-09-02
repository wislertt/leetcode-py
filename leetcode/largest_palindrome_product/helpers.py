def run_largest_palindrome(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.largest_palindrome(n)


def assert_largest_palindrome(result: int, expected: int) -> bool:
    assert result == expected
    return True
