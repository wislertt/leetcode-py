def run_count_palindromic_subsequences(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.count_palindromic_subsequences(s)


def assert_count_palindromic_subsequences(result: int, expected: int) -> bool:
    assert result == expected
    return True
