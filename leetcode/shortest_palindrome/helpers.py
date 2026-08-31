def run_shortest_palindrome(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.shortest_palindrome(s)


def assert_shortest_palindrome(result: str, expected: str) -> bool:
    assert result == expected
    return True
