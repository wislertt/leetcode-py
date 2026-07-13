def run_valid_palindrome(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.valid_palindrome(s)


def assert_valid_palindrome(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
