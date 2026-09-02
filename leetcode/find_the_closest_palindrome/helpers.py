def run_nearest_palindromic(solution_class: type, n: str):
    implementation = solution_class()
    return implementation.nearest_palindromic(n)


def assert_nearest_palindromic(result: str, expected: str) -> bool:
    assert result == expected
    return True
