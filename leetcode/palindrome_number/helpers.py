def run_is_palindrome(solution_class: type, x: int):
    implementation = solution_class()
    return implementation.is_palindrome(x)


def assert_is_palindrome(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
