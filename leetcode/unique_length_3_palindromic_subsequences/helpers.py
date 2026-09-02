def run_count_palindromic_subsequence(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.count_palindromic_subsequence(s)


def assert_count_palindromic_subsequence(result: int, expected: int) -> bool:
    assert result == expected
    return True
