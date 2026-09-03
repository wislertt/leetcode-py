def run_prime_palindrome(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.prime_palindrome(n)


def assert_prime_palindrome(result: int, expected: int) -> bool:
    assert result == expected
    return True
