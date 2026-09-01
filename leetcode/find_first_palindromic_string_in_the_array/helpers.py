def run_first_palindrome(solution_class: type, words: list[str]):
    implementation = solution_class()
    return implementation.first_palindrome(words)


def assert_first_palindrome(result: str, expected: str) -> bool:
    assert result == expected
    return True
