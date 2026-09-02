def run_is_valid_palindrome(solution_class: type, s: str, k: int):
    implementation = solution_class()
    return implementation.is_valid_palindrome(s, k)


def assert_is_valid_palindrome(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
